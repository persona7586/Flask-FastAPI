from flask import Flask
import test

app = Flask(__name__)

host = '127.0.0.1'
port = '5000'

if __name__ == "__main__":
    app.run(host=host, port=port)


#api.naver.com/api/v1/users