#include <Adafruit_GFX.h>
#include <Adafruit_SSD1351.h>
#include <SPI.h>

// Screen dimensions
#define SCREEN_WIDTH  128
#define SCREEN_HEIGHT 128

//Pin Definitions
#define SCLK_PIN 18
#define MOSI_PIN 23
#define DC_PIN   13
Turn#define CS_PIN    5 
#define RST_PIN  12

//Colour Definitions - Temporary will be fixed for spike
#define BLACK           0x0000
#define BLUE            0x001F
#define RED             0xF800
#define GREEN           0x07E0
#define CYAN            0x07FF
#define MAGENTA         0xF81F
#define YELLOW          0xFFE0  
#define WHITE           0xFFFF

//Initialise display lib and assign tft to screen.
Adafruit_SSD1351 tft = Adafruit_SSD1351(SCRAEEN_WIDTH, SCREEN_HEIGHT, CS_PIN, DC_PIN, MOSI_PIN, SCLK_PIN, RST_PIN);

void setup() {
  Serial.begin(9600);
  Serial.println("Hello!");
  tft.begin();
  tft.setRotation(0); // Roatate display if needed.
  Serial.println("Initialized");
  tft.fillRect(0, 0, 128, 128, BLUE); //Clear Display
  
}

void loop() {
  //Do Nothing
}
