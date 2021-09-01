const int cal = 600;
const int ledOnDelay = 3;
const int ledOffDelay = 10;
const int photoPin = 0;

bool tailLight = false;
int photoCounter = 0;

const int ledPin = 3;



void setup() {
  Serial.begin(115200);
}


void loop() {
  int value = analogRead(photoPin);
  Serial.println(value);
  if ((value < cal) && (!ledStat || counter > 0)){
    counter--;
  }
  else if ((value > cal) && (ledStat || counter < 0)){
    counter++;
  }

  if (counter < ledOnDelay*-1){
    counter = 0;
    ledStat = true;
  }
  else if (counter > ledOffDelay){
    counter = 0;
    ledStat = false;
  }
  digitalWrite(ledPin, ledStat);
  Serial.print("Count: ");
  Serial.println(counter);
  delay(350);
}
