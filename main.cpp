//M5stack-chanにコンパイルするプログラム
#include <M5Unified.h>
#include <Avatar.h>

using namespace m5avatar;

Avatar avatar;

const Expression expressions[] = {
  Expression::Angry,
  Expression::Sleepy,
  Expression::Happy,
  Expression::Sad,
  Expression::Doubt,
  Expression::Neutral
};
int play_time;
void setup() {
  // init lcd, serial, not init sd card
  M5.begin();
  M5.Power.begin();
  Serial.begin(115200);

  avatar.init();
}

// Add the main program code into the continuous loop() function
void loop() {
  M5.update();

  if(Serial.available()){
    play_time = Serial.read();
  }
  if(play_time == 65){
    avatar.setMouthOpenRatio(random(1, 15)*0.1);// if want use Releasefor; suggest use Release in press event
  }else if(play_time ==66){
    
  }
}
