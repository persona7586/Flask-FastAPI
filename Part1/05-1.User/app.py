from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    users = [
        {"username": "doctor", "name": "Alice"},
        {"username": "judge", "name": "Carloll"},
        {"username": "congressman", "name": "Grace"}
    ]
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)