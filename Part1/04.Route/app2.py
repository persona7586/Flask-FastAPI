from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, This is Main Page!"

@app.route('/company')
def about():
    return "This is the company page!"
# Alt + Shift + 화살표 위/아래 (드래그 된것 밑으로 복사)

# 동적으로 URL 파라미터 값을 받아서 처리해준다.
# http://127.0.0.1:5000/user/taemun -> 주소창에 입력하면 페이지에 UserName : taemun으로 나옴
@app.route('/user/<username>')
def user_profile(username):

    return f'UserName : {username}'

#http://127.0.0.1:5000/number/123 -> 주소창에 입력하면 페이지에 Number : 123으로 나옴
@app.route('/number/<int:number>')
def number(number):

    return f'Number : {number}'

# post 요청 날리는 법
# (1) postman
# (2) requests
import requests #pip install requests
@app.route('/test')
def test():
    url = 'http://127.0.0.1:5000/submit'
    data = 'test data'
    response = requests.post(url=url, data=data)

    return response

@app.route('/submit', methods=['GET', 'POST', 'PUT', 'DELETE'])
def submit():
    print(request.method)

    if request.method == 'GET':
        print("GET method")

    if request.method == 'POST':
        print("***POST method***", requests.data)

    return Response("Successfully submitted", status=200)



if __name__ == "__main__":
    app.run()