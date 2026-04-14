import cv2
# 검출 객체 2개 생성(얼굴 인식용 1개, 눈 인식용 1개)
faceClassifier = cv2.CascadeClassifier('./haar-cascade-files-master/haarcascade_frontalface_default.xml')
eyeClassifier = cv2.CascadeClassifier('./haar-cascade-files-master/haarcascade_eye.xml')
# 카메라 객체 생성
camera = cv2.VideoCapture(0, cv2.CAP_V4L)
camera.set(cv2.CAP_PROP_BUFFERSIZE, 1) # 버퍼 크기를 1로 설정
while True:
	camera.grab( ) # 버퍼에 저장된 카메라의 이전 프레임 제거
	# 버퍼에서 현재 카메라가 촬영한 프레임 읽기
	ret, image = camera .read( )
	if ret == False:
		continue
	# 이미지를 흑백으로 바꾸고 얼굴과 눈 탐지
	image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	faces = faceClassifier.detectMultiScale(image_gray) # 얼굴 탐지
	eyes = eyeClassifier.detectMultiScale(image_gray) # 눈 탐지
	# 노란색(0, 255, 255) 사각형으로 얼굴 표시
	for x, y, w, h in faces:
		cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 4)
	# 빨간색(0, 0, 255) 사각형으로 눈 표시
	for x, y, w, h in eyes:
		cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 4)
	cv2.imshow('preview', image) # 이미지를 preview 이름의 창에 출력
	if cv2.waitKey(1) == 27: # ESC 키(키 값27)이면 프로그램 종료
		break
camera.release( )
cv2.destroyAllWindows( )
