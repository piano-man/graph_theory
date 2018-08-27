#include<bits/stdc++.h>
#include<string>
#include<ctime>
using namespace std;
void createLog(int maxim,int increment,char * logfile, char *execfile)
{



  ofstream logs(logfile,ios::app);
  ofstream out;
  for( int i = 4; i < maxim ; i += increment )
  {
    cout << 1 << endl;
    out.open("./temps/input");
    cout << 2 << endl;
    float r = static_cast <float> (rand()) / static_cast <float> (RAND_MAX);
    out << i << " "  <<  r  << endl;

    out.close();
    cout << 3 << endl;
    int status = system(execfile);
    ifstream in;
    string ss;
    in.open("./temps/output");
    in >> ss;
    logs <<i << " " <<  ss << endl;
    cout << 4 ;
    cout << i << " completed" << endl;
  }
  logs.close();
}
int main()
{
  int maxim,increment;
  cout << "Enter the maximum number and the increment: " << endl;
  cin >> maxim >> increment;
  int st = system("rm  ./logs/*");
  char* logs[] = {"./logs/traditional","./logs/vertexMatch"};
  char * execs[] = {
    "./execs/traditional < ./temps/input > ./temps/output",
    "./execs/vertexMatch < ./temps/input > ./temps/output"

                  };
  for(int i = 0; i < 2; i ++ )
  {
    createLog(maxim,increment,logs[i],execs[i]);
  }
}
