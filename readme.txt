# Simha's Macropad RP2040

This is a custom 2x3 macropad with a rotary encoder and an OLED screen.
![Simha_Macropad_Main_Image]

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

**Visuals:**

| Schematic | PCB | Case |
| :---: | :---: | :---: |
| ![Simha Macropad Schematic] | ![Simha Macropad PCB] | ![Simha Macropad Case] |
![image](https://github.com/user-attachments/assets/8ce0ab16-e0b0-42d0-b748-d4ee08ce5972)    |  ![image](https://github.com/user-attachments/assets/556275d9-b148-4d51-b6e8-0c6bf95b5a16)  | ![image](https://github.com/user-attachments/assets/bcfd98e1-e562-48c3-b617-4d55031ebec4)

**Notes:**

I might add QMK later if it works