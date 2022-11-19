#define S_sensorPin A1 // Arduino pin that connects to AOUT pin of moisture sensor


void setup() {
  Serial.begin(9600); // Begin serial communication at 9600 baud rate
}

void loop() {

  int S_value = analogRead(S_sensorPin); // read the analog value from sensor

  if (S_value < 100)
    Serial.print("The soil is DRY (");
  else
    Serial.print("The soil is WET (");

  Serial.print(S_value);
  Serial.println(")");

  delay(1000);
}