const int cal = 600;
const int ledOnDelay = 3;
const int ledOffDelay = 10;
const int photoPin = 0;

bool tailLight = false;
int photoCounter = 0;

const int ledPin = 3;
bool ledStat = true;



void setup() {
  Serial.begin(115200);
}


void loop() {
  int value = analogRead(photoPin);
  Serial.println(value);
  if ((value < cal) && (!ledStat || photoCounter > 0)){
    photoCounter--;
  }
  else if ((value > cal) && (ledStat || photoCounter < 0)){
    photoCounter++;
  }

  if (photoCounter < ledOnDelay*-1){
    photoCounter = 0;
    ledStat = true;
  }
  else if (photoCounter > ledOffDelay){
    photoCounter = 0;
    ledStat = false;
  }
  digitalWrite(ledPin, ledStat);
  Serial.print("Count: ");
  Serial.println(photoCounter);
  delay(350);
}
