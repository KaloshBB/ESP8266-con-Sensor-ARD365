
#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <WiFiClient.h>

int val=0;

const int sensorPin = A0;

const uint16_t port = 8585;
const char *host = "192.168.1.82";

WiFiClient client;
void setup()
{
    pinMode(16, OUTPUT);
    pinMode(15,OUTPUT);//VERDE
    pinMode(13,OUTPUT);//AMARILLO
    pinMode(12,OUTPUT);//ROJO
    Serial.begin(115200);
    Serial.println("Connecting...\n");
    WiFi.mode(WIFI_STA);
    WiFi.begin("INFINITUMEFA3_2.4", "3b8CMuQqXu");
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print(".");
    }
    delay(500);
}

void loop() {

   delay(500);

    if (!client.connect(host, port))
    {
        Serial.println("Connection to host failed");
        delay(1000);
        return;
    }
    Serial.println("Connected to server successful!");

    val=analogRead(sensorPin);

  if(val<=100){
    digitalWrite(12,HIGH);
    digitalWrite(13,LOW);
    digitalWrite(15,LOW);
  }else if(val>=101 && val <=500){
    digitalWrite(13,HIGH);
    digitalWrite(12,LOW);
    digitalWrite(15,LOW);
  }else if(val >=501 && val<=1023){
    digitalWrite(15,HIGH);
    digitalWrite(12,LOW);
    digitalWrite(13,LOW);
  }

    //client.write(val);
    Serial.print(val+"\n");
   client.print("Nivel de agua:"+String(val)+"\n");
          delay(1000);
    while (client.available() > 0)
    {
        char c = client.read();
        Serial.write(c);
    }
    Serial.print('\n');
    client.stop();

  delay(1000);
}