##############################################
# The MIT License (MIT)
# Copyright (c) 2017 Kevin Walchko
# Copyright (c) 2021 Nick Stiffler
# see LICENSE for full details
##############################################
# Changelog:
#   This differs from other implementations as it uses the Python3 Enum class
##############################################

"""
create_oi.py - Contains the Open Interface (OI) constants for the iRobot Create 2.
"""

from enum import IntEnum

# Note for students: 0x?? is equivalent to 0b????????, hex is used for compactness

# -------------------- Robot Specs --------------------
class ROBOT(IntEnum):
	"""Information about the robot specifications."""
	TICK_PER_REV     = 508.8  # Number of encoder ticks per wheel revolution
	WHEEL_DIAMETER   = 72  # Diameter of wheels in mm
	WHEEL_BASE       = 235  # Distance between wheels in mm
	TICK_TO_DISTANCE = 0.44456499814949904317867595046408  # Conversion factor from ticks to distance traveled

# -------------------- Days of the Week --------------------
class DAYS(IntEnum):
	"""Bitmask representation of the days of the week used in scheduling."""
	SUNDAY    = 0x01  # Sunday represented as bit 0x01
	MONDAY    = 0x02  # Monday represented as bit 0x02
	TUESDAY   = 0x04  # Tuesday represented as bit 0x04
	WEDNESDAY = 0x08  # Wednesday represented as bit 0x08
	THURSDAY  = 0x10  # Thursday represented as bit 0x10
	FRIDAY    = 0x20  # Friday represented as bit 0x20
	SATURDAY  = 0x40  # Saturday represented as bit 0x40

# -------------------- Baud Rates --------------------
class BAUD_RATE(IntEnum):
	"""Baud rates supported for serial communication with the robot."""
	BAUD_300    = 0  # 300 baud rate
	BAUD_600    = 1  # 600 baud rate
	BAUD_1200   = 2  # 1200 baud rate
	BAUD_2400   = 3  # 2400 baud rate
	BAUD_4800   = 4  # 4800 baud rate
	BAUD_9600   = 5  # 9600 baud rate (default)
	BAUD_14400  = 6  # 14400 baud rate
	BAUD_19200  = 7  # 19200 baud rate
	BAUD_28800  = 8  # 28800 baud rate
	BAUD_38400  = 9  # 38400 baud rate
	BAUD_57600  = 10 # 57600 baud rate
	BAUD_115200 = 11 # 115200 baud rate

# -------------------- Operating Modes --------------------
class MODES(IntEnum):
	"""Operating modes of the robot that define its behavior and control access."""
	OFF     = 0  # Robot is powered off
	PASSIVE = 1  # Passive mode, listens for commands but does not drive motors
	SAFE    = 2  # Safe mode, movement with restrictions to prevent damage
	FULL    = 3  # Full mode, complete control without safety restrictions

# -------------------- Drive Modes --------------------
class DRIVE(IntEnum):
	"""Drive commands defining movement behavior."""
	STRAIGHT = 0x8000  # Drive straight ahead
	TURN_CW  = -1  # Turn clockwise
	TURN_CCW = 1  # Turn counterclockwise

class MOTORS(IntEnum):
	"""Motor bitmasks used to control different motorized components."""
	SIDE_BRUSH           = 0x01  # Side brush motor control
	VACUUM               = 0x02  # Vacuum motor control
	MAIN_BRUSH           = 0x04  # Main brush motor control
	SIDE_BRUSH_DIRECTION = 0x08  # Side brush rotation direction
	MAIN_BRUSH_DIRECTION = 0x10  # Main brush rotation direction

# -------------------- LEDs --------------------
class LEDS(IntEnum):
	"""LED indicators for status reporting."""
	DEBRIS      = 0x01  # Indicates debris detected
	SPOT        = 0x02  # Spot cleaning mode active
	DOCK        = 0x04  # Robot is docking
	CHECK_ROBOT = 0x08  # Check robot indicator

class SCHEDULING_LEDS(IntEnum):
	"""Scheduling LED indicators for time-related functions."""
	COLON    = 0x01  # Colon separator in the display
	PM       = 0x02  # PM indicator
	AM       = 0x04  # AM indicator
	CLOCK    = 0x08  # Clock display indicator
	SCHEDULE = 0x10  # Schedule mode active

# -------------------- Opcodes --------------------
class OPCODES(IntEnum):
	"""Command opcodes used to interact with the robot."""
	# Getting started commands
	START = 128  # Enter Open Interface mode
	RESET = 7  # Reset the robot
	STOP  = 173  # Stop the robot immediately
	BAUD  = 129  # Change baud rate

	# Mode control commands
	SAFE = 131  # Enter Safe mode
	FULL = 132  # Enter Full mode

	# Cleaning commands
	CLEAN     = 135  # Start standard cleaning
	MAX       = 136  # Start maximum cleaning cycle
	SPOT      = 134  # Start spot cleaning cycle
	SEEK_DOCK = 143  # Locate and return to docking station

# -------------------- Opcodes --------------------
class OPCODES(IntEnum):
	"""Command opcodes used to interact with the robot."""
	# Getting started commands (pg 8)
	START = 128 # Enter Open Interface mode, initializes communication
	RESET = 7   # Reset the robot, bringing it back to initial state
	STOP  = 173 # Stop the robot immediately, halting all movement
	BAUD  = 129 # Change the baud rate for serial communication

	# Mode control commands (pg 10)
	SAFE = 131  # Enter Safe mode, allows movement with some restrictions
	FULL = 132  # Enter Full mode, complete control without safety constraints

	# Cleaning commands (pg 11)
	CLEAN        = 135  # Start standard cleaning cycle
	MAX          = 136  # Start maximum cleaning cycle, runs until battery is low
	SPOT         = 134  # Start spot cleaning cycle, focused on small areas
	SEEK_DOCK    = 143  # Locate and return to docking station for charging
	POWER        = 133  # Turn off the robot power
	SCHEDULE     = 167  # Set cleaning schedule
	SET_DAY_TIME = 168  # Set the current day and time

	# Actuator commands (page 13)
	DRIVE           = 137  # Command to drive with velocity and radius
	DRIVE_DIRECT    = 145  # Direct control of left and right wheel velocities
	DRIVE_PWM       = 146  # Set wheel drive power using PWM values
	MOTORS          = 138  # Enable or disable motors (side brush, main brush, vacuum)
	MOTORS_PWM      = 144  # Control motor speeds using PWM values
	LED             = 139  # Control the LED indicators
	SCHEDULING_LED  = 162  # Control scheduling-related LEDs
	BUTTONS         = 165  # Read button presses
	DIGIT_LED_ASCII = 164  # Display ASCII characters on digit LEDs
	SONG            = 140  # Define a song to be played later
	PLAY            = 141  # Play a pre-defined song

	# Input commands (page 21)
	SENSORS             = 142  # Retrieve sensor data packets
	QUERY_LIST          = 149  # Query multiple sensor packets
	STREAM              = 148  # Enable continuous sensor data streaming
	PAUSE_RESUME_STREAM = 150  # Pause or resume data stream

	# -------------------- Sensors --------------------
class CHARGE_SOURCE(IntEnum):
	"""Charge sources for the robot's battery."""
	INTERNAL  = 0x01  # Internal charging source (direct power)
	HOME_BASE = 0x02  # Charging via the home docking station

class CHARGING_STATE(IntEnum):
	"""Represents different charging states of the robot."""
	NOT_CHARGING     = 0  # Robot is not charging
	RECONDITIONING   = 1  # Reconditioning charge mode
	FULL_CHARGING    = 2  # Actively charging battery to full
	TRICKLE_CHARGING = 3  # Maintaining charge with low power input
	WAITING          = 4  # Awaiting charging input
	CHARGING_FAULT   = 5  # Charging error detected

class BUTTONS(IntEnum):
	"""Bitmask representations of buttons on the robot."""
	CLEAN    = 0x01  # Clean button pressed
	SPOT     = 0x02  # Spot cleaning button pressed
	DOCK     = 0x04  # Dock button pressed
	MINUTE   = 0x08  # Minute adjustment button pressed
	HOUR     = 0x10  # Hour adjustment button pressed
	DAY      = 0x20  # Day adjustment button pressed
	SCHEDULE = 0x40  # Schedule setting button pressed
	CLOCK    = 0x80  # Clock setting button pressed

class WHEEL_OVERCURRENT(IntEnum):
	"""Indicates overcurrent detection for the wheels and brushes."""
	SIDE_BRUSH  = 0x01  # Overcurrent detected on the side brush motor
	MAIN_BRUSH  = 0x02  # Overcurrent detected on the main brush motor
	RIGHT_WHEEL = 0x04  # Overcurrent detected on the right wheel motor
	LEFT_WHEEL  = 0x08  # Overcurrent detected on the left wheel motor

class BUMPS_WHEEL_DROPS(IntEnum):
	"""Bitmask representations for bump and wheel drop sensors."""
	BUMP_RIGHT       = 0x01  # Right bumper triggered
	BUMP_LEFT        = 0x02  # Left bumper triggered
	WHEEL_DROP_RIGHT = 0x04  # Right wheel is off the ground
	WHEEL_DROP_LEFT  = 0x08  # Left wheel is off the ground

class LIGHT_BUMPER(IntEnum):
	"""Represents light bumper sensors detecting obstacles."""
	LEFT         = 0x01  # Left light bumper triggered
	FRONT_LEFT   = 0x02  # Front-left light bumper triggered
	CENTER_LEFT  = 0x04  # Center-left light bumper triggered
	CENTER_RIGHT = 0x08  # Center-right light bumper triggered
	FRONT_RIGHT  = 0x10  # Front-right light bumper triggered
	RIGHT        = 0x20  # Right light bumper triggered

class STASIS(IntEnum):
	"""Indicates the stasis state of the robot."""
	TOGGLING = 0x01  # Robot is in toggling state
	DISABLED = 0x02  # Stasis detection is disabled

class SENSOR_PACKETS(IntEnum):
	"""Sensor packet IDs used to retrieve specific sensor data."""
	BUMPS_AND_WHEELDROPS     = 7  # Bump and wheel drop sensors
	WALL                     = 8  # Wall sensor status
	CLIFF_LEFT               = 9  # Left cliff sensor
	CLIFF_FRONT_LEFT         = 10  # Front-left cliff sensor
	CLIFF_FRONT_RIGHT        = 11  # Front-right cliff sensor
	CLIFF_RIGHT              = 12  # Right cliff sensor
	VIRTUAL_WALL             = 13  # Virtual wall sensor
	WHEEL_OVERCURRENTS       = 14  # Wheel overcurrent status
	DIRT_DETECT              = 15  # Dirt detection sensor
	IR_OPCODE                = 17  # IR sensor opcode received
	BUTTONS                  = 18  # Button press status
	DISTANCE                 = 19  # Distance traveled since last read
	ANGLE                    = 20  # Angle turned since last read
	CHARGE_STATE             = 21  # Current charging state
	VOLTAGE                  = 22  # Battery voltage
	CURRENT                  = 23  # Current flowing into or out of the battery
	TEMPERATURE              = 24  # Battery temperature
	BATTERY_CHARGE           = 25  # Current battery charge level
	BATTERY_CAPACITY         = 26  # Maximum battery capacity
	WALL_SIGNAL              = 27  # Strength of wall sensor signal
	CLIFF_LEFT_SIGNAL        = 28  # Strength of left cliff sensor signal
	CLIFF_FRONT_LEFT_SIGNAL  = 29  # Strength of front-left cliff sensor signal
	CLIFF_FRONT_RIGHT_SIGNAL = 30  # Strength of front-right cliff sensor signal
	CLIFF_RIGHT_SIGNAL       = 31  # Strength of right cliff sensor signal
	CHARGING_SOURCES         = 34  # Available charging sources
	OI_MODE                  = 35  # Current Open Interface mode
	SONG_NUMBER              = 36  # Currently selected song number
	SONG_PLAYING             = 37  # Whether a song is currently playing
	OI_STREAM_PACKET_SIZE    = 38  # Size of incoming streaming packet
	VELOCITY                 = 39  # Current velocity of the robot
	TURN_RADIUS              = 40  # Current turn radius
	VELOCITY_RIGHT           = 41  # Current velocity of right wheel
	VELOCITY_LEFT            = 42  # Current velocity of left wheel
	ENCODER_LEFT             = 43  # Left wheel encoder count
	ENCODER_RIGHT            = 44  # Right wheel encoder count
	LIGHT_BUMPER             = 45  # Light bumper status
	LIGHT_BUMP_LEFT          = 46  # Left light bumper signal strength
	LIGHT_BUMP_FRONT_LEFT    = 47  # Front-left light bumper signal strength
	LIGHT_BUMP_CENTER_LEFT   = 48  # Center-left light bumper signal strength
	LIGHT_BUMP_CENTER_RIGHT  = 49  # Center-right light bumper signal strength
	LIGHT_BUMP_FRONT_RIGHT   = 50  # Front-right light bumper signal strength
	LIGHT_BUMP_RIGHT         = 51  # Right light bumper signal strength
	IR_OPCODE_LEFT           = 52  # Left IR sensor opcode received
	IR_OPCODE_RIGHT          = 53  # Right IR sensor opcode received
	LEFT_MOTOR_CURRENT       = 54  # Current draw of left motor
	RIGHT_MOTOR_CURRENT      = 55  # Current draw of right motor
	MAIN_BRUSH_CURRENT       = 56  # Current draw of main brush motor
	SIDE_BRUSH_CURRENT       = 57  # Current draw of side brush motor
	STASIS                   = 58  # Stasis sensor reading