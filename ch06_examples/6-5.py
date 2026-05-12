from flask import Flask

app = Flask(__name__)

@app.route('/<name>/')
def hello(name):
    if name == 'kitae':
        result = "<h2>Hello, Kitae</h2>"
    elif name == 'jmlee':
        result = "<h2>Hello, Jmlee</h2>"
    else:
        result = ""
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
