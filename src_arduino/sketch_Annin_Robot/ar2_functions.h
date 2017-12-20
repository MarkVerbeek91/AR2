#ifndef AR2_FUNCS   // if x.h hasn't been included yet...
#define AR2_FUNCS   //   #define this so the compiler knows it has been included

#include <Servo.h>

void writeServerPosition(int, int, int, int, Servo);
void calibrateRobot(String);
void moveRobot(String);
#endif 

