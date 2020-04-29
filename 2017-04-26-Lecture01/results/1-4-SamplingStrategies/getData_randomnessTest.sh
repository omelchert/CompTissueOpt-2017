

M=100000
for N in 20 100 500;
do
  echo "samples:" $N  "sets:" $M
  #python main_randomnessTest_unitVectors.py $N $M \
  #    > ./dataRandomnessTest/rTest_N${N}_M${M}.dat 

  python main_randomnessTest_unitVectors_BAD.py $N $M \
      > ./dataRandomnessTest/rTest_BAD_N${N}_M${M}.dat 
done

