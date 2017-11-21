# AR2

## 6 axis stepper motor robot and control software

This project includes:

- Bill of materials and instructions
- CAD files to 3D print components to build the robot
- Arduino sketch for stepper driver control
- Software to program and operate robot
- Kinematic model

All geared stepper motors and drivers are available from  [www.omc-stepperonline.com](https://www.omc-stepperonline.com/?tracking=59c1139e8987b) and all other misc. hardware are off-the-shelf items available from multiple sources (see the bill of materials file).

[![Alt text](https://img.youtube.com/vi/CCgI4R1TEzI/0.jpg)](https://www.youtube.com/watch?v=CCgI4R1TEzI)

Startup & Calibration: [Calibration Video](https://youtu.be/MMESgfq2Mjg)

Programming: [Programming Video](https://youtu.be/BozgdjE-HR8)

How the math works: [Kinematic Videos](https://youtu.be/FIx6olybAeQ)

Questions: chris.annin@gmail.com
#
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

