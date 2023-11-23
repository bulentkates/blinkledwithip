int ledPin = 13;
void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}
void loop() {
  if (Serial.available() > 0) {
    char incomingByte = Serial.read();
    if (incomingByte == '1') {
      digitalWrite(ledPin, HIGH);  
    } else if (incomingByte == '2') {
      for (int i = 0; i < 5; i++) {
        digitalWrite(ledPin, HIGH);  
        delay(500);
        digitalWrite(ledPin, LOW);   
        delay(500);
      }
    } else if (incomingByte == '0') {
      digitalWrite(ledPin, LOW); 
    }
  }
}
