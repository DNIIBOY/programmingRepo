#include <Adafruit_NeoPixel.h>
#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;

const int PIXELPIN = 2;   // input pin Neopixel is attached to
const int NUMPIXELS = 21; // number of neopixels in strip

const int photoCal = 800;  // Calibration value for photoresistor
const int ledOnDelay = 3;
const int ledOffDelay = 10;
const int photoPin = 0;

bool tailLight = false;
int photoCounter = 0;

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, PIXELPIN, NEO_GRB + NEO_KHZ800);

int allPixels[NUMPIXELS] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1};
int leftArrow[NUMPIXELS] = {1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0};
int rightArrow[NUMPIXELS] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1};

int midLight[NUMPIXELS] = {0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0};
int midCircle[NUMPIXELS] = {0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0};

bool leftFlash = false;
bool rightFlash = false;

bool breaking = false;

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
}

void loop() {
  Vector rawGyro = mpu.readRawGyro();
  int xGyr = rawGyro.XAxis;
  int value = analogRead(photoPin);
  Serial.println(value);
  if ((value < photoCal) && (!tailLight || photoCounter > 0)){
    photoCounter--;
  }
  else if ((value > photoCal) && (tailLight || photoCounter < 0)){
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
  if (tailLight){
    setColor(30, 0, 0, midCircle, false);
  }
  else if (!breaking){
    setColor(0, 0, 0, midLight, false);
  }
  Serial.print("Count: ");
  Serial.println(photoCounter);
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
