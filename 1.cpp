#include <iostream>
#include <fstream>
#include <string.h>
using namespace std; 
int main()
{
   ifstream fin("as.txt");
   int i=100;
   char out[100];
   char *p;
   fin.getline(out,i);
   cout<<out[4]<<"\n";

   
   const char *d = " ";  
   p = strtok(out ,"1 6");
   int l = 0;
   while(p&&l<10)
   {
   l+=1;
   printf("%s\n",out );
   p = strtok(NULL ,d);
   }
//   file.close();
}
