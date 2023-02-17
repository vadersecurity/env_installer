#!/bin/bash
# Requires: acpi, iostat, lm-sensors, pamixer.

#DISK

hdd() {
    hdd="$(df -h /home | grep /dev | awk '{print $3 "/" $5}')"
    echo -e "$hdd"
}

#RAM

mem() {
    used="$(free -h | grep Mem: | awk '{print $3}')"
    total="$(free -h| grep Mem: | awk '{print $2}')"
    totalh="$(free -h | grep Mem: | awk '{print $2}' | sed 's/Gi/G/')"
    usedh="$(free -h | grep Mem: | awk '{print $3}' | sed 's/Mi/M/' | sed 's/Gi/G/')"
    ram="$usedh/$totalh"
    echo $ram
}

#CPU

cpu() {
    read cpu a b c previdle rest < /proc/stat
    prevtotal=$((a+b+c+previdle))
    sleep 0.5
    read cpu a b c idle rest < /proc/stat
    total=$((a+b+c+idle))
    cpu=$((100*( (total-prevtotal) - (idle-previdle) ) / (total-prevtotal) ))
    echo -e " $cpu%"
}

#VOLUME

vol() {
    vol="$(pulsemixer --get-volume)"
    echo -e "$vol"
}

#vol() {
#	vol="$(amixer -D default get Master | awk -F'[][]' 'END{ print $2 }')"
#	echo -e j $vol"
#}

#MIC

# mic() {
#     state="$()"
#     if [ state = 1 ]; then
#         echo "on"
#     else
#         echo "off"
#     fi
# }

#VPN

vpn() {
    # state="$(ip a | grep 'wg0\|proton0\|tun0' | grep inet | wc -l)"
    state="$(ip a sh | grep -E "wg[0-9].*?|tun[0-9].*?" | grep -c inet)"
   if [ "$state" = 1 ]; then
        echo "on"
    else
        echo "off"
    fi
}

#WEATHER

weather() {
    wthr="$(sed 20q ~/.config/weather.txt | grep value | awk '{print $2 $3}' | sed 's/"//g')"
    echo " $wthr"
}

#TEMP

temp() {
    tmp="$(grep temp_C ~/.config/weather.txt | awk '{print $2}' | sed 's/"//g' | sed 's/,/ C/g')"
    echo " $tmp"
}

#BATTERY

bat() {
    batstat="$(cat /sys/class/power_supply/BAT0/status)"
    battery="$(cat /sys/class/power_supply/BAT0/capacity)"
    if [ $batstat = 'Unknown' ]; then
        batstat=""
    elif [[ $battery -ge 5 ]] && [[ $battery -le 19 ]]; then
        batstat=""
    elif [[ $battery -ge 20 ]] && [[ $battery -le 39 ]]; then
        batstat=""
    elif [[ $battery -ge 40 ]] && [[ $battery -le 59 ]]; then
        batstat=""
    elif [[ $battery -ge 60 ]] && [[ $battery -le 79 ]]; then
        batstat=""
    elif [[ $battery -ge 80 ]] && [[ $battery -le 95 ]]; then
        batstat=""
    elif [[ $battery -ge 96 ]] && [[ $battery -le 100 ]]; then
        batstat=""
    fi

    echo "$batstat  $battery%"
}

#NETWORK

network() {
    # wire="$(ip a | grep -E 'enp.*?' | grep 'inet' | wc -l)"
    # wifi="$(ip a | grep -E 'wlan[0-9].*?' | grep 'inet' | wc -l)"
    wire="$(ip a | grep 'enp[0-9].*?|eth[0-9].*?' | grep -c inet)"
    wifi="$(ip a | grep -E 'wlan[0-9].*?' | grep -c inet)"

    if [ $wire = 1 ]; then
        echo ""
    elif [ $wifi = 1 ]; then
        echo ""
    else
        echo "睊"
    fi
}

# UTC CLOCK

universal_time() {
  TZ=UTC date -R | awk '{print $4,$5,$6}'
}

# FINAL BAR

SLEEP_SEC=2
#loops forever outputting a line every SLEEP_SEC secs
    while :; do
      echo "$(cpu) |  $(mem) |  $(hdd) |  $(vpn) |  $(vol) | $(bat) | $(network) | $(universal_time) |"
        sleep $SLEEP_SEC
    done
