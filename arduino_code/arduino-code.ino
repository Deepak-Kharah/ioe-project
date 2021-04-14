#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>
#include <ArduinoJson.h>
#include <ACS712.h>
#include <math.h>

ACS712 sensor(ACS712_20A, A0);
float voltage = 230;
float Wh = 0;
float current;
float power;
unsigned long last_time =0;
unsigned long current_time =0;
 
void setup() {
 
  Serial.begin(115200);                 //Serial connection
  WiFi.begin("**********", "**********");   //WiFi connection
  sensor.calibrate();
 
  while (WiFi.status() != WL_CONNECTED) {  //Wait for the WiFI connection completion
 
    delay(500);
    Serial.println("Waiting for connection");
 
  }
 
}

 
void loop() {

 current = sensor.getCurrentAC();
 Serial.println((String)"Current: " + current);
 power = current * voltage;
 Serial.println((String)"power: " + power);
 last_time = current_time;
 current_time = millis();    
 Wh =  power *(( current_time -last_time) /3600000.0) ; 
 Wh = roundf(Wh * 10000) / 10000.0;
 Serial.println((String)"power str: " + Wh);
 
 if(WiFi.status()== WL_CONNECTED){   //Check WiFi connection status
 
   HTTPClient http;    //Declare object of class HTTPClient
 
   http.begin("********************************");      //Specify request destination
   http.addHeader("Content-Type", "application/json");  //Specify content-type header

  String data;
   DynamicJsonDocument doc(1024);
   doc["power"] = Wh;
   serializeJson(doc, Serial);
   serializeJson(doc, data);   
   
   int httpCode = http.POST(data);   //Send the request
   String payload = http.getString();                  //Get the response payload
 
   Serial.println(httpCode);   //Print HTTP return code
   Serial.println(payload);    //Print request response payload
 
   http.end();  //Close connection
 
 }else{
 
    Serial.println("Error in WiFi connection");   
 
 }
 
  delay(3000);  //Send a request every 3 seconds
 
}
