from marshmallow import Schema, fields
from marshmallow import Schema, fields

class BookSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.String(required=True)
    author = fields.String(required=True)
    title = fields.String(required=True)
    author = fields.String(required=True)

    #schemas.py: 책 정보를 위한 스키마를 정의합니다. 여기서는 책의 제목과 저자가 필요하며, 책의 고유 ID는 자동으로 설정됩니다.