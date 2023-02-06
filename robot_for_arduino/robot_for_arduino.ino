
// LIBRARIES
#include <Servo.h>

// SERVOS
Servo rightArmServo;
Servo rightHandServo;
Servo leftArmServo;
Servo leftHandServo;
Servo headServo;

// LEDS NUMBERS
int ledPin1 = 5;
int ledPin2 = 6;

// DELAY NUMBER
int delayTime = 500;

// BOOLEANS
bool stopping_h_bool = true;
bool stopping_ra_bool = true;
bool stopping_la_bool = true;
bool stopping_allb_bool = true;

// STRINGS
String read_text;

void setup()
{
  // SERIAL
	Serial.begin(9600);
  
  // RIGHT ARM
  rightArmServo.attach(12);

  // RIGHT HAND
  rightHandServo.attach(3);

  // LEFT ARM
  leftArmServo.attach(2);

  // LEFT HAND
  leftHandServo.attach(4);

  // HEAD
  headServo.attach(7);

  // WRITE FOR RIGHT SERVOS
  rightArmServo.write(110);
  rightHandServo.write(110);
  
  // WRITE FOR LEFT SERVOS
  leftArmServo.write(90); 
  leftHandServo.write(110);

  // WRITE FOR HEAD   ----   ANGLE:  20 ---> 50 ---> 80
  headServo.write(50);

  delay(500);

  // TWO LEDS
	pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);

  // EYES (LEDS) ARE TURNING
  digitalWrite(ledPin1, HIGH);
  digitalWrite(ledPin2, HIGH);
}

void loop()
{

  // SERIAL IS SEARCHING A LINE
  if (Serial.available())
  {
      read_text = Serial.readString();  // Read a data
  }

  // -- ROBOT'S BODY -- //
  if (read_text == "H" && stopping_h_bool == true)  // Head
  {
    stopping_ra_bool = false;
    stopping_la_bool = false;
    stopping_allb_bool = false;
    
    delay(delayTime);
    
    for(int h_body = 50; h_body < 110; h_body += 1)
    {
      headServo.write(h_body);
      delay(8);
    }
    delay(delayTime);
    for(int h_body = 110; h_body >= 0; h_body -= 1)
    {
      headServo.write(h_body);
      delay(8);
    }
    delay(delayTime);
    for(int h_body = 0; h_body < 50; h_body += 1) 
    {
      headServo.write(h_body);
      delay(8);
    }
    
    delay(delayTime);
    
    read_text = "";
    
    stopping_ra_bool = true;
    stopping_la_bool = true;
    stopping_allb_bool = true;
  }
  if (read_text == "RA" && stopping_ra_bool == true)  // Right arm
  {
    stopping_h_bool = false;
    stopping_la_bool = false;
    stopping_allb_bool = false;
    
    delay(delayTime);
    
    for(int ra_body = 110; ra_body > 20; ra_body -= 1)
    {
      rightArmServo.write(ra_body);
      delay(10);
    }
    for(int ra_body = 110; ra_body > 10; ra_body -= 1)
    {
      rightHandServo.write(ra_body);
      delay(8);
    }
    for(int ra_body = 10; ra_body < 110; ra_body += 1)
    {
      rightHandServo.write(ra_body);
      delay(8);
    }
    for(int ra_body = 20; ra_body < 110; ra_body += 1)
    {
      rightArmServo.write(ra_body);
      delay(10);
    }
    
    delay(delayTime);
    
    read_text = "";
    
    stopping_h_bool = true;
    stopping_la_bool = true;
    stopping_allb_bool = true;
  }
  if (read_text == "LA" && stopping_la_bool == true)  // Left arm
  {
    stopping_h_bool = false;
    stopping_ra_bool = false;
    stopping_allb_bool = false;

    delay(delayTime);

    for(int la_body = 90; la_body < 180; la_body += 1)
    {
      leftArmServo.write(la_body);
      delay(10);
    }
    for(int la_body = 110; la_body < 180; la_body += 1)
    {
      leftHandServo.write(la_body);
      delay(8);
    }
    for(int la_body = 180; la_body > 110; la_body -= 1)
    {
      leftHandServo.write(la_body);
      delay(8);
    }
    for(int la_body = 180; la_body > 90; la_body -= 1)
    {
      leftArmServo.write(la_body);
      delay(10);
    }

    delay(delayTime);
    
    read_text = "";
    
    stopping_h_bool = true;
    stopping_ra_bool = true;
    stopping_allb_bool = true;
  }
  if (read_text == "ALLB" && stopping_allb_bool == true)  // All bodies
  {
    stopping_h_bool = false;
    stopping_ra_bool = false;
    stopping_la_bool = false;
    
    delay(delayTime);
    
    for(int all_body = 50; all_body < 110; all_body += 1)
    {
      headServo.write(all_body);
      delay(8);
    }
    delay(delayTime);
    for(int ra_body = 110; ra_body > 20; ra_body -= 1)
    {
      rightArmServo.write(ra_body);
      delay(10);
    }
    for(int ra_body = 110; ra_body > 10; ra_body -= 1)
    {
      rightHandServo.write(ra_body);
      delay(8);
    }
    for(int ra_body = 10; ra_body < 110; ra_body += 1)
    {
      rightHandServo.write(ra_body);
      delay(8);
    }
    delay(delayTime);
    for(int ra_body = 20; ra_body < 110; ra_body += 1)
    {
      rightArmServo.write(ra_body);
      delay(10);
    }
    delay(delayTime);
    for(int all_body = 110; all_body >= 0; all_body -= 1)
    {
      headServo.write(all_body);
      delay(8);
    }
    delay(delayTime);
    for(int la_body = 90; la_body < 180; la_body += 1)
    {
      leftArmServo.write(la_body);
      delay(10);
    }
    for(int la_body = 110; la_body < 180; la_body += 1)
    {
      leftHandServo.write(la_body);
      delay(8);
    }
    for(int la_body = 180; la_body > 110; la_body -= 1)
    {
      leftHandServo.write(la_body);
      delay(8);
    }
    delay(delayTime);
    for(int la_body = 180; la_body > 90; la_body -= 1)
    {
      leftArmServo.write(la_body);
      delay(10);
    }
    delay(delayTime);
    for(int all_body = 0; all_body < 50; all_body += 1) 
    {
      headServo.write(all_body);
      delay(8);
    }

    delay(delayTime);
    
    read_text = "";
    
    stopping_h_bool = true;
    stopping_ra_bool = true;
    stopping_la_bool = true;
  }
  
}
