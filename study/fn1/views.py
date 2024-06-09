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

@fn1.route("/contact")
def contact():

    # レスポンスオブジェクトを取得する
    response = make_response(render_template("fn1/contact.html"))
    # クッキーを設定する
    response.set_cookie("flaskbook key", "flaskbook value")
    # セッションを設定する
    session["username"] = "test-user"
    return response

@fn1.route("/contact_complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        # form属性を使ってフォームの値を取得する
        username = request.form['username']
        email = request.form["email"]
        description = request.form["description"]

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

        if not description:
            flash("問い合わせ内容は必須です")
            is_valid = False

        if not is_valid:
            return redirect(url_for("fn1.contact"))
        
        # メールを送る(最後に実装)

        # contactエンドポイントへリダイレクトする
        flash("問い合わせありがとうございました。")
        return redirect(url_for("fn1.contact_complete"))
    
    return render_template("fn1/contact_complete.html")

