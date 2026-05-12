import cv2

camera = None

def init(camera_id=0, width=640, height=480, buffer_size=1):
    global camera
    camera = cv2.VideoCapture(camera_id, cv2.CAP_V4L)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    camera.set(cv2.CAP_PROP_BUFFERSIZE, buffer_size)

def take_picture(most_recent=False):
    global camera
    length = 0 if most_recent == False else camera.get(cv2.CAP_PROP_BUFFERSIZE)
    while length > 0:
        camera.grab()
        length -= 1
    success, image = camera.read()
    if not success:
        return None
    return image

def final():
    global camera
    if camera != None:
        camera.release()
    camera = None
