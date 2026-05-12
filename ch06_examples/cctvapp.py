import cv2
from flask import Flask, render_template
import camera

app = Flask(__name__)
camera.init(width=320, height=240)

@app.route('/cctv')
def cctv():
    image = camera.take_picture(most_recent=True)
    if image is not None:
        cv2.imwrite('./static/cctv.jpg', image)
        return render_template('cctv.html', fname='/static/cctv.jpg')
    return '<h2>카메라 이미지를 읽을 수 없습니다.</h2>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
