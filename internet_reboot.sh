while true; do
	if ifconfig wlan0 | grep -q "10.105.134.231"; then
		sleep 60
	else
		echo "Network connection down, attempting to reconnect."
		sudo ifconfig wlan0 up
		
		sleep 10
	fi
done
