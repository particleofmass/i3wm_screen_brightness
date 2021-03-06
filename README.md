# i3wm-backlight-hotkeys
Map your hot keys to increase or decrease the screen brightness in i3 wm using easy python code

# Enter the following commmand:
ls /sys/class/backlight

# If you see amdgpu_bl0 then follow these commands:
sudo chmod 777 /sys/class/backlight/amdgpu_bl0/brightness
# Clone the repository in your user directory
git clone 
# Now add these lines to your i3 config file(~/.config/i3/config)
bindsym XF86MonBrightnessUp exec python3 ~/i3wm-backlight-hotkeys/brightness_py/amdgpu/brightness_up.py
bindsym XF86MonBrightnessDown exec python3 ~/i3wm-backlight-hotkeys/brightness_py/amdgpu/brightness_down.py
# If you cloned the repo in directory other than the use directory then:
bindsym XF86MonBrightnessUp exec python3 <location of the amdgpu/brightness_up.py file>
bindsym XF86MonBrightnessDown exec python3 <location of the amdgpu/brightness_down.py file>

# If you see intel_backlight then follow these commands:
sudo chmod 777 /sys/class/backlight/intel_backlight/brightness
# Clone the repository in your user directory
git clone 
# Now add these lines to your i3 config file(~/.config/i3/config)
bindsym XF86MonBrightnessUp exec python3 ~/i3wm-backlight-hotkeys/brightness_py/intelgpu/brightness_up.py
bindsym XF86MonBrightnessDown exec python3 ~/i3wm-backlight-hotkeys/brightness_py/intelgpu/brightness_down.py
# If you cloned the repo in directory other than the use directory then:
bindsym XF86MonBrightnessUp exec python3 <location of the intelgpu/brightness_up.py file>
bindsym XF86MonBrightnessDown exec python3 <location of the intelgpu/brightness_down.py file>
