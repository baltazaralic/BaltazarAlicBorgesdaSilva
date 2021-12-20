 #include <stdio.h>
 #include "fibonacci.h"
 #include "fibprint.h"
    
   int main(void)
   {
     int n;
     printf("digite o ultimo numero da sequencia: "); 
     scanf("%d", &n);
     fibprint(fib(n),n);
     return 0;
   }