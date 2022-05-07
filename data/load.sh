for i in $(seq 1 100)
do
    sleep 0.01 
    echo $i
done | whiptail --title 'E0' --gauge 'Loading...' 6 60 0
