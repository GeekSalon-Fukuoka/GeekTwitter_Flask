from flask import Flask, redirect,render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc, or_
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os
import datetime

BASE_DIR = os.path.dirname(__file__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'db/test.db')
app.config['SECRET_KEY'] = os.urandom(24)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    body = db.Column(db.String(140), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(50), nullable=False, unique=True)
	password = db.Column(db.String(25))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@login_manager.unauthorized_handler
def unauthorized():
    flash('ログインしてください')
    return redirect('/login')

@app.route('/')
def top():
    return render_template('top.html')

@app.route('/tweets', methods=['GET'])
def index():
    text_input = request.args.get('search')
    if text_input is None or len(text_input) == 0:
        tweets = Tweet.query.all()
    else:
        tweets = db.session.query(Tweet).filter(or_(Tweet.body.like(text_input), Tweet.title.like(text_input))).all()
    return render_template('tweets/index.html', tweets=tweets)

@app.route('/tweets/new',methods=['GET','POST'])
@login_required
def create():
    if request.method == 'POST':
        # POSTメソッドの時の処理。
        title = request.form.get('title')
        body = request.form.get('body')

        tweet = Tweet(title=title,body=body,user_id=current_user.id)
        # DBに値を送り保存する
        db.session.add(tweet)
        db.session.commit()
        flash('投稿しました')
        return redirect('/tweets')
    else:
        # GETメソッドの時の処理
        return render_template('tweets/new.html')

@app.route('/tweets/<int:id>/edit',methods=['GET','POST'])
@login_required
def update(id):
    tweet = Tweet.query.get(id)
    if request.method == 'GET':
        return render_template('tweets/edit.html',tweet=tweet)
    else:
        tweet.title = request.form.get('title')
        tweet.body = request.form.get('body')
        db.session.commit()
        flash('投稿を編集しました')
        return redirect('/tweets')

@app.route('/tweets/<int:id>/delete',methods=['GET'])
@login_required
def delete(id):
    tweet = Tweet.query.get(id)
    #投稿を削除
    db.session.delete(tweet)
    #削除を反映
    db.session.commit()
    flash('投稿を削除しました')
    return redirect('/tweets')

@app.route('/tweets/<int:id>',methods=['GET'])
@login_required
def show(id):
    tweet = Tweet.query.get(id)
    return render_template('tweets/show.html',tweet=tweet)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        # Userのインスタンスを作成
        user = User(username=username, password=generate_password_hash(password, method='sha256'))
        if user is not None:
            try:
                db.session.add(user)
                db.session.commit()
                flash('アカウント登録しました！ログインしてください')
                return redirect('login')
            except exc.IntegrityError:
                db.session.rollback()
                flash('アカウント登録に失敗しました。ユーザ名とパスワードを確認してください')
                return redirect('signup')
        else:
            flash('アカウント登録に失敗しました')
            return redirect('signup')
    else:
        return render_template('users/signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        # Userテーブルからusernameに一致するユーザを取得
        user = User.query.filter_by(username=username).first()
        if user is not None and check_password_hash(user.password, password):
                login_user(user)
                flash('ログインしました')
                return redirect('/tweets')
        else:
            flash('ユーザ名またはパスワードが間違っています。再入力してください')
            return redirect('login')
    else:
        return render_template('users/login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('ログアウトしました')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port="5001")
