

function singleRun {

  N=$1
  MUA=$2
  MUS=$3
  G=$4
  L=$5

  echo $N $MUA $MUS $G $L
  
  time python main_simpleBeam_fluence.py $N $MUA $MUS $G  > ./data_simpleBeam_murine/Wz_N${N}_MUA${MUA}_MUS${MUS}_G${G}_L${L}.dat 
  #time python main_simpleBeam.py $N $MUA $MUS $G  > ./data_simpleBeam_murine/Wrz_N${N}_MUA${MUA}_MUS${MUS}_G${G}_L${L}.dat 

}



# MURIN (mice; albino) DATA: 
singleRun 100000 27.2  24.55 0.80 2100
singleRun 100000  6.6  44.20 0.91 1320
#singleRun 100000  5.9  60.90 0.92 1064
#singleRun 100000  5.7  97.00 0.94  800
#singleRun 100000  6.5 143.70 0.95  633
#singleRun 100000 12.2 173.50 0.93  488



