from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    name = 'sunbo'
    movies = [
        {'title': '扫赌1', 'year': '2003'},
        {'title': '扫赌2', 'year': '2018'},
        {'title': '扫赌3', 'year': '2016'},
        {'title': '扫赌4', 'year': '2020'},
        {'title': '扫赌5', 'year': '1989'},
        {'title': '扫赌6', 'year': '2020'},
        {'title': '扫赌7', 'year': '2020'},
        {'title': '扫赌8', 'year': '2017'},
        {'title': '扫赌9', 'year': '2005'},
        {'title': '扫赌10', 'year': '2015'}
    ]
    return  render_template('index.html',name=name,movies=movies)
