# Accreditation
The main idea for this project came from [Servet Gulnaroglu](https://www.youtube.com/watch?v=p09i_hoFdd0&ab_channel=ServetGulnaroglu) 
video programming a rotating cube in C.  I wanted to do a small project in Python to also practice some GitHub Committing, so
I tried their concept in Python.

# Use Notes
- I designed it with **escape codes** first, but couldn't get them to work in my mac terminal, so I went to using **`os`** and **`system`** to
erase drawn cubes as they are printed
- When printing to the terminal, for me, I needed to **increase the terminal window size** past a certain size to make the cube print out and look
good, without any stuttering
- Alter **`cubeWidth`** and **`distanceFromCam`** to play around with how dense and how far the cube is when printed
  - Play around with it to figure it out, but I've found I like width from 10 - 20, and distance from 40 - 100 for good results
