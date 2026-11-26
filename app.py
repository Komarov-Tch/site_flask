from flask import Flask
from flask import render_template, flash, redirect, url_for
from flask import request
from config import Config
from forms import Login

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        flash('Получен логин для пользователя {}, запомнить {}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Вход', form=form)


@app.route('/hello')
def hello():
    return 'Привет, мир!'

@app.route('/about')
def about():
    return 'Это вторая строка нашего сервиса'

@app.route('/user/<username>')
def user_profile(username):
    return render_template('hello.html', name=username)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form(['name'])
    return f'Hello, {name}'

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Egor'}
    post = [{'autor': {'username': 'Тим Кук'},
           'body': 'Мы изобрели новый IPHONE 100 цена 10000$'    
  },
  {'autor': {'username': 'Илон Маск'},
           'body': 'Наша тесла начала летать!'    
  }]
    return render_template('index.html', title='Home', user=user, posts=post)




if __name__ == '__main__':
    app.run(debug=True)
