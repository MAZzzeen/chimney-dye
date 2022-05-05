//mapping pins
#define S0 2
#define S1 3
#define S2 4
#define S3 5
#define sensorOut 6

//calibration
int whiteMin = 66;
int whiteMax = 282;

//making variables
int colordeg = 0;

int whiteValue;

//setting pin modes
void setup() {
 
  pinMode(S0, OUTPUT);
  pinMode(S1, OUTPUT);
  pinMode(S2, OUTPUT);
  pinMode(S3, OUTPUT);
  
  pinMode(sensorOut, INPUT);
  
  digitalWrite(S0,HIGH);
  digitalWrite(S1,LOW);
 
 //starting serial
  Serial.begin(57600);
}

void loop() {
 //getting values
  colordeg = getcolordeg();
  whiteValue = map(colordeg, whiteMin, whiteMax, 255, 0);
  delay(200);

  Serial.println(whiteValue);
}

int getcolordeg() {
  digitalWrite(S2,HIGH);
  digitalWrite(S3,LOW);

  int deg;
  deg = pulseIn(sensorOut,LOW);
  return deg;
}
