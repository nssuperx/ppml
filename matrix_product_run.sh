#!/bin/sh

proclist=(1 2 3 4 5 6 8 10 12 16 20 24 30 40 60)

for i in {0..2}
do
	for proc in ${proclist[@]}
	do
        mpiexec -n ${proc} ./a.out 1200A.dat 1200B.dat Answer.dat
        mkdir output/result_${i}_${proc}
        mv Elapse-* ./output/result_${i}_${proc}
	done
done

zip -r result.zip output
