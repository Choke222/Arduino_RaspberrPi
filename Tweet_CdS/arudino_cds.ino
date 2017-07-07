int pin = 0; //センサーのピン番号
int get_a0 = 0; //センサーデータ取得用
int flag = 0;
int s=0;
void setup(){
  Serial.begin(9600);

}

void loop()
{

  get_a0 = analogRead(pin); // 照度センサーからデータを取得
  s = 0;
  Serial.println(s); // シリアルモニタに出力
  if ( get_a0 <= 200 ) {
    if(flag == 0){
      s = 1000;//OFF!
      Serial.println(s); // シリアルモニタに出力
    }
    flag=1;
  } else if ( get_a0 > 200 ) {
    if(flag == 1){
      s = 2000;//ON
      Serial.println(s); // シリアルモニタに出力
    }
    flag=0;
  }
  delay(200);
}