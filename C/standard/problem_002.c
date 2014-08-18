#include <stdio.h>

int
main()
{
  int a, pprev, prev, current;
  
  current = 0;
  a = 2;

  for(pprev = 1, prev = 2; current < 4000000; ) {
    current = pprev + prev;
    if (current % 2 == 0)
      a += current;
    pprev = prev;
    prev = current;
  }
  
  printf("%d\n", a);
}
