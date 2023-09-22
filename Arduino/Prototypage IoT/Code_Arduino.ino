// Librairies
#include <LiquidCrystal_I2C.h>
#include <RFID.h>
#include <SPI.h>
#include <SoftwareSerial.h>

// Définitions
#define LED_PIN 5
#define LED_PIN 6
#define LED_PIN 7
#define SS_PIN 10
#define RST_PIN 5

// Création des classes
LiquidCrystal_I2C lcd(0x27, 16, 2);
SoftwareSerial serie(2, 3);
RFID rfid(10, 9);
unsigned char status;
unsigned char str[MAX_LEN];  //MAX_LEN c'est 16 : taille du tableau

// Fonction vérification transmission I2C
bool I2CAddrTest(uint8_t addr) {
  Wire.begin();
  Wire.beginTransmission(addr);

  // Gère la fin de transmission
  if (Wire.endTransmission() == 0) {
    return true;
  } else {
    return false;
  };
};

// Fonction vérification type badge
void TypeBadge(unsigned char* type) {
  Serial.print("Type de carte : ");
  if (type[0] == 0x04 && type[1] == 0x00) {
    Serial.println("MFOne-S50");
  } else if (type[0] == 0x02 && type[1] == 0x00) {
    Serial.println("MFOne-S70");
  } else if (type[0] == 0x44 && type[1] == 0x00) {
    Serial.println("MF-UltraLight");
  } else if (type[0] == 0x08 && type[1] == 0x00) {
    Serial.println("MF-Pro");
  } else if (type[0] == 0x44 && type[1] == 0x03) {
    Serial.println("MF Desire");
  } else {
    Serial.println("Inconnu");
  };
};

// Configuration
void setup() {
  // Sorties PIN
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);

  // Test adresse I2C
  if (!I2CAddrTest(0x27)) {
    lcd = LiquidCrystal_I2C(0x3F, 16, 2);
  };

  // Initialisations écran LCD, série 9600 bauds, bus SPI et RFID
  lcd.init();
  Serial.begin(9600);
  serie.begin(9600);
  SPI.begin();
  rfid.init();

  // Affichage écran LCD
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Présentez badge");
  Serial.print("\n- Présentez badge :\n");
};

// Boucle infinie
void loop() {
  LectureBadge();
};

// Fonctions
void LEDbleue() {  // Allume LED bleue
  digitalWrite(5, LOW);
  digitalWrite(7, HIGH);
  digitalWrite(6, HIGH);
};

void LEDrouge() {  // Clignote LED rouge
  digitalWrite(7, LOW);
  digitalWrite(6, HIGH);
  digitalWrite(5, HIGH);
  delay(2000);
  digitalWrite(5, HIGH);
  digitalWrite(6, HIGH);
  digitalWrite(7, HIGH);
  delay(100);
};

void LEDvert() {  // Clignote LED vert
  digitalWrite(5, HIGH);
  digitalWrite(6, LOW);
  digitalWrite(7, HIGH);
  delay(2000);
  digitalWrite(5, HIGH);
  digitalWrite(6, HIGH);
  digitalWrite(7, HIGH);
  delay(100);
};

void LEDoff() {  // Eteindre LED
  digitalWrite(5, HIGH);
  digitalWrite(6, HIGH);
  digitalWrite(7, HIGH);
};

void LectureBadge() {  // Lecture et identification badge RFID
  String numeroAutorise = "630c68ad"; // Numéro du badge autorisé
  LEDbleue();

  if (rfid.findCard(PICC_REQIDL, str) == MI_OK) {  // Recherche carte et retourne le type
    String numeroCarte="";
    Serial.println("Carte trouvée");
    TypeBadge(str);  // Affiche le type de carte
    bool auth = 0; // Variable authentification

    // Détection anti-collision et lecture numéro série carte
    if (rfid.anticoll(str) == MI_OK) {  
      Serial.print("Numéro de la carte : ");
      for(int i = 0; i < 4; i++) {
        // Incrémentation de la variable avec le numéro de la carte
        numeroCarte += String(0x0F & (str[i] >> 4), HEX);
        numeroCarte += String(0x0F & str[i], HEX);
      }

      // Affiche numéro carte
      Serial.print(numeroCarte);
      Serial.print("\n");

      // Vérification du numéro
      if (numeroCarte == numeroAutorise){
        auth = 1;
      } else {
        auth = 0;
      };
    };

    // Envoi numéro carte
    serie.print(numeroCarte);
    Serial.print("Envoyé");
    Serial.print(numeroCarte);

    // Test de l'authentification
    if(auth == 1){
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Acces autorisé");
      LEDoff();
      LEDvert();
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Présentez badge");
    } else {
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Acces refusé");
      LEDoff();
      LEDrouge();
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Présentez badge");
    };
    rfid.selectTag(str); //card selection (lock card to prevent redundant read, //removing //the line will make the sketch read cards continually)
  };
  rfid.halt();  // command the card to enter sleeping state
};