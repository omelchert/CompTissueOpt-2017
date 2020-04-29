
for F in  ../Rg_N100000_MUA*_G0.0.dat;
do
        echo $F
        python main_summaryStats.py $F >> summaryStats.dat
done
