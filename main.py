#라즈베리파이환경
#아두이노 초음파센서 코드

void setup()
{
	Serial.begin(9600);		//시리얼 통신 정의
	pinMode(2,OUTPUT);	//초음파가 나오는 Trig 핀2번 설정
	pinMode(3,INPUT);		// 초음파를 받는 Echo 핀3번 설정
}

void loop()
{
	long duraton, cm;		
	digitalWrite(2,HIGH);
	delayMicroseconds(10);
	digitalWrite(2,LOW);
	
	duration = pulseIn(3,HIGH);	//물체에 반사되어 돌아온 초음파의 시간을 저장
	cm = duration * 34 / 1000;	//돌아온 초음파의 시간을 cm로 환산
	Serial.print(cm);		//측정된 물체로부터 cm를 보여준다
	Serial.println();
	delay(2000);		//2초마다 측정값을 보여준다
}


---------------------------------------------------------------------

#라즈베리파이4 환경
#초음파센서 거리값을 통신받고 센서보드에 결과값을 출력해주는 코드

import serial
from sense_hat import SenseHat	
sense = SenseHat()

port = '/dev/ttyACM0'		# 시리얼통신에 사용할 포트
brate = 9600			# 통신속도 지정
cmd = 'temp'

seri = serial.Serial(port, baudrate = brate, timeout = None)	# serial 객체 생성
print(seri.name)

seri.write(cmd.encode())

a = 1
while a:
	content = seri.readline()			# 아두이노 출력값 읽어오기
	if(int(content.decode()) < 10):		# 거리값이 10cm보다 작으면
		print(content.decode())		# 물체와의 거리가 몇cm인지 출력하고
		#sense.show_message("<<<car<<<")	# sense_hat에 왼쪽에서 차가오는것을 표시 / 통합센서보드 X 보류
	else:					# 거리값이 10cm보다 크면	
		print("차가 오지 않습니다.")		# 차가 오지 않음을 출력
		print(content.decode())		# 물체와의 거리값만 출력