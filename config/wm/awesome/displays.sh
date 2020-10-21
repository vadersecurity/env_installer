#!/bin/bash
# download and adjust to your needs --
# @dualfade

xrandr --output eDP-1 --primary
xrandr --output eDP-1 --mode 1920x1080 --rate 60
xrandr --output DP-1 --right-of eDP-1 --auto
xrandr --output HDMI-2 --left-of eDP-1 --auto
#xrandr --output HDMI-1 --right-of eDP-1 --auto
