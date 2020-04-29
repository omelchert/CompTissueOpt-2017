M=200
for G in 0.1 0.3 0.5 0.7 0.9;
do
echo $G
for N in 12 16 24 32 48 64 96 128 192 256 384 512 ; # 768 1024 ;
do
    echo $N
    python main_3DRW_stats.py $N $M $G >> ./data_3DRW/res_3DRW_M${M}_G${G}.out
done
done
