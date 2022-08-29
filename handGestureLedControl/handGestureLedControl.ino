#include<cvzone.h>

SerialData serialdata(1,4);
int receiveData[1];
int led = 9;


void setup() {
  serialdata.begin();
  pinMode(led,OUTPUT);
  
}

void loop() {
  serialdata.Get(receiveData);
  analogWrite(led,receiveData[0]);  
  
}
