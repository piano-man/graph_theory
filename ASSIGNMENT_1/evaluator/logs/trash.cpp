#include<bits/stdc++.h>
using namespace std;
int main()
{
	ofstream ss("incidence_space");
	for ( int i = 1; i < 100; i += 5  )
	{
		for(int j = 1; j < 100 ; j += 5 )
		{
			ss << i << " " << j << " " << i * j * 4 << endl;
		}
	}
	ss.close();
	ofstream ss2("efficient_space");
	for(int i = 1; i < 100; i += 5)
	{
		for(int j = 1; j < 100 ; j += 5)
		{
			ss2 << i << " " << j << " " <<((j * 12)+4)*2 << endl;
		}
	}
	ss2.close();
}
