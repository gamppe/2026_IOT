from flask import Flask, request

app = Flask(__name__)

@app.route('/search')
def echo_request():
    result = "<h4>request.url=" + request.url + "</h4>"
    result += "<h4>request.full_path=" + request.full_path + "</h4>"
    result += "<h4>request.path=" + request.path + "</h4>"
    result += "<h4>request.method=" + request.method + "</h4>"
    if request.method == 'GET':
        result += "<h4>city=" + request.args['city'] + "</h4>"
        result += "<h4>name=" + request.args['name'] + "</h4>"
    elif request.method == 'POST':
        result += "<h4>city=" + request.form['city'] + "</h4>"
        result += "<h4>name=" + request.form['name'] + "</h4>"
        result += "</h4>"
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
