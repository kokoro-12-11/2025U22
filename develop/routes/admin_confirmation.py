from flask import Blueprint, render_template, request, session, redirect, url_for

admin_confirmation_bp = Blueprint("admin_confirmation", __name__)

@admin_confirmation_bp.route("/admin_board_confirm", methods=["POST"])
def admin_confirmation():
    # フォームの値を受け取る
    title = request.form.get("title")
    content = request.form.get("content")
    start = request.form.get("start")

    # session に保存
    session["board_data"] = {
        "title": title,
        "content": content,
        "start": start
    }

    # 確認画面へリダイレクト
    return redirect(url_for("admin_confirmation.confirmation_page"))

@admin_confirmation_bp.route("/admin_confirmation", methods=["GET"])
def confirmation_page():
    board_data = session.get("board_data", {})
    return render_template("admin_confirmation.html", data=board_data)
