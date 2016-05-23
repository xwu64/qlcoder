#include <stdio.h>
#include <stdlib.h>
#include <cstdio>
#include <cstring>
using namespace std;
long long twist(long long u,long long v)
{
	return (((u & 0x80000000L) | (v & 0x7fffffffL)) >> 1) ^ ((v & 1) == 1 ? 0x9908b0dfL : 0);
}
long long state[624];
int left=1;

void next_state()
{
	int p = 0;
	left = 624;
	for (int j = 228; --j > 0; p++) 
		state[p] = state[p+397] ^ twist(state[p], state[p + 1]);

	for (int j=397;--j>0;p++) 
		state[p] = state[p-227] ^ twist(state[p], state[p + 1]);

	state[p] = state[p-227] ^ twist(state[p], state[0]);
}
long long next()
{
	if (--left == 0) next_state();
	return state[624-left];
}
int main()
{
    char * filename = (char *)calloc(20,sizeof(char));
    FILE * fp;
    long long Value;
    int hValue;
    int i, j;
    int flag[500];
    long long tempData[500][1000];

    for(i=0; i<500; i++){
            flag[i] = 0;
    }

    for(i=0; i<500; i++){
        for(j = 0; j<1000; j++){
            tempData[i][j] = 0;
        }
    }

	for(int j=1;j<624;j++)
	{
		state[j] = (1812433253L * (state[j - 1] ^ (state[j - 1] >> 30)) + j);
		state[j] &= 0xffffffffL;
	}
	for(long long  i=0;i<5000000000L;i++)
	{
        Value = next();
        hValue = Value % 500;
        tempData[hValue][flag[hValue]] = Value;
        flag[hValue]++;
        if(flag[hValue] == 1000){
            sprintf(filename, "%d", hValue);
            fp = fopen(filename, "a");
            for(j = 0; j<1000; j++){
                fprintf(fp, "%lld\n", tempData[hValue][j]);
            }
            flag[hValue] = 0;
            fclose(fp);
        }
		//printf("%lld\n",next());
	}
	return 0;
}

