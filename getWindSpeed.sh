#!/bin/sh
X=$(ls /mnt/1-wire/[123456789]*/counters.ALL); 
	for f in $X; 
	do d=$(dirname $f);
		echo "$(date '+%Y%m%d%H%M%S'),$(cat $d/address),$(cat $f | sed -e's/^[ \t]*//'),," >> /mnt/onewire/WeatherData/WindSpeed/$HOSTNAME.WindSpeed.$(date '+%Y%m%d'); 
	done