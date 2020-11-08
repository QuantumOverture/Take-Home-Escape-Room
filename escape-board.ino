#include <LiquidCrystal.h>
#include <Keypad.h>
const byte ROWS = 2;
const byte COLS = 2;
char hexaKeys[ROWS][COLS] = {
  {'1','2'},
  {'4','5'}
};
byte rowPins[ROWS] = {13, 7};
byte colPins[COLS] = {8, 1};
Keypad customKeypad = Keypad( makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS);
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
String wireModel;
String rgbModel;
int randWire;
int div3[4] = {0, 3, 6, 9};
int ind3;
int i;
const int alex = A0;
const int rgb = A1;
String keyModel;
int keys[4] = {1, 2, 4, 5};
String pass;
int counter = 0;
const int redLEDPin = 10;
const int blueLEDPin = 9;
const int greenLEDPin = 6;
String colors[5] = {"red", "magenta", "blue", "green"};
unsigned long interval = 500;
long previousTime = -500;
int ind4;
int nextColor = -1;
int digit;
long pressTime = -1;
long holdTime = -1;
int modInd;
String modelArray[3];
void setup() {
  Serial.begin(9600);
  lcd.begin(16,2);
  lcd.setCursor(0,1);
  for(i = 0; i < 8; i++) {
    randomSeed(analogRead(5));
    ind3 = random(4);
    wireModel += div3[ind3];
  }
  Serial.println(wireModel);
  randomSeed(analogRead(5));
  randWire = random(3);
  Serial.println(randWire);
  for(i=0; i < 4; i++) {
    randomSeed(analogRead(5));
    ind3 = random(10);
    keyModel += 0;
    keyModel += ind3;
  }
  Serial.println(keyModel);
  for (i=0; i < 4; i++) {
    randomSeed(analogRead(5));
    ind3 = random(4);
    pass += keys[ind3];
  }
  Serial.println(pass);
    for(i=0; i < 4; i++) {
    randomSeed(analogRead(5));
    ind3 = random(10);
    rgbModel += 4;
    rgbModel += ind3;
  }
  Serial.println(rgbModel);
  pinMode(greenLEDPin, OUTPUT);
  pinMode(redLEDPin, OUTPUT);
  pinMode(blueLEDPin, OUTPUT);
  randomSeed(analogRead(5));
  ind3 = random(4);
  ind3 = 2;
  Serial.println(ind3);
  if(ind3 == 0) {
    analogWrite(redLEDPin,255);
    analogWrite(greenLEDPin,0);
    analogWrite(blueLEDPin,0);
  }
  else if(ind3 == 1) {
    analogWrite(redLEDPin,255);
    analogWrite(greenLEDPin,0);
    analogWrite(blueLEDPin,255);
  }
  else if(ind3 == 2) {
    analogWrite(redLEDPin,0);
    analogWrite(greenLEDPin,0);
    analogWrite(blueLEDPin,255);
  }
  else {
    analogWrite(redLEDPin,0);
    analogWrite(greenLEDPin,255);
    analogWrite(blueLEDPin,0);
  }
  randomSeed(analogRead(5));
  digit = random(11);
  Serial.println(digit);
  if (digit != 10) {
    randomSeed(analogRead(5));
    nextColor = random(4);
  }
  randomSeed(analogRead(5));
  modInd = random(3);
  randWire = 1;
  pass = "4411";
  wireModel = "39663336";
  keyModel = "01020304";
  rgbModel = "41424344";
  nextColor = 2;
  digit = 3;
  modelArray[0] = wireModel;
  modelArray[1] = keyModel;
  modelArray[2] = rgbModel;
}

void loop() {
  unsigned long currentTime = millis();
  if (120000 - currentTime >= 100000) {
    lcd.setCursor(13,0);
  }
  else if (120000 - currentTime >= 10000) {
    lcd.setCursor(13,0);
    lcd.print(" ");
    lcd.setCursor(14,0);
  }
  else {
    lcd.setCursor(14,0);
    lcd.print(" ");
    lcd.setCursor(15,0);
  }
  if (120000 - currentTime >= 1000) {
    lcd.print(120000 - currentTime);
  }
  else {
    Serial.println("Failure");
    lcd.clear();
    lcd.print("YOU DIED TIME");
    exit(0);
  }
  if(currentTime - previousTime > interval*2) {
    lcd.setCursor(0,1);
    previousTime = currentTime;
    lcd.print(modelArray[modInd]);
    modInd++;
    if (modInd == 3) {
      modInd = 0;
    }
  }
  // put your main code here, to run repeatedly:
  int alexV = analogRead(alex);
  //Serial.println(alexV);
  if(randWire == 0 && alexV < 409) {
    Serial.println("Success");
  }
  else if(randWire == 1 && alexV > 409 && alexV < 556) {
    Serial.println("Success");
  }
  else if(randWire == 2 && alexV > 556 && alexV < 597) {
    Serial.println("Success");
  }
  else if (alexV < 596) {
    Serial.println(alexV);
    Serial.println("Failure");
    lcd.clear();
    lcd.print("YOU DIED VOLT");
    exit(0);
  }
  char customKey = customKeypad.getKey();
  if(customKey){
    Serial.println(customKey);
  }
  if (counter < 4 && customKey && customKey == pass[counter]) {
    counter++;
    if(counter == 4){
      Serial.println("Access granted");
    }
  }
  else if (counter < 4 && customKey && customKey != pass[counter]) {
    Serial.println("Failure");
    lcd.clear();
    lcd.print("YOU DIED");
    exit(0);
  }
  if (pressTime == -1 && analogRead(rgb) > 509) {
    pressTime = currentTime;
    Serial.println("Pressed");
    Serial.println(pressTime);
    if(nextColor != -1 && nextColor == 0) {
      analogWrite(redLEDPin,255);
      analogWrite(greenLEDPin,0);
      analogWrite(blueLEDPin,0);
    }
    else if(nextColor == 1) {
      analogWrite(redLEDPin,255);
      analogWrite(greenLEDPin,0);
      analogWrite(blueLEDPin,255);
    }
    else if(nextColor == 2) {
      analogWrite(redLEDPin,0);
      analogWrite(greenLEDPin,0);
      analogWrite(blueLEDPin,255);
    }
    else {
      analogWrite(redLEDPin,0);
      analogWrite(greenLEDPin,255);
      analogWrite(blueLEDPin,0);
    }
  }
  if (pressTime != -1 && analogRead(rgb) < 509) {
    holdTime = currentTime - pressTime;
    Serial.println("Released");
    Serial.println(currentTime);
    pressTime = -1;
  }
  if (pressTime == -1 && holdTime != -1 && digit == 10 && holdTime > interval) {
    Serial.println(holdTime);
    Serial.println("Failure");
    lcd.clear();
    lcd.print("YOU DIED PRESS");
    exit(0);
    holdTime = -1;
  }
  unsigned long currTimeSec = int(currentTime/1000);
  //Serial.println(currTimeSec);
  String stringTime = String(119 - currTimeSec);
  //Serial.println(stringTime);
  if (pressTime == -1 && holdTime != -1 && digit != 10) {
    int i;
    int indFound = 0;
    for (i = 0; i < stringTime.length(); i++) {
      if (String(stringTime[i]).equals(String(digit))) {
        indFound = 1;
        Serial.println(indFound);
      }
    }
    if (!indFound) {
      Serial.println("Failure");
      lcd.clear();
      lcd.print("YOU DIED");
      Serial.println(stringTime);
      exit(0);
      holdTime = -1;
    }
    else {
      Serial.println("Success");
      holdTime = -1;
    }
  }
}
