#!/bin/bash
# @dualfade

# conected displays --
# xrandr | grep -w connected | cut -f '1' -d ' '

# laptop; primary --
/usr/bin/xrandr --output eDP-1 --primary
/usr/bin/xrandr --output eDP-1 --mode 1920x1080 --auto
/usr/bin/xrandr --output eDP-1 --brightness 1.2

# decgear overhead --
# /usr/bin/xrandr --output DP-1 --left-of eDP-1 --auto
# G: 2.0 R: 47 B: 46 G: 52
/usr/bin/xrandr --output DP-1 --left-of eDP-1 --mode 2560x1440 --auto
/usr/bin/xrandr --output DP-1 --brightness 1.0

# Desktop main --
/usr/bin/xrandr --output DP-3 --right-of eDP-1 --mode 3440x1440 --auto
/usr/bin/xrandr --output DP-3 --brightness 1.0

# start other shit --
# -> yain network-manager-applet
# required by protonvpn-cli; stupid dep  --
# /usr/bin/nm-applet &
# /usr/bin/feh --bg-fill ~/.wallpaper/dark-cubes-hd-wallpaper.jpg &
/usr/bin/feh --bg-fill ~/.wallpaper/purple-9.jpg &
/usr/bin/xrdb -merge ~/.Xresources &
