#include<bits/stdc++.h>
#include<string>
#include<ctime>
using namespace std;
//string filenames[] = [string a("gagan"),string b("vinay")];
string getInput(int V , int E,bool isVinay)
{
	string s;
	if(isVinay)
		s += " 1\n" ;
	stringstream ss,ss2;
	int random,random1,weight;
	for(int i = 0; i < E; i ++ )
	{
		random =  i % V;
		random1 = (rand()+1)%V;
		weight = rand() % E;
		ss << " " << random << " " << random1 << " " << weight << " " << endl;
		s += ss.str();

	}
	s += "-1 ";
	for(int i = E + 1; i < V ; i ++ )
	{
		ss2 << " " << i << " " << i << " " << 0 << endl;
		s += ss2.str();
	}
	s += "-1\n";
	return s;
}
void run(int i , int j,bool isVinay)
{
	char * code,*timeoutput,*spaceoutput,*executable;
	clock_t start = clock();
	ofstream myfile;
	char * space,*time,*exec;
	if(isVinay)
	{
		 space = "vinay_space";
		time = "vinay_time";
		exec = "./vinay < input > output";
	}
	else
	{
		space = "gagan_space";
		time = "gagan_time";
		exec = "./gagan < input > output";
	}
	ofstream output(space,ios::app),output2(time,ios::app);
	myfile.open ("input");
	myfile << getInput(i,j,isVinay);
	myfile.close();
	start = clock();
	int status = system(exec);
	clock_t end = clock();
	ifstream file;
	file.open("output");
	string ss;
	file >> ss;
	output <<i << " " << j << " "  <<  ss << endl;
	output.close();
	output2 << i << " " << j << " " << (end -start )/(float)CLOCKS_PER_SEC << endl;
	output2.close();
	
}
int main()
{
	for(int i = 1; i < 100; i += 5)
	{
		for(int j = 1; j < 100; j += 5)
		{
			run(i,j,true);
		}
	}
	cout << "vinay completed" << endl;
	for(int i = 1; i < 100; i += 5)
	{
		for(int j = 1; j < 100; j += 5)
		{
			run(i,j,false);
		}
	}
	cout << "gagan completed"<<endl;
}
