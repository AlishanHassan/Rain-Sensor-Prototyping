byte address = 0x11;
int CS= D5;
int i=0;


void setup()
{
    pinMode(CS, OUTPUT);
    Serial.begin(9600);
    SPI1.setClockDivider(SPI_CLOCK_DIV8);
    //SPI1.setDataMode(SPI_MODE0);
    //SPI1.setBitOrder(LSBFIRST);
    SPI1.begin(CS);
    digitalPotWrite(0x00);
    delay(1000);

    digitalPotWrite(0x80);
    delay(1000);byte address = 0x11;
int CS= D5;
int i=0;


void setup()
{
    pinMode(CS, OUTPUT);
    Serial.begin(9600);
    SPI1.setClockDivider(SPI_CLOCK_DIV8);
    //SPI1.setDataMode(SPI_MODE0);
    //SPI1.setBitOrder(LSBFIRST);
    SPI1.begin(CS);
    digitalPotWrite(0x00);
    delay(1000);

    digitalPotWrite(0x80);
    delay(1000);

   // adjust Lowest Resistance .
   digitalPotWrite(0xFF);
   delay(1000);


}


void loop()
{
    /*
    digitalWrite(CS, LOW);
    SPI1.transfer(address);
    SPI1.transfer(100);
    digitalWrite(CS, HIGH);
    Serial.println(address);
*/

    for (i = 0; i <= 255; i++)
    {
      digitalPotWrite(i);
      //Serial.println("Pot up");
      delay(10);
    }
    delay(500);
    Serial.println("Pot flip");
    for (i = 255; i >= 0; i--)
    {
      digitalPotWrite(i);
      //Serial.println("Pot down");
      delay(10);
    }
    Serial.println("Pot flip");
}

int digitalPotWrite(int value)
{
  digitalWrite(CS, LOW);
  SPI1.transfer(address);
  Serial.println(address);
  SPI1.transfer(value);
  Serial.println(value);
  digitalWrite(CS, HIGH);
}


   // adjust Lowest Resistance .
   digitalPotWrite(0xFF);
   delay(1000);


}


void loop()
{
    /*
    digitalWrite(CS, LOW);
    SPI1.transfer(address);
    SPI1.transfer(100);
    digitalWrite(CS, HIGH);
    Serial.println(address);
*/

    for (i = 0; i <= 255; i++)
    {
      digitalPotWrite(i);
      //Serial.println("Pot up");
      delay(10);
    }
    delay(500);
    Serial.println("Pot flip");
    for (i = 255; i >= 0; i--)
    {
      digitalPotWrite(i);
      //Serial.println("Pot down");
      delay(10);
    }
    Serial.println("Pot flip");
}

int digitalPotWrite(int value)
{
  digitalWrite(CS, LOW);
  SPI1.transfer(address);
  Serial.println(address);
  SPI1.transfer(value);
  Serial.println(value);
  digitalWrite(CS, HIGH);
}
