#include<stdlib.h>
   
   int *fib(int n)                             
   {                                         
     int i, *f, soma;   
   	 f = (int *) malloc((n-1) * sizeof(int));   
	 f[0]=0;
	 f[1]=1;
	 f[2]=1;    
     for (i = 3; i < n; i = i + 1)           
     {                                        
       f[i] = f[i-1] + f[i-2];                                               
     }                                        
     return f;                             
   }                                          
   