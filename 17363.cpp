#include <stdio.h>

int main(){
	int N,M;

	char inputZ[100][100];
	char outputZ[100][100];

	scanf("%d %d",&N,&M);

	for(int i = 0 ; i < N; i++){
			scanf("%s", &inputZ[i]);
	}
	
	int Z = M-1;
	for(int i = 0 ; i < M; i++){
		for(int j = 0 ; j < N; j++){
			char X = inputZ[j][Z];
			if(X == '-') X = '|';
			else if(X == '|') X = '-';
			else if(X == '/') X = '\\';
			else if(X == '\\') X = '/';
			else if(X == '^') X = '<';
			else if(X == '<') X = 'v';
			else if(X == 'v') X = '>';
			else if(X == '>') X = '^';
			outputZ[i][j] = X;
		}
		--Z;
	}



	for(int i = 0 ; i < M; i++){
		for(int j = 0 ; j < N; j++){
			printf("%c", outputZ[i][j]);
		}
		printf("\n");
	}

	return 0;
}