#include <Servo.h>

Servo myservo;
int servopin = 2; // D4
int moveDelay = 15;
int relayDelay = 400;
int servoRelay = 16; // D0

int dcRelay = 5; // D1

void setup()
{
  myservo.attach(servopin);
  pinMode(servoRelay, OUTPUT);
  pinMode(dcRelay, OUTPUT);
  digitalWrite(dcRelay, HIGH);
  digitalWrite(servoRelay, HIGH);
  Serial.begin(115200);
}


void loop(){
  spinMotor(dcRelay, 2000);
  delay(2000);
  servoReturn(servoRelay, 0, 174, moveDelay, relayDelay, 3000);
  delay(5000);
}


void servoReturn(int relay, int from, int to, int moveDelay, int relayDelay, int pause){
  
  int pos = 0;
  digitalWrite(relay, LOW);
  delay(relayDelay);
  
  for (pos = from; pos <= to; pos += 1) {
      myservo.write(pos);
      Serial.println(pos);
      delay(moveDelay);
  }
  
  delay(pause);
  
  for (pos = 174; pos >= 0; pos -= 1) {
      myservo.write(pos);
      Serial.println(pos);
      delay(moveDelay);
  }
  
  delay(relayDelay);
  digitalWrite(servoRelay, HIGH);
}

void spinMotor(int relay, int duration){
  digitalWrite(relay, LOW);
  delay(duration);
  digitalWrite(relay, HIGH);
}
