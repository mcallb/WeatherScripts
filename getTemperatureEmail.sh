temp=`cat /mnt/1-wire/10.56217F010800/temperature | awk '{printf "%.0f\n", $1}'`
if `$temp + 100 | bc < 50`;
then 
mail -s "Alert - Temperature low" mcallb@gmail.com
echo 1
else 
echo 2
fi



