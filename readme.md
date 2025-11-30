# Simha's Macropad RP2040

This is a custom 2x3 macropad with a rotary encoder and an OLED screen.
![image](https://github.com/firesareba/Simha-s-Hackropad/blob/d07858936782be31b3da56834d2cbd88fa9aed29/Screenshot%202025-11-29%20215759.png)

### Inspiration

I wanted to create a macropad that was both functional and aesthetically pleasing. I created a macropad featuring a 2x3 key matrix, a rotary encoder with a push button, and an OLED display, all powered by a **Seeed XIAO RP2040**.

### Challenges

This was my first time using Fusion 360. It was a really cool experience to learn. A lot of my friends tell me to use Onshape so I might stick with that in the future because Fusion360 was very clunky in my opinion. I was first very intimidated by having to create a entire PCB from scratch but the guide was super useful and taught me the basics of KiCad (i might make my own board one day). I big issue for me was creating the firmware, as QMK was just not complying so I went with a KMK firmware instead.

THANKS HACK CLUB! 

### Specifications

**Bill of Materials (BOM):**

-   6x Cherry MX Switches
-   6x 1N4148 Diodes
-   1x Seeed XIAO RP2040
-   1x SSD1306 0.91" 128x32 I2C OLED Display
-   1x Rotary Encoder (EC11-style with switch)
-   6x Blank DSA Keycaps
-   1x Rotary Encoder Knob
-   4x M3x16 Bolt
-   4x M3 Heatset

---

****A BOM CSV is also included but doesn't account for things outside the PCB***

**Visuals:**

| Schematic | PCB | Case |
| :---: | :---: | :---: |
| ![Simha Macropad Schematic] | ![Simha Macropad PCB] | ![Simha Macropad Case] |
![image](https://github.com/firesareba/Simha-s-Hackropad/blob/d07858936782be31b3da56834d2cbd88fa9aed29/unnamed.png)    |  ![image](https://github.com/firesareba/Simha-s-Hackropad/blob/d07858936782be31b3da56834d2cbd88fa9aed29/Screenshot%202025-11-29%20215950.png)  | ![image](https://github.com/firesareba/Simha-s-Hackropad/blob/d07858936782be31b3da56834d2cbd88fa9aed29/Screenshot%202025-11-29%20221238.png)

**Notes:**

I might add QMK later if it works
