# admin.py

from flask import Blueprint, render_template, request, redirect, flash, session, url_for

admin_bp = Blueprint('admin', __name__)

# 仮の管理者情報
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin1234"

# ログイン画面表示
@admin_bp.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # 固定情報と照合
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            flash("管理者としてログインしました", "success")
            return redirect('/admin_top')
        else:
            flash("ユーザー名またはパスワードが違います", "danger")
            return redirect('/admin_login')

    return render_template('admin_login.html')

# ログアウト処理
@admin_bp.route('/admin_logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    flash("ログアウトしました", "info")
    return redirect(url_for('admin.admin_login'))
