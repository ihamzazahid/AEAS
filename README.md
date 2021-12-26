# AEAS
**bold Automated Entrance Authorization System
Final Year Project bold**
Project Advisor: Mr. Ali Faheem
Project Secondary Advisor: Ms. Maria Tamoor
Presented by: 
Hassaan Waseem 21-11499
Hamza Zahid 21-10563
Rai Shahnawaz Khan 20-10609
Department of Computer Science
Forman Christian College (A Chartered University)
Automated Entrance Authorization System
By 
Hamza Zahid
Hassaan Waseem 
Rai Shahnawaz Khan
Project submitted to 
Department of Computer Science,
Forman Christian College (A Chartered University), 
Lahore, Pakistan.
in partial fulfillment of the requirements for the degree of
BACHELOR OF SCIENCE 
IN
COMPUTER SCIENCE (Honors)
Primary Project Advisor Secondary Project Advisor
Senior Project Management 
Committee Representative
1
Abstract
In this report of the Automated Entrance Authorization System, all aspects of the mentioned 
system are discussed and explained. The necessity of this system raised due to Covid-19 
pandemic. Due to the Covid pandemic people need to distance themselves from each other, but 
daily life cannot stop. Individual cannot lose our time and money. This system is also aiming 
to do this task; it can allow entrance to schools, colleges, universities and workplaces without 
touching anything for identification. Students, teachers and staff at institutions can walk in the 
campus freely with this hassle free, clean and secure system. They do not have to worry about 
touching any infected thing. The whole World is in a difficult situation due to Covid-19. 
Pakistan is going through tough times. New corona cases have reached 5,152 till today (19, 
April 2021). And Death toll is around 16,316 since March 2020 till today. Despite all the safety 
precautions the condition is worsening. This project is an effort to reduce physical interaction 
with any machine or person while entering your workplace and/or home etc. Airports, banks 
and events are using facial recognition for entrance. These systems are very successful and 
working in many developed countries. This is built on Python language using different 
algorithms. This system is to use Raspberry Pi which has a limited processing power and 
memory, so it needed an algorithm which is light weight as well as accurate. So, this program 
is using MobileNet Architecture which is a Convolutional Neural Network (CNN) for deep 
learning in facemask detection. And Viola-Jones Algorithm/Haar Cascade Classifiers is being 
used for facial recognition. The system will be considered complete when the accuracy of the 
system lies between 95-99% for facial recognition, 85-90% for mask detection and ±0.2°C for 
temperature measurement. The system will perform each task within a minimum amount of 
time possible and with maximum efficiency. To conclude, this system is an aid or facilitation 
in reducing workload, securing entrance authorization and ensuring health safety measures.
2
Acknowledgement
First and foremost, we thank Allah Almighty. Our instructors have been our strength throughout 
this project. We are very thankful to our parents and teachers for their support. We specially 
give our gratitude towards our primary advisor Sir Ali Faheem who has helped us throughout 
the way to accomplish the target by leading us from the problems and pros and cons of the 
system. This project is made possible because of our parents’ prayers, our teachers’ support and 
the department's tireless effort to provide the best facilities. And at last we want to thank 
ourselves for the support and cooperation we have received from each other.
3
List of Figures
Figure 1 Use Case Diagram 11
Figure 2 Sequence Diagram 15
Figure 3 ER Diagram 15
Figure 4 Technical Architecture 16
Figure 5 Characteristics of methods of object detection 16
Figure 6 Component-Component Interaction 18
Figure 7 Workflow Flowchart 19
Figure 8 Screenshot 1 20
Figure 9 Screenshot 2 20
Figure 10 Screenshot 3 21
Figure 11 Screenshot 4 21
Figure 12 Screenshot 5 22
Figure 13 Screenshot 6 22
4
List of Tables
Table 1 UC-1 6
Table 2 UC-2 7
Table 3 UC-3 8
Table 4 UC-4 9
Table 5 UC-5 10
Table 6 System Information 14
Table 7.1 TC-1 24
Table 7.2 TC-2 24
Table 7.3 TC-3 25
Table 7.4 TC-4 25
Table 7.5 Summary of All Test Results 26
5
TABLE OF CONTENTS
Abstract
1
Acknowledgement
2
List of Figures
3
List of Tables
4
Chapter 1. Introduction
1
1.1 Introduction
1
1.2 Objectives
1
1.3 Problem Statement
2
1.4 Scope
2
Chapter 2. Requirements Analysis
3
2.1 Literature Review
3
2.2 User Classes and Characteristics
3
2.3 Design and Implementation Constraints
4
2.4 Assumptions and Dependencies
4
2.5 System Features / Functional Requirements
4
2.5.1 PIR (Motion Sensor)
6
2.5.2 Face Recognition
7
2.5.3 Facemask Detection
8
2.5.4 Temperature Measurement
9
2.5.5 Grant Entrance 10
2.6 Use Case Diagram 11
2.7 Nonfunctional Requirements 12
2.7.1 Performance Requirements 12
2.7.2 Safety Requirements 12
2.7.3 Security Requirements 12
2.7.4 Additional Software Quality Attributes 12
2.8 Other Requirements 13
Chapter 3. System Design 14
3.1 Application and Data Architecture 14
3.2 Component Interactions and Collaborations 15
3.3 System Architecture 16
3.4 Architecture Evaluation 16
3.5 Component
-External Entities Interface 18
3.6 Screenshots/Prototype 19
3.6.1 Workflow 19
3.6.2 Screens 20
3.7 Other Design Details 23
Chapter 4. Test Specification and Results 24
4.1 Test Case Specification 24
4.2 Summary of Test Results 26
Chapter 5. Conclusion and Future Work 27
5.1 Project summary 27
5.2 Problems faced and lessons learned 27
5.3 Future work 27
References 28
6
Appendix A Glossary 30
Appendix B Deployment/Installation Guide 31
Appendix C User Manual 32
Appendix D Student Information Sheet 34
Appendix E Plagiarism Free Certificate 35
Appendix F Plagiarism Report 36
7
Revision History
Name Date Reason For Changes Version
1
st Draft 03-05-2021 Many issues like; formatting, references, 
abstract, introduction and some other sections.
1
Revision 26-05-2021 Citations and some changes in content of 
different sections
2
Revision 30-05-2021 Formatting and some new screenshots 3
Revision 05-07-2021 Changes in Literature Review, Non Functional 
Requirements and Architecture Evaluation
4
1
Chapter 1. Introduction
1.1 Introduction
The necessity of Automated Entrance Authorization system arised because of the Covid-19 pandemic. 
The Corona virus is attacking once more and again the whole World is suffering from it. People take 
safety precautions like distancing themselves from others, wearing face masks, using sanitizers and 
by following other SOPs given by the World Health Organization (WHO). In spite of our best efforts, 
the population is facing the third wave of this worldwide pandemic. Considering this, the mentioned 
project is another measure to keep us secure and safe at the same time by distancing. Making 
individuals free of barcode and thumb scanning so that physical contact can be to a minimum level. 
It will be an Automated Entrance System using face recognition. It will also measure body 
temperature and check whether the individual is wearing a facemask or not; allowing entrance only 
to authorized individuals with proper health safety measures. If in case a person fails to pass any of 
the tests, the system will not allow the entrance to him. It is a hardware embedded system working 
on Raspberry Pi using deep learning with Python. This system has a wide usability, it can be used at 
any place where people enter for work or to stay.
1.2 Objectives
The primary objective of this system is to offer a system that simplifies and automates the process of 
entrance without physical contact, through facial recognition, mask detection and body temperature 
measurement. In today's pandemic conditions, physical distance from each other is mandatory. 
Following the SOPs people have to avoid physical contact, wear facemasks and keep their distance. 
It is a biometric technology, aiming to recognize a person from a camera. Additionally, we seek to:
● Provide a valuable service to teachers, students and staff by granting entrance without any 
physical interaction.
● Bring down manual process errors by providing a reliable automated system.
● Increase security and privacy as no other unauthorized person can enter the premises.
2
1.3 Problem Statement
As of the current Coronavirus situation and in accordance with the SOPs provided by WHO (World 
Health Organization) people need to distance themselves from each other and wear facemasks while 
also avoiding any direct or indirect contact with things around them. This system is an idea to keep 
people in contact free while entering a place of work, especially in our educational institutions. It is a 
hardware embedded system working on Raspberry Pi using deep learning with Python.
1.4 Scope
The final product will enable the users to avoid physical interaction with the public devices and grant 
the access to the authorized users by facial recognition, mask detection and by measuring their body 
temperature. Through these measures, taken by this system human workload and physical interaction 
will be significantly reduced. This system can be used at entrances at schools, offices and events.
Automated Entrance Authorization System can be used at the entrance of places of work, airports, 
educational institutions, banks and events among many others. This system provides proper security 
by granting entrance to only authorized people, also checking if proper health safety measures are 
taken. Schools, colleges and universities can use this system at their entrances. They have to add 
students, teachers and staff in databases, after that the system checks whether the person in front of 
the camera is allowed to enter the premises or not, also whether the person is wearing a facemask or 
not and whether his/her body temperature is in the acceptable range or not. If all these conditions are 
met only then the system grants entrance to the person.
3
Chapter 2. Requirements Analysis
2.1 Literature Review
Face Recognition technology is being used widely now-a-days. Airports in developed countries are 
starting to use face recognition for boarding. They have passports which are compatible with facial 
recognition. This method replaces the conventional boarding method of screening your ticket and 
passport. So, they go through a hassle-free system without any effort.
National Australia Bank has joined forces with Microsoft for unlocking cash machines with face 
scan due to ATM crimes in those areas. It is a cloud-based system, designed with the use of Azure 
Cognitive Services, and it is developed to better the customer service by removing the demand for 
physical cards or devices to access cash from ATMs. Through this construct, a customer who joined 
the program is capable to withdraw cash from an ATM with the use of facial recognition technology 
and a PIN.
The San Francisco-based company developed the Mask detector in early times, when they heard 
about COVID-19 in 2020. The purpose was to comply with the public needs in order to calculate the 
face mask demand in surroundings and to check how many people are wearing the mask and try to 
take precautions for others as well as themselves.
Severe acute respiratory syndrome (SARS) spread in Asia in 2013. IRT was the method to measure 
body temperature. A surface emits thermal energy when the temperature is higher than the absolute 
temperature. The IR thermometer detects this released energy through the sensing element and 
converts it into an electrical signal. In 2014 five airports of USA used IRT to detect Ebola infection.
Brit Awards and National Television Awards at The O2, London used facial recognition for entrance 
by scanning their guests' faces via multiple booths at entrances.
2.2 User Classes and Characteristics
The system gives access only to the authorized users. In case of AEAS (Automated Entrance 
Authorization System), authorized users are students, faculty members and the staff.
Administrator: The administrator have the admin access to add, delete and modify end-user’s data 
stored in the database.
4
1) Administrator must be an employee of the organization.
2) He/She must have the knowledge of the software life cycle.
3) He/She must know how to operate an OS.
2.3 Design and Implementation Constraints
1. Memory: The device has a memory of 8 GB.
2. Secondary Memory: Raspberry Pi have a SD card slot and a program can read and write in that 
card. The program cannot exceed the amount of SD card’s memory.
3. Language Requirements: Software uses Python 3 and its extended libraries.
2.4 Assumptions and Dependencies
It is acknowledged that the hardware design works correctly with the third-party operating system 
(Raspberry Pi OS, Raspbian) and the developed computer software. Because system acquires new 
updates, the user must have access to make changes. Updates should be done from time to time to 
minimize the inconvenience in the system.
2.5 System Features / Functional Requirements
Since Automated Entrance Authorization System consists of three major parts named Facial 
Recogniser, Mask Detector and Temperature Measurer, so functional requirements are examined in 
three parts:
● Functional Requirements of Facial Recogniser
● Functional Requirements of Mask Detector
● Functional Requirements of Temperature Measurer
Functional Requirements of Facial Recogniser
There are three features of this which are described below:
Pattern: This feature provides the ability to draw a pattern on the face for detection.
Description and Priority: If the user brings his/her face in front of the camera, the pattern of his 
facial features are matched with the pattern of facial features in the database. Detection of the face 
pattern is done by Facial Recogniser, so this function is between the user and the FR.
Stimulus and Priority:
Basic Data Flow:
1. First of all, the user brings his/her face in front of the camera
5
2. The state/movement of the face is detected by the camera.
3. The face is recognised by the camera.
4. The result of the real-time scenario is displayed on the screen.
Functional Requirements of Mask Detector
There are three features of this which are described below:
Pattern: This feature provides the ability to draw a pattern on the face which is having a mask for 
detection.
Description and Priority: After face recognition is done, the user's mask is to be detected next. 
Detection of the mask is done by the Mask Detector, so this function is between the user and the MD.
Stimulus and Priority:
Basic Data Flow:
1. First of all, the user brings his/her face in front of the camera.
2. The state/movement of the face’s mask is detected by the camera.
3. The mask is recognised by the camera.
4. The result of the real-time scenario is displayed on the screen.
6
2.5.1 PIR (Motion Sensor)
Identifier PIR (Motion Sensor)
Purpose To detect any person in front of camera for entrance
Priority Medium
Pre-conditions System powered on (Red light)
Post-conditions Camera module starts working
Typical Course of Action
S# Actor Action System Response
1 A user comes in front of the system
PIR detects motion and sends signal to 
camera module
Alternate Course of Action
S# Actor Action System Response
1 No one is in front of system
Only PIR is working other features on 
standby
Table 1: UC-1
7
2.5.2 Face Recognition
Identifier Face Recognition
Purpose To recognise any person’s face in front of camera
Priority High
Pre-conditions A person in proximity (1st Orange light)
Post-conditions Facemask detection starts working
Typical Course of Action
S# Actor Action System Response
1 A user comes in front of the system
PIR detects motion and sends signal to 
camera module
2
Camera module looks up the person’s 
face in database
Alternate Course of Action
S# Actor Action System Response
1 No one is in front of system
Only PIR is working other features on 
stand by
Table 2: UC-2
8
2.5.3 Facemask Detection
Identifier Facemask Detection
Purpose To detect if the person is wearing facemask
Priority High
Pre-conditions User is authorized to enter (2nd Orange light)
Post-conditions Temperature module starts measuring temperature
Typical Course of Action
S# Actor Action System Response
1 A user comes in front of the system
PIR detects motion and sends signal to 
camera module
2
Camera module looks up the person’s 
face in database
3 Facemask detected
Alternate Course of Action
S# Actor Action System Response
1 No one is in front of system
Only PIR is working other features on 
stand by
Table 3: UC-3
9
2.5.4 Temperature Measurement
Identifier Temperature Measurement
Purpose To measure temperature of person entering
Priority Medium
Pre-conditions Facemask should be detected (3rd Orange light)
Post-conditions Grant entrance by moving the bar
Typical Course of Action
S# Actor Action System Response
1 A user comes in front of the system
PIR detects motion and sends signal to 
camera module
2
Camera module looks up the person’s 
face in database
3 Facemask detected
4 Measures temperature
Alternate Course of Action
S# Actor Action System Response
1 No one is in front of system
Only PIR is working other features on 
stand by
Table 4: UC-4
10
2.5.5 Grant Entrance
Identifier Grant Entrance
Purpose To grant entrance by moving the bar up
Priority Medium
Pre-conditions
All the 3 conditions are met/All 3 orange lights and then green 
light.
Post-conditions Bar is down and the system is reset for new a user
Typical Course of Action
S# Actor Action System Response
1 A user comes in front of the system
PIR detects motion and sends signal to 
camera module
2
Camera module looks up the person’s 
face in database
3 Facemask detected
4 Measures temperature
5 Allows person to pass
Alternate Course of Action
S# Actor Action System Response
1 A user comes in front of the system
PIR detects motion and sends signal to 
camera module
Table 5: UC-5
11
2.6 Use Case Diagram
Figure 1: Use Case Diagram
In Figure 1, use case diagram of the system is shown which tells the relationship between user, the 
system and the administration.
12
2.7 Nonfunctional Requirements
2.7.1 Performance Requirements
The system must be interactive, and the delays involved must be less. So, in every action-response 
of the system, there are no immediate delays. In the case of popping error messages, evaluations, 
there are no delays less than a couple of seconds. This is also applicable on the computation for 
greater than 95% of the Information stored regarding the registered users.
2.7.2 Safety Requirements
There are less risks involved in the system as the developers try their best to develop something 
which is not crashing as the functionalities are fulfilling their tasks as per their assignment in a 
defined pattern.
2.7.3 Security Requirements
The security requirements of the system are the primary one. The product is be handled only by the 
administrator and the authorized users. Only the administrator has the rights to assign permissions 
like creating new accounts and handling them. Only the authorized users, who are created by the 
administrator, get the access for entrance.
2.7.4 Additional Software Quality Attributes
Reliability:
The reliability of our system is stated in terms of measurements. Measurements are taken 
during testing when we are collecting and analyzing data about the performance of the software. In 
other words, is tracking the occurrence of failures during testing.
Usability:
In general, the system is easier to use in order to obtain the desired goal. Since it is a realtime surveillance, therefore users find it quite easy to use.
Portability:
The system is Hardware Oriented composed of both hardware and software components. It 
is built in Python modules and the Hardware is Raspbian having an OS. So, it is a system 
dependent on the hardware and the operating system.
13
Correctness:
Correctness includes the output of the system. Our system is giving an accuracy in a bracket 
of 95%. It follows IEEE standards of documentation.
Efficiency:
The Raspberry Pi has a processor of 2.4GHz and a RAM of 8GB. So, there is quite a chance 
that the system gets slow. Moreover, AEAS does not eat up the whole of the memory of our 
Raspberry as we are placing a feature of motion detection. This allows the system to wake only 
when a person is being sensed otherwise it is on sleeping mode. So, in this way the system is quite 
efficient.
Integrity or Security:
In every existing system, integrity comes with the help of security. In the case of AEAS, 
prevention of unauthorized access to system functions, preventing information loss, ensuring that 
the software is protected from virus infection, and protecting the privacy of data entered the system. 
It is so because only the admin has the right to make changes, no external device can be connected 
to the system and lastly no internet connection is given so there are no chances of viruses in the 
system.
Availability:
In general, the system is available for fulfilling the assigned tasks. Since the team is 
ensuring a top-notch availability, therefore the repairing of operating faults is done in a minimum 
amount of time so that service does not outrage for long.
Robustness:
The only condition that is affecting the working of the system is external. This includes the 
weather conditions. The system should not be placed in damp, moist or extremely hot conditions. 
This can result in system failure and ultimately the product dies.
2.8 Other Requirements
For information regarding nonfunctional requirements, refer to section 2.5: “System Features”. 
Each feature has its requirements listed alongside the feature information. There are no additional 
functional requirements.
14
Chapter 3. System Design
3.1 Application and Data Architecture
This system is hardware embedded which runs on Raspberry Pi. It has camera and temperature 
modules embedded on it. The face recognition function requires a dataset of faces of authorized 
people. The facial recognition part retrieves features of faces in a real time process. The facemask 
function does not require a dataset in real time as it is pre-trained model, checking the facemask of 
the person in front of the camera. The temperature function measures temperature using the IR 
temperature module.
Programming Language Python (3.8)
System Custom Built
Hardware Platform Raspberry Pi 4 (8GB)
Architecture Client side
Database No Database
System host Local Host on any machine
Processing Analytical Report
Network architecture WLAN and Local host
Built Functions Image recognition
Ingrained system CPU
Data Training GPU for fast training and better accuracy
Frame work Tensorflow, OpenCV, Numpy. Scipy, Keras
Table 6: System Information
15
3.2 Component Interactions and Collaborations
Figure 2: Sequence Diagram
In Figure 2 the sequence diagram of the system is shown which represents the sequence of actions 
inside and outside the system.
Figure 3: ER Diagram
In Figure 3 the Entity Relationship diagram of the system is shown which represents the 
relationship and links between different entities of the Automated Entrance Authorization System.
16
3.3 System Architecture
Technical Architecture:
Figure 4: Technical Architecture
In Figure 4 the Technical Architecture of the system is shown which tells system architecture used 
for different features and the whole system combined.
3.4 Architecture Evaluation
For object detection, the similarities and differences between CNN and Haar Cascade Classifiers 
were studied. We used the following characteristics to assess and estimate the quality and the 
performance of various methodologies for real-time object detection and detecting objects from 
images, see Figure 5.
Figure 5: Characteristics of methods of object detection
17
Accuracy (Precision)
CNN and Haar Cascade Classifiers, both have comparatively a high level of accuracy when they 
are detecting objects in the images. Simultaneously, the LBP classifier has a high percentile value 
of false positives and a low accuracy.
Scale Consistency (Invariance)
Due a very strong invariance i.e., remaining constant, objects can be handled and managed quite 
easily by Haar Cascade and LPB Classifiers. Whereas, due to very low scale invariance, the CNN 
cannot handle and manage the scaling objects.
Number of Experiments (For Working Model)
For object detection, a very few experiments are by the Cascade Classifiers to get a working model 
whereas on the other hand dozens of attempts are required by the CNN and it is not so fast.
Processing Overhead (Time)
For processing, a CNN does not require much time. On the other hand, the LBP Classifier also does 
not require much time too. On contrary, Haar Cascades take a much longer time to carry their 
processes.
Consistency with Tilting Objects
With tilting objects, another extraordinary advantage of the CNN is that it remains consistent. 
Whereas on the other side, in this case, the Cascades are not consistent.
In several scenarios and cases, the CNN beats the Cascade Classifiers. If the objects do not scale 
much and you have sufficient time to train the model, it is an intelligent approach to use 
Convolutional Neural Network.
18
3.5 Component-External Entities Interface
Figure 6: Component-Component Interaction
In Figure 6 component to component interaction of the Automated Entrance Authorization System 
is shown which shows how different components of the system interacts with each other.
19
3.6 Screenshots/Prototype
3.6.1 Workflow
Figure 7: Workflow Flowchart
In Figure 7 workflow of the Automated Entrance Authorization System is shown which shows how 
the system works from start to end.
20
3.6.2 Screens
Screenshots of working face recognition and facemask detection functions.
Figure 8: Screenshot 1
In Figure 8, working of system is shown when there is no mask on the face of a person.
Figure 9: Screenshot 2
In Figure 9, working of system is shown when there is a mask on the face of a person.
21
Figure 10: Screenshot 3
In Figure 10, working of the system is shown when the mask is below the nose.
Figure 11: Screenshot 4
In Figure 11, working of the system is shown when the mask is on chin.
22
Figure 12: Screenshot 5
In Figure 12, working of the system is shown when the person is trying to cheat with the system 
by put hands on the face instead of mask.
Figure 13: Screenshot 6
In Figure 13, working of face-detector is shown
23
3.7 Other Design Details
The project can be run on any python interpreter. You can use Jupyter notebook, PyCharm 
Professional, Anaconda etc. This design details includes the dependencies of the packages installed 
able to run the project. NumPy, SciPy, OpenCV, TensorFlow, Keras among other libraries and 
frameworks were used.
24
Chapter 4. Test Specification and Results
4.1 Test Case Specification
Identifier TC-1
Related requirements(s) Face recognition
Short description This function recognises a face from camera using given dataset
Pre-condition(s) Person’s face should be in the dataset
Input data Face image
Detailed steps Deep learning model recognizes the face
Expected result(s) Accurate face recognition
Post-condition(s) Move towards next function (facemask detection)
Actual result(s) Accurate face recognition
Test Case Result Accurate face recognition
Table 7.1: TC-1
Identifier TC-2
Related requirements(s) Facemask detection
Short description This function detects a facemask from camera
Pre-condition(s) Person should be authorized
Input data Face image
Detailed steps Deep learning model detects the facemask
Expected result(s) Accurate facemask detection
Post-condition(s) Move towards next function (temperature measurement)
Actual result(s) Accurate facemask detection
Test Case Result Accurate facemask detection
Table 7.2: TC-2
25
Identifier TC-3
Related requirements(s) Temperature Measurement
Short description This function measure temperature
Pre-condition(s) Person should be authorized to enter
Input data IR
Detailed steps IR sensor measures temperature
Expected result(s) Measure temperature
Post-condition(s) Move towards next function
Actual result(s) Measuring accurate temperature
Test Case Result Turns off automatically
Table 7.3: TC-3
Identifier TC-4
Related requirements(s) Temperature Measurement
Short description This function measure temperature
Pre-condition(s) Person should be authorized to enter
Input data IR
Detailed steps IR sensor measures temperature
Expected result(s) Measure temperature
Post-condition(s) Move towards next function
Actual result(s) Measuring accurate temperature
Test Case Result Measuring accurate temperature
Table 7.4: TC-4
26
4.2 Summary of Test Results
Module Name Test cases run
Number of defects 
found
Number of 
defects 
corrected so far
Number of 
defects still 
need to be 
corrected
Face recognition TC1 0 0 0
Facemask Detection TC 2 0 0 0
Temperature 
measurement
TC 3
1 1 0
Temperature 
measurement
TC 4
0 0 0
Complete System 4 1 1 0
Table 7.5: Summary of All Test Results
27
Chapter 5. Conclusion and Future Work
5.1 Project summary
This project has provided a safe and secure solution for entrance by allowing a contactless entry, 
checking facemask and temperature alongside face recognition. It becomes a need in keeping with 
the current pandemic situation, where everyone is worried about their health and taking 
precautionary measures. This system provides an entrance system with facial recognition, mask 
detection and temperature measurement. Making it very useful and productive in most 
environments.
5.2 Problems faced and lessons learned
Many problems were faced during the completion of this project. First, it is a huge project. It was a 
difficult task to learn and implement. We had no prior knowledge of computer vision and different 
modules.
No Physical meetings were held which was a huge difficulty. Help of the Instructors was very 
limited as we were working remotely for the entire year. It was difficult for us to manage time and 
our team.
We had many technical problems like working on code and hardware. The temperature sensor was 
making the Raspberry Pi trip, after trying many different solutions we found out that the problem 
was with the soldering of wires.
We learned a lot of different things like all the modules, libraries and frameworks. We learned a 
great lesson that by mutual understanding, communication and support we can achieve great things.
5.3 Future work
In future versions of this system an LCD can be embedded with it, showing user activity and 
interacting with the user so that the system can be more user friendly.
A database of authorized people can be included so that it can be used for a large number of people. 
The system can be linked to the cloud, so that the administrator can see any activity related to the 
system.
28
References
Akar M.C., Aslanbas C., Baltaci U., Ekici C., “Controlling Mobile Devices via Gesture 
Recognition”
Bharat, “Face Recognition”, https://www.slideshare.net/bharath55/face-recognition-16130663
Chen H.Y., Chen A., Chen C., (May, 2020), “Investigation of the Impact of Infrared Sensors on 
Core Body Temperature Monitoring by Comparing Measurement Sites”, 
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7284737/#:~:text=When%20the%20temperature%
20of%20a,it%20into%20an%20electrical%20signal
Joseph, Jomon, and K. P. Zacharia. (2013), "Automatic attendance management system using face 
recognition.", International Journal of Science and Research (IJSR)
Mert A.G., Kivilcim B.B., Sekerci E.U., Arkayin Y., (2016), “Turkish Text Summarizer with Deep 
Learning”, METU - Department of Computer Engineering
NAMMPSoft Inc., (2007), “nTravel”
“Non Functional Requirements”, 
https://aakashtechsupportdocs.readthedocs.io/en/latest/nonfunc.html
Panda B. P., Khade P.M., Shinde K.D., Dhatrak C.V., (2015), “Smart Face Recognition System”, 
International Journal of Engineering Research and General Science Volume 3, Issue 2
Rastogi, S., (2015), “Student Software Management”, Department of Computer Science and 
Engineering, Dewan V.S. Institute of Engineering and Technology, Meerut.
RoshanTharanga, J. G., et al., (2013), "Smart attendance using real time face recognition (smartfr)." Department of Electronicand Computer Engineering, Sri Lanka Institute of Information 
Technology (SLIIT), Malabe, Sri Lanka
29
Sai M.V., Varalakshmi G., Balakumar G., Prasad J., (2017), “Face Recognition System with Face 
Detection”, Jawaharlal Nehru Technological University Kakinada
Selvi, K. Senthamil, P. Chitrakala, and A. Antony Jenitha., (2014), "Face recognition based 
attendance marking system."
“Smart Attendance Tracking and Monitoring System using BLE Beacon”, 
https://smartattendancesystem.wordpress.com/srs/
“Where is the facial recognition used”, https://www.thalesgroup.com/en/markets/digital-identityand-security/government/inspired/where-facial-recognition-used
Wójcik W., Gromaszek K., and Junisbekov M., (2016), “Face Recognition: Issues, Methods and 
Alternative Applications”
Yan W., (September, 2020), “Facemask Recognition has arrieves-for better or worse”, 
https://www.nationalgeographic.com/science/article/face-mask-recognition-has-arrived-forcoronavirus-better-or-worse-cvd
Yang L., “Face Recognition System”
30
Appendix A Glossary
AEAS - Automated Entrance Authorization System
OS - Operating System. An operating system (OS) is system software that manages computer 
hardware, software resources, and provides common services for computer programs.
FR - Facial Recognition. Facial recognition is a way of identifying or confirming an individual's 
identity using their face.
HDMI - High Definition Multimedia Interface. The most frequently used HD signal for transferring 
both high definition audio and video over a single cable.
MD - Mask Detector. It identifies whether a person is wearing a mask or not. 
TM - Temperature Measurer. It measures the temperature.
31
Appendix B Deployment/Installation Guide
(Connect the System with Power Supply)
⚫ Attach DC power with system.
(Connect the System with Internet)
⚫ Take any PC or Laptop (installed environment)
⚫ Connect the AEAS with the same Internet connection on which Laptop or PC is connected
(Create Data Set)
⚫ Create data set according to the requirements.
(Execution)
⚫ The system is ready to perform its task according to the given data set.
32
Appendix C User Manual
This document introduces the interaction with the system.
• Hardware needs a consistent DC power supply.
Mask Detection:
• In order to get your mask checked, bring face in front of the camera with mask. To pass this 
check, mask should properly worn. If mask is placed under the nose the condition will not be 
fulfilled and it will not move to the next step. If the face is not recognized in 10 seconds the 
system will restart and it starts again. After restarting it checks for a motion to be detected.
Facial Recognition:
• In order to get your face recognized, bring your face in front of the camera. If the face is not 
recognized in 10 seconds the system will restart and it starts again from the step of mask 
detection.
Temperature Measurement:
• In order to get your body temperature measured, bring your hand close to the sensor. System will 
measure your body temperature and compare it with optimum temperature. If and only if the 
temperature is less than or equal to the optimum temperature, the system will allow the access to 
the person.
Grant Entrance:
• After passing these three tests, the motor opens the barrier for the person for 5 seconds to let him 
pass through it. After the barrier comes back to its mean position, the system again looks for a 
motion to detect and perform all the three above mentioned functionalities.
33
Appendix D Student Information Sheet
Roll No Name Email Address (FC College) Frequently 
Checked 
Email
Address
Personal Cell 
Phone 
Number
20- Rai Shahnawaz 20- Daily 03040480845
10609 Khan 10609@formanite.fccollege.edu.pk
21- Hassaan Waseem 21-11499@formanite. Daily 03177003389
11499 fccollege.edu.pk
21- Hamza Zahid 21- Daily 03224144766
10563 10563@formanite.fccollege.edu.pk
34
Appendix E Plagiarism Free Certificate
This is to certify that, I am Hamza Zahid S/o Zahid Taj Din, group leader of FYP under registration no 3
at Computer Science Department, Forman Christian College (A Chartered University), Lahore. I declare that 
my final year project report is checked by my supervisor and the similarity index is 17% that is less than 
20%, an acceptable limit by HEC. Report is attached herewith as Appendix F. To the best of my knowledge 
and belief, the report contains no material previously published or written by another person except where 
due reference is made in the report itself.
Date: Name of Group Leader: Signature:
Name of Supervisor: Ali Faheem Co-Supervisor: Maria Tamoor
Designation: Lecturer Designation: Assistant Professor
Signature: Signature:
Senior Project Management Committee Representative:
Signature:
35
Appendix F Plagiarism Report
36
