X=$(ls /mnt/1-wire/[123456789]*/temperature);
	for f in $X; 
	do d=$(dirname $f);
		echo "$(date '+%Y%m%d%H%M%S'),$(cat $d/address),$(cat $f | sed -e's/^[ \t]*//'),,," >> /mnt/WeatherData/Temperature/$HOSTNAME.Temperature.$(date '+%Y%m%d');  
	done