from flask import Flask, abort

app = Flask(__name__)

@app.route('/example')
def example():
    # 어떠한 조건에서 오류를 발생시키고 처리
    error_condition = True

    if error_condition:
        abort(500, description="An error occurred while processing the request.")

    '''
    abort를 사용하지 않을 경우 아래와 같은 오류반환 과정의 작업을 해줘야 한다.

    if error_condition:
        error_response = jsonify({"error": "An error occurred while processing the request."})
        error_response.status_code = 500
        return error_response
    '''

    # 정상적인 응답
    return "Success!"

if __name__ == "__main__":
    app.run()