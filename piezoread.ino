int piezopin = A0;
int piezovalue;

int ledpin = D0;

void setup() {
    
    Serial.begin(9600);
    pinMode(piezopin, INPUT);
    pinMode(ledpin, OUTPUT);
    
    Spark.variable("piezovalue", &piezovalue, INT);
 //   Spark.function("led",ledFlash);
    
        Spark.function("piezo",piezo);


}

void loop() {
    
    piezovalue = analogRead(piezopin);
    if (piezovalue > 500)
    {
        ledFlash();
    }
    Serial.println(piezovalue);
    delay(100);
}

void ledFlash() {

        digitalWrite(ledpin,HIGH);
        delay(50);
        digitalWrite(ledpin,LOW);

}

int piezo(String command)
{
    return piezovalue;
}