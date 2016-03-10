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
        file.write("\n")
    file.close()
    return "logged"

@app.route('/history')
def history():
    out=''
    with open('data.txt', 'r') as file:
        for line in file:
            out+=(line+'<br>')
    file.close()
    return out

if __name__ == '__main__':
    app.run(debug=True, port=8080)