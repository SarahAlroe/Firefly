r=0
g=0
b=0

result=$(sudo arp-scan -l -r5)

if echo $result | grep -q $2; then
	r=255
fi

if echo $result | grep -q $3; then
	g=255
fi


if echo $result | grep -q $4; then
	b=255
fi

curl --data "bug=$1&r=$r&g=$g&b=$b" http://firefly.fenrok.tk/set/
