#include <Adafruit_NeoPixel.h>
#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;

bool moving = false;
bool breaking = false;

int accelCount = 0;


const int button1Pin = 4;
const int button2Pin = 5;

int leftState = 0;
int rightState = 0;

bool flashOn = false;

int flashCount = 0;


const int photoCal = 600;  // Calibration value for photoresistor
const int ledOnDelay = 3;
const int ledOffDelay = 10;
const int photoPin = 0;

bool tailLight = false;
int photoCounter = 0;


const int PIXELPIN = 2;   // input pin Neopixel is attached to
const int NUMPIXELS = 21; // number of neopixels in strip

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, PIXELPIN, NEO_GRB + NEO_KHZ800);

int allPixels[NUMPIXELS] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1};
int leftArrow[NUMPIXELS] = {1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0};
int rightArrow[NUMPIXELS] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1};

int midLight[NUMPIXELS] = {0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0};
int midCircle[NUMPIXELS] = {0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0};

int sides[NUMPIXELS] = {1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1};

bool leftFlash = false;
bool rightFlash = false;


void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  Serial.println("Serial conection started, waiting for instructions...");
  pixels.begin();
  setColor(0, 0, 0, allPixels, false);

  // Initialize MPU6050
  Serial.println("Initialize MPU6050");
  while(!mpu.begin(MPU6050_SCALE_2000DPS, MPU6050_RANGE_2G))
  {
    Serial.println("Could not find a valid MPU6050 sensor, check wiring!");
    delay(500);
  }
  mpu.calibrateGyro();
  mpu.setThreshold(3);

  pinMode(button1Pin, INPUT_PULLUP);
  pinMode(button2Pin, INPUT_PULLUP);
}

void loop() {
  Vector rawGyro = mpu.readRawGyro();
  int xGyr = rawGyro.XAxis;
  int photoValue = analogRead(photoPin);
  leftState = !digitalRead(button1Pin);
  rightState = !digitalRead(button2Pin);
  bool leftFlash = leftState;
  bool rightFlash = rightState;
  Serial.println(photoValue);

  if (leftState || rightState){
    
  }
  
  if ((photoValue < photoCal) && (!tailLight || photoCounter > 0)){
    photoCounter--;
  }
  else if ((photoValue > photoCal) && (tailLight || photoCounter < 0)){
    photoCounter++;
  }

  if (photoCounter < ledOnDelay*-1){
    photoCounter = 0;
    tailLight = true;
  }
  else if (photoCounter > ledOffDelay){
    photoCounter = 0;
    tailLight = false;
  }
  if (tailLight && !breaking){
    setColor(30, 0, 0, midCircle, false);
  }
  else if (!breaking){
    setColor(0, 0, 0, midLight, false);
  }

  if (rightFlash && !flashOn){
      setColor(50, 10, 0, rightArrow, false);
      flashOn = true;
      delay(400);
  }

  if (leftFlash && !flashOn){
    setColor(50, 10, 0, leftArrow, false);
    flashOn = true;
    delay(400);
  }

  if ((rightFlash || leftFlash) && flashOn){
    setColor(0, 0, 0, sides, false);
    flashOn = false;
    delay(400);
  }
  
  if (breaking){
    setColor(255, 0, 0, midLight, false);
    accelCount++;
  }
  if (breaking && accelCount > 5){
    accelCount = 0;
    breaking = false;
    setColor(0, 0, 0, midLight, false);
  }

  if ((xGyr > 1000 || xGyr < -1000) && !moving && !breaking){
    accelCount++;
  }

  else if (xGyr < 1000 && xGyr > -1000 && moving && !breaking){
    accelCount --;
  }

  if (accelCount >= 3 && !breaking){
    moving = true;
    accelCount = 0;
  }

  if (accelCount <= -2){
    moving = false;
    breaking = true;
    accelCount = 0;
  }

  Serial.print(" Xraw = ");
  Serial.println(xGyr);
  
  delay(400);
}


void setColor(int r, int g, int b, int onPixels[NUMPIXELS], bool offOthers){
  
  if (offOthers){
    for (int i=0; i< NUMPIXELS; i++){
      pixels.setPixelColor(i, pixels.Color(0, 0, 0));
    }  
  }
  
  for (int i=0; i < NUMPIXELS; i++) {
    if (onPixels[i] == 1){
      pixels.setPixelColor(i, pixels.Color(r, g, b));
    }
  }
  pixels.show();
}
