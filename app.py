from flask import Flask, redirect,render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    body = db.Column(db.String(140), nullable=False)


@app.route('/')
def top():
    return render_template('top.html')

@app.route('/tweets')
def index():
    tweets = Tweet.query.all()
    return render_template('tweets/index.html', tweets=tweets)

@app.route('/tweets/new',methods=['GET','POST'])
def create():
    if request.method == 'POST':
        # POSTメソッドの時の処理。
        title = request.form.get('title')
        body = request.form.get('body')

        tweet = Tweet(title=title,body=body)
        # DBに値を送り保存する
        db.session.add(tweet)
        db.session.commit()
        return redirect('/')
    else:
        # GETメソッドの時の処理
        return render_template('tweets/new.html')

@app.route('/tweets/<int:id>/edit',methods=['GET','POST'])
def update(id):
    tweet = Tweet.query.get(id)
    if request.method == 'GET':
        return render_template('tweets/edit.html',tweet=tweet)
    else:
        tweet.title = request.form.get('title')
        tweet.body = request.form.get('body')
        db.session.commit()
        return redirect('/')

@app.route('/tweets/<int:id>/delete',methods=['GET'])
def delete(id):
    tweet = Tweet.query.get(id)
    #投稿を削除
    db.session.delete(tweet)
    #削除を反映
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port="5001")
