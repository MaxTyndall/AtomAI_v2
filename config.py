# config.py

# ==================================================
# OPENAI
# ==================================================

CHAT_MODEL = "gpt-4o-mini"
TTS_MODEL = "gpt-4o-mini-tts"
VOICE_NAME = "alloy"

# ==================================================
# PCA9685 SERVO CHANNELS
# ==================================================

LEFT_X = 0
LEFT_Y = 1
LEFT_BLINK = 2

RIGHT_X = 3
RIGHT_Y = 4
RIGHT_BLINK = 5

# ==================================================
# SERVO POSITIONS
# ==================================================

CENTER_X = 90
CENTER_Y = 90

LOOK_LEFT = 70
LOOK_RIGHT = 110

LOOK_UP = 70
LOOK_DOWN = 110

LEFT_EYE_OPEN = 80
LEFT_EYE_CLOSED = 95

RIGHT_EYE_OPEN = 110
RIGHT_EYE_CLOSED = 95

# ==================================================
# NEO PIXEL
# ==================================================

NEOPIXEL_PIN = 18
NUM_PIXELS = 8
BRIGHTNESS = 0.3

# ==================================================
# AUDIO
# ==================================================

SAMPLE_RATE = 44100
CHANNELS = 1
CHUNK_SIZE = 1024

# ==================================================
# ANIMATION
# ==================================================

BLINK_DELAY = 0.15
THINKING_DELAY = 1.0
