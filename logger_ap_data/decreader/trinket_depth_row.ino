
#include <Wire.h>
#include "MS5837.h"

MS5837 sensor;

void setup() {
  Serial.begin(115200);

  Serial1.begin(1200);

  Wire.begin();

  sensor.setModel(MS5837::MS5837_02BA);
  sensor.init();
  
  sensor.setFluidDensity(997); // kg/m^3 (997 freshwater, 1029 for seawater)
  
}

int i =0;
void loop() {

sensor.read();
  float d = sensor.depth();
  float p = sensor.pressure();
  float t = sensor.temperature();
 
  
  Serial.print(i);

  
  //String is=String(i);
  Serial1.print(t);
  Serial1.print(",");
  Serial1.print(p);
  Serial1.print(",");
  Serial1.println(d);
  
  //if (Serial2.available()) {
    //Serial.print(" -> 0x"); Serial.print(Serial2.read(), HEX);
  //}
  //Serial.println();
  i=i+1;
  
  delay(1000);
}
