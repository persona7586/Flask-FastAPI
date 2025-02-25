from flask import Flask  # Flask 애플리케이션 생성
from flask_smorest import Api  # Flask-Smorest API 사용 (자동 문서화 및 데이터 검증)
from api import book_blp  # book_blp(Blueprint) 가져오기

# Flask 애플리케이션 생성
app = Flask(__name__)

# Flask-Smorest API 설정 (API 문서화를 위한 설정 포함)
app.config['API_TITLE'] = 'Book API'  # API 이름 설정
app.config['API_VERSION'] = 'v1'  # API 버전 지정
app.config['OPENAPI_VERSION'] = '3.0.2'  # OpenAPI(Swagger) 버전 지정
app.config["OPENAPI_URL_PREFIX"] = "/"  # OpenAPI 문서의 기본 URL 경로 설정
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"  # Swagger UI 접근 경로
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"  
# Swagger UI의 정적 파일을 CDN에서 가져와 사용

# Flask-Smorest API 인스턴스 생성
api = Api(app)

# book_blp(Blueprint) 등록 → "/books" 엔드포인트 추가
api.register_blueprint(book_blp)

# Flask 애플리케이션 실행
if __name__ == '__main__':
    app.run(debug=True)  # 디버그 모드 활성화 (코드 변경 시 자동 재시작)

#app.py: Flask 애플리케이션과 Flask-Smorest API의 기본 설정을 포함합니다. Swagger UI 경로도 설정됩니다.