#!/bin/sh

for i in {1..5}
do
	./a.out
	mv pipe_perf1.dat out1/pipe_perf1_${i}.txt
done

zip -r pipe1_result.zip out1

