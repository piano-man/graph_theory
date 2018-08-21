#include<bits/stdc++.h>
#include<string>
#include<ctime>
using namespace std;
//string filenames[] = [string a("gagan"),string b("vinay")];
string getInput(int V , int E,bool isVinay,bool isTime)
{
	string s;
	if(isTime)
		s += "1\n";
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
void run(int i , int j,bool isVinay,bool isTime)
{
	char * code,*timeoutput,*spaceoutput,*executable;
	clock_t start = clock();
	ofstream myfile;
	char * space,*time,*exec;
	if(isVinay)
	{
		space = "./logs/vinay_space";
		time = "./logs/vinay_time";
		exec = "./execs/vinay < ./temps/input > ./temps/output";
	}
	else
	{
		space = "./logs/gagan_space";
		time = "./logs/gagan_time";
		exec = "./execs/gagan < ./temps/input > ./temps/output";
	}
	ofstream output(space,ios::app),output2(time,ios::app);
	myfile.open ("./temps/input");
	myfile << getInput(i,j,isVinay,isTime);
	myfile.close();
	start = clock();
	int status = system(exec);
	clock_t end = clock();
	ifstream file;
	file.open("./temps/output");
	string ss;
	file >> ss;
	if(!isTime)
	{
		output <<i << " " << j << " "  <<  ss << endl;
		output.close();
	}
	else
	{
		output2 << i << " " << j << " " << ss << endl;
		output2.close();
	}

}
int main()
{
	char * clear;
	clear = "rm ./logs/*";
	int count = 0,previousPercentage = 0;
	int maxim = 1000;
	int increment = 50;
	int total = maxim/increment;
	total *= total;
	int status = system(clear);
	for(int i = 1; i < maxim; i += increment)
	{
		for(int j = 1; j < maxim; j += increment)
		{
			run(i,j,true,true);
			run(i,j,true,false);
			count ++;
			cout << i << " " << j << endl;
			int percentage = (100*count)/total;
			if(percentage != previousPercentage)
				cout << percentage << endl;
			previousPercentage = percentage;	
		}
	}
	count = 0;
	previousPercentage = 0;
	cout << "vinay completed" << endl;
	for(int i = 1; i < maxim; i += increment)
	{
		for(int j = 1; j < maxim; j += increment)
		{
			run(i,j,false,true);
			run(i,j,false,false);
			count ++;
			int percentage =(100 * count) / total;
			if(previousPercentage != percentage)
				cout << percentage << endl;
			previousPercentage = percentage;
		}
	}
	cout << "gagan completed" <<endl;
}
