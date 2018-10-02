#include <iostream>
#include <fstream>
#include <string.h>
#include <vector>
using namespace std; 
int main()
{
   ifstream fin("as.txt");
   string str1 ;
   vector<vector<int> > direction;
   vector<vector<int> > revdir;
   while(getline(fin,str1))
   {
      int flag=0;
      char c=' ' ;
      for(int x= 0 ;x<str1.size();++x)
      {
            if (str1[x] == c)
            {
               flag= x;
            } 
      }
      vector<int> a;
      vector<int> b;
      a.push_back(stoi(str1.substr(0,flag)));
      a.push_back(stoi(str1.substr(flag+1,str1.size())));
      b.push_back(stoi(str1.substr(flag+1,str1.size())));
      b.push_back(stoi(str1.substr(0,flag)));
      direction.push_back(a);
      revdir.push_back(b);
   }
   cout<<direction.size()<<endl;

}

 