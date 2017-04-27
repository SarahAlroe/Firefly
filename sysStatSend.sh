r=`grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*255/($2+$4+$5)} END {print int(usage)}'`
g=`free -m | grep 'Mem:' | awk 'END {print int($3/$2*255)}'`
counter=0

sda=`hdparm -C /dev/sda | grep 'drive state is' | awk 'END{print $4}'`
if [ "$sda" = 'active/idle' ]; then
counter=$((counter + 1))
fi;

sdb=`hdparm -C /dev/sdb | grep 'drive state is' | awk 'END{print $4}'` 
if [ "$sdb" = 'active/idle' ]; then
counter=$((counter + 1))
fi;

sdc=`hdparm -C /dev/sdc | grep 'drive state is' | awk 'END{print $4}'` 
if [ "$sdc" = 'active/idle' ]; then
counter=$((counter + 1))
fi;

sdd=`hdparm -C /dev/sdd | grep 'drive state is' | awk 'END{print $4}'` 
if [ "$sdd" = 'active/idle' ]; then
counter=$((counter + ))
fi;

b=$((counter*255/4))

curl --data "bug=1&r=$r&g=$g&b=$b" http://firefly.fenrok.tk/set/
