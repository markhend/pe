#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(int argc, char *argv[])
{
    
    FILE *fp;
    int c, answer=0;
    fp = fopen("20.txt", "r");
    	
    /*
    while ((c = fgetc(fp)) != EOF){
    	if ((c == '0') || (c == '1') || (c == '2') || (c == '3') || (c == '4') ||
         (c == '5') || (c == '6') || (c == '7') || (c == '8') || (c == '9'))
    		answer += (c - '0');
    }
    */

    while ((c = fgetc(fp)) != EOF)
        if (isdigit(c)) answer += (c - '0');
        
    printf("answer %d\n", answer);
    fclose(fp);
    //system("PAUSE");	
    return 0;
}
