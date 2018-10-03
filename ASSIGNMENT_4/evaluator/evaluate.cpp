#include<bits/stdc++.h>
using namespace std;
void createInputFile(int i, int j)
{
  ofstream myfile;
  myfile.open("input.txt");
  stringstream s;
  s <<" " <<  i << " " << j;
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
  for(int i = 2; i <= v; i ++ )
  {
      createInputFile(i,j);
      //int status = system.exec();
      int timet = i * j * i;

      stringstream s;
      s <<" " <<  i << " " <<( i * (i - 1)) / 2 << " " << timet << "\n";
      string st = s.str();
      out << st;

  }
  out.close();
}
