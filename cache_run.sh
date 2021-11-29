#!/bin/sh

sizelist=(128 256 512 1024 2048 4096 8192)

for i in {1..5}
do
	for size in ${sizelist[@]}
	do
		./a.out ${size} > ./output/norm_${size}_${i}.txt
	done
done

zip -r cache_result.zip output
