from flask import Flask
app = Flask(__name__)

@app.route('/')
def mesage():
    return app.send_static_file('index.html')


@app.route('/history')
def history():
    return 'his'

if __name__ == '__main__':
    app.run(debug=True, port=8000)