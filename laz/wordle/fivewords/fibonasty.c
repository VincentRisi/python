#include <stdio.h>
#include <sys/time.h>
#include <limits.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/resource.h>

static double micro_time_of_call() 
{
  static struct timeval stp;
  if ( stp.tv_sec == 0 ) // must be zero to start with by decree
    gettimeofday(&stp, 0);
  struct timeval tp;
  int rc=gettimeofday (&tp, 0);
  double a = tp.tv_sec-stp.tv_sec;
  long b = tp.tv_usec-stp.tv_usec;
  // The while could be an if. it's emulating a subtraction with carry
  while (b < 0) 
  {
    a-=1; 
    b+=1000000;
  }
  return a + b / 1000000.0;
}

static double nano_time_of_call()
{
  static struct timespec stp;
  if (stp.tv_sec == 0) // must be zero to start with by decree
    clock_gettime(0, &stp);
  struct timespec tp;
  int rc=clock_gettime (0, &tp);
  double a = tp.tv_sec-stp.tv_sec;
  long b = tp.tv_nsec-stp.tv_nsec;
  // The while could be an if. it's emulating a subtraction with carry
  while (b < 0) 
  {
    a-=1; 
    b+=1000000000;
  }
  return a + b / 1000000000.0;
}

int main(int argc, char* argv[])
{
  double timeof = nano_time_of_call();
  int times = 1000, i, t;
  int procs = 1;
  if (argc > 1)
    times = atoi(argv[1]);
  if (argc > 2)
    procs = atoi(argv[2]);
  if (times < 0 || times > 2000000000)
    times = 2000000000;
  if (procs < 1 || procs > 16)
    procs = 16;
  t = times / procs;
  long long sum, max = LLONG_MAX;
  printf("times %d procs %d t %d\n", times, procs, t);
  fflush(stdout);
  pid_t pid, ppid;
  if (procs > 1)
  {
    pid = fork();
    if (pid == 0)
    {
      while (--procs > 1)
        if (fork()) break;
    }
  }
#if defined(OLD_WAY)  
  unsigned long long p0, p1, p2;
  while (t--)
  {
    p1 = 1, p2 = 2;
    sum = 0;
    while (p2 < max)
    {
      p0 = p1;
      p1 = p2;
      p2 = p1+p0;
      if ((p0 % 2) == 0)
        sum += p0;
    }
  }
#else
  unsigned long long p1, p2, p3;
  while (t--)
  {
    sum=0;p1=1;p2=2;
    while (p2 < max)
    {
      sum+=p2;
      p3=p1+p2;
      p1=p2+p3;
      p2=p3+p1;
    }
  }
#endif  
  timeof = nano_time_of_call() - timeof;
  printf("%d: times:%d max:%lld sum:%lld secs:%f\n",getpid(), times, max, sum, timeof);
}
