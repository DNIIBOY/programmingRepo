#include <Adafruit_NeoPixel.h>

#define PIN 2   // input pin Neopixel is attached to

#define NUMPIXELS 21 // number of neopixels in strip

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

int allPixels[NUMPIXELS] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1};
int leftArrow[NUMPIXELS] = {1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0};
int rightArrow[NUMPIXELS] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1};
int midLight[NUMPIXELS] = {0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0};
int midCircle[NUMPIXELS] = {0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0};

bool leftFlash = false;
bool rightFlash = false;

// Buffer to store incoming commands from serial port
String inData;

void setColor(int r, int g, int b, int onPixels[NUMPIXELS]){
  for (int i=0; i< NUMPIXELS; i++){
    pixels.setPixelColor(i, pixels.Color(0, 0, 0));
  }
  
  for (int i=0; i < NUMPIXELS; i++) {
    if (onPixels[i] == 1){
      pixels.setPixelColor(i, pixels.Color(r, g, b));
    }
  }
  pixels.show();
}

void setup() {
    Serial.begin(115200);
    Serial.setTimeout(1);
    Serial.println("Serial conection started, waiting for instructions...");
    pixels.begin();
    setColor(20, 20, 20, allPixels);
}


void loop() {
    while (Serial.available() > 0)
    {
        char recieved = Serial.read();
        inData += recieved; 

        // Process message when new line character is recieved
        if (recieved == '\n')
        {
            Serial.print("Arduino Received: ");
            Serial.print(inData);

            if (inData == "lowRed\n"){
              setColor(30, 0, 0, midCircle);
              rightFlash = false;
              leftFlash = false;
            }

            else if (inData == "highRed\n"){
              setColor(255, 0, 0, midLight);
              rightFlash = false;
              leftFlash = false;
            }

            else if (inData == "right\n"){
              rightFlash = true;
              leftFlash = false;
            }

            else if (inData == "left\n"){
              rightFlash = false;
              leftFlash = true;
            }

            inData = ""; // Clear recieved buffer
        }
    }
    if (rightFlash){
      setColor(50, 10, 0, rightArrow);
      delay(500);
    }

    if (leftFlash){
      setColor(50, 10, 0, leftArrow);
      delay(800);
    }


  if (rightFlash || leftFlash){
    setColor(0, 0, 0, allPixels);
    delay(800);
  }
}
