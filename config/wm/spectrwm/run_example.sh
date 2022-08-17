#!/bin/bash
# download and adjust to your needs --
# @dualfade

/usr/bin/xrandr --output eDP1 --primary
/usr/bin/xrandr --output eDP1 --mode 1920x1080 --auto
/usr/bin/xrandr --output DP1 --left-of eDP1 --auto
/usr/bin/xrandr --output DP3 --right-of eDP1 --mode 3440x1440 --auto

# start other shit --
# required by protonvpn-cli; stupid dep  --
# yain network-manager-applet
#/usr/bin/nm-applet &
#/usr/bin/feh --bg-fill ~/.wallpaper/dark-cubes-hd-wallpaper.jpg &
/usr/bin/xrdb -merge ~/.Xresources &
