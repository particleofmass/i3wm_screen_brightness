# i3wm-backlight
Map your hot keys to increase or decrease the screen brightness in i3 wm using easy python code

## Install brightnessctl
### ARCH
sudo pacman -S brightnessctl
### DEBIAN
sudo apt-get install brightnessctl
### FEDORA
sudo dnf install brightnessctl


## Paste these lines in your i3 config file(~/.config/i3/config)

bindsym XF86MonBrightnessUp exec brightnessctl -q set +5 

bindsym XF86MonBrightnessDown exec brightnessctl -q set $(($(brightnessctl get)-5))

