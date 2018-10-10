#include<bits/stdc++.h>
#include<ctime>
using namespace std;
void createInputFile(int i, int j)
{
  ofstream myfile;
  myfile.open("input.txt");
  stringstream s;
  s <<" " <<  i;
  string st = s.str();
  myfile << st;
  myfile.close();
}
int main()
{
  int e = 10;
  int v = 10;
  ofstream myfile;
  ofstream out;
  out.open("ymw.txt");
  stringstream st;
  for(int i = 1; i <= v; i ++)
  {
      int j = (i * ( i - 1) ) / 2;
      createInputFile(i,j);
      clock_t t = clock();
      int status = system("./spanning < input.txt > output.txt");
      cout << i << endl;
      t = clock() - t;
      int timet = i * j * i;

      stringstream s;
      ifstream in;
      in.open("output.txt");
      string stk;
      in >> stk;
      s <<" " <<  i << " " << j << " " << stk << "\n";
      string st = s.str();
      out << st;

  }
  out.close();
}
