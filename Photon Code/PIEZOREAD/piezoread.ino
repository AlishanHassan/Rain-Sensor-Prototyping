int piezopin = A0;
int piezovalue;
int testpin = A2;
int testout = 0;
int dir = 1;
int ledpin = D0;
int bucketpin = D1;
int bucketCount = 0;
int bucketFlip = 0;
int preBucketFlip = 0;
byte address = 0x11;
int CS = D5;

//SPI1 is pins D3 to D5

unsigned long elapsedTime;


void setup() {

    Serial.begin(9600);

    pinMode(piezopin, INPUT);
    pinMode(ledpin, OUTPUT);
    pinMode(testpin, OUTPUT);
    pinMode(bucketpin, INPUT);

    pinMode(CS, OUTPUT);
    SPI1.setClockDivider(SPI_CLOCK_DIV8);
    SPI1.begin(CS);

    //set digital pot resistance here -> R = 100e3 * (256 - value)/256 - 125
    digitalPotWrite(0x0F);

    Particle.variable("piezovalue", &piezovalue, INT);
 //   Spark.function("led",ledFlash);

    Particle.function("piezo",piezo);

    //PLX-DAQ stuff
    //Serial.println("CLEARDATA");
    //Serial.println("LABEL,Time,Elapsed,Piezo,Flip,Count");

    //Serial.println("Elapsed,PiezoValue,BucketFlip,BucketCount");


}

void loop() {

    analogWrite(testpin, testout);
    piezovalue = analogRead(piezopin);
    if (piezovalue > 500)
    {
        ledFlash(TRUE);
    }
    else
    {
        ledFlash(FALSE);
    }


    bucketFlip = digitalRead(bucketpin);
    bucketCounter();
    preBucketFlip = bucketFlip;

    //Serial.print(Time.now());
    elapsedTime = millis();


    //Serial.print("DATA,TIME,"); //PLX-DAQ doesn't want to work in Windows 7


    Serial.print(Time.timeStr());
    Serial.print(",");
    Serial.print(elapsedTime);
    Serial.print(",");
    Serial.print(piezovalue);
    Serial.print(",");
    Serial.print(bucketFlip);
    Serial.print(",");
    Serial.print(bucketCount);
    Serial.println();

    String returnString = Time.timeStr() + "," + elapsedTime + "," + piezovalue + "," + bucketFlip + "," + bucketCount;

    String piezoString = piezovalue + "";

    Particle.publish("Pizeo Value", piezoString);
    /*
    Serial.print(elapsedTime);
    Serial.print("   ");
    Serial.print(piezovalue);
    Serial.print("   ");
    Serial.print(bucketFlip);
    Serial.print("   ");
    Serial.print(bucketCount);

    Serial.println();
    */



    testFunction();


    delay(5);
}

void ledFlash(bool on) {

    if(on == TRUE)
    {
        digitalWrite(ledpin,HIGH);
    }
    else
    {
        digitalWrite(ledpin,LOW);
    }

}

void testFunction() {

    if(testout == 200)
    {
        dir = -1;
    }
    if(testout == 0)
    {
        dir = 1;
    }
    if(dir == 1)
    {
        testout += 1;
    }
    else
    {
        testout -= 1;
    }
}

void bucketCounter() {
    if(preBucketFlip == 0 && bucketFlip == 1)
    {
        bucketCount++;
    }

}

int digitalPotWrite(int value)
{
  digitalWrite(CS, LOW);
  SPI1.transfer(address);
  SPI1.transfer(value);
  digitalWrite(CS, HIGH);
}


int piezo(String command)
{
    return piezovalue;
}
