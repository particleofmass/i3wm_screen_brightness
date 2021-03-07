# i3wm-backlight
Map your hot keys to increase or decrease the screen brightness in i3 wm using easy python code

# Enter the following commmand:
ls /sys/class/backlight
# We just need the location of the file named "brightness"

# If you see/have amdgpu_bl0 then follow these commands or scroll down for intel_backlight :
# Clone the repository in your user directory
git clone https://github.com/particleofmass/.i3wm-backlight-hotkeys.git
# Move the file .i3wm-backlight-hotkeys/amdgpu/brightness_py.service to /etc/systemd/system/
# If you cloned the repo in the user directory then use
mv ~/.i3wm-backlight-hotkeys/amdgpu/brightness_py.service /etc/systemd/system/
# Enable and start the service file. So run:
sudo systemctl enable backlight_py.service
sudo systemctl start backlight_py.service
# Now add these lines to your i3 config file(~/.config/i3/config)
# for increasing brightness
bindsym XF86MonBrightnessUp exec python3 ~/.i3wm-backlight-hotkeys/brightness_py/amdgpu/brightness_up.py
# for decreasing brightness
bindsym XF86MonBrightnessDown exec python3 ~/.i3wm-backlight-hotkeys/brightness_py/amdgpu/brightness_down.py
# If you cloned the repo in directory other than the use directory then:
# for increasing brightness
bindsym XF86MonBrightnessUp exec python3 <location of the amdgpu/brightness_up.py file>
# for decreasing brightness
bindsym XF86MonBrightnessDown exec python3 <location of the amdgpu/brightness_down.py file>


# If you see/have intel_backlight then follow these commands:
# Clone the repository in your user directory
git clone https://github.com/particleofmass/i3wm-backlight-hotkeys.git
# Move the file i3wm-backlight-hotkeys/intelgpu/brightness_py.service to /etc/systemd/system/
# If you cloned the repo in the user directory then use
mv ~/.i3wm-backlight-hotkeys/intelgpu/brightness_py.service /etc/systemd/system/
# Enable and start the service file. So run:
sudo systemctl enable backlight_py.service
sudo systemctl start backlight_py.service
# Now add these lines to your i3 config file(~/.config/i3/config)
# for increasing brightness
bindsym XF86MonBrightnessUp exec python3 ~/.i3wm-backlight-hotkeys/brightness_py/intelgpu/brightness_up.py
# for decreasing brightness
bindsym XF86MonBrightnessDown exec python3 ~/.i3wm-backlight-hotkeys/brightness_py/intelgpu/brightness_down.py
# If you cloned the repo in directory other than the use directory then:
bindsym XF86MonBrightnessUp exec python3 <location of the intelgpu/brightness_up.py file>
bindsym XF86MonBrightnessDown exec python3 <location of the intelgpu/brightness_down.py file>
