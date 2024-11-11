
int pwmPins[8] = {3,5,6,9,10,11,7,8};//pins 7 and 8 do not support pwm, just using to fill array
int pwmValues[8] = {0,0,0,0,0,0,0,0};

void setup() {
  Serial.begin(9600);
  SetPins();

}

void loop() {
 ParseData();
 WritePwm();
 PrintData();
}

//this function sets the pins wired to the LEDS as output pins. only 6 pins are assigned as output because pins 7 & 8 do not have pwm capabilty
void SetPins() { 
 for(int i = 0; i < 7; i++) {
  pinMode(pwmPins[i], OUTPUT);
 }
}//end SetPins

//This function reads in up to 8 CSV as input and stores them in an array
void ParseData(){
  //pwmValues[8] = '/0';
  if (Serial.available() > 0) {
    for(int i = 0; i < 8; i++) {
      pwmValues[i] = Serial.parseInt();
    } //end for loop
  } //end outer if
}//end function

//This function takes a CSV from the pwmValues array and writes its value to a digital pin. Up to 8 CSVs can be written to 8 separate pins
//Note: The arduino nano only has 6 pwm compatable pins so the last two values are assigned to pins(7 & 8) without PWM capabilty. 
void WritePwm() {
  int i;
  for(i = 0; i < 8; i++){
    analogWrite(pwmPins[i],pwmValues[i]);
  }//end for loop
}//end function

//Used to check the output to ensure data is being read in and assigned to the correct pins
void PrintData() {
  int i;
  for (i = 0; i < 8; i++) {
    Serial.print("Assigned: ");
    Serial.println(pwmValues[i]);
    Serial.print("to pin: ");
    Serial.println(pwmPins[i]);
  }
}//end function
  