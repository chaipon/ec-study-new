from flask import Flask
import logging


# create_app関数を作成する
def create_app():
    # Flaskインスタンス作成
    app = Flask(__name__)
    # fn1パッケージからviewsをimportする
    from study.fn1 import views as fn1_views

    # SECRET_KEYを追加する
    app.config["SECRET_KEY"] = "12345678"
    # ログレベルを設定する
    app.logger.setLevel(logging.DEBUG)
    # app.logger.critical("fatal error")
    # app.logger.error("error")
    # app.logger.warning("warning")
    # app.logger.info("info")
    # app.logger.debug("debug")


    # register_blueprintを使いviewsのfn1をアプリへ登録する
    app.register_blueprint(fn1_views.fn1, url_prefix="/fn1")

    return app