wget -w 2 -m http://www.gutenberg.org/robot/harvest?filetypes[]=txt&langs[]=en
cat www.gutenberg.org/robot/* > allLinks
grep -oh 'http://[a-zA-Z0-9./]*.zip' allLinks > zipList
for URL in $(cat zipList)
	do
		wget $URL 
		sleep 2
	done 
rm -rf www.gutenberg.org/
