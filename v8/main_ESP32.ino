#include <Adafruit_GFX.h>
#include <Adafruit_SSD1351.h>
#include <SPI.h>

// Screen dimensions
#define SCREEN_WIDTH  128
#define SCREEN_HEIGHT 128 // Change this to 96 for 1.27" OLED.

// You can use any (4 or) 5 pins 
#define SCLK_PIN 18
#define MOSI_PIN 23
#define DC_PIN   13
#define CS_PIN    5 
#define RST_PIN  12


#define GPIO_PIN_0  32  // GPIO 20 - 1
#define GPIO_PIN_1  33  // GPIO 26 - 2
#define GPIO_PIN_2  25  // GPIO 16 - 4
#define GPIO_PIN_3  26  // GPIO 19 - 8

#define BLACK 0x0000

struct Color {
    uint16_t hexCode;
};

Color colors[] = {
    {0xF800}, // 0
    {0x001F}, // 1
    {0xF800}, // 2
    {0x001F}, // 3
    {0xF800}, // 4
    {0x001F}, // 5
    {0x001F}, // 6
    {0x001F}, // 7
    {0xF800}, // 8
    {0x0000}, // 9 blank
    {0x0000}, // 10 blank
    {0x0000}, // 11 blank
    {0x0000}, // 12 blank
    {0x0000}, // 13 blank
    {0x0000}  // 14 blank
};

Adafruit_SSD1351 tft = Adafruit_SSD1351(SCREEN_WIDTH, SCREEN_HEIGHT, CS_PIN, DC_PIN, MOSI_PIN, SCLK_PIN, RST_PIN);

void setup() {
  Serial.begin(115200);
  Serial.println("Hello!");
  tft.begin();
  tft.setRotation(1); // Rotate the display if needed
  Serial.println("Initialized");
  tft.fillRect(0, 0, 128, 128, BLACK); //Clear Display 

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

  // Check if the index is within bounds
  if (binary_value >= 0 && binary_value < sizeof(colors) / sizeof(colors[0])) {
      // Set the screen color to the associated color in the array
      uint16_t color = colors[binary_value].hexCode;
      tft.fillRect(0, 0, 128, 128, color);
  } else {
      // If index is out of bounds, set the screen to black
      tft.fillRect(0, 0, 128, 128, BLACK);
  }
  
  delay(250);
}
