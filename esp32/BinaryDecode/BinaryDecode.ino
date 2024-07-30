#define GPIO_PIN_0  25  // GPIO 19
#define GPIO_PIN_1  33  // GPIO 16
#define GPIO_PIN_2  26  // GPIO 26
#define GPIO_PIN_3  32  // GPIO 20

void setup() {
  Serial.begin(115200);

  // Set pin modes for input
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

  // Print the binary value
  Serial.print("Detected class index: ");
  Serial.println(binary_value);

  
  delay(250);  // Delay for 1 second
}
