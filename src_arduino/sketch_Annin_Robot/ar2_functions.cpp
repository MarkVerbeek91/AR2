/*
   Collection of command function of the AR2 arduino



*/
#include <Servo.h>
#include <ArduinoUnit.h>

#include "ar2_functions.h"

test(wirteServerPosition)
{
  assertTrue(true);
}

void writeServerPosition(int Start, int Stop, int servoNum, int servoPos, Servo servo0)
{

  if (servoNum == 0)
  {
    servo0.write(servoPos);
  }
  /*
    if (servoNum == 1)
    {
    servo1.write(servoPOS);
    }
    if (servoNum == 2)
    {
    servo2.write(servoPOS);
    }
    if (servoNum == 3)
    {
    servo3.write(servoPOS);
    }
    if (servoNum == 4)
    {
    servo4.write(servoPOS);
    }
    if (servoNum == 5)
    {
    servo5.write(servoPOS);
    }
    if (servoNum == 6)
    {
    servo6.write(servoPOS);
    }
    if (servoNum == 7)
    {
    servo7.write(servoPOS);
    }
  */

  return;
}


void calibrateRobot(String inData)
{
  /*
    int J1start = inData.indexOf('A');
    int J2start = inData.indexOf('B');
    int J3start = inData.indexOf('C');
    int J4start = inData.indexOf('D');
    int J5start = inData.indexOf('E');
    int J6start = inData.indexOf('F');
    int J1step = (inData.substring(J1start + 1, J2start).toInt()) + 200;
    int J2step = (inData.substring(J2start + 1, J3start).toInt()) + 200;
    int J3step = (inData.substring(J3start + 1, J4start).toInt()) + 200;
    int J4step = (inData.substring(J4start + 1, J5start).toInt()) + 200;
    int J5step = (inData.substring(J5start + 1, J6start).toInt()) + 200;
    int J6step = (inData.substring(J6start + 1).toInt()) + 200;

    //RESET COUNTERS
    int J1done = 0;
    int J2done = 0;
    int J3done = 0;
    int J4done = 0;
    int J5done = 0;
    int J6done = 0;

    String J1calStat = "0";

    //SET DIRECTIONS
    // J1 //
    if (J1rotdir == 1 && J1caldir == 1) {
      digitalWrite(J1dirPin, HIGH);
    }
    else if (J1rotdir == 0 && J1caldir == 1) {
      digitalWrite(J1dirPin, LOW);
    }
    else if (J1rotdir == 1 && J1caldir == 0) {
      digitalWrite(J1dirPin, LOW);
    }
    else if (J1rotdir == 0 && J1caldir == 0) {
      digitalWrite(J1dirPin, HIGH);
    }

    // J2 //
    if (J2rotdir == 1 && J2caldir == 1) {
      digitalWrite(J2dirPin, HIGH);
    }
    else if (J2rotdir == 0 && J2caldir == 1) {
      digitalWrite(J2dirPin, LOW);
    }
    else if (J2rotdir == 1 && J2caldir == 0) {
      digitalWrite(J2dirPin, LOW);
    }
    else if (J2rotdir == 0 && J2caldir == 0) {
      digitalWrite(J2dirPin, HIGH);
    }

    // J3 //
    if (J3rotdir == 1 && J3caldir == 1) {
      digitalWrite(J3dirPin, HIGH);
    }
    else if (J3rotdir == 0 && J3caldir == 1) {
      digitalWrite(J3dirPin, LOW);
    }
    else if (J3rotdir == 1 && J3caldir == 0) {
      digitalWrite(J3dirPin, LOW);
    }
    else if (J3rotdir == 0 && J3caldir == 0) {
      digitalWrite(J3dirPin, HIGH);
    }

    // J4 //
    if (J4rotdir == 1 && J4caldir == 1) {
      digitalWrite(J4dirPin, HIGH);
    }
    else if (J4rotdir == 0 && J4caldir == 1) {
      digitalWrite(J4dirPin, LOW);
    }
    else if (J4rotdir == 1 && J4caldir == 0) {
      digitalWrite(J4dirPin, LOW);
    }
    else if (J4rotdir == 0 && J4caldir == 0) {
      digitalWrite(J4dirPin, HIGH);
    }

    // J5 //
    if (J5rotdir == 1 && J5caldir == 1) {
      digitalWrite(J5dirPin, HIGH);
    }
    else if (J5rotdir == 0 && J5caldir == 1) {
      digitalWrite(J5dirPin, LOW);
    }
    else if (J5rotdir == 1 && J5caldir == 0) {
      digitalWrite(J5dirPin, LOW);
    }
    else if (J5rotdir == 0 && J5caldir == 0) {
      digitalWrite(J5dirPin, HIGH);
    }

    // J6 //
    if (J6rotdir == 1 && J6caldir == 1) {
      digitalWrite(J6dirPin, HIGH);
    }
    else if (J6rotdir == 0 && J6caldir == 1) {
      digitalWrite(J6dirPin, LOW);
    }
    else if (J6rotdir == 1 && J6caldir == 0) {
      digitalWrite(J6dirPin, LOW);
    }
    else if (J6rotdir == 0 && J6caldir == 0) {
      digitalWrite(J6dirPin, HIGH);
    }

    int Speed = 1200;

    //DRIVE MOTORS FOR CALIBRATION
    while (digitalRead(J1calPin) == LOW && J1done < J1step || digitalRead(J2calPin) == LOW && J2done < J2step || digitalRead(J3calPin) == LOW && J3done < J3step || digitalRead(J4calPin) == LOW && J4done < J4step || digitalRead(J5calPin) == LOW && J5done < J5step || digitalRead(J6calPin) == LOW && J6done < J6step)
    {
      if (J1done < J1step && (digitalRead(J1calPin) == LOW))
      {
        digitalWrite(J1stepPin, LOW);
      }
      delayMicroseconds(5);
      if (J1done < J1step && (digitalRead(J1calPin) == LOW))
      {
        digitalWrite(J1stepPin, HIGH);
        J1done = ++J1done;
      }
      delayMicroseconds(5);
      if (J2done < J2step && (digitalRead(J2calPin) == LOW))
      {
        digitalWrite(J2stepPin, LOW);
      }
      delayMicroseconds(5);
      if (J2done < J2step && (digitalRead(J2calPin) == LOW))
      {
        digitalWrite(J2stepPin, HIGH);
        J2done = ++J2done;
      }
      delayMicroseconds(5);
      if (J3done < J3step && (digitalRead(J3calPin) == LOW))
      {
        digitalWrite(J3stepPin, LOW);
      }
      delayMicroseconds(5);
      if (J3done < J3step && (digitalRead(J3calPin) == LOW))
      {
        digitalWrite(J3stepPin, HIGH);
        J3done = ++J3done;
      }
      delayMicroseconds(5);
      if (J4done < J4step && (digitalRead(J4calPin) == LOW))
      {
        digitalWrite(J4stepPin, LOW);
      }
      delayMicroseconds(5);
      if (J4done < J4step && (digitalRead(J4calPin) == LOW))
      {
        digitalWrite(J4stepPin, HIGH);
        J4done = ++J4done;
      }
      delayMicroseconds(5);
      if (J5done < J5step && (digitalRead(J5calPin) == LOW))
      {
        digitalWrite(J5stepPin, LOW);
      }
      delayMicroseconds(5);
      if (J5done < J5step && (digitalRead(J5calPin) == LOW))
      {
        digitalWrite(J5stepPin, HIGH);
        J5done = ++J5done;;
      }
      delayMicroseconds(5);
      if (J6done < J6step && (digitalRead(J6calPin) == LOW))
      {
        digitalWrite(J6stepPin, LOW);
      }
      delayMicroseconds(5);
      if (J6done < J6step && (digitalRead(J6calPin) == LOW))
      {
        digitalWrite(J6stepPin, HIGH);
        J6done = ++J6done;
      }
      ///////////////DELAY BEFORE RESTARTING LOOP
      delayMicroseconds(Speed);
    }
    //OVERDRIVE
    int OvrDrv = 0;
    while (OvrDrv <= 10)
    {
      digitalWrite(J1stepPin, LOW);
      digitalWrite(J2stepPin, LOW);
      digitalWrite(J3stepPin, LOW);
      digitalWrite(J4stepPin, LOW);
      digitalWrite(J5stepPin, LOW);
      digitalWrite(J6stepPin, LOW);
      ///////////////DELAY AND SET HIGH
      delayMicroseconds(Speed);
      digitalWrite(J1stepPin, HIGH);
      digitalWrite(J2stepPin, HIGH);
      digitalWrite(J3stepPin, HIGH);
      digitalWrite(J4stepPin, HIGH);
      digitalWrite(J5stepPin, HIGH);
      digitalWrite(J6stepPin, HIGH);
      OvrDrv = ++OvrDrv;
      ///////////////DELAY BEFORE RESTARTING LOOP AND SETTING LOW AGAIN
      delayMicroseconds(Speed);
    }
    //SEE IF ANY SWITCHES NOT MADE
    delay(500);
    if (digitalRead(J1calPin) == HIGH && digitalRead(J2calPin) == HIGH && digitalRead(J3calPin) == HIGH && digitalRead(J4calPin) == HIGH && digitalRead(J4calPin) == HIGH && digitalRead(J5calPin) == HIGH && digitalRead(J6calPin) == HIGH)
    {
      Serial.println("pass\n");
    }
    else
    {
      Serial.println("J1fail\n");
    }
    inData = ""; // Clear recieved buffer
  */
  return;
}

void moveRobot(String inData)
{
  /*
        int J1start = inData.indexOf('A');
        int J2start = inData.indexOf('B');
        int J3start = inData.indexOf('C');
        int J4start = inData.indexOf('D');
        int J5start = inData.indexOf('E');
        int J6start = inData.indexOf('F');
        int Adstart = inData.indexOf('G');
        int Asstart = inData.indexOf('H');
        int Ddstart = inData.indexOf('I');
        int Dsstart = inData.indexOf('K');
        int SPstart = inData.indexOf('S');
        int J1dir = inData.substring(J1start + 1, J1start + 2).toInt();
        int J2dir = inData.substring(J2start + 1, J2start + 2).toInt();
        int J3dir = inData.substring(J3start + 1, J3start + 2).toInt();
        int J4dir = inData.substring(J4start + 1, J4start + 2).toInt();
        int J5dir = inData.substring(J5start + 1, J5start + 2).toInt();
        int J6dir = inData.substring(J6start + 1, J6start + 2).toInt();
        int J1step = inData.substring(J1start + 2, J2start).toInt();
        int J2step = inData.substring(J2start + 2, J3start).toInt();
        int J3step = inData.substring(J3start + 2, J4start).toInt();
        int J4step = inData.substring(J4start + 2, J5start).toInt();
        int J5step = inData.substring(J5start + 2, J6start).toInt();
        int J6step = inData.substring(J6start + 2, SPstart).toInt();
        float SpeedIn = inData.substring(SPstart + 1, Adstart).toFloat();
        float ACCdur = inData.substring(Adstart + 1, Asstart).toInt();
        float ACCspd = inData.substring(Asstart + 1, Ddstart).toInt();
        float DCCdur = inData.substring(Ddstart + 1, Dsstart).toInt();
        float DCCspd = inData.substring(Dsstart + 1).toInt();
        Serial.print("command recieved");

        //FIND HIGHEST STEP
        int HighStep = J1step;
        if (J2step > HighStep)
        {
          HighStep = J2step;
        }
        if (J3step > HighStep)
        {
          HighStep = J3step;
        }
        if (J4step > HighStep)
        {
          HighStep = J4step;
        }
        if (J5step > HighStep)
        {
          HighStep = J5step;
        }
        if (J6step > HighStep)
        {
          HighStep = J6step;
        }

        int J1_PE = 0;
        int J2_PE = 0;
        int J3_PE = 0;
        int J4_PE = 0;
        int J5_PE = 0;
        int J6_PE = 0;

        int J1_SE_1 = 0;
        int J2_SE_1 = 0;
        int J3_SE_1 = 0;
        int J4_SE_1 = 0;
        int J5_SE_1 = 0;
        int J6_SE_1 = 0;

        int J1_SE_2 = 0;
        int J2_SE_2 = 0;
        int J3_SE_2 = 0;
        int J4_SE_2 = 0;
        int J5_SE_2 = 0;
        int J6_SE_2 = 0;

        int J1_LO_1 = 0;
        int J2_LO_1 = 0;
        int J3_LO_1 = 0;
        int J4_LO_1 = 0;
        int J5_LO_1 = 0;
        int J6_LO_1 = 0;

        int J1_LO_2 = 0;
        int J2_LO_2 = 0;
        int J3_LO_2 = 0;
        int J4_LO_2 = 0;
        int J5_LO_2 = 0;
        int J6_LO_2 = 0;

        //reset
        int J1cur = 0;
        int J2cur = 0;
        int J3cur = 0;
        int J4cur = 0;
        int J5cur = 0;
        int J6cur = 0;

        int J1_PEcur = 0;
        int J2_PEcur = 0;
        int J3_PEcur = 0;
        int J4_PEcur = 0;
        int J5_PEcur = 0;
        int J6_PEcur = 0;

        int J1_SE_1cur = 0;
        int J2_SE_1cur = 0;
        int J3_SE_1cur = 0;
        int J4_SE_1cur = 0;
        int J5_SE_1cur = 0;
        int J6_SE_1cur = 0;

        int J1_SE_2cur = 0;
        int J2_SE_2cur = 0;
        int J3_SE_2cur = 0;
        int J4_SE_2cur = 0;
        int J5_SE_2cur = 0;
        int J6_SE_2cur = 0;

        int highStepCur = 0;



        //SET DIRECTIONS

        /////// J1 /////////
        if (J1dir == 1 && J1rotdir == 1)
        {
          digitalWrite(J1dirPin, LOW);
        }
        else if (J1dir == 1 && J1rotdir == 0)
        {
          digitalWrite(J1dirPin, HIGH);
        }
        else if (J1dir == 0 && J1rotdir == 1)
        {
          digitalWrite(J1dirPin, HIGH);
        }
        else if (J1dir == 0 && J1rotdir == 0)
        {
          digitalWrite(J1dirPin, LOW);
        }

        /////// J2 /////////
        if (J2dir == 1 && J2rotdir == 1)
        {
          digitalWrite(J2dirPin, LOW);
        }
        else if (J2dir == 1 && J2rotdir == 0)
        {
          digitalWrite(J2dirPin, HIGH);
        }
        else if (J2dir == 0 && J2rotdir == 1)
        {
          digitalWrite(J2dirPin, HIGH);
        }
        else if (J2dir == 0 && J2rotdir == 0)
        {
          digitalWrite(J2dirPin, LOW);
        }

        /////// J3 /////////
        if (J3dir == 1 && J3rotdir == 1)
        {
          digitalWrite(J3dirPin, LOW);
        }
        else if (J3dir == 1 && J3rotdir == 0)
        {
          digitalWrite(J3dirPin, HIGH);
        }
        else if (J3dir == 0 && J3rotdir == 1)
        {
          digitalWrite(J3dirPin, HIGH);
        }
        else if (J3dir == 0 && J3rotdir == 0)
        {
          digitalWrite(J3dirPin, LOW);
        }

        /////// J4 /////////
        if (J4dir == 1 && J4rotdir == 1)
        {
          digitalWrite(J4dirPin, LOW);
        }
        else if (J4dir == 1 && J4rotdir == 0)
        {
          digitalWrite(J4dirPin, HIGH);
        }
        else if (J4dir == 0 && J4rotdir == 1)
        {
          digitalWrite(J4dirPin, HIGH);
        }
        else if (J4dir == 0 && J4rotdir == 0)
        {
          digitalWrite(J4dirPin, LOW);
        }

        /////// J5 /////////
        if (J5dir == 1 && J5rotdir == 1)
        {
          digitalWrite(J5dirPin, LOW);
        }
        else if (J5dir == 1 && J5rotdir == 0)
        {
          digitalWrite(J5dirPin, HIGH);
        }
        else if (J5dir == 0 && J5rotdir == 1)
        {
          digitalWrite(J5dirPin, HIGH);
        }
        else if (J5dir == 0 && J5rotdir == 0)
        {
          digitalWrite(J5dirPin, LOW);
        }

        /////// J6 /////////
        if (J6dir == 1 && J6rotdir == 1)
        {
          digitalWrite(J6dirPin, LOW);
        }
        else if (J6dir == 1 && J6rotdir == 0)
        {
          digitalWrite(J6dirPin, HIGH);
        }
        else if (J6dir == 0 && J6rotdir == 1)
        {
          digitalWrite(J6dirPin, HIGH);
        }
        else if (J6dir == 0 && J6rotdir == 0)
        {
          digitalWrite(J6dirPin, LOW);
        }


        /////CALC SPEEDS//////
        float ACCStep = (HighStep * (ACCdur / 100));
        float DCCStep = HighStep - (HighStep * (DCCdur / 100));
        float AdjSpeed = (SpeedIn / 100);
        //REG SPEED
        float CalcRegSpeed = (SpeedMult / AdjSpeed);
        int REGSpeed = int(CalcRegSpeed);

        //ACC SPEED
        float ACCspdT = (ACCspd / 100);
        float CalcACCSpeed = ((SpeedMult + (SpeedMult / ACCspdT)) / AdjSpeed);
        float ACCSpeed = (CalcACCSpeed);
        float ACCinc = (REGSpeed - ACCSpeed) / ACCStep;

        //DCC SPEED
        float DCCspdT = (DCCspd / 100);
        float CalcDCCSpeed = ((SpeedMult + (SpeedMult / DCCspdT)) / AdjSpeed);
        float DCCSpeed = (CalcDCCSpeed);
        float DCCinc = (REGSpeed + DCCSpeed) / DCCStep;
        DCCSpeed = REGSpeed;


        ///// DRIVE MOTORS /////
        while (J1cur < J1step || J2cur < J2step || J3cur < J3step || J4cur < J4step || J5cur < J5step || J6cur < J6step)
        {

          /////// J1 ////////////////////////////////
          ///find pulse every
          J1_PE = (HighStep / J1step);
          ///find left over 1
          J1_LO_1 = (HighStep - (J1step * J1_PE));
          ///find skip 1
          if (J1_LO_1 > 0)
          {
            J1_SE_1 = (HighStep / J1_LO_1);
          }
          else
          {
            J1_SE_1 = 0;
          }
          ///find left over 2
          if (J1_SE_1 > 0)
          {
            J1_LO_2 = HighStep - ((J1step * J1_PE) + ((J1step * J1_PE) / J1_SE_1));
          }
          else
          {
            J1_LO_2 = 0;
          }
          ///find skip 2
          if (J1_LO_2 > 0)
          {
            J1_SE_2 = (HighStep / J1_LO_2);
          }
          else
          {
            J1_SE_2 = 0;
          }
          ////////////////////////
          if (J1cur < J1step)
          {
            if (J1_SE_2 == 0)
            {
              J1_SE_2cur = (J1_SE_2 + 1);
            }
            if (J1_SE_2cur != J1_SE_2)
            {
              J1_SE_2cur = ++J1_SE_2cur;
              if (J1_SE_1 == 0)
              {
                J1_SE_1cur = (J1_SE_1 + 1);
              }
              if (J1_SE_1cur != J1_SE_1)
              {
                J1_SE_1cur = ++J1_SE_1cur;
                J1_PEcur = ++J1_PEcur;
                if (J1_PEcur == J1_PE)
                {
                  J1cur = ++J1cur;
                  J1_PEcur = 0;
                  digitalWrite(J1stepPin, LOW);
                  delayMicroseconds(5);
                  digitalWrite(J1stepPin, HIGH);
                }
              }
              else
              {
                J1_SE_1cur = 0;
              }
            }
            else
            {
              J1_SE_2cur = 0;
            }
          }
          /////////////////////////////////////////


          /////// J2 ////////////////////////////////
          ///find pulse every
          J2_PE = (HighStep / J2step);
          ///find left over 1
          J2_LO_1 = (HighStep - (J2step * J2_PE));
          ///find skip 1
          if (J2_LO_1 > 0)
          {
            J2_SE_1 = (HighStep / J2_LO_1);
          }
          else
          {
            J2_SE_1 = 0;
          }
          ///find left over 2
          if (J2_SE_1 > 0)
          {
            J2_LO_2 = HighStep - ((J2step * J2_PE) + ((J2step * J2_PE) / J2_SE_1));
          }
          else
          {
            J2_LO_2 = 0;
          }
          ///find skip 2
          if (J2_LO_2 > 0)
          {
            J2_SE_2 = (HighStep / J2_LO_2);
          }
          else
          {
            J2_SE_2 = 0;
          }
          ////////////////////////
          if (J2cur < J2step)
          {
            if (J2_SE_2 == 0)
            {
              J2_SE_2cur = (J2_SE_2 + 1);
            }
            if (J2_SE_2cur != J2_SE_2)
            {
              J2_SE_2cur = ++J2_SE_2cur;
              if (J2_SE_1 == 0)
              {
                J2_SE_1cur = (J2_SE_1 + 1);
              }
              if (J2_SE_1cur != J2_SE_1)
              {
                J2_SE_1cur = ++J2_SE_1cur;
                J2_PEcur = ++J2_PEcur;
                if (J2_PEcur == J2_PE)
                {
                  J2cur = ++J2cur;
                  J2_PEcur = 0;
                  digitalWrite(J2stepPin, LOW);
                  delayMicroseconds(5);
                  digitalWrite(J2stepPin, HIGH);
                }
              }
              else
              {
                J2_SE_1cur = 0;
              }
            }
            else
            {
              J2_SE_2cur = 0;
            }
          }
          /////////////////////////////////////////


          /////// J3 ////////////////////////////////
          ///find pulse every
          J3_PE = (HighStep / J3step);
          ///find left over 1
          J3_LO_1 = (HighStep - (J3step * J3_PE));
          ///find skip 1
          if (J3_LO_1 > 0)
          {
            J3_SE_1 = (HighStep / J3_LO_1);
          }
          else
          {
            J3_SE_1 = 0;
          }
          ///find left over 2
          if (J3_SE_1 > 0)
          {
            J3_LO_2 = HighStep - ((J3step * J3_PE) + ((J3step * J3_PE) / J3_SE_1));
          }
          else
          {
            J3_LO_2 = 0;
          }
          ///find skip 2
          if (J3_LO_2 > 0)
          {
            J3_SE_2 = (HighStep / J3_LO_2);
          }
          else
          {
            J3_SE_2 = 0;
          }
          ////////////////////////
          if (J3cur < J3step)
          {
            if (J3_SE_2 == 0)
            {
              J3_SE_2cur = (J3_SE_2 + 1);
            }
            if (J3_SE_2cur != J3_SE_2)
            {
              J3_SE_2cur = ++J3_SE_2cur;
              if (J3_SE_1 == 0)
              {
                J3_SE_1cur = (J3_SE_1 + 1);
              }
              if (J3_SE_1cur != J3_SE_1)
              {
                J3_SE_1cur = ++J3_SE_1cur;
                J3_PEcur = ++J3_PEcur;
                if (J3_PEcur == J3_PE)
                {
                  J3cur = ++J3cur;
                  J3_PEcur = 0;
                  digitalWrite(J3stepPin, LOW);
                  delayMicroseconds(5);
                  digitalWrite(J3stepPin, HIGH);
                }
              }
              else
              {
                J3_SE_1cur = 0;
              }
            }
            else
            {
              J3_SE_2cur = 0;
            }
          }
          /////////////////////////////////////////


          /////// J4 ////////////////////////////////
          ///find pulse every
          J4_PE = (HighStep / J4step);
          ///find left over 1
          J4_LO_1 = (HighStep - (J4step * J4_PE));
          ///find skip 1
          if (J4_LO_1 > 0)
          {
            J4_SE_1 = (HighStep / J4_LO_1);
          }
          else
          {
            J4_SE_1 = 0;
          }
          ///find left over 2
          if (J4_SE_1 > 0)
          {
            J4_LO_2 = HighStep - ((J4step * J4_PE) + ((J4step * J4_PE) / J4_SE_1));
          }
          else
          {
            J4_LO_2 = 0;
          }
          ///find skip 2
          if (J4_LO_2 > 0)
          {
            J4_SE_2 = (HighStep / J4_LO_2);
          }
          else
          {
            J4_SE_2 = 0;
          }
          ////////////////////////
          if (J4cur < J4step)
          {
            if (J4_SE_2 == 0)
            {
              J4_SE_2cur = (J4_SE_2 + 1);
            }
            if (J4_SE_2cur != J4_SE_2)
            {
              J4_SE_2cur = ++J4_SE_2cur;
              if (J4_SE_1 == 0)
              {
                J4_SE_1cur = (J4_SE_1 + 1);
              }
              if (J4_SE_1cur != J4_SE_1)
              {
                J4_SE_1cur = ++J4_SE_1cur;
                J4_PEcur = ++J4_PEcur;
                if (J4_PEcur == J4_PE)
                {
                  J4cur = ++J4cur;
                  J4_PEcur = 0;
                  digitalWrite(J4stepPin, LOW);
                  delayMicroseconds(5);
                  digitalWrite(J4stepPin, HIGH);
                }
              }
              else
              {
                J4_SE_1cur = 0;
              }
            }
            else
            {
              J4_SE_2cur = 0;
            }
          }
          /////////////////////////////////////////


          /////// J5 ////////////////////////////////
          ///find pulse every
          J5_PE = (HighStep / J5step);
          ///find left over 1
          J5_LO_1 = (HighStep - (J5step * J5_PE));
          ///find skip 1
          if (J5_LO_1 > 0)
          {
            J5_SE_1 = (HighStep / J5_LO_1);
          }
          else
          {
            J5_SE_1 = 0;
          }
          ///find left over 2
          if (J5_SE_1 > 0)
          {
            J5_LO_2 = HighStep - ((J5step * J5_PE) + ((J5step * J5_PE) / J5_SE_1));
          }
          else
          {
            J5_LO_2 = 0;
          }
          ///find skip 2
          if (J5_LO_2 > 0)
          {
            J5_SE_2 = (HighStep / J5_LO_2);
          }
          else
          {
            J5_SE_2 = 0;
          }
          ////////////////////////
          if (J5cur < J5step)
          {
            if (J5_SE_2 == 0)
            {
              J5_SE_2cur = (J5_SE_2 + 1);
            }
            if (J5_SE_2cur != J5_SE_2)
            {
              J5_SE_2cur = ++J5_SE_2cur;
              if (J5_SE_1 == 0)
              {
                J5_SE_1cur = (J5_SE_1 + 1);
              }
              if (J5_SE_1cur != J5_SE_1)
              {
                J5_SE_1cur = ++J5_SE_1cur;
                J5_PEcur = ++J5_PEcur;
                if (J5_PEcur == J5_PE)
                {
                  J5cur = ++J5cur;
                  J5_PEcur = 0;
                  digitalWrite(J5stepPin, LOW);
                  delayMicroseconds(5);
                  digitalWrite(J5stepPin, HIGH);
                }
              }
              else
              {
                J5_SE_1cur = 0;
              }
            }
            else
            {
              J5_SE_2cur = 0;
            }
          }
          /////////////////////////////////////////


          /////// J6 ////////////////////////////////
          ///find pulse every
          J6_PE = (HighStep / J6step);
          ///find left over 1
          J6_LO_1 = (HighStep - (J6step * J6_PE));
          ///find skip 1
          if (J6_LO_1 > 0)
          {
            J6_SE_1 = (HighStep / J6_LO_1);
          }
          else
          {
            J6_SE_1 = 0;
          }
          ///find left over 2
          if (J6_SE_1 > 0)
          {
            J6_LO_2 = HighStep - ((J6step * J6_PE) + ((J6step * J6_PE) / J6_SE_1));
          }
          else
          {
            J6_LO_2 = 0;
          }
          ///find skip 2
          if (J6_LO_2 > 0)
          {
            J6_SE_2 = (HighStep / J6_LO_2);
          }
          else
          {
            J6_SE_2 = 0;
          }
          ////////////////////////
          if (J6cur < J6step)
          {
            if (J6_SE_2 == 0)
            {
              J6_SE_2cur = (J6_SE_2 + 1);
            }
            if (J6_SE_2cur != J6_SE_2)
            {
              J6_SE_2cur = ++J6_SE_2cur;
              if (J6_SE_1 == 0)
              {
                J6_SE_1cur = (J6_SE_1 + 1);
              }
              if (J6_SE_1cur != J6_SE_1)
              {
                J6_SE_1cur = ++J6_SE_1cur;
                J6_PEcur = ++J6_PEcur;
                if (J6_PEcur == J6_PE)
                {
                  J6cur = ++J6cur;
                  J6_PEcur = 0;
                  digitalWrite(J6stepPin, LOW);
                  delayMicroseconds(5);
                  digitalWrite(J6stepPin, HIGH);
                }
              }
              else
              {
                J6_SE_1cur = 0;
              }
            }
            else
            {
              J6_SE_2cur = 0;
            }
          }
          /////////////////////////////////////////


          // inc cur step
          highStepCur = ++highStepCur;


          ////DELAY/////
          if (highStepCur <= ACCStep)
          {
            delayMicroseconds(ACCSpeed);
            ACCSpeed = ACCSpeed + ACCinc;
          }
          else if (highStepCur >= DCCStep)
          {
            delayMicroseconds(DCCSpeed);
            DCCSpeed = DCCSpeed + DCCinc;
          }
          else
          {
            delayMicroseconds(REGSpeed);
          }

        }
        ////////MOVE COMPLETE///////////
        inData = ""; // Clear recieved buffer
        Serial.print("Move Done");
      }
  */
  return;
}
