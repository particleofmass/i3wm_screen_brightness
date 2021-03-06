#!/usr/bin/env python

# Reading the current level of brightness using read mode
f = open("/sys/class/backlight/intel_backlight/brightness", "r")

# bl stores the current brightness level
bl = int(f.read())

# Closing the file
f.close()

# Opens the file that adjusts brightness in write mode to overwrite the existing value
f = open("/sys/class/backlight/intel_backlight/brightness", "w")

# increase brightness by 5
bl += 5

# Replace the old brightness level with the new one
f.write(str(bl))

f.close()



