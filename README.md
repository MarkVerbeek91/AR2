# AR2

## 6 axis stepper motor robot and control software

https://www.anninrobotics.com/

The AR2 is a small desktop robot that is modeled similar to an industrial 6 axis robot.  This is a DIY project that can be built from 3D printed components or from machined aluminum components, uses low cost stepper motors and arduino controller.

This project includes:

- Bill of materials and instructions
- CAD files to 3D print components to build the robot
- Arduino sketch for stepper driver control
- Software to program and operate robot
- Kinematic model

All geared stepper motors and drivers are available from  [www.omc-stepperonline.com](https://www.omc-stepperonline.com/?tracking=59c1139e8987b) and all other misc. hardware are off-the-shelf items available from multiple sources (see the bill of materials info within each manual).

[![Alt text](https://img.youtube.com/vi/EAcU4k2Qskk/0.jpg)](https://www.youtube.com/watch?v=EAcU4k2Qskk)

Startup & Calibration: [Calibration Video](https://youtu.be/MMESgfq2Mjg)

Programming: [Programming Video](https://youtu.be/BozgdjE-HR8)

How the math works: [Kinematic Videos](https://youtu.be/FIx6olybAeQ)

Please review all of the videos on programming and calibration,
I will try to answer as many emails as I can: chris.annin@gmail.com
#
Its important to me that this project is free and available to everyone but any donations that
can help with all that has gone into it would be hugely appreciated.  Thank you very much.
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.me/ChrisAnnin)

## Notes by Mark

A new stucture file and folder is created by Mark to allow for better version control and extenteded features. 

Explanation of the file stucture: 
- build: contains the lastest stable executable version the AR2 control interface and arduino binairy. 
- CAD: contains the STEP files which can be imported into almost all CAD programs. 
- conf: contains configuration and calibration files. 
- docs: contrains the PDF documentation and the reStructure Text files for documentation. 
- images: contains images
- samples: contains sample programs, position and movements
- src: contains the python source files and build scripts. These can also be run just like the files in 'build'.
- src_arduino: contrains the c-file for the arduino software. 
- stl: contrains the latest export of the CAD files to the STL format for printing. 
- tests: contains the unittest files and other tests. 

## TASKs (by Mark)

A (very) short overview of tasks that needed to be done:

- implement functionality in all modules.
- add tests for all about implemented functionality.
- restructure c-file for arduino. 
- update documentation on running, building, etc of all software
- add documentation to scr files (python and c)
- make a better TO DO list

