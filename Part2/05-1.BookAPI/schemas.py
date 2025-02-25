from marshmallow import Schema, fields  # 데이터 검증 및 직렬화를 위한 Marshmallow 가져오기

# BookSchema: 책 정보를 위한 데이터 스키마 정의
class BookSchema(Schema):
    id = fields.Int(dump_only=True)  # `id` 필드: 정수형, 응답에서만 포함 (클라이언트가 직접 설정할 수 없음)
    title = fields.String(required=True)  # `title` 필드: 문자열, 필수 입력값
    author = fields.String(required=True)  # `author` 필드: 문자열, 필수 입력값

    #schemas.py: 책 정보를 위한 스키마를 정의합니다. 여기서는 책의 제목과 저자가 필요하며, 책의 고유 ID는 자동으로 설정됩니다.