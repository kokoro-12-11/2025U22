from flask import Blueprint, render_template, request, session, redirect, url_for
from routes.config import get_db_connection

admin_confirmation_bp = Blueprint("admin_confirmation", __name__)

# ★県名取得用の関数
def get_prefecture_name_by_id(prefecture_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT prefecture_name FROM prefectures WHERE prefecture_id = %s", (prefecture_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result:
            return result['prefecture_name']
        else:
            return "不明"
    except Exception as e:
        print("都道府県取得エラー:", e)
        return "取得失敗"

@admin_confirmation_bp.route("/admin_board_confirm", methods=["POST"])
def admin_confirmation():
    # フォームの値を受け取る
    content = request.form.get("content")
    prefecture_id = request.form.get("prefecture_id")
    start = request.form.get("start")

    # session に保存
    session["board_data"] = {
        "content": content,
        "prefecture_id": prefecture_id,
        "start": start
    }

    # 確認画面へリダイレクト
    return redirect(url_for("admin_confirmation.confirmation_page"))

# GET: 表示
@admin_confirmation_bp.route("/admin_confirmation", methods=["GET"])
def confirmation_page():
    board_data = session.get("board_data", {})

    # ★県名取得
    prefecture_id = board_data.get("prefecture_id")
    prefecture_name = get_prefecture_name_by_id(prefecture_id)

    # 表示用に追加
    board_data["prefecture_name"] = prefecture_name

    return render_template("admin_confirmation.html", data=board_data)
