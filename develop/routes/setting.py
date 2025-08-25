from flask import Blueprint, render_template, request, redirect, url_for, session, flash
import mysql.connector
import os
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

load_dotenv()

setting_bp = Blueprint('setting', __name__)

db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}

@setting_bp.route('/setting', methods=['GET', 'POST'])
def setting():
    if request.method == 'POST':
        user_id = session.get('user_id')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        location = request.form.get('location')
        
        # パスワードをハッシュ化（入力がある場合のみ）
        hashed_password = generate_password_hash(password)
        
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE users
                SET user_name=%s, email=%s, password=%s, prefecture_id=%s, updated_at=NOW()
                WHERE user_id=%s
            """, (username, email, hashed_password, location, user_id))

            conn.commit()
            
            session['user_name'] = username  
            
            flash("設定を更新しました！", "success")
            return redirect(url_for('setting.setting_completed'))

        except mysql.connector.Error as err:
            print("DB Error:", err)
            flash("更新中にエラーが発生しました", "danger")
            return redirect(url_for('setting.setting'))

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    return render_template('setting.html')

@setting_bp.route('/setting_completed')
def setting_completed():
    return render_template('setting_completed.html')