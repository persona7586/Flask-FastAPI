from flask import Flask, request  # ✅ request import 추가
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

items = []  # DB의 대체 역할 (간단한 DB 역할)

class Item(Resource):

    # 특정 아이템 조회
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {"msg": "Item not found"}, 404  # ✅ 루프 종료 후 반환

    # 특정 아이템 생성
    def post(self, name):
        for item in items:
            if item['name'] == name:
                return {"msg": "Item Already exists"}, 400

        data = request.get_json()  # ✅ request 사용 가능

        new_item = {'name': name, 'price': data['price']}
        items.append(new_item)

        return new_item, 201  # ✅ 201 Created 반환

    # 특정 아이템 업데이트
    def put(self, name):
        data = request.get_json()

        for item in items:
            if item['name'] == name:
                item['price'] = data['price']
                return item

        new_item = {'name': name, 'price': data['price']}
        items.append(new_item)

        return new_item, 201  # ✅ 새로운 아이템 추가 시 201 반환

    # 특정 아이템 삭제
    def delete(self, name):
        global items

        items = [item for item in items if item['name'] != name]

        return {"msg": "Item Deleted"}

api.add_resource(Item, '/item/<string:name>')  # 경로 추가

if __name__ == "__main__":
    app.run(debug=True)
