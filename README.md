# Inspiration
I owe the idea to **Servet Gulnaroglu** on YouTube, who made a video coding a spinning cube in **C**.
Here is a link to the video:  [ASMR Programming - Spinning Cube - No Talking](https://www.youtube.com/watch?v=p09i_hoFdd0&ab_channel=ServetGulnaroglu)

# Reasoning
I liked what **Servet Gulnaroglu** did and wanted to form a similar code, but I didn't want to just 
take the idea, so I decided to try coding it in **Python**.  By the end, this project gave me better 
practice in calling code from my *Mac* terminal and in creating a git repository, so it helped me learn 
a few important points.

# Use Notes
- The original **C** version used **ANSI escape codes** to clear the screen after every square gets printed,
but I couldn't get them to work on my terminal, so I imported `os` and `sys` to do it manually with `os.system('clear')` and `sys.stdout.flush()`.
- If using a *Mac* terminal to call this file, the terminal window needs to be large enough, or the squares will print out very jittery, so increase
size of window so squares print well inside terminal.
- I don't own a *Windows* computer, and I haven't used this **Python** file on one, so I don't know if the code would work on it's version of a terminal
or console.  Perhaps the **ANSI escape codes** would work for you while `os` and `sys` will not.  Experimentation will help.
