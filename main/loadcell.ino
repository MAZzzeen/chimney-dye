//including libraries
#include <HX711_ADC.h>
#if defined(ESP8266)|| defined(ESP32) || defined(AVR)
#include <EEPROM.h>
#endif

//defining pins
const int HX711_dout = 7;
const int HX711_sck = 8;
const int enA = 10;
const int in1 = 12;
const int in2 = 11;

//HX711 constructor:
HX711_ADC LoadCell(HX711_dout, HX711_sck);

const int calVal_calVal_eepromAdress = 0;
unsigned long t = 0;

void setup() {
  Serial.begin(57600); delay(10);  //starting serial

  float calibrationValue;
  calibrationValue = 414.70; //calibration

  LoadCell.begin();
  unsigned long stabilizingtime = 2000; 
  boolean _tare = true; 
  LoadCell.start(stabilizingtime, _tare);
  if (LoadCell.getTareTimeoutFlag()) {
    Serial.println("Timeout, check MCU>HX711 wiring and pin designations");
  }
  else {
    LoadCell.setCalFactor(calibrationValue); // set calibration factor (float)
  }

  //setting up motors
  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  analogWrite(enA, 255);

  // Turn on motor A & B
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  delay(800);

  // Turn off motors
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  
}

//reading load cell output
void loop() {
  static boolean newDataReady = 0;
  const int serialPrintInterval = 500; 

  if (LoadCell.update()) newDataReady = true;

  if (newDataReady) {
    if (millis() > t + serialPrintInterval) {
      float i = LoadCell.getData();
      Serial.println(i);
      newDataReady = 0;
      t = millis();
    }
  }

  if (Serial.available() > 0) {
    char inByte = Serial.read();
    if (inByte == 't') LoadCell.tareNoDelay();
  }

  if (LoadCell.getTareStatus() == true) {
    Serial.println("Tare complete");
  }

}
