#ifndef _GST_H
#define _GST_H
/*
这个程序能得到一个任意长度，输入的字符串且无需声明长度，并返回，而且内存进行了优化。
*/
char *buff=NULL ,*temp,*out;
char c;
int size = 8, num = 0;
char* getstring(void);

#endif