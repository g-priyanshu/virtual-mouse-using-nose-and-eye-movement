# virtual-mouse-using-nose-and-eye-movement

This HCI (Human-Computer Interaction) application in Python(3.6) will allow you to control your mouse cursor with your facial movements, works with just your regular webcam. Its hands-free, no wearable hardware or sensors needed.

The list of actions include:

>Squinting your eyes (squint - To look with the eyes partly closed, as in bright sunlight)

>Winking for left and right click

>Moving your head around (pitch and yaw) for cursor movement

>Opening your mouth to activate the virtual mouse

#Code requirements
>Numpy - 1.13.3

>OpenCV - 3.2.0

>PyAutoGUI - 0.9.36

>Dlib - 19.4.0

>Imutils - 0.4.6

#Execution

Order of Execution is as follows:


Follow these installation guides -

https://pypi.org/project/numpy/,
https://pypi.org/project/numpy/, 
https://pyautogui.readthedocs.io/en/latest/install.html, https://pyautogui.readthedocs.io/en/latest/install.html,
https://github.com/jrosebr1/imutils 

and install the right versions of the libraries (mentioned above).

Make sure you have the model downloaded. Read the README.txt file inside the model folder for the link.

python mouse-cursor-control.py

Please raise an issue in case of any errors.

#Usage
![githubmyproject](https://github.com/g-priyanshu/virtual-mouse-using-nose-and-eye-movement/assets/134190092/d8bc8ec8-a4e5-44af-8aaf-be53d1fdaf2a)

#How it works

Dlib's prebuilt model, helps us to find the 68 facial landsmarks of a face using which a Eye aspect ratio and mouth aspect ratio is calculted and these values are then used to trigger the certain mouse actiona using PyautoGUI





