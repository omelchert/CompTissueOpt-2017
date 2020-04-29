M=100000
N=10
for G in 0.1 0.3 0.5 0.7 0.9;
do
    echo $G
    python main_3DRW_hist.py $N $M $G >> ./data_3DRWHist/resHist_3DRW_M${M}_G${G}.out
done
