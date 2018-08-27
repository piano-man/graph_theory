#include<bits/stdc++.h>
#include<string>
#include<ctime>
using namespace std;
int main()
{

  int maxim,increment;
  cin >> maxim >> increment;
  ofstream logs("logs",ios::app);
  ofstream out;
  for( int i = 0; i < maxim ; i += increment )
  {
    cout << 1 << endl;
    out.open("input");
    cout << 2 << endl;
    float r = static_cast <float> (rand()) / static_cast <float> (RAND_MAX);
    out << i << " "  <<  r  << endl;

    out.close();
    cout << 3 << endl;
    int status = system("./traditional < input > output ");
    ifstream in;
    in.open("output");
    in >> time;
    logs << time;
    cout << 4 ;
    cout << i << " completed" << endl;
  }
  logs.close();
}
