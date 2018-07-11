# Car_Accident_Detection_System
### system that detects accident car and transfers accident pictures and location to the situation room
----------------------------------------------------------------------------------------------------------------------------------------


 ## About
 ---------------------------------------------------------------------------------------------------------------------------------------
 ### o Team name
 ##### : HANARO(하나로)
 ### o Team members
 ##### : 이찬희, 신지훈, 김태현
 ### o Subject
 ##### : Systems that detects accident car by camera and transfers accident images and location to the situation room
 ### o Abstract
 ##### : In order to comply with the Golden Hour in traffic accidents, the traffic accidents are detected through video or image analysis and the scenes of the accident are transferred to the situation room.



 ## Suggestion Background
 ---------------------------------------------------------------------------------------------------------------------------------------

#### o According to the Ministry of Health and Welfare, the average arrival rate of the final treatment institution within the appropriate time of the servere emergency patients is less than half.
 #### o According to the hospital, patients who have been treated quickly can alleviate pain more quickly. 
 #### o It is important to respond quickly when an accident occurs on the road.
 #### o It is difficult to tell the exact location in the accident scene.
 #### oThe Golden Hour is important in the accident scene, so we need a quick mobilization.

![Suggestion 1](https://github.com/Kim-Taehyeon/Car_Accident_Detection_System/blob/master/suggestion1.jpg)
![Suggestion 2](https://github.com/Kim-Taehyeon/Car_Accident_Detection_System/blob/master/suggestion2.jpg)
![Suggestion 3](https://github.com/Kim-Taehyeon/Car_Accident_Detection_System/blob/master/suggestion3.jpg)


 ## Function
---------------------------------------------------------------------------------------------------------------------------------------

### o Raspberry Pi 1
 ####  1 When we push the button, start the system.
 ####  2 Use the Pi Camera to display the captured image on the display.
 ####  3 Send photos and location variables to the Raspberry Pi 2 at regular intervals.

### o Raspberry Pi 2
 ####  1 Receive photos and location variables sent from Raspberry Pi 1.
 ####  2 Send photos to Nanonets at regular intervals.
 ####  3 Receive the detected result values from Nanonets.
 ####  4 If result value is more than 70%, it is judged as an accident.
 #####  - the monitor displays the location of the accident on the map.
 #####  - if you click the marked point, display the accident pictures.
 #####  - LED
 ######   turn on the Red LED, click the '출동' button on the monitor.
 ######   turn on the Yellow LED, click the '도착' button on the monitor.
 ######   turn on the Green LED, click the '처리' button on the monitor.
      
![System Flow](https://github.com/Kim-Taehyeon/Car_Accident_Detection_System/blob/master/system_flow.jpg)

## Effects
---------------------------------------------------------------------------------------------------------------------------------------

### o Change of Paradigm

#### - It is common for a person to call or send message directly.
#### - However, in our system, we break the universal idea and open a new paradigm.
#### - This is the same as when a cell phone that only made a voice call or text changed into a smartphone and opened a new paradigm of the mobile phone.

### o Fast

#### - It is possible for a machine to report more quickly than a person to report by telephone or text.
#### - This difference can be felt to be a great time for those who feel the threat of life.
 
### o Accuracy

#### - It is easy to find the exact location
#### - So, you can know the location more precisely.
 
### o Situation Awareness

#### - We can know the scale of the accident through accident images.
#### - There is an advantage in improving the efficiency of incident handling.
 


## Video Link
---------------------------------------------------------------------------------------------------------------------------------------

### o Soldering(Button)
[Watch the Video 1](https://www.youtube.com/watch?v=9d2xdspRXdA&feature=youtu.be)

### o Raspberry Pi 1 Case Making
[Watch the Video 2](https://www.youtube.com/watch?v=ifxCiW4i114&feature=youtu.be)

### o LCD Connection Method
[Watch the Video 3](https://www.youtube.com/watch?v=sOUA0RG7VCg&feature=youtu.be)

### o System Control



## Conclusion
---------------------------------------------------------------------------------------------------------------------------------------
 
 

