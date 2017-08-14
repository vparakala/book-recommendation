for URL in $(cat zipList)
	do
		wget $URL 
		sleep 2
	done 
