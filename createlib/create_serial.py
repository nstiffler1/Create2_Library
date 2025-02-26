##############################################
# The MIT License (MIT)
# Copyright (c) 2021 Nick Stiffler
#############################################
# The following draws from:
#   Copyright (c) 2020 iRobot Corporation
#   Copyright (c) 2017 Kevin Walchko
##############################################
# The following is an interface between
#   - Create 2 and 
#   - pyserial 
# to be used in by our tkinter driver file 
#############################################
# Changelog:
#   + threading - repeatable lock for "locking" communication channel

import serial 
import struct
import threading
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class SerialCommandInterface(object):
    """Handles sending commands to the iRobot Create 2 over serial."""

    def __init__(self):
        """
        Initializes a serial communication object but does not open it yet.
        """

        self.ser = serial.Serial()
        self.lock = threading.RLock()

    def __del__(self):
        """
        Destructor.

        Closes the serial port
        """
        self.close()

    def open(self, port, baud=115200, timeout=1):
        """
        Opens a serial port to the create.

        port: the serial port to open, ie, '/dev/ttyUSB0'
        buad: default is 115200, but can be changed to a lower rate via the create api
        """
        self.ser.port = port
        self.ser.baudrate = baud
        self.ser.timeout = timeout

        # close the serial connection if it has already been opened
        if self.ser.is_open:
            self.ser.close()

        try:
            self.ser.open()
            logging.info(f"Connected to {port} at {baud} baud")
        except serial.SerialException as e:
            logging.error(f"Failed to open serial port {port}: {e}")
            raise

    def write(self, opcode, data=None):
        """
        Writes a command to the create. There needs to be an opcode and optionally
        data. Not all commands have data associated with it.

        opcode: see create api
        data: a tuple with data associated with a given opcode (see api)
        """
        with self.lock:
            msg = (opcode,)

            # Sometimes opcodes don't need data. Since we can't add
            # a None type to a tuple, we have to make this check.
            if data:
                msg += data

            self.ser.write(struct.pack('B' * len(msg), *msg))
            self.ser.flush()

    def read(self, num_bytes):
        """
        Read a string of 'num_bytes' bytes from the robot.

        Arguments:
            num_bytes: The number of bytes we expect to read.
        """
        if not self.ser.is_open:
            raise Exception("You must open the serial port first")

        with self.lock:
            return self.ser.read(num_bytes)

    def flush(self):
        """
        Flush the input buffer, discarding all contents
        """
        if not self.ser.is_open:
            raise Exception("You must open the serial port first")

        self.ser.flushInput()

    def close(self):
        """
        Closes the serial connection.
        """
        if self.ser.is_open:
            logging.info(f"Closing port {self.ser.port} at {self.ser.baudrate} baud")
            self.ser.close()