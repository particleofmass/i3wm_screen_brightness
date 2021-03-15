# i3wm_screen_brightness
Map your hot keys to increase or decrease the screen brightness in i3 wm

## Install brightnessctl
### ARCH
sudo pacman -S brightnessctl
### DEBIAN
sudo apt-get install brightnessctl
### FEDORA
sudo dnf install brightnessctl


## Paste these lines in your i3 config file(~/.config/i3/config)

# Increase brightness
bindsym XF86MonBrightnessUp exec --no-startup-id brightnessctl set +5%
# Decrease brightness
bindsym XF86MonBrightnessDown exec --no-startup-id brightnessctl set 5%-


