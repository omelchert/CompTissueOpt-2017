
function singleRun {
  N=$1
  MUA=$2
  MUS=$3
  G=$4
  echo $N $MUA $MUS $G
  python main_fluenceRate.py $N $MUA $MUS $G > ./data/fluenceRateMC_N${N}_MUA${MUA}_MUS${MUS}_G${G}.dat
}

#singleRun 10000 10. 10. 0.0
#singleRun 10000 10. 10. 0.3
#singleRun 10000 10. 10. 0.5
#singleRun 10000 10. 10. 0.7
#singleRun 10000 10. 10. 0.9

singleRun 10000 2. 20. 0.0


