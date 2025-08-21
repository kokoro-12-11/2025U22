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
@answer_bp.route('/answer/<int:post_id>', methods=['GET'])
def answer(post_id):
    question_content = None
    board_id = None
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT board_id, post_content FROM posts WHERE post_id = %s", (post_id,))
        row = cursor.fetchone()
        if row:
            question_content = row['post_content']
            board_id = row['board_id']
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
    return render_template('board_sent.html')