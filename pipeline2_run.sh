#!/bin/sh

for i in {1..5}
do
	./a.out
	mv pipe_perf2.dat out2/pipe_perf2_${i}.txt
done

zip -r pipe2_result.zip out2

