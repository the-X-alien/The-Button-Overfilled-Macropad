# Dhiaan's Button Overfilled Macropad

## The final product in Fusion 360
![image](https://github.com/user-attachments/assets/c62c340f-9aaa-4140-a2d7-ae20d1dec6a3)
### My Schematic
![image](https://github.com/user-attachments/assets/aa7759fa-7315-400d-ae56-446b218044cb)

I followed the Hackpad tutorial for the first version but after I figured out that 16 GPIO pins are too much I switched to a Matrix tutorial.
I followed the tutorial but instead of a 3x3 I made a 4x4.
The tutorial also explained how Anti-Ghosting worked so I also added diodes to incorperate the feature.

### My PCB
![image](https://github.com/user-attachments/assets/ae04ad39-6e21-424c-8025-9ef1d103ac58)

For the PCB I did it on my own besides the OLED display for which I took help from the Hackpad chat.

### The Case
![image](https://github.com/user-attachments/assets/c3f21b7f-f7e3-472a-9fe7-296841d8b309)
*The cover is facing the wrong way

The case was the part I thought was the hardest but ended up becoming really easy from the Hackpad tutorial.
The only thing I had trouble with was finding out where to place the OLED on the top panel beacuse since we added 20 mm to each dimension.

### BOM

Idk what this is so I am going to put the KiCad thing
https://docs.google.com/spreadsheets/d/10YrJsM2fY9kX1iMAhUJcFAUprBF40cdHoe6Sq5_inwc/edit?usp=sharing
Everything is free tho

### The Firmware

(This part is exactly the Firmware's README)

#### How I made it

I took the starter code from the Hackpad guide and used a tutorial to make it use a matrix instead.
Then I used ChatGPT to learn how to program the display.

#### What it does

The firmware makes the 4x4 Matrix into two parts. 
The top 3x4 is a numpad with 1-9 and the mulpitication and division function.
The bottom is a 4 key row where the 1st (leftmost) button types my whole email out,
the 2nd writes my school email out,
the 3nd writes my school password out,
and the 4th writes my home address which is very useful cause I always mess up on the 'Buellis' part

---


