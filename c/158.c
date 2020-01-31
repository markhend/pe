#include <stdio.h>

int main(void) {

    // char a[] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
    int a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z;
    int cnt = 0, tmp;
    for (a = 'a'; a <= 'z'; a++) {
    for (b = 'a'; b <= 'z'; b++) {
    for (c = 'a'; c <= 'z'; c++) {
    for (d = 'a'; d <= 'z'; d++) {
    //for (e = 'a'; e <= 'z'; e++) {
    //for (f = 'a'; f <= 'z'; f++) {
    //for (g = 'a'; g <= 'z'; g++) {
    //for (h = 'a'; h <= 'z'; h++) {
        tmp = 0;
        if (a < b) tmp++;
        if (b < c) tmp++;
        if (c < d) tmp++;
        //if (d < e) tmp++;
        //if (e < f) tmp++;
        //if (f < g) tmp++;
        //if (g < h) tmp++;
        if (tmp == 1) cnt++;
    }}}}
    printf("%d\n", cnt);
    return 0;
}
                
        


/*Taking three different letters from the 26 letters of the alphabet, character
strings of length three can be formed.  Examples are 'abc', 'hat' and 'zyx'.
When we study these three examples we see that for 'abc' two characters come
lexicographically after its neighbour to the left.  For 'hat' there is exactly
one character that comes lexicographically after its neighbour to the left. For
'zyx' there are zero characters that come lexicographically after its neighbour
to the left.  In all there are 10400 strings of length 3 for which exactly one
character comes lexicographically after its neighbour to the left.

We now consider strings of n<=26 different characters from the alphabet.  For
every n, p(n) is the number of strings of length n for which exactly one
character comes lexicographically after its neighbour to the left.

What is the maximum value of p(n)?
*/
