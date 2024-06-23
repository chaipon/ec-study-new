# Flaskクラスをimportする
from flask import (
    Blueprint,
    render_template, 
    url_for, 
    # current_app, 
    # g, 
    request, 
    redirect,
    flash,
    make_response,
    session
)
from study.models.question import Question
from study.database import db_session

from email_validator import validate_email, EmailNotValidError

# Blueprintでfn1アプリを生成する
fn1 = Blueprint(
    "fn1",
    __name__,
    static_folder="static",
    template_folder="templates",
)

# indexエンドポイントを作成し、index.htmlを返す
@fn1.route("/")
def index():
    return render_template("fn1/index.html")

# show_nameエンドポイントを作成する
@fn1.route("/name/<na>")
def show_name(na):
    # 変数をテンプレートエンジンに渡す
    return render_template("fn1/index.html", param1=na)

@fn1.route("/contacts/new", methods=['GET', 'POST'])
def contact_new():

    if request.method == 'GET':
        # レスポンスオブジェクトを取得する
        return render_template("fn1/contact_new.html")
        # クッキーを設定する
        #response.set_cookie("flaskbook key", "flaskbook value")
        # セッションを設定する
        #session["username"] = "test-user"
        #return response

    if request.method == 'POST':
        # form属性を使ってフォームの値を取得する
        username = request.form.get('username')
        email = request.form.get('email')
        content = request.form.get('description')

        # 入力チェック
        is_valid = True

        if not username:
            flash("ユーザ名は必須です")
            is_valid = False
        if not email:
            flash("メールアドレスは必須です")
            is_valid = False
        
        try:
            validate_email(email)
        except EmailNotValidError:
            flash("メールアドレスの形式で入力して下さい")
            is_valid = False

        if not content:
            flash("問い合わせ内容は必須です")
            is_valid = False

        if not is_valid:
            return redirect(url_for("fn1.contact_new"))
        question = Question(name = username, mail = email, content=content)
        db_session.add(question)
        db_session.commit()
        questions = Question.query.all()

        return render_template('fn1/contacts.html', questions=questions)

@fn1.route("/contacts", methods=['GET'])
def contacts():
    questions = Question.query.all()
    return render_template("fn1/contacts.html", questions=questions)


