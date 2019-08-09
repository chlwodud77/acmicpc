#include <stdio.h>

int is_right(int a, int b, int c);

int main(){
	int a,b,c;
	a = 1;
	b = 1;
	c = 1;

	while(a != 0 and b != 0 and c != 0){
		scanf("%d %d %d",&a,&b,&c);
		if(is_right(a,b,c) == 1) printf("right\n");
		else if(is_right(a,b,c) == 0) printf("wrong\n");
	}
}

int is_right(int a, int b, int c){
	if(a == 0 and b == 0 and c == 0) return 2;
	if((a*a) + (b*b) == (c*c)) return 1;
	else if((a*a) + (c*c) == (b*b)) return 1;
	else if((b*b) + (c*c) == (a*a)) return 1;

	return 0;
}