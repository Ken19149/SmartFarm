#include "DHT.h"
#include <TridentTD_LineNotify.h>

DHT dht;

#define SSID "Ken"
#define PASSWORD String(int(111111111*9))
#define LINE_TOKEN "qFdrPqzhPp91PcMXbOxqN0qeJJYlL7cTJcqc7MJk2Fl"
#define TIME_DELAY 5 //mins

void setup() {
  Serial.begin(9600);
  dht.setup(D7);

  Serial.println(LINE.getVersion());

  WiFi.begin(SSID, PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(400);
  }
  Serial.printf("\nWiFi connected\nIP : ");
  Serial.println(WiFi.localIP());

  LINE.setToken(LINE_TOKEN);
  LINE.notify("LINE Notify Activated");
  LINE.notify(String("Notification Delay: " + String(TIME_DELAY) + " mins"));
}

void loop() {
  delay(dht.getMinimumSamplingPeriod());
  float humidity = dht.getHumidity();
  float temp = dht.getTemperature();
  String data = "Humidity: " + String(humidity) + "\tTemperature: " + String(temp) + "C " + String(dht.toFahrenheit(temp)) + "F";
  LINE.notify(data);
  //Serial.println(data);
  delay(int(1000 * 60 * int(TIME_DELAY)));
}
