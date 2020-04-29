
function singleRun {
  N=$1
  MUA=$2
  MUS=$3
  G=$4
  echo $N $MUA $MUS $G
  python main_gyrationRadius.py $N $MUA $MUS $G > ./data_distribRg/Rg_N${N}_MUA${MUA}_MUS${MUS}_G${G}.dat
}

#singleRun 100000 25.0 25.0 0.0
#singleRun 100000 25.0 25.0 0.3
#singleRun 100000 25.0 25.0 0.5
#singleRun 100000 25.0 25.0 0.7
#singleRun 100000 25.0 25.0 0.9

#singleRun 100000  1.0 20.0 0.0
#singleRun 100000  2.0 20.0 0.0
#singleRun 100000  5.0 20.0 0.0
#singleRun 100000 10.0 20.0 0.0
#singleRun 100000 15.0 20.0 0.0
#singleRun 100000 20.0 20.0 0.0
#singleRun 100000  40.0 20.0 0.0
#singleRun 100000  60.0 20.0 0.0

#singleRun 100000  1.0 20.0 0.3
#singleRun 100000  1.0 20.0 0.5
#singleRun 100000  1.0 20.0 0.7
#singleRun 100000  1.0 20.0 0.9

#singleRun 100000  20.0 20.0 0.3
#singleRun 100000  20.0 20.0 0.5
#singleRun 100000  20.0 20.0 0.7
#singleRun 100000  20.0 20.0 0.9
singleRun 100000  20.0 20.0 0.99


