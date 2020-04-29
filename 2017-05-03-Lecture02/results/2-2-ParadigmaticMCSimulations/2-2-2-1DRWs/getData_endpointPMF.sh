
M=100000
for N in 10 50 100;
do
    echo $N
    python main_1DRW_endpointPMF_compare.py $N $M 'BAD' > ./data_endpointPMF/pmf_BAD_N${N}_M${M}.dat 
    python main_1DRW_endpointPMF_compare.py $N $M 'RANDU' > ./data_endpointPMF/pmf_RANDU_N${N}_M${M}.dat 
    #python main_1DRW_endpointPMF_compare.py $N $M 'MT' > ./data_endpointPMF/pmf_MT_N${N}_M${M}.dat 
done
