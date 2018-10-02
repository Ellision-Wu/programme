#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include "gst.c"

/*
这是一个文本加密程序，它能把输入（英文）文本以给定的数字进行字母位移，包括大小写，但是数字和字符则不做处理。
*/


int main (int argc, char* argv[])
{
	if (argc>=3||argc<=1)
	{
		printf("error\n");
		exit(0);
	}
	int len,i,step;
	char*str,c;
	step= atoi(argv[1]);
	printf("Please input:\n" );
	str=getstring();
	len = strlen(str);
	for (i=0;i<(len);i++)
	{
		c=str[i];
		if isalpha(c)
		{
			if islower(c)
			{
				printf("%c",((c-97+step)%26)+97);
			}
			else
			{
				printf("%c",((c-65+step)%26)+65);
			}
		}
		else
		{
			printf("%c",c);
		}
	}
	printf("\n");
	return 0;
}