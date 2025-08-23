# admin.py

from flask import Blueprint, render_template, request, redirect, flash, session, url_for
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
import os
from dotenv import load_dotenv
from collections import defaultdict
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import logging
import textwrap


load_dotenv()

admin_bp = Blueprint('admin', __name__)

db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}

# Pillowのフォント
font_path = "static/fonts/NotoSansJP-Bold.ttf"
font_path2 = "static/fonts/NotoSansJP-Regular.ttf"
font_title = ImageFont.truetype(font_path, 38)
font_text = ImageFont.truetype(font_path2, 28)

@admin_bp.route('/admin_top')
def admin_top():
    return render_template("admin_top.html")


# -------------------------
# 管理者新規登録ページ 表示と処理
# -------------------------
@admin_bp.route('/admin_register', methods=['GET', 'POST'])
def admin_register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        prefecture_id = request.form.get('prefecture_id')

        hashed_password = generate_password_hash(password)

        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor(dictionary=True)

            # メールアドレス重複チェック
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            existing_user = cursor.fetchone()
            if existing_user:
                flash("そのメールアドレスはすでに登録されています", "warning")
                return redirect('/admin_register')

            # 管理者として登録
            cursor.execute("""
                INSERT INTO users (user_name, email, password, prefecture_id, role, created_at, updated_at)
                VALUES (%s, %s, %s, %s, 'admin', NOW(), NOW())
            """, (username, email, hashed_password, prefecture_id))
            conn.commit()

            flash("管理者アカウントを登録しました。ログインしてください。", "success")
            return redirect('/admin_login')

        except mysql.connector.Error as err:
            print("DB Error:", err)
            flash("登録中にエラーが発生しました", "danger")
            return redirect('/admin_register')

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    return render_template("admin_register.html")



# -------------------------
# 管理者ログイン
# -------------------------
@admin_bp.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor(dictionary=True)

            # ユーザー名で検索
            cursor.execute("SELECT * FROM users WHERE user_name = %s", (username,))
            admin_user = cursor.fetchone()

            # パスワード一致かつ管理者かチェック
            if admin_user and check_password_hash(admin_user['password'], password):
                if admin_user['role'] == 'admin':
                    session['admin_logged_in'] = True
                    session['admin_user_name'] = admin_user['user_name']
                    session['admin_user_id'] = admin_user['user_id']
                    flash("管理者としてログインしました", "success")
                    return redirect("/admin_top")
                else:
                    flash("管理者権限がありません", "danger")
                    return redirect("/admin_login")

            flash("ユーザー名またはパスワードが正しくありません", "danger")
            return redirect("/admin_login")

        except mysql.connector.Error as err:
            print("DB Error:", err)
            flash("ログイン中にエラーが発生しました", "danger")
            return redirect('/admin_login')

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    return render_template("admin_login.html")



# -------------------------
# 管理者ログアウト
# -------------------------
@admin_bp.route('/admin_logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    session.pop('admin_user_name', None)
    session.pop('admin_user_id', None)
    flash("管理者をログアウトしました", "info")
    return redirect(url_for('admin.admin_login'))



# 回覧板入力画面（admin_board_create.html）
@admin_bp.route('/admin_board_create', methods=['GET'])
def admin_board_create():
    if not session.get('admin_logged_in'):
        flash("管理者ログインが必要です", "warning")
        return redirect(url_for('admin.admin_login'))

    today = date.today().isoformat()
    return render_template('admin_board_create.html', today=today)



# -------------------------
# レポート集計
# -------------------------
@admin_bp.route('/admin_report')
def admin_report():
    print("✅ admin_report に入りました")
    if not session.get('admin_logged_in'):
        flash("管理者ログインが必要です", "warning")
        return redirect(url_for('admin.admin_login'))

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        # 各県ごとの最新の回覧板IDを取得（send_atの最大値でグループ化）
        cursor.execute("""
            SELECT 
                b.board_id,
                p.prefecture_id,
                b.send_at
            FROM boards b
            JOIN posts p ON b.board_id = p.board_id
            INNER JOIN (
                SELECT p.prefecture_id, MAX(b.send_at) AS latest_send_at
                FROM boards b
                JOIN posts p ON b.board_id = p.board_id
                GROUP BY p.prefecture_id
            ) latest ON p.prefecture_id = latest.prefecture_id AND b.send_at = latest.latest_send_at
        """)
        latest_boards = cursor.fetchall()
        latest_board_ids = [row['board_id'] for row in latest_boards]

        if not latest_board_ids:
            flash("回覧板が存在しません", "info")
            return redirect(url_for('admin.admin_top'))

        # 最新のboard_idに対応する投稿と回答を取得
        format_strings = ','.join(['%s'] * len(latest_board_ids))
        query = f"""
            SELECT 
                b.board_id,
                p.prefecture_id,
                b.send_at,
                p.post_content,
                a.answer_text
            FROM boards b
            JOIN posts p ON b.board_id = p.board_id
            LEFT JOIN answers a ON p.post_id = a.post_id
            WHERE b.board_id IN ({format_strings})
            ORDER BY p.prefecture_id, b.board_id
        """
        cursor.execute(query, latest_board_ids)
        result = cursor.fetchall()

        # 整形: 県ごとに集計
        from collections import defaultdict
        report_data = defaultdict(lambda: {
            "board_id": None,
            "send_at": None,
            "question": "",
            "answers": []
        })

        for row in result:
            pref_id = row['prefecture_id']
            report_data[pref_id]["board_id"] = row['board_id']
            report_data[pref_id]["send_at"] = row['send_at']
            report_data[pref_id]["question"] = row['post_content']
            if row['answer_text']:
                report_data[pref_id]["answers"].append(row['answer_text'])

        print("✅ 集計結果:", report_data)
        
        template_path = os.path.join('static', 'images', 'template.png')
        output_dir = "static/boards"
        os.makedirs(output_dir, exist_ok=True)

        for pref_id, data in report_data.items():
            image = Image.open(template_path).convert("RGB")
            draw = ImageDraw.Draw(image)

            # 【質問】
            draw.text((230, 270), "【質問】", font=font_text, fill="black")  # 少し下へ
            q_lines = textwrap.wrap(data['question'], width=24)  # 少し詰める
            y = 320  # 質問本文の開始位置（質問タイトルの下）
            for line in q_lines:
                draw.text((240, y), line, font=font_title, fill="black")  # 太字フォントで強調
                y += 45  # 少しゆとりを持った行間

            # 【回答】
            y += 100  # 質問と回答の間にスペース
            draw.text((230, y), "【回答】", font=font_text, fill="black")
            y += 50  # 回答本文の開始位置

            for i, ans in enumerate(data['answers'], 1):
                lines = textwrap.wrap(f"{i}. {ans}", width=36)  # 回答文も詰め気味
                for line in lines:
                    draw.text((240, y), line, font=font_text, fill="black")
                    y += 42  # 回答行間

            # ファイル保存
            filename = f"board_pref_{pref_id}.png"
            image_path = os.path.join(output_dir, filename)
            image.save(image_path)
            print(f"✅ 生成: {image_path}")

            # 相対パスをDBに保存
            relative_path = f"static/boards/{filename}"
            cursor.execute(
                "UPDATE boards SET image_path = %s WHERE prefecture_id = %s",
                (relative_path, pref_id)
            )
            conn.commit()


    except mysql.connector.Error as err:
        print("DB Error:", err)
        flash("集計中にエラーが発生しました", "danger")
        return redirect(url_for('admin.admin_top'))

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

    return render_template('report_completed.html', report_data=report_data)
