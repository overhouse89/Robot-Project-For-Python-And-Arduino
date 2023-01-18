
// LIBRARIES
#include <Servo.h>

// SERVOS
Servo rightArmServo;
Servo rightHandServo;
Servo headServo;
Servo leftArmServo;

// LEDS NUMBERS
int ledPin1 = 5;
int ledPin2 = 6;

// DELAY NUMBER
int delayTime = 500;

// SERVOS NUMBERS
float servoNum1 = 0;
float servoNum2 = 0;
float servoNum3 = 0;

String read_text;

void setup()
{
  // SERIAL
	Serial.begin(9600);

/*
  // RIGHT ARM
  rightArmServo.attach(12);

  // RIGHT HAND
  rightHandServo.attach(3);

  // LEFT ARM
  leftArmServo.attach(2);

  // HEAD
  headServo.attach(4);

  // WRITE FOR SERVOS
  rightArmServo.write(180);
  rightHandServo.write(70);
  leftArmServo.write(180);
  headServo.write(50);

  // DELAY
  delay(1000);
*/

  // TWO LEDS
	pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
}

void loop()
{

  // SERIAL IS SEARCING A LINE
  if (Serial.available())
  {
    read_text = Serial.readString();  // Read a data
  }

  // -- ROBOT'S EYES -- //
  if (read_text == 'a')  // Eyes on
  {
    digitalWrite(ledPin1, HIGH);
    digitalWrite(ledPin2, HIGH);
  }
  else if (read_text == 'b')  // Eyes off
  {
    digitalWrite(ledPin1, LOW);
    digitalWrite(ledPin2, LOW);  
  }

  /*

  // SERVOS ARE RUNNING
  if (servoNum1 < -130)
  {
    if (servoNum2 < -130)
    {
      servoNum2 = -131;
      delay(1000);
      servoNum1 = 0;
      servoNum2 = 0;
    }
    else
    {
      servoNum1 = -131;
      servoNum2 -= 0.8;

      rightArmServo.write(50 - servoNum2);
      leftArmServo.write(50 - servoNum2);

      Serial.println(servoNum2);
    }
  }
  else
  {
    servoNum1 -= 0.8;

    rightArmServo.write(180 + servoNum1);
    leftArmServo.write(180 + servoNum1);

    Serial.println(servoNum1);
  }
  */
}

