let client = null; // MQTT 클라이언트의 역할을 하는 Client 객체를 가리키는 전역변수
let connectionFlag = false; // 연결 상태이면 true
const CLIENT_ID = "client-"+Math.floor((1+Math.random())*0x10000000000).toString(16) // 사용자 ID 랜덤 생성

function connect() { // 브로커에 접속하는 함수
	if(connectionFlag == true)
		return; // 현재 연결 상태이므로 다시 연결하지 않음

	let broker = document.getElementById("broker").value; // 브로커의 IP 주소
	let port = document.getElementById("port").value; // 브로커의 포트 번호

	document.getElementById("messages").innerHTML += '<span>브로커에 접속 : ' + ' 포트 ' + port + '</span><br/>';
	document.getElementById("messages").innerHTML += '<span>사용자 ID : ' + CLIENT_ID + '</span><br/>';

	client = new Paho.MQTT.Client(broker, Number(port), CLIENT_ID);

	client.onConnectionLost = onConnectionLost; // 접속 끊김 시 onConnectLost() 실행
	client.onMessageArrived = onMessageArrived; // 메시지 도착 시 onMessageArrived() 실행
	client.connect({
		onSuccess:onConnect, // 브로커로부터 접속 응답 시 onConnect() 실행
	});
}

// 브로커로부터 접속 성공 응답을 받을 때 호출되는 함수
function onConnect() {
	let topic = document.getElementById("topic").value; // 사용자가 입력한 토픽 문자열
	client.subscribe(topic); // 브로커에 구독 신청
	document.getElementById("messages").innerHTML += '<span>구독신청: 토픽 ' + topic + '</span><br/>';
	connectionFlag = true; // 연결 상태로 설정
}

// 접속이 끊어졌을 때 호출되는 함수
function onConnectionLost(responseObject) { // responseObject는 응답 패킷
	document.getElementById("messages").innerHTML += '<span>오류 : 접속 끊어짐</span><br/>';
	if (responseObject.errorCode !== 0) {
		document.getElementById("messages").innerHTML += '<span>오류 : ' + responseObject.errorMessage + '</span><br/>';
	}
	connectionFlag = false; // 연결 되지 않은 상태로 설정
}

// 메시지가 도착할 때 호출되는 함수
function onMessageArrived(msg) { // 매개변수 msg는 도착한 MQTT 메시지를 담고 있는 객체
	console.log("onMessageArrived: " + msg.payloadString);
	document.getElementById("messages").innerHTML += '<span>토픽 : ' + msg.destinationName + ' | ' + msg.payloadString + '</span><br/>';
}

// disconnection 버튼이 선택되었을 때 호출되는 함수
function disconnect() {
	if(connectionFlag == false)
		return; // 연결 되지 않은 상태이면 그냥 리턴
	client.disconnect(); // 브로커와 접속 해제
	document.getElementById("messages").innerHTML += '<span>연결종료</span><br/>';
	connectionFlag = false; // 연결 되지 않은 상태로 설정
}
