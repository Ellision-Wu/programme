#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include "gst.h"
/*
这是一个文本加密程序，它能把输入（英文）文本以循环给定的字符串进行字母位移，包括大小写，但是数字和字符则不做处理。
*/

int main (int argc, char* argv[])
{
	if (argc>=3||argc<=1)
	{
		printf("error\n");
		exit(0);
	}

	int len,i,len_i,count,e;
	char*str,c,p,*ch;
	ch=argv[1];
	len_i = strlen(ch);
	int step[len_i];
	for (i=0;i<(len_i);i++)
	{
		p=ch[i];
		if isalpha(p)
		{
			e=toupper(p);
			step[i]=e-65;
		}
		else
		{
			printf("error\n");
			exit(0);
		}
	}

	printf("Please input:\n" );
	str=getstring();
	len = strlen(str);
	count=0;
	for (i=0;i<(len);i++)
	{
		c=str[i];
		if isalpha(c)
		{
			if islower(c)
			{
				printf("%c",((c-97+step[count%len_i])%26)+97);
				count++;
			}
			else
			{
				printf("%c",((c-65+step[count%len_i])%26)+65);
				count++;
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