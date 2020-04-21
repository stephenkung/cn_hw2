rm -rf log*
fuser -k -n tcp 23456
sleep 10 

	echo "Begin wireshark"
sleep 2 
python3 server.py  &
	echo "server run"
sleep 30
timeout 60s python3 client.py -wait 20 -length 20  &
	echo "client 1 run"
sleep 30
timeout 50s python3 client.py -wait 40 -length 20  &
	echo "client 2 run"
sleep 30
sleep 30
	echo "end wireshark"
exit 1

