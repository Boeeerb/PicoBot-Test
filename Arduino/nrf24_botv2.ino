#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

#define CE_PIN 8
#define CSN_PIN 7

####################### Configuration ##############################
## lightintense needs changing to environment to find other Picos ##
## BotID is manually assigned to each, first will be 0, next is 1 ##
####################################################################
int lightintense = 400;
const int BotID = 0;

const uint64_t pipes[4] = { 
  0xABCDABCD71LL, 0xABCDABCD61LL, 0xABCDABCD51LL, 0xABCDABCD41LL };
const uint64_t srvpipe = 0xe8e8f0f0e1LL;
RF24 radio(CE_PIN, CSN_PIN);

const int white = 9;
const int trig = 18;
const int echo = 19;
const int ldr1 = A1;
const int ldr2 = A0;
const int motor1a = 2;
const int motor1b = 3;
const int motor2a = 4;
const int motor2b = 5;

const int redled = 6;
const int greled = 16;
const int bluled = 17;


int cm;
int light[2];
int role = 0;
int blah[2];
int id = 0;
int data;
int count = 0;
int colour = 0;

void setup() {
  digitalWrite(A0, HIGH);
  digitalWrite(A1, HIGH);
  pinMode(motor1a, OUTPUT); 
  pinMode(motor1b, OUTPUT); 
  pinMode(motor2a, OUTPUT); 
  pinMode(motor2b, OUTPUT);
  pinMode(white, OUTPUT);
   
  pinMode(redled, OUTPUT); 
  pinMode(greled, OUTPUT);
  pinMode(bluled, OUTPUT);

  Serial.begin(9600);
  radio.begin();
  radio.setChannel(0x4c);
  radio.setAutoAck(1);
  radio.setRetries(15,15);
  radio.setDataRate(RF24_250KBPS);
  radio.setPayloadSize(32);
  radio.openWritingPipe(srvpipe);
  radio.openReadingPipe(1,pipes[BotID]);

  digitalWrite(motor1a, LOW);
  digitalWrite(motor2a, LOW);
}

void loop()
{

  if ( role == 0 ) {
    digitalWrite(6, HIGH);
    blah[0] = BotID+1;
    radio.stopListening();
    radio.write( &blah, sizeof(blah) );
    digitalWrite(6, LOW);
    radio.startListening();
    while ( count < 100 ) {
      radio.read( &data, sizeof(data) );
      if ( data == 54 ) {
        role = 1;
        colour = 1;
      }
      if ( data == 55 ) {
        role = 1;
        colour = 2;
      }
      if ( data == 56 ) {
        role = 1;
        colour = 3;
      }
      if ( data == 57 ) {
        role = 1;
        colour = 4;
      }
      Serial.print( count );
      Serial.print( " - data: " );
      Serial.println( data );
      count++;
    }
    count = 0;

    delay(500);

  } 
  else {

    if ( colour == 1 ) {
        digitalWrite(redled, HIGH);
    }
    if ( colour == 2 ) {
        digitalWrite(greled, HIGH);
    }
    if ( colour == 3 ) {
        digitalWrite(bluled, HIGH);
    }
    if ( colour == 4 ) {
        digitalWrite(redled, HIGH);
        digitalWrite(greled, HIGH);
    }


    distance(cm);
    light[0] = analogRead(ldr1);
    light[1] = analogRead(ldr2);
    if ( cm > 20 ) {

      if ( light[0] < lightintense ) {
        digitalWrite(motor1a, LOW);
        digitalWrite(motor1b, HIGH);
      }
      else {
        digitalWrite(motor1a, LOW);
        digitalWrite(motor1b, LOW);
      }

      if ( light[1] < lightintense ) {
        digitalWrite(motor2a, LOW);
        digitalWrite(motor2b, HIGH);
      }
      else {
        digitalWrite(motor2a, LOW);
        digitalWrite(motor2b, LOW);
      }

      // Seek light
      if ( light[0] > lightintense && light[1] > lightintense ) {

        digitalWrite(motor1a, HIGH);
        digitalWrite(motor1b, LOW);
        digitalWrite(motor2a, LOW);
        digitalWrite(motor2b, HIGH);
      }

      digitalWrite(white, LOW);
    } 
    else {
      digitalWrite(motor1b, LOW);
      digitalWrite(motor2b, LOW);
      digitalWrite(motor1a, LOW);
      digitalWrite(motor2a, LOW);

      digitalWrite(white, HIGH);
    }
  }
}




void distance(int &ret) {

  long duration, cm;

  pinMode(echo, INPUT);
  pinMode(trig, OUTPUT);
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(5);
  digitalWrite(trig, LOW);

  duration = pulseIn(echo, HIGH);

  ret = duration / 29 / 2;

}






