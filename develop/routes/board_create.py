from flask import Blueprint,request, jsonify, session
# DB
import mysql.connector ,traceback
from mysql.connector import Error
from routes.config import get_db_connection
# AI
from routes.config import model


board_create_bp = Blueprint('board_create', __name__)

@board_create_bp.route('/board_create', methods=['POST'])
def board_create():
    question = "地元に関する質問を1つ生成  質問のみ出力"

    try:
        response = model.generate_content(question)
        answer = response.text
        print(answer)
    except Exception as e:
        answer = f"エラーが発生しました:\n{str(e)}\n詳細:\n{traceback.format_exc()}"
        print(answer)


    return jsonify({'answer': answer})
