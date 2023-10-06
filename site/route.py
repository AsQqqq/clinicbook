from flask import render_template, request, Flask, redirect, send_from_directory
from flask import jsonify

app = Flask(__name__)
list_number = []


@app.route('/', methods = ['GET'])
def index() -> render_template:
    """Главная страница"""
    return render_template('index.html')

@app.route('/download', methods = ['GET'])
def download():
    """Главная страница"""
    return render_template('download.html')


def upload_route() -> bool:
    """Функция прогрузки"""
    return True