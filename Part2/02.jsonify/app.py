from flask import Flask, jsonify, request

app = Flask(__name__)

# GET
# (1) 전체 게시글을 불러오는 API
@app.route('/api/v1/feeds', methods=['GET'])
def show_all_feeds():
    data = {'result':'success', 'data':{'feed1':'data1', 'feed2':'data2'}}

    return data

# (2) 특정 게시글을 불러오는 API
# http://127.0.0.1:5000/api/v1/feeds -> get방식으로 검색창에 입력하게 되면 json형태로 나타냄냄
@app.route('/api/v1/feeds/<int:feed_id>', methods=['GET'])
def show_one_feed(feed_id):
    print(feed_id)

    data = {'result':'success', 'data':{'feed1':'data1'}}

    return data

# POST
# (1) 게시글을 작성하는 API
@app.route('/api/v1/feeds', methods=['POST'])
def create_one_feed():
    name = request.form['name']
    age = request.form['age']

    print(name, age)

    return jsonify({'result':'success'})

datas = [{"items": [{"name": "item1", "price": 10}]}]

@app.route('/api/v1/datas', methods=['GET'])
def get_datas():
    return {"datas":datas}

@app.route('/api/v1/datas', methods=['POST'])
def create_data():
    request_data = request.get_json() #json의 형태로 get

    new_data = {'items': request_data.get('items', [])} #new data를 만들어서 위에 있는 datas의 내용에 추가 해주겠다는 뜻
    datas.append(new_data)

    return new_data, 201 