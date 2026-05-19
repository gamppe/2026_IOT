import paho.mqtt.client as mqtt

def on_connect(client, userdata, flag, rc, prop=None):
	print("letter 토픽으로 메시지 구독 신청")
	client.subscribe("letter") # 메시지 구독 신청

def on_message(client, userdata, msg):
	print(msg.topic, end=", ") # 토픽 출력
	print(str(msg.payload.decode('utf-8'))) # 메시지 데이터 출력

ip = input("브로커의 IP 주소>>") # 브로커 IP 주소 입력

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.connect(ip, 1883) # 1883 포트로 브로커에 접속
client.loop_forever() # 메시지 루프 실행
