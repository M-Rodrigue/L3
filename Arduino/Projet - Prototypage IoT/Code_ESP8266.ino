// Librairies
#include <ESP8266WiFi.h>
#include "Adafruit_MQTT.h"
#include "Adafruit_MQTT_Client.h"

// Paramètres Wi-Fi
#define WLAN_SSID "OTERIA_Guest"
#define WLAN_PASS "OteriaCyberSchool$2022"

// Paramètres Adafruit IO
#define AIO_SERVER "io.adafruit.com"
#define AIO_SERVERPORT 1883
#define AIO_USERNAME "Binome"
#define AIO_KEY "aio_Cqko433njsgwQUnPXQHC9xpfXlRe"

// LED connexion Wi-Fi
int ledPin = 5; //D1 = GPIO5

// Création des classes
WiFiClient client;
Adafruit_MQTT_Client mqtt(&client, AIO_SERVER, AIO_SERVERPORT, AIO_USERNAME, AIO_KEY);
Adafruit_MQTT_Publish Attendance = Adafruit_MQTT_Publish(&mqtt, AIO_USERNAME "/feeds/TP-Arduino");

// Fonction de configuration
void setup() {

  // Initialisation de la communication série 9600 baud/s
  pinMode(ledPin,OUTPUT);
  digitalWrite(ledPin,LOW);
  Serial.begin(9600);
  delay(1000);

  // Connexion Wi-Fi
  Serial.println();
  delay(10);
  Serial.print("Connexion à ");
  Serial.println(WLAN_SSID);

  // Vérification de la connexion Wi-Fi
  WiFi.begin(WLAN_SSID, WLAN_PASS);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  // Connexion Wi-Fi effectuée
  digitalWrite(ledPin , HIGH);
  Serial.println();
  Serial.println("Connecté au Wi-Fi !");
  Serial.print("NodeMCU adresse IP : ");
  Serial.println(WiFi.localIP() );

  // Connexion Adafruit IO
  connect();
}

// Fonction connexion Adafruit IO en MQTT
void connect() {
  Serial.println("Connexion à Adafruit IO... ");
  int8_t ret;

  // Gestion des erreurs de connexion MQTT avec Adafruit IO
  while ((ret = mqtt.connect()) != 0) {
    switch (ret) {
      case 1: Serial.println("Wrong protocol"); break;
      case 2: Serial.println("ID rejected"); break;
      case 3: Serial.println("Server unavail"); break;
      case 4: Serial.println("Bad user/pass"); break;
      case 5: Serial.println("Not authed"); break;
      case 6: Serial.println("Failed to subscribe"); break;
      default: Serial.println("Connection failed"); break;
    }

   if(ret >= 0)
      mqtt.disconnect();

    Serial.println("Tentative de reconnexion...");
    delay(5000);
  }
  Serial.println("Connecté à Adafruit IO");
}

// Boucle infinie
void loop() {
  // Ping à Adafruit IO pour vérifier la connexion
  if(! mqtt.ping(3)) {
    // Reconnexion à Adafruit IO
    if(! mqtt.connected())
      connect();
  }
  
  if (Serial.available()){
    // Création d'un tableau de 9 caractères
    char data[9];

    // Récupération des informations du bus série
    for (int i = 0; i < 8 ; i++){
      data[i] = Serial.read();
    }

    // Publication vers Adafruit IO
    if (!Attendance.publish(data)){
      Serial.println("Echec");
    } else {
      Serial.println("Envoyé !");
    };
  };
}