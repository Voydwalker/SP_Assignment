from flask import Flask, request
import json


app = Flask(__name__)



@app.route('/')
def default():
    return app.send_static_file('index.html')


@app.route('/message', methods=['GET', 'POST'])
def message():
    with open('data.txt', 'a') as file:
        json.dump(request.json, file)
    return "logged"

@app.route('/history')
def history():
    return ''

if __name__ == '__main__':
    app.run(debug=True, port=8080)