#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <WiFiClient.h>

int val=0;

const int sensorPin = A0;

const uint16_t port = PUERTO DEL SERVIDOR;
const char *host = "IP DEL SERVIDOR";

WiFiClient client;
void setup()
{
    pinMode(15,OUTPUT);//VERDE
    pinMode(13,OUTPUT);//AMARILLO
    pinMode(12,OUTPUT);//ROJO
    Serial.begin(9600);
    Serial.println("Connecting...\n");
    WiFi.mode(WIFI_STA);
    WiFi.begin("NOMBRE DE LA RED", "CONTRASEÑA DE LA RED");
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print(".");
    }
    delay(500);
}
//SI NO SE PUEDE ESTABLECER CONEXION CON EL SERVIDOR, NO SE TOMA EN CUENTA EL SENSOR, NO OBTIENE LOS DATOS

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

//CODIGO DE UN SEMAFORO QUE ENCIENDE UN LED DEPENDIENDO DEL VALOR DEL SENSOR
if(val<=100){
digitalWrite(12,HIGH);
digitalWrite(13,LOW);
digitalWrite(15,LOW);
}else if(val>=101&&val<=500){
digitalWrite(12,LOW);
digitalWrite(13,HIGH);
digitalWrite(15,LOW);
}else if(val>=501&&val<=1023){
digitalWrite(12,LOW);
digitalWrite(13,LOW);
digitalWrite(15,HIGH);
}

//IMPRIME EL VALOR DEL SENSOR EN EL MONITOR SERIAL
    Serial.print(val+"\n");
    //ENVIA EL VALOR DEL SENSOR AL SERVIDOR CON UN MENSAJE
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