from flask import Blueprint,render_template,request,session
from routes.config import get_db_connection,clear_session

main_route = Blueprint('main_route', __name__)
