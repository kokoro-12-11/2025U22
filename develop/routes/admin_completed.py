from flask import Blueprint, render_template, request ,session
from routes.config import get_db_connection
from datetime import datetime
import mysql.connector
import os

admin_completed_bp = Blueprint("admin_completed", __name__)

db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}


@admin_completed_bp.route("/admin_completed", methods=["POST"])
def completed_page():
    content = request.form.get("content")
    prefecture_id = request.form.get("prefecture_id")
    start = request.form.get("start")  
    user_id = session.get("admin_user_id")
    

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            INSERT INTO boards (user_id,prefecture_id, send_at,is_skipped)
            VALUES (%s, %s,%s,%s)
        """, (user_id,prefecture_id, start,0)) 
        board_id = cursor.lastrowid

        cursor.execute("""
            INSERT INTO posts (prefecture_id, post_content, created_at)
            VALUES ( %s, %s, NOW())
        """, (prefecture_id, content))
        
        post_id = cursor.lastrowid

        cursor.execute("UPDATE boards SET post_id = %s WHERE board_id = %s", (post_id, board_id))

        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        print("DBエラー:", e)
        return "エラーが発生しました", 500

    session.pop("board_data", None)

    return render_template("admin_completed.html")
