#define GPIO_PIN_0  32  // GPIO 20 - 1
#define GPIO_PIN_1  33  // GPIO 26 - 2
#define GPIO_PIN_2  25  // GPIO 16 - 4
#define GPIO_PIN_3  26  // GPIO 19 - 8

void setup() {
  Serial.begin(9600);
  pinMode(GPIO_PIN_0, INPUT);
  pinMode(GPIO_PIN_1, INPUT);
  pinMode(GPIO_PIN_2, INPUT);
  pinMode(GPIO_PIN_3, INPUT);
}

void loop() {
  // Read the state of each GPIO pin
  int bit0 = digitalRead(GPIO_PIN_0);
  int bit1 = digitalRead(GPIO_PIN_1);
  int bit2 = digitalRead(GPIO_PIN_2);
  int bit3 = digitalRead(GPIO_PIN_3);

  // Reconstruct the binary value
  int binary_value = (bit3 << 3) | (bit2 << 2) | (bit1 << 1) | bit0;

  // Print the detected class index and its binary representation
  Serial.print("Detected class index: ");
  Serial.print(binary_value);
  Serial.print(" (Binary: ");
  
  // Print binary representation with leading zeros for 4-bit value
  for (int i = 3; i >= 0; i--) {
    Serial.print((binary_value >> i) & 1);
  }
  
  Serial.println(")");

  delay(250);
}
