from flask.views import MethodView  # Flask의 클래스 기반 뷰를 사용하기 위해 import
from flask_smorest import Blueprint, abort  # Blueprint(라우팅 그룹) 및 abort(오류 처리) 가져오기
from schemas import BookSchema  # 데이터 검증을 위한 Marshmallow 스키마 import

# Blueprint 생성 (이름: 'books', url_prefix: '/books')
book_blp = Blueprint('books', 'books', url_prefix='/books', description='Operations on books')

# 임시 데이터 저장 (DB 대신 리스트 사용)
books = []

# [GET] 전체 도서 조회 & [POST] 새로운 도서 추가
@book_blp.route('/')
class BookList(MethodView):
    # [GET] 모든 책을 조회
    @book_blp.response(200, BookSchema(many=True))  # 200 응답 시 BookSchema의 리스트 형태로 반환
    def get(self):
        return books  # 전체 도서 목록 반환

    # [POST] 새로운 책 추가
    @book_blp.arguments(BookSchema)  # 요청 본문을 BookSchema에 맞게 검증
    @book_blp.response(201, BookSchema)  # 201 응답 시 BookSchema 형태로 반환
    def post(self, new_data):
        new_data['id'] = len(books) + 1  # 새 책의 ID 자동 할당 (간단한 방식)
        books.append(new_data)  # 리스트에 추가
        return new_data  # 추가된 책 데이터 반환

# [GET] 특정 도서 조회, [PUT] 특정 도서 업데이트, [DELETE] 특정 도서 삭제
@book_blp.route('/<int:book_id>')  # URL 파라미터로 book_id를 받음
class Book(MethodView):
    # [GET] 특정 ID의 책 조회
    @book_blp.response(200, BookSchema)  # 200 응답 시 BookSchema 형태로 반환
    def get(self, book_id):
        # 리스트에서 해당 ID를 가진 책 찾기 (없으면 None 반환)
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            abort(404, message="Book not found.")  # 책이 없으면 404 에러 반환
        return book  # 찾은 책 반환

    # [PUT] 특정 ID의 책 정보 업데이트
    @book_blp.arguments(BookSchema)  # 요청 본문을 BookSchema에 맞게 검증
    @book_blp.response(200, BookSchema)  # 200 응답 시 BookSchema 형태로 반환
    def put(self, new_data, book_id):
        # 리스트에서 해당 ID를 가진 책 찾기
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            abort(404, message="Book not found.")  # 책이 없으면 404 에러 반환
        book.update(new_data)  # 기존 책 데이터를 새 데이터로 업데이트
        return book  # 업데이트된 책 정보 반환

    # [DELETE] 특정 ID의 책 삭제
    @book_blp.response(204)  # 204 No Content 응답 (삭제 성공)
    def delete(self, book_id):
        global books  # 전역 리스트 수정하기 위해 선언
        # 리스트에서 해당 ID를 가진 책 찾기
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            abort(404, message="Book not found.")  # 책이 없으면 404 에러 반환
        # 해당 ID의 책을 리스트에서 제거
        books = [book for book in books if book['id'] != book_id]
        return ''  # 204 응답이므로 내용 없음

    

    #api.py: 책 목록을 관리하는 API 엔드포인트를 구현합니다. GET, POST, PUT, DELETE 메소드를 사용하여 책 목록을 조회, 추가, 수정, 삭제할 수 있습니다.