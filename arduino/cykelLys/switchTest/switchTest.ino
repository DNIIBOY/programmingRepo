// constants won't change. They're used here to set pin numbers:
const int button1Pin = 4;
const int button2Pin = 5;

// variables will change:
int button1State = 0;
int button2State = 0;

void setup() {
  Serial.begin(115200);
  pinMode(button1Pin, INPUT_PULLUP);
  pinMode(button2Pin, INPUT_PULLUP);
}

void loop() {
  button1State = !digitalRead(button1Pin);
  button2State = !digitalRead(button2Pin);
  Serial.print("But1: ");
  Serial.println(button1State);
  Serial.print("But2: ");
  Serial.println(button2State);
  delay(500);
}
