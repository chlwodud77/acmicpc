#include <iostream>
#include <deque>

using namespace std;

int main(){
	deque<int> dq;

	int N;
	cin >> N;
	for(int i = 1 ; i <= N; i++){
		dq.push_back(i);
	}

	// printf("%d", vec.size());

	while(dq.size() != 1){
		int tmp;
		dq.pop_front();
		// printf("%d", vec.size());
		tmp = dq[0];
		dq.push_back(tmp);
		dq.pop_front();
	}

	printf("%d\n", dq[0]);




	return 0;
}