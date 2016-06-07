//Testing SPI on Arduino to control MCP41100
//Source: http://www.instructables.com/id/Digital-Potentiometer-MCP41100-and-Arduino/

#include <SPI.h>
byte address = 0x11;
int CS= 10;
int i=0;

void setup()
{
  pinMode (CS, OUTPUT);
  SPI.begin();
  digitalPotWrite(0x00);
  delay(1000);
  digitalPotWrite(0x80);
  delay(1000);
  digitalPotWrite(0xFF);
  delay(1000);
}

void loop()
{
    for (i = 0; i <= 255; i++)
    {
      digitalPotWrite(i);
      delay(10);
    }
    delay(500);
    for (i = 255; i >= 0; i--)
    {
      digitalPotWrite(i);
      delay(10);
    }
    delay(500);
}

int digitalPotWrite(int value)
{
  digitalWrite(CS, LOW);
  SPI.transfer(address);
  SPI.transfer(value);
  digitalWrite(CS, HIGH);
}
