#!/usr/bin/env bash

function run {
  if ! pgrep -f $1 ;
  then
    $@&
  fi
}

# run program [some arguments]
run /usr/bin/picom --config ~/.config/picom/picom.conf
run /usr/bin/feh --bg-fill ~/.wallpaper/pins_skull.jpg
run /usr/bin/xbacklight -set 85
run /usr/bin/xrdb -merge ~/.Xresources

# add your own --
run ~/Scripts/set_multi_displays.sh
# run /usr/bin/keybase login username && /usr/bin/systemctl start --user kbfs
