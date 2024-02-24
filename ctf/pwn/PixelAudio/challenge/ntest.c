#include <stdio.h> 
  
int main() 
{ 
  int c = 0, d = 0; 
  //printf("geeks for %ngeeks %n\n", &c, &d); 
  printf("%48879c%1$n%495c%2$n\n", &c, &d); 
  printf("%x, %x\n", c, d); 
  return 0; 
} 
