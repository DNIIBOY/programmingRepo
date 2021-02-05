int dcMotorTrans = 7; // pin for transistor with power for DC motor

void setup() {
  pinMode(dcMotorTrans, OUTPUT);
}

void loop() {
  digitalWrite(dcMotorTrans, HIGH);
  delay(2000);
  digitalWrite(dcMotorTrans, LOW);
  delay(4000);
}
