from flask import Blueprint, jsonify , render_template, redirect, session
from routes.config import get_db_connection
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

top_bp = Blueprint('top', __name__)

db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME'),
    'charset': 'utf8mb4'
}



@top_bp.route('/top')
def top_page():
    user_id = session.get("user_id")
    if not user_id:
        return redirect("/login")

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT board_id,role FROM board_members
            WHERE user_id = %s AND role = 'editor'
        """, (user_id,))
        result = cursor.fetchone()

        # ボタン表示フラグ
        has_board = bool(result)


        if result:
            session["board_id"] = result["board_id"]


        # ユーザー名取得（ヘッダーに表示用）
        cursor.execute("SELECT user_name FROM users WHERE user_id = %s", (user_id,))
        user = cursor.fetchone()

        cursor.close()
        conn.close()

    except Exception as e:
        print("DBエラー:", e)
        return "エラーが発生しました", 500

    return render_template(
        "top.html",
        user_name=user["user_name"] if user else "名無し",
        has_board=has_board
    )



@top_bp.route('/get_board_image/<int:pref_id>')
def get_board_image(pref_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT image_path
        FROM boards
        WHERE prefecture_id = %s
        ORDER BY send_at DESC
        LIMIT 1
    """, (pref_id,))
    
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if result:
        return jsonify({'image_path': result['image_path']})
    else:
        return jsonify({'image_path': None})
