#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;

bool moving = false;

int accelCount = 0;

const int ledPIN = 3; // D3

void setup(){
  Serial.begin(115200);
  pinMode(ledPIN, OUTPUT);

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
  int xGyr = rawGyro.xGyr;

  if ((xGyr > 1000 || xGyr < -1000) && !moving){
    accelCount++;
  }

  else if (xGyr < 1000 && xGyr > -1000 && moving){
    accelCount --;
  }

  if (accelCount >= 3){
    moving = true;
    accelCount = 0;
  }

  if (accelCount <= -2){
    moving = false;
    Serial.println("LOLOL");
    accelCount = 0;
  }

  Serial.print(" Xraw = ");
  Serial.println(xGyr);
  
  delay(500);
}
