#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    
    int i, answer = 0;
    char ones[100];
    char teens[100];
    char tens[100];
        
    strcpy(ones, "onetwothreefourfivesixseveneightnine");
    strcpy(teens, "teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen");
    strcpy(tens, "twentythirtyfortyfiftysixtyseventyeightyninety");
    //strcpy(hundred, "hundred");
    //strcpy(hundredand, "hundredand");
    
    answer += strlen(ones)*9*10;
    answer += strlen(teens)*10;
    answer += strlen(tens)*10*10;
    
    answer += strlen(ones) + strlen("hundred")*9;
    answer += strlen("onehundredand")*99;
    answer += strlen("twohundredand")*99;
    answer += strlen("threehundredand")*99;
    answer += strlen("fourhundredand")*99;
    answer += strlen("fivehundredand")*99;
    answer += strlen("sixhundredand")*99;
    answer += strlen("sevenhundredand")*99;
    answer += strlen("eighthundredand")*99;
    answer += strlen("ninehundredand")*99;
    answer += strlen("onethousand");
        
    printf("answer is %d\n", answer);
    return 0;
}

