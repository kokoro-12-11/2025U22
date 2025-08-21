from flask import Blueprint, jsonify
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
