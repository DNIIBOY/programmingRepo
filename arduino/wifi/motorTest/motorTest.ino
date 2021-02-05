#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int servopin = 9;
int butpin = 2;
int motorTrans = 7;

int moveDelay = 15; // delay between moves (in ms)

int pos = 0;    // variable to store the servo position
int butstat = 1;
bool motorClose = false;

void setup() {
  myservo.attach(servopin);  // attaches the servo on pin 9 to the servo object
  Serial.begin(115200);
  pinMode(butpin, INPUT);
  pinMode(motorTrans, OUTPUT);
  myservo.write(0);
}

void loop() {
  //butstat = digitalRead(butpin);
  //Serial.println(butstat);
  if (butstat == HIGH and motorClose == false){
    digitalWrite(motorTrans, HIGH);
    for (pos = 0; pos <= 174; pos += 1) {
      myservo.write(pos);              // tell servo to go to position in variable 'pos'
      Serial.println(pos);
      delay(moveDelay);
    }
    motorClose = true;
    digitalWrite(motorTrans, LOW);
    delay(1000);
  }
  else if (butstat == HIGH and motorClose == true) {
    digitalWrite(motorTrans, HIGH);
    for (pos = 174; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
      myservo.write(pos);              // tell servo to go to position in variable 'pos'
      Serial.println(pos);
      delay(moveDelay);                       // waits 15ms for the servo to reach the position
    }
    motorClose = false;
    digitalWrite(motorTrans, LOW);
    delay(1000);
  }
}
