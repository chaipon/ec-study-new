# ec-study
Flask sample program for studying web system

# 環境作成

    > git clone https://github.com/ykachip/ec-study.git
    > cd ec-study
    > python -m venv .venv
    > .venv/Scripts/activate.ps1
    > python -m pip install --upgrade pip
    > python -m pip install build
    > python -m build --wheel
    > python -m pip install .\dist\study-1.0.0-py2.py3-none-any.whl

# ローカル環境実行

    > flask run

# Build & Copy to AWS 

    > python -m build --wheel
    > scp -i path_to_secreat_key dist/study-1.0.0-py2.py3-none-any.whl user_name@aws_ipaddress:~/

# AWS上でのInstall & 実行

    > mkdir ec-study
    > cd ec-study
    > python -m venv .venv
    > source .venv\bin\activate
    > python3 -m pip install ../study-1.0.0-py2.py3-none-any.whl
    > waitress-serve  --listen=192.168.10.10:50xx --call 'study:create_app'