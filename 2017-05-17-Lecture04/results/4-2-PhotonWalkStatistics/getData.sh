
function singleRun {
  N=$1
  MUA=$2
  MUS=$3
  G=$4
  echo $N $MUA $MUS $G
  python main_gyrationRadius.py $N $MUA $MUS $G > ./data/Rg_N${N}_MUA${MUA}_MUS${MUS}_G${G}.dat
}

# MURIN (mice; albino) DATA: 
# LAMBDA = 2100 nm, MUA = 27.2 cm-1, MUS = 24.55 cm-1, G = 0.80  
singleRun 100000 27.2 24.55 0.80

singleRun 100000 25.0 25.0 0.0
singleRun 100000 25.0 25.0 0.3
singleRun 100000 25.0 25.0 0.5
singleRun 100000 25.0 25.0 0.7
singleRun 100000 25.0 25.0 0.9




