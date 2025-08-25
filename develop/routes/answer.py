from flask import Blueprint, render_template, request, redirect, url_for, session, flash
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

answer_bp = Blueprint('answer', __name__)

db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}

# 回答入力画面
@answer_bp.route('/answer', methods=['GET'])
def answer():
    question_content = None
    board_id = session.get('board_id')
    print(board_id)
    
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute("SELECT post_id FROM boards WHERE board_id = %s", (board_id,))
        row = cursor.fetchone()
        post_id = row['post_id']
        
        cursor.execute("SELECT post_content FROM posts WHERE post_id = %s", (post_id,))
        row = cursor.fetchone()
        if row:
            question_content = row['post_content']
    except mysql.connector.Error as err:
        print("DB Error (fetch question):", err)
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

    # post_id と board_id を hidden に渡す
    return render_template(
        'answer.html',
        post_id=post_id,
        board_id=board_id,
        question_content=question_content,
        user_name=session.get('user_name')
    )
    
    
# 回答入力フォームの送信を受けるルート
@answer_bp.route('/submit_answer', methods=['POST'])
def submit_answer():
    session['answer_text'] = request.form.get('answer')
    session['post_id'] = request.form.get('post_id')
    session['board_id'] = request.form.get('board_id')
    
    print("DEBUG: post_id=", session['post_id'], " board_id=", session['board_id'])
    
    return redirect(url_for('answer.posted_confirmation'))



# 投稿確認画面
@answer_bp.route('/posted_confirmation', methods=['GET', 'POST'])
def posted_confirmation():
    if request.method == 'POST':
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO answers (board_id, post_id, user_id, answer_text, created_at)
                VALUES (%s, %s, %s, %s, NOW())
            """, (
                session.get('board_id'),
                session.get('post_id'),
                session.get('user_id'),
                session.get('answer_text')
            ))
            conn.commit()

            flash("回答を投稿しました！", "success")
            return redirect(url_for('answer.board_sent'))

        except mysql.connector.Error as err:
            print("DB Error (insert):", err)
            flash(f"投稿中にエラーが発生しました: {err}", "danger")
            return redirect(url_for('answer.answer', post_id=session.get('post_id')))

        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()

    # GET の場合: 確認画面表示
    question_content = None
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT post_content FROM posts WHERE post_id = %s", (session.get('post_id'),))
        row = cursor.fetchone()
        if row:
            question_content = row['post_content']
    except mysql.connector.Error as err:
        print("DB Error (fetch question):", err)
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

    return render_template(
        'posted_confirmation.html',
        question_content=question_content,
        answer_text=session.get('answer_text'),
        user_name=session.get('user_name')
    )



@answer_bp.route('/board_sent')
def board_sent():
    board_id = session.get('board_id')
    user_id = session.get('user_id')

    if not board_id or not user_id:
        return redirect('/top')

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        #回答者を viewer に変更
        cursor.execute("""
            UPDATE board_members
            SET role = 'viewer'
            WHERE board_id = %s AND user_id = %s
        """, (board_id, user_id))

        #まだ editor になっていない owner を取得
        cursor.execute("""
            SELECT user_id FROM board_members
            WHERE board_id = %s AND role = 'owner'
        """, (board_id,))
        remaining_users = cursor.fetchall()

        if remaining_users:
            import random
            next_editor = random.choice(remaining_users)['user_id']

            #新しい editor に role 更新
            cursor.execute("""
                UPDATE board_members
                SET role = 'editor'
                WHERE board_id = %s AND user_id = %s
            """, (board_id, next_editor))

        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        print("DBエラー:", e)
        return "エラーが発生しました", 500

    return render_template('board_sent.html')