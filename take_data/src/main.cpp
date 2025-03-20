#include <Arduino.h>


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.println("Hello World");
}

void loop() {
  // put your main code here, to run repeatedly:
  float a[3] = {0, 0, 0};
  // unsigned long ll = millis();
  for (int i = 0; i < 100; i++)
  {
    unsigned long now = millis();
    a[0] = now;
    a[1] = sin(now);
    a[2] = cos(now);
    Serial.print(a[0]);
    Serial.print(" ");
    Serial.print(a[1]);
    Serial.print(" "); 
    Serial.println(a[2]);
    delay(100);
  }
  delay(2000);
  
}
