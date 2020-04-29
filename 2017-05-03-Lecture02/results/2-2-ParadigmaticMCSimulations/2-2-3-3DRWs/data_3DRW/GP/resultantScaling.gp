
set xlabel 'N'
set ylabel 'R(g)'

set yr [2:200]
set key left

set logs 

set size 0.6,0.6

#f(x)=a*sqrt(x)
#a=1.
#fit [x=:] f(x) '../res_3DRW_M200_G0.9.out' u 1:2:3 via a 

p '../res_3drw_m200_g0.1.out' u 1:2:3 w yerrorlines t 'g=0.1'\
, '../res_3DRW_M200_G0.3.out' u 1:2:3 w yerrorlines t '0.3'\
, '../res_3DRW_M200_G0.5.out' u 1:2:3 w yerrorlines t '0.5'\
, '../res_3DRW_M200_G0.7.out' u 1:2:3 w yerrorlines t '0.7'\
, '../res_3DRW_M200_G0.9.out' u 1:2:3 w yerrorlines t '0.9'\



