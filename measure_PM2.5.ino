#include <TridentTD_LineNotify.h>

int measurePin = A0;

int samplingTime = 280;
int deltaTime = 40;
int sleepTime = 9680;

float voMeasured = 0;
float calcVoltage = 0;
float dustDensity = 0;

#define SSID "Ken"
#define PASSWORD String(int(111111111*9))
#define LINE_TOKEN "qNzHkBG1CXV8JuihiyaHpnhZCuxG3xgpUgS9cGpxSXJ"


void setup() {
  Serial.begin(9600);
  WiFi.begin(SSID, PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(400);
  }
  Serial.printf("\nWiFi connected\nIP : ");
  Serial.println(WiFi.localIP());
  LINE.setToken(LINE_TOKEN);
  Serial.println("PM2.5 Sensor Activated");
  //LINE.notify("PM2.5 Sensor STOPPED");
}

void loop() {
  delayMicroseconds(samplingTime);
  voMeasured = analogRead(measurePin); // read the dust value
  delayMicroseconds(deltaTime);
  delayMicroseconds(sleepTime);

  calcVoltage = voMeasured * (5.0/1024.0);
  dustDensity = 0.17 * calcVoltage - 0.1;

  String data = "Name: Ken | Raw Signal Value: " + String(voMeasured) + " | Voltage: " + String(calcVoltage) + " | Dust Density: " + String(dustDensity);
  Serial.println(data);
  //LINE.notify(data);
  delay(5000);
}
