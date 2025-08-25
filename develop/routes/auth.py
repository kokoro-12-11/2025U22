from flask import Blueprint, render_template, request, redirect, flash, session, url_for
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

auth_bp = Blueprint('auth', __name__)

# .env からDB接続情報を取得
db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}

# -------------------------
# 新規登録ページ 表示と処理
# -------------------------
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        prefecture_id  = request.form.get('prefecture_id')

        # パスワードをハッシュ化
        hashed_password = generate_password_hash(password)

        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor(dictionary=True)

            # メールアドレスの重複チェック
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            existing_user = cursor.fetchone()
            if existing_user:
                return redirect('/register')

            # 登録処理
            cursor.execute(
                """INSERT INTO users (user_name, email, password, prefecture_id, created_at, updated_at)
                VALUES (%s, %s, %s, %s, NOW(), NOW())""",
                (username, email, hashed_password, prefecture_id)
            )
            conn.commit()
            return redirect('/login')

        except mysql.connector.Error as err:
            print("DB Error:", err)
            return redirect('/register')

        finally:
            if conn:
                cursor.close()
                conn.close()

    return render_template("register.html")



# -------------------------
# ログインページ 表示と処理
# -------------------------
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor(dictionary=True, buffered=True)

            # ユーザー名でユーザー取得
            cursor.execute("SELECT * FROM users WHERE user_name = %s", (username,))
            user = cursor.fetchone()

            if user and check_password_hash(user['password'], password):
                session['user_id'] = user['user_id']
                session['user_name'] = user['user_name']
                return redirect("/top")
            else:
                flash("ユーザー名またはパスワードが正しくありません", "danger")
                return redirect("/login")

        except mysql.connector.Error as err:
            print("DB Error:", err)
            return redirect("/login")

        finally:
            if conn:
                cursor.close()
                conn.close()

    return render_template("login.html")



# -------------------------
# ログアウト
# -------------------------
@auth_bp.route('/logout')
def logout():
    session.clear()  # セッション情報をすべてクリア
    return redirect(url_for('auth.login'))  # ログインページへリダイレクト