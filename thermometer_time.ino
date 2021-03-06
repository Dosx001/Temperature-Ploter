#include <Wire.h>
#include <Adafruit_MLX90614.h>

Adafruit_MLX90614 mlx = Adafruit_MLX90614();

void setup() {
  Serial.begin(9600);
  Serial.println("Adafruit MLX90614 test");  
  mlx.begin();  
}

void loop() {
  Serial.print(mlx.readObjectTempF());
  Serial.print(' ');
  Serial.println(mlx.readAmbientTempF());
  delay(500);
}
