#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;

void setup(){
  Serial.begin(115200);

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

  Serial.print(" Xraw = ");
  Serial.println(rawGyro.XAxis);
  
  delay(500);
}
