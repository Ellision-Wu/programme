#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "gst.h"
/*
这个程序能得到一个任意长度，输入的字符串且无需声明长度，并返回，而且内存进行了优化。
*/
char* getstring(void)
{
	buff = (char*)malloc(size);
	if (buff == NULL)
	{
		printf("ERROR!");
		exit(1);
	}
	while ((c = getc(stdin)) != EOF && c != '\n')
	{
		num += 1;
		if (size<num)
		{
			size *= 2;
			temp = (char*)realloc(buff,size);
			buff=temp;
		}
		
		buff[num-1]=c;
	}
	if (num == 0)
	{
		return 	0;
	}
	out = (char*)malloc(num);
	strncpy(out,buff,num);
	out[num]='\0';
	free(buff);
	return out;
}