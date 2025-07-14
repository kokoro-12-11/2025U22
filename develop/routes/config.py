from dotenv import load_dotenv
from mysql.connector import Error
from flask import session
import os
import mysql.connector
import google.generativeai as genai

# .envファイルから環境変数を読み込む
load_dotenv()

def clear_session():
    """セッションをクリアする関数"""
    session.clear()

db_config = {
    'host': os.getenv('DB_HOST', ''),
    'user': os.getenv('DB_USER', ''),
    'password': os.getenv('DB_PASSWORD', ''),
    'database': os.getenv('DB_NAME', '')
}

def get_db_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        print("DB connection successful")
        return conn
    except Error as e:
        print(f"Error: {e}")
        return None

# generativeAi apiの設定
genai.configure(api_key=os.getenv('GENAI_API_KEY', ''))

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    generation_config=genai.types.GenerationConfig(
        max_output_tokens=5000
    )
)