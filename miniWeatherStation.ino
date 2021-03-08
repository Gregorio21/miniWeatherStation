#include <stdio.h> 
#include <DHT.h>
#include <LiquidCrystal.h>
#include <time.h>
#define DHTPIN 8
#define DHTTYPE DHT11
DHT dht(DHTPIN,DHTTYPE);
const int RS = 2, EN = 3, D4 = 4, D5 = 5, D6 = 6, D7 = 7;
LiquidCrystal lcd(RS,EN,D4,D5,D6,D7);
void setup() {
  // put your setup code here, to run once:
  lcd.begin(16,2);
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  //Delay 20 seconds temp doesn't need that frequent updates
  delay(20000);
  //get current time in seconds
  time_t t = millis()/1000;
  float temp = dht.readTemperature(true);
  float humidity = dht.readHumidity();
  //send time,temp and humidity to serial for debugging and use on python program/data collection 
  Serial.println(t);
  Serial.println(temp);
  Serial.println(humidity);
  //check if the sensor malfunctioned
  if (isnan(humidity) || isnan(temp)) {
  Serial.println(F("Failed to read from DHT sensor!"));
  return;
  }
  //write to first line of lcd display
  lcd.setCursor(0,0);
  lcd.print("Temp: ");
  lcd.print(temp);
  lcd.print("F");
  //write to second line of lcd display
  lcd.setCursor(0,1);
  lcd.print("Hum: ");
  lcd.print(humidity);
  lcd.print("%"); 
}
