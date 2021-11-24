#!/bin/bash
# download and adjust to your needs --
# @dualfade

/usr/bin/xrandr --output eDP1 --primary
/usr/bin/xrandr --output eDP1 --mode 1920x1080 --auto
/usr/bin/xrandr --output DP1 --left-of eDP1 --auto
/usr/bin/xrandr --output DP3 --right-of eDP1 --mode 3440x1440 --auto

# start other shit --
/usr/bin/picom --config ~/.config/picom/picom.conf &
/usr/bin/feh --bg-fill ~/.wallpaper/min_skull.jpg &
/usr/bin/xrdb -merge ~/.Xresources &
