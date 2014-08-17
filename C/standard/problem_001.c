#include <stdio.h>

int
main()
{
  int a, n;

  for(a = 0, n = 0; n < 1000; n++)
    if (n % 3 == 0 || n % 5 == 0)
      a += n;
  printf("%d\n", a);
}
