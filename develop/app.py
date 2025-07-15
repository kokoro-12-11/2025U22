from flask import Flask,render_template
import os

##### blueprint #####
from routes.route import main_route

app = Flask(__name__)
app.secret_key = '2025u22_key'

##### blueprintの登録 #####
app.register_blueprint(main_route)

##### エラーハンドル #####
@app.errorhandler(404)
def not_found_error(error):
  return render_template('404.html',traceback=str(error))

@app.errorhandler(500)
def internal_server_error(error):
  return render_template('500.html',traceback=str(error))

##### 開発用(エラーページ表示) #####
@app.route('/404')
def rend404():
  return render_template('404.html')

@app.route('/500')
def rend500():
  return render_template('500.html')

##### 開発用(ページ一覧) #####
@app.route('/')
def develop():
  return render_template('develop.html')


##### 表示用 #####
@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/register')
def register():
  return render_template('register.html')

@app.route('/answer')
def answer():
  return render_template('answer.html')

@app.route('/posted_confirmation')
def posted_confirmation():
  return render_template('posted_confirmation.html')

@app.route('/board_sent')
def board_sent():
  return render_template('board_sent.html')

@app.route('/setting')
def setting():
  return render_template('setting.html')

@app.route('/admin_login')
def admin_login():
  return render_template('admin_login.html')

@app.route('/admin_top')
def admin_top():
  return render_template('admin_top.html')

@app.route('/aadmin_board_create')
def admin_board_create():
  return render_template('admin_board_create.html')

if __name__ == "__main__":
  app.run(debug=True)