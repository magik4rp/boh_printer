while true; do
	if ifconfig wlan0 | grep -q "10.105.133.77" ; then
		sleep 60
	else
		echo "Network connection down, attempting to reconnect."
		sudo ifconfig wlan0 up
		node printer.js
		sleep 10
	fi
done
