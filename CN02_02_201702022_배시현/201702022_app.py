from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/test_get')
def test_get():
    return render_template('get.html')

@app.route('/test_post')
def test_post():
    return render_template('post.html')

@app.route('/get', methods=['GET'])
def get():
    value = request.args.get('test')
    return value

@app.route('/post', methods=['POST'])
def post():
    value = request.form.get('test')
    return value

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
