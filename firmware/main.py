# You import all the IOs of your board
import board
# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation # For matrix scanning
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros # Keep macros for future use
from kmk.extensions.media_keys import MediaKeys # For volume/mute
from kmk.extensions.encoders import EncoderHandler # For rotary encoder

# OLED Display Libraries
import busio
import displayio
import terminalio # For default font
from adafruit_display_text import label
import adafruit_ssd1306

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Add media keys extension for volume/mute
keyboard.extensions.append(MediaKeys())

# --- Matrix Configuration (2 Rows x 3 Columns) ---
# Derived directly from your schematic pin assignments
keyboard.col_pins = (board.GP10, board.GP9, board.GP11)
keyboard.row_pins = (board.GP0, board.GP1)
keyboard.diode_orientation = DiodeOrientation.COL2ROW # Based on your schematic

# --- Encoder Configuration ---
# Derived directly from your schematic pin assignments
encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.GP27, board.GP28, board.GP29),) # (A, B, Push_Button)
keyboard.extensions.append(encoder_handler)

# --- OLED Display Configuration (SSD1306 128x32) ---
displayio.release_displays() # Release any existing displays to avoid errors

# I2C setup (SCL, SDA) - Order needs to match your wiring for busio.I2C
# Your schematic suggests GP7 (SCL) and GP6 (SDA)
i2c = busio.I2C(board.GP7, board.GP6)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C) # Common address, confirm for yours
# !!! IMPORTANT CHANGE: height=32 for your specific OLED !!!
display = adafruit_ssd1306.SSD1306(display_bus, width=128, height=32)

# Make the display context and show it
splash = displayio.Group()
display.show(splash)

# Create a text label for the layer
layer_text = label.Label(terminalio.FONT, text="LAYER: 0", color=0xFFFFFF)
layer_text.x = 0
# For 32-pixel height, y=8 gives a good top-aligned look for one line.
# If you need more lines, you'd need a smaller font or more careful Y placement.
layer_text.y = 8
splash.append(layer_text)

# --- Keymap Definition ---
# This defines what each key does.
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [
        # Layer 0: Base Layer (Default)
        # Matrix (2 rows x 3 columns):
        KC.Q, KC.W, KC.E, # Top Row Keys
        KC.A, KC.S, KC.D  # Bottom Row Keys
    ]
]

# --- Encoder Keymap Definition ---
# This maps encoder turns and button presses to keycodes.
@encoder_handler.map_encoders
def encoder_map(encoder_index, clockwise):
    if encoder_index == 0:  # For the first (and only) encoder
        if clockwise:
            return KC.VOLU # Turn clockwise = Volume Up
        else:
            return KC.VOLD # Turn counter-clockwise = Volume Down
    return KC.NO # No action if something goes wrong or for other encoders

@encoder_handler.map_encoder_buttons
def encoder_button_map(encoder_index, is_pressed):
    if encoder_index == 0: # For the first (and only) encoder's button
        if is_pressed:
            return KC.MUTE # Press button = Mute
    return KC.NO # No action

# --- OLED Update Function ---
# This function is a hook that KMK calls after each matrix scan.
# It updates the OLED with the current layer.
def update_oled(keyboard):
    current_layer = keyboard.active_layers[0] # Get the current active layer
    layer_text.text = f"LAYER: {current_layer}"

keyboard.after_matrix_scan_hooks.append(update_oled)


# Start kmk!
if __name__ == '__main__':
    keyboard.go()