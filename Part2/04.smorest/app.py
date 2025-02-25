from flask import Flask
from flask_smorest import Api
from api import blp

app = Flask(__name__)

# OpenAPI 관련 설정
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
api.register_blueprint(blp)

if __name__ == "__main__":
    app.run(debug=True)


    #127.0.0.1:5000/swagger-ui 로 주소창에 검색하면 실행중은 API작업 내용을 깔끔한 툴을 이용해서 정리해서 볼 수 있음
    #프론트엔드 개발자에게 공유해서 내용을 서로 알기가 쉬워서 좋음음