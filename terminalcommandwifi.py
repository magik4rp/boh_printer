./internet_reboot.sh

while true; do
    if ifconfig wlan0 | grep -q "inet 10.105.132.212"; then
        sleep 60
    else
        echo "network connection down, attempting to reconnect"
        sudo ifconfig wlan0 up
        node printer.js
        sleep 10
    fi
done