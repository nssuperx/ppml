#include<stdio.h>
#include<stdlib.h>
#define N 3         // 縦横の要素数 N*N配列を作る

int main(void){
    int i,j;

    int array1[N][N];
    for(i=0; i<N; i++){
        for(j=0; j<N; j++){
            printf("%p, ", &array1[i][j]);
        }
        printf("\n");
    }



    int **array2;
    if((array2 = (int**)malloc(sizeof(int*) * N )) == NULL){
        exit(-1);
    }

    for(i=0; i<N; i++){
        if((array2[i] = (int*)malloc(sizeof(int) * N)) == NULL){
            exit(-1);
        }
    }

    for(i=0; i<N; i++){
        for(j=0; j<N; j++){
            printf("%p, ", &array2[i][j]);
        }
        printf("\n");
    }

    return 0;
}
