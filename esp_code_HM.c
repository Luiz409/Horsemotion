#include <SD.h>
#include <SPI.h>
#include "FS.h"
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

const int bottomButtonPin = 13;
const int ledPin = 14;
const int sdDetectedPin = 25;
const int chipSelect = 5;

Adafruit_MPU6050 mpu;

void setup() {
  Serial.begin(9600);

  while (!Serial) {
    delay(1000);
  }
  
  pinMode(sdDetectedPin, INPUT);
  pinMode(bottomButtonPin, INPUT_PULLUP);
  pinMode(ledPin, OUTPUT);

  digitalRead(sdDetectedPin);

  if (!SD.begin(chipSelect)) {
    Serial.println("Falha ao inicializar o cartão de memória!");
    while (1){
      digitalWrite(ledPin, HIGH);
      delay(1000);
      digitalWrite(ledPin, LOW);
      delay(1000);
    }
  }

  if (!mpu.begin()) {
    Serial.println("Falha ao inicializar o sensor!");
    while (1){
      digitalWrite(ledPin, HIGH);
      delay(1000);
      digitalWrite(ledPin, LOW);
      delay(1000);
    }
  }

  mpu.setAccelerometerRange(MPU6050_RANGE_2_G);
  mpu.setGyroRange(MPU6050_RANGE_250_DEG);
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
}

void loop() {
    int bottomButtonState = digitalRead(bottomButtonPin);
    static bool record = false;
    static File file;
    String dataString = "";

    if (bottomButtonState == LOW && record == false) {
        delay(1000);
        record = true;
        file = SD.open("/dados.txt", FILE_APPEND);
        if (!file) {
            Serial.println("Falha ao abrir o arquivo!");
        }else{
            Serial.println("Arquivo aberto com sucesso!");
            digitalWrite(ledPin, HIGH);
            delay(1000);
        }
    }

    if (record == true){
        sensors_event_t a, g, temp;
        mpu.getEvent(&a, &g, &temp);
        dataString = String(a.acceleration.x) + "," + String(a.acceleration.y) + "," + String(a.acceleration.z) + "," + String(g.gyro.x) + "," + String(g.gyro.y) + "," + String(g.gyro.z) + "," + String(temp.temperature);
        file.println(dataString);
    }else{
        Serial.println("Aguardando...");
    }

    bottomButtonState = digitalRead(bottomButtonPin);
    if (bottomButtonState == LOW && record == true) {
        digitalWrite(ledPin, LOW);
        delay(1000);
        record = false;
        Serial.println("Gravacao desativada!");
        file.close();
        delay(1000);
    }

    delay(80);
}

