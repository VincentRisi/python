#ifndef _UFORTIFY_H_
#define _UFORTIFY_H_ "$Revision: 92 $ $Date: 2005-04-21 11:34:40 +0200 (Thu, 21 Apr 2005) $"
#include "versions.h"
HEADER_VERSION(_UFORTIFY_H_);
/*
 * FILE:
 *   ufortify.h
 *
 * DESCRIPTION:
 *   User options for fortify. Changes to this file require fortify.c to be
 * recompiled, but nothing else.
 */

#define FORTIFY_STORAGE              /* storage for public functions   */

#define FORTIFY_ALIGNMENT        sizeof(double) /* Byte alignment of all memory blocks */

#define FORTIFY_BEFORE_SIZE      32  /* Bytes to allocate before block */
#define FORTIFY_BEFORE_VALUE   0xA3  /* Fill value before block        */

#define FORTIFY_AFTER_SIZE       32  /* Bytes to allocate after block  */
#define FORTIFY_AFTER_VALUE    0xA5  /* Fill value after block         */

#define FORTIFY_FILL_ON_ALLOCATE               /* Nuke out malloc'd memory       */
#define FORTIFY_FILL_ON_ALLOCATE_VALUE   0xA7  /* Value to initialize with       */

#define FORTIFY_FILL_ON_DEALLOCATE             /* free'd memory is cleared       */
#define FORTIFY_FILL_ON_DEALLOCATE_VALUE 0xA9  /* Value to de-initialize with    */

#define FORTIFY_FILL_ON_CORRUPTION             /* Nuke out corrupted memory    */

/* #define FORTIFY_CHECK_ALL_MEMORY_ON_ALLOCATE */
/* #define FORTIFY_CHECK_ALL_MEMORY_ON_DEALLOCATE */
#define FORTIFY_PARANOID_DEALLOCATE

/* #define FORTIFY_WARN_ON_ZERO_MALLOC */ /* A debug is issued on a malloc(0) */
/* #define FORTIFY_FAIL_ON_ZERO_MALLOC */ /* A malloc(0) will fail            */

#define FORTIFY_WARN_ON_ALLOCATE_FAIL    /* A debug is issued on a failed alloc  */
#define FORTIFY_WARN_ON_FALSE_FAIL       /* See Fortify_SetAllocateFailRate      */
#define FORTIFY_WARN_ON_SIZE_T_OVERFLOW  /* Watch for breaking the 64K limit in  */
                                         /* some braindead architectures...      */

#define FORTIFY_TRACK_DEALLOCATED_MEMORY
#define FORTIFY_DEALLOCATED_MEMORY_LIMIT 1048576 /* Maximum amount of deallocated bytes to keep */
/* #define FORTIFY_WARN_WHEN_DISCARDING_DEALLOCATED_MEMORY */
/* #define FORTIFY_VERBOSE_WARN_WHEN_DISCARDING_DEALLOCATED_MEMORY */

/* #define FORTIFY_NO_PERCENT_P */       /* sprintf() doesn't support %p */
/* #define FORTIFY_STRDUP       */       /* if you use non-ANSI strdup() */

#define FORTIFY_LOCK()
#define FORTIFY_UNLOCK()

#define FORTIFY_DELETE_STACK_SIZE    256

#ifdef __cplusplus                /* C++ only options go here */

    #define FORTIFY_PROVIDE_ARRAY_NEW
    #define FORTIFY_PROVIDE_ARRAY_DELETE
    #define FORTIFY_FAIL_ON_ZERO_MALLOC
    /*#define FORTIFY_AUTOMATIC_LOG_FILE*/
    #define FORTIFY_LOG_FILENAME            "fortify.log"
    #include "ti.h"
     
    #define FORTIFY_FIRST_ERROR_FUNCTION     cout << "\a\a\aFortify Hit Generated!\n"
    
#endif /* __cplusplus */

#if YOU_WANT_A_LOT_OF_COMPILE_ERRORS_DEFINE_ME
/*        Fortify - A fortified memory allocation shell for C and C++
        -----------------------------------------------------------
                        written by Simon P. Bullen

                       Version 2.2, 1 November 1995



            This  software  is  not public domain.  All material in
        this  archive  is (C) Copyright 1995 Simon P.  Bullen.  The
        software  is  freely distributable, with the condition that
        no   more   than  a  nominal  fee  is  charged  for  media.
        Everything  in  this distribution must be kept together, in
        original, unmodified form.
            The software may be modified for your own personal use,
        but modified files may not be distributed.
            The  material  is  provided "as is" without warranty of
        any  kind.  The author accepts no responsibility for damage
        caused by this software.
            This  software  may not be used in any way by Microsoft
        Corporation  or  its  subsidiaries, or current employees of
        Microsoft Corporation or its subsidiaries.
            This  software  may  not  be used for the construction,
        development,  production,  or  testing of weapon systems of
        any kind.
            This  software  may  not  be used for the construction,
        development,  production,  or  use  of plants/installations
        which  include  the  processing  of radioactive/fissionable
        material.



    If  you  use  this  software  at  all,  I'd love to hear from you.  All
    questions, criticisms, suggestions, praise and postcards are most welcome.

                     email:    sbullen@cybergraphic.com.au

                     snail:    Simon P. Bullen
                               PO BOX 12138
                               A'Beckett St.
                               Melbourne 3000
                               Australia



    CONTENTS
    --------
    Your archive should have the following files:

    fortify.doc - This file. Read it first
    fortify.cxx - Actual code. Rename to fortify.c for C only development
    fortify.h   - Each file in your program should #include this
    ufortify.h  - User configuration file. Here is where you set your options

    test.c      - C tester
    test2.cxx   - C++ tester
    makefile    - Makefile for GCC to build the testers.



    OVERVIEW
    --------
    Fortify  is  a  (fortified)  shell for memory allocations.  It supports
malloc/calloc/realloc/strdup/free  and  new/delete.  It traps memory leaks,
writes beyond and before memory blocks, writes to freed memory, free twice,
freeing  memory  never  allocated,  and removes all randomness from reading
uninitialized or free memory.
  It  is a descendant of a library I wrote way back in 1990 called SafeMem.
It can be adapted to most memory management functions; the original version
of SafeMem worked only with the Amiga's AllocMem/FreeMem.
    Fortify works by allocating extra space on each block.  This includes a
private  header (which is used to keep track of Fortify's list of allocated
memory),  and  two  "fortification zones" or "sentinels" (which are used to
detect writing outside the bound of the user's memory).




    PORTABILITY
    -----------
    Fortify is intended to be a highly portable tool.  It should work quite
happily  in  any vaguely ANSI C/C++ environment, on any operating system or
processor architecture without modification.
    It  does  not,  however, support bizarre memory models.  A pointer is a
pointer  is  a  pointer.  I have no intention of ever supporting any of the
non-flat memory models used by some pretend operating systems.


    Fortify INSTALLATION (C++)
    --------------------------
    To install Fortify, each source file will need to #include "fortify.h".
To  enable  Fortify,  define  the symbol FORTIFY.  The makefile is the best
place  to  do  this.   The symbol FORTIFY will need to be defined for every
module, this includes "fortify.c" or "fortify.cxx".
    If FORTIFY is not defined, it will compile away to nothing - it will be
as  if  Fortify  was  never  installed  at  all  (you  should recompile all
sourcecode with Fortify disabled for a release of your software).
    If you do not have stdout available, you may wish to set an alternative
output        function.         See       Fortify_SetOutputFunc()       and
FORTIFY_AUTOMATIC_LOGFILE, below.
    Your  program  will  need  to  link  in  "fortify.cxx" (after it's been
compiled, of course).
	You may also need to adjust some options in "ufortify.h" before Fortify
will work correctly.  See "Compile Time Customizations", below.



    Fortify INSTALLATION (C)
    ------------------------
    To  install  Fortify  into  a C program, simply rename "fortify.cxx" to
"fortify.c",  and  follow  the  C++ instructions above.  "fortify.cxx" will
compile  quite happily as C, as all the core Fortify code is C, and the C++
specific code is surrounded by #ifdef __cplusplus/#endif.
	You may also need to adjust some options in "ufortify.h" before Fortify
will work correctly.  See "Compile Time Customizations", below.





    COMPILE TIME CUSTOMIZATIONS
    ---------------------------
    The  file  "ufortify.h"  contains  many  #defines  that  you can use to
customize  Fortify's  behavior.   Fortify  will  do  it's  best  to provide
sensible  defaults  for  most of these options, if for some reason they are
not present in "ufortify.h".
  Most  of  the  options  are  merely user preferences that you may wish to
change  or  turn  on  only when you are trying to track down a particularly
nasty  bug.   There are a couple of configuration items, however, that will
need  to be set correctly for Fortify to compile on your particular system.
When  it  can,  Fortify  will  detect  a  compiler  and set the appropriate
options.
    Ideally,  Fortify would be able to be built under all compilers without
modification, but due to differences in compilers and the devious nature of
some  of  the stuff Fortify has to acheive, this is sadly not possible.  It
is  my  aim  to  make  Fortify automatically configure itself for all major
compilers   out   there,   so   if   you  need  to  adjust  some  of  these
compiler-specific options to get Fortify to work under your system, I would
greatly appreciate the code fragment that detects your compiler and sets up
the correct options (these live in "fortify.h" - search for __GNUG__ for an
example).



    #define FORTIFY_PROVIDE_ARRAY_NEW
    #define FORTIFY_PROVIDE_ARRAY_DELETE

    Some  C++  compilers  have  separate  operators for newing and deleting
arrays.   If  your  compiler does, you will need to define this symbol.  If
you  are  unsure, turn them both on.  Your program won't compile or link if
they  should  be off (providing your test code actually news and deletes an
array).   GCC 2.6.3 and Borland C++ 4.5 both need these symbols.  Microsoft
C++  1.5  and  SAS  6.5 C++ both don't.  Fortify will automatically turn on
this option for GCC and Borland..
    If both array new and array delete are enabled, Fortify will be able to
ensure  that  you  always use the correct form of delete, and will issue an
error message if you use the wrong one.

    Fortify: Incorrect deallocator "delete[]" detected at test2.cxx.17
             (0x7438ac2,1,test2.cxx.13) was allocated with "new"


    #define FORTIFY_STRDUP

    strdup()  is  a  non-ANSI function that is essentially a malloc() and a
strcpy().    If   you   use   this   function,  you  will  need  to  enable
FORTIFY_STRDUP,  so  that  the  memory  you  get back from strdup() will be
allocated by Fortify.
	If  you  don't do this, Fortify will generate an error message when you
attempt to free the memory.


    #define FORTIFY_NO_PERCENT_P

    Some  non-ANSI  versions  of sprintf() do not recognize "%p" as a valid
conversion  specification.   Fortify  uses  "%p"  to  output  all  of  it's
pointers.     If   your   sprintf()   does   not   support   "%p",   define
FORTIFY_NO_PERCENT_P, and Fortify will use "%lx" instead.


    #define FORTIFY_STORAGE

    You  can  use  this to apply a storage type to all Fortify's exportable
functions.   If  you  are putting Fortify in an export library for example,
you may need to put __export here, for example.


    #define FORTIFY_BEFORE_SIZE       32
    #define FORTIFY_BEFORE_VALUE    0xA3
    #define FORTIFY_AFTER_SIZE        32
    #define FORTIFY_AFTER_VALUE     0xA5

    These  values  define  how  much  "fortification" is placed around each
memory  block  you  allocate.  Fortify will place FORTIFY_BEFORE_SIZE bytes
worth  of  memory  right  before  your memory block, and FORTIFY_AFTER_SIZE
bytes   after   your  memory  block,  and  these  will  be  initialized  to
FORTIFY_BEFORE_VALUE and FORTIFY_AFTER_VALUE respectively.  If your program
then  accidentally writes into either of these regions, Fortify will detect
this, and issue an error message.
    If  you don't want these fortifications to be allocated, specify a size
of 0.  Note that the value parameters are 8 bits.

    Fortify: Underwrite detected before block (0x743b462,123,test.c.14) at
             test.c.16
             Memory integrity was last verified at test.c.14
       Address   Offset Data (a3)
                        ...64 bytes skipped...
     0x743b45a       64 a3a3a3a3 a3a3a341                      "�������A"


    #define FORTIFY_ALIGNMENT            sizeof(double)

    Many  processors  require  data objects to have a specific alignment in
memory.   The  memory  allocators on these machines will only return memory
blocks  aligned  correctly for the largest of these requirements.  Fortify,
however,  adds  some  magic  cookies  to  the  start of it's memory blocks.
Fortify  will guarantee that the amount of memory it adds to the front of a
memory  block  will  be  a  multiple  of FORTIFY_ALIGNMENT (It does this by
increasing  the  FORTIFY_BEFORE_SIZE, after taking into account the size of
it's  private  header).   The default of sizeof(double) should work on most
systems.


    #define FORTIFY_FILL_ON_ALLOCATE
    #define FORTIFY_FILL_ON_ALLOCATE_VALUE        0xA7

    Programs  often  rely  on  uninitialized  memory  being  certain values
(usually  0).   If you define FORTIFY_FILL_ON_ALLOCATE, all memory that you
allocate  will  be initialized to FORTIFY_FILL_ON_ALLOCATE_VALUE, which you
should  define  to  be  some  horrid  value  (definitely NOT 0).  This will
encourage  all  code  that  relies on uninitialized memory to behave rather
differently  when  Fortify  is  running.  If you ever see a pointer that is
0xA7A7A7A7, you can be certain that it is uninitialized.


    #define FORTIFY_FILL_ON_DEALLOCATE
    #define FORTIFY_FILL_ON_DEALLOCATE_VALUE    0xA9

    Programmers  often  try to use memory after they've freed it, which can
sometimes  work  (so long as nobody else has modified the memory before you
look  at  it), but is incredibly dangerous and definitely bad practice.  If
FORTIFY_FILL_ON_DEALLOCATE  is defined, all memory you free will be stomped
out  with  FORTIFY_FILL_ON_DEALLOCATE_VALUE, which ensures that any attempt
to  read  freed  memory  will  give  incorrect  results.  If you ever see a
pointer that is 0xA9A9A9A9, it definately came from free'd memory.


    #define FORTIFY_FILL_ON_CORRUPTION

    Fortify  will  never  free  memory  that  has  had  it's fortifications
overwritten.   This  is  so that you have ample opportunity to examine this
memory in a debugger.  If the memory remains corrupted, Fortify will report
this  each  time  it  does  a  check  of memory, which can be annoying (but
useful,  if  the  program  continues  to modify the memory).  If you define
FORTIFY_FILL_ON_CORRUPTION,   Fortify   will   re-initialize   a  corrupted
fortification  after  it  issues it's message.  Fortify will then no longer
complain about this memory, until it is corrupted again.
    This  has  the  extra  advantage  that software that tries to read this
memory will probably break.


    #define FORTIFY_CHECK_ALL_MEMORY_ON_ALLOCATE
    #define FORTIFY_CHECK_ALL_MEMORY_ON_DEALLOCATE

    CHECK_ALL_MEMORY_ON...   means  that for every single memory allocation
or  deallocation,  every  single block of memory will be checked.  This can
slow  down  programs considerably   if  you  have  a large number of blocks
allocated.   You would normally only need to turn this on if you are trying
to pinpoint where a corruption was occurring.
    A  block  of  memory  is  always  checked  when  it  is  freed,  so  if
CHECK_ALL...    isn't  turned  on,  corruptions  will  still  be  detected,
eventually.
    You  can  also  force  Fortify  to  check  all  memory  with  a call to
Fortify_CheckAllMemory().   If you have a memory corruption you can't find,
sprinkling  these  through the suspect code will help narrow it down.  When
you get a message regarding a corruption, part of the output will be a line
that  says  "Memory  integrity  was  last  verified  at  file.line".   This
corresponds  to  when  the "CheckAllMemory" operation was last successfully
performed,    either   automatically,   or   by   an   explicit   call   to
Fortify_CheckAllMemory().


    #define FORTIFY_PARANOID_DEALLOCATE

    FORTIFY_PARANOID_DEALLOCATE  causes Fortify to traverse the memory list
to  ensure  the  memory  you  are about to free was really allocated.  This
option  is recommended in a protected memory operating system.  If a free()
of  a  garbage  pointer  is attempted, Fortify will generate a segmentation
fault  when  it  attempts  to checksum the memory pointed to by the garbage
pointer.   If, however, FORTIFY_PARANOID_DELETE is on, Fortify will be able
to  determine  that the pointer is garbage without crashing the system, and
will be able to generate an error message.
    Note  that  in  C++, however, if you try to "delete" a garbage pointer,
you  will  most  likely crash before Fortify gets a look in.  When you do a
"delete"  in  C++,  the first thing that happens is the object's destructor
gets  called.  Depending on what the destructor actually does, it may crash
due  to  having  a  bogus  "this".   The memory isn't freed until AFTER the
destructor,  which  is  when  Fortify  would  be able to detect the invalid
pointer  (too  late).   If  you are having problems with a weird crash in a
destructor,  you may wish to add Fortify_CheckPointer(this) to the start of
the  destructor,  but be warned that Fortify will generate an error message
if you destruct an object that was created on the stack.
    FORTIFY_PARANOID_DEALLOCATE  adds a small amount of overhead to freeing
memory        (though        not        nearly       as       much       as
FORTIFY_CHECK_ALL_MEMORY_ON_DEALLOCATE).  Paranoid mode would be quicker if
Fortify  didn't  use a naive linked list to store it's memory on (see TO DO
LIST, below).


	#define FORTIFY_WARN_ON_ZERO_MALLOC
	#define FORTIFY_FAIL_ON_ZERO_MALLOC

	In  some  implementations,  a  malloc(0)  will  always  fail  (This  is
non-ANSI).   If Fortify is turned on, malloc(0) won't actually reach malloc
as  a  malloc(0)  -  Fortify adds fortifications, which means it won't be a
zero byte allocation anymore, and will probably succeed.
	Thus it is possible to write code that would work if Fortify was turned
on,  but  fail  when Fortify is turned off.  If the version of malloc() you
are   using   does   not  allow  malloc(0)  to  succeed,  you  must  enable
FORTIFY_FAIL_ON_ZERO_MALLOC  to  enable  your  program to function properly
with Fortify turned on.


    #define FORTIFY_WARN_ON_ALLOCATE_FAIL

    This  causes  a  debug to be issued whenever an allocation fails.  This
can be very useful when identifying the cause for a crash.


    #define FORTIFY_WARN_ON_FALSE_FAIL

    A  debug  will  be  issued  when  an allocation is "false failed".  See
Fortify_SetAllocateFailRate()  and  Fortify_SetAllocationLimit()  for  more
information.

    Fortify: A "malloc()" of 128 bytes "false failed" at test.c.27



    #define FORTIFY_WARN_ON_SIZE_T_OVERFLOW

    This  causes Fortify to check for breaking the size_t limit.  This is a
problem  in  16-bit  applications  where  breaking  the  16  bit  limit  is
reasonably likely.
    The problem is that Fortify adds a small amount of overhead to a memory
block;  so  in  a  16-bit size_t environment, if you tried to allocate 64K,
Fortify  would  make  that  block bigger than 64K and your allocation would
fail  due  to  the  presence of Fortify.  With size_t being 32 bits for all
environments  worth  programming  in,  this  problem  is extremely unlikely
(Unless you plan to allocate 4 gigabytes).


    #define FORTIFY_AUTOMATIC_LOG_FILE
    #define FORTIFY_LOG_FILENAME             "fortify.log"
    #define FORTIFY_FIRST_ERROR_FUNCTION    cout << "\a\a\aOh Dear!\n"

    If  FORTIFY_AUTOMATIC_LOG_FILE is defined (C++ only), then Fortify will
output to a log file.  It will also automatically call Fortify_EnterScope()
at program initialization, and Fortify_LeaveScope() at program termination.
    If Fortify generated no output, the log file will not be altered.
    FORTIFY_FIRST_ERROR_FUNCTION  will  be  called  upon  generation of the
first  Fortify  message,  so that the user can tell if a Fortify report has
been  generated.   Otherwise,  Fortify  would quietly write all this useful
stuff out to the log file, and no-one would know to look there!
    You  don't  need  to use Fortify_SetOutputFunc() at all if you're using
the automatic log file.


    #define FORTIFY_LOCK()
    #define FORTIFY_UNLOCK()

    In  a  multi-threaded  environment,  we need to arbitrate access to the
fortify  memory list.  This is what FORTIFY_LOCK() and FORTIFY_UNLOCK() are
used  for.  The calls to FORTIFY_LOCK() and FORTIFY_UNLOCK() must nest.  If
no  two  threads/tasks/processes will be using the same Fortify at the same
time,  then FORTIFY_LOCK() and FORTIFY_UNLOCK() can safely be #defined away
to nothing.


    #define FORTIFY_TRACK_DEALLOCATED_MEMORY
    #define FORTIFY_DEALLOCATED_MEMORY_LIMIT 1048576
    #define FORTIFY_WARN_WHEN_DISCARDING_DEALLOCATED_MEMORY
    #define FORTIFY_VERBOSE_WARN_WHEN_DISCARDING_DEALLOCATED_MEMORY

    If  FORTIFY_TRACK_DEALLOCATED_MEMORY is enabled, Fortify won't actually
free   memory   when  you  deallocate  it.   Freed  memory  goes  onto  the
"deallocated"  list, where Fortify will keep an eye on it.  If you write to
the  memory  after  it's  been freed, Fortify will be able to tell.  If you
attempt to free memory twice, Fortify will be able to tell you for certain,
rather than just suspect.
    Deallocated  memory  tracking is only active if you've entered at least
one  level  of  Fortify  scope.   This  is  so that Fortify will be able to
actually free the deallocated memory when the scope is left.

    Fortify: Write to deallocated block (0x75c4502,126,test.c.21)
             detected at test.c.40
             Memory block was deallocated by "realloc()" at test.c.34
             Memory integrity was last verified at test.c.35
    Address   Offset Data (a9)
    0x75c4502      0 58a9a9a9 a9a9a9a9 a9a9a9a9 a9a9a9a9 "X"
                     ...110 bytes skipped...

    FORTIFY_DEALLOCATED_MEMORY_LIMIT,  if defined, is the maximum amount of
memory  that  Fortify  should  keep  on  it's  deallocated  list.   If  you
deallocate  some  memory,  and the total amount of deallocated memory being
tracked is greater than this number, then Fortify will throw away (actually
free)  the  oldest  chunks of memory, until it's under this threshold.  You
don't  have to worry about running out of memory if this value is set high,
Fortify  will  discard  deallocated  memory  in  preference  to  letting an
allocation fail.  The main reason for this option is to restrict the amount
of  time  spent  checking  freed  memory  for corruption.
    FORTIFY_WARN_WHEN_DISCARDING_DEALLOCATED_MEMORY  will  cause Fortify to
issue  a  warning  whenever  it has to free some deallocated memory when it
didn't  really  want  to.  If an allocation was going to fail, or if it was
over  the FORTIFY_DEALLOCATED_MEMORY_LIMIT, and it had to free some memory,
then  a warning would be issued.  Freeing deallocated memory when leaving a
Fortify scope does not cause a warning.
    FORTIFY_VERBOSE_WARN_WHEN_DISCARDING_DEALLOCATED_MEMORY  is useful when
you are trying to track down a particular write to some deallocated memory.
Fortify  will  list  the details of all blocks being discarded, so that you
can  tell  if  the  block  you  are interested in is still being watched by
Fortify.
    Note  that  Fortify  will  always  perform one last check on the memory
before  it  discards it, so you can be sure that all memory being discarded
is corruption free.

    Fortify: Warning - Discarding deallocated memory at test.c.46
                    (0x743e8b2,126,test.c.22,test.c.35)
                    (0x743f0b2,456,test.c.32,test.c.46)



    #define FORTIFY_DELETE_STACK_SIZE 256

    Due  to  the  way  that  delete works, Fortify has to maintain it's own
stack  of  delete  source-code  information.  For simplicity, this has been
implemented  in a static array.  The size of this stack reflects the number
of  levels  of  recursion that Fortify will be able to track during deletes
(ie  deletes  being called from destructors called from a delete call).  If
this  recursion  limit  is exceeded, Fortify will simply output the deepest
sourcecode level known.  I think 256 levels should be ample.




    typedef void (*Fortify_NewHandlerFunc)(void);
    #define FORTIFY_NEW_HANDLER_FUNC Fortify_NewHandlerFunc

    By  default,  Fortify  will  use  the  standard  new  handler  function
prototype.   However,  some  non-standard compiler implementations (such as
Microsoft  Visual  C++  2.0)  use  non-standard  prototypes  for  their new
handlers.   FORTIFY_NEW_HANDLER_FUNC is the type that Fortify uses for it's
new  handler function pointer.  Note that Fortify won't pass any parameters
to  the  new  handler,  so  changing this is probably quite useless at this
point in time.



    RUN TIME CONTROL
    ----------------
    Fortify  can  also  be  controlled  at  run  time  with  a  few special
functions, which compile away to nothing if FORTIFY isn't defined.

    Fortify_Disable()  -  Fortify  can be disabled at run-time.  Previously
this   would   only   work   if   no  memory  was  allocated  at  the  time
Fortify_Disable() was called, but in C++ environments, this is almost never
possible.   After  Fortify_Disable()  has  been called, all new allocations
will not be Fortified.  Deallocations will be treated slightly differently.
Fortify  will  check to see if it allocated the memory, and if so, free it.
If  not, it will pass it on to free().  Fortify_Disable() is useful to turn
off Fortify if the overhead or bugs being induced by Fortify are getting in
the  way.   To  correctly  remove  Fortify  for  software release, you must
compile it out.
	Note that once you've called Fortify_Disable(), there is no way to turn
it back on again.

    Fortify_SetOutputFunc(Fortify_OutputFuncPtr Output) - Sets the function
used  to  output  all error and diagnostic messages by Fortify.  The output
function takes a single (const char *) argument, and must be able to handle
newlines.   The default output function is a printf() to stdout, unless you
are using FORTIFY_AUTOMATIC_LOG_FILE, where the default is to output to the
log file.  The function returns the old pointer.


    Fortify_SetAllocateFailRate(int   Percent)   -  Fortify  will  make  an
allocation attempt "fail" this "Percent" of the time, even if the memory IS
available.  Useful to "stress-test" an application.  Returns the old value.
The fail rate defaults to 0.


    Fortify_SetAllocationLimit(unsigned  long  AllocationLimit)  - Impose a
limit on the amount of memory the application can allocate.  This limit may
be  changed  at  any  time.   If  you set this to 0, memory allocations are
guaranteed  to  fail.   The  default is 0xffffffff, which is essentially no
limit.   Returns the old value.  Fortify_GetCurrentAllocation() can be used
to  find  out  how  much  memory  is  currently  allocated (see STATISTICAL
FUNCTIONS, below).


    DIAGNOSTIC FUNCTIONS
    --------------------
    Fortify also provides some additional diagnostic functions which can be
used  to  track  down  memory  corruption  and memory leaks.  If Fortify is
disabled,  these functions do nothing.  If calling these functions directly
from  a debugger, remember to add the "const char *file" and "unsigned long
line"  parameters  to  each  of  the calls (these are normally added by the
preprocessor macros).


    Fortify_CheckPointer(void *uptr) - Returns true if the uptr points to a
valid block of allocated memory.  The memory must be on Fortify's list, and
it's  sentinels must be in tact.  If anything is wrong, an error message is
issued (if Fortify is disabled, this function always returns true).


	Fortify_LabelPointer(void *uptr, const char *label) - Labels the memory
block  with  a  string provided by the user.  This function takes a copy of
the  passed  in  string.   The  pointer  MUST  be one returned by a Fortify
allocation function.
	This  function  can  be  very  useful  to track a memory block that was
allocated  on  the  same  line as a bunch of other memory blocks.  Whenever
Fortify  outputs  the information about this memory block, the label string
will also be output.


    Fortify_CheckAllMemory()  -  Checks  the  sentinels  of all memory that
Fortify   knows   about.    This   includes   allocated   memory,   and  if
FORTIFY_TRACK_DEALLOCATED_MEMORY  is turned on, any deallocated memory that
Fortify  is  still  tracking.  Returns the number of blocks that failed (if
Fortify is disabled, this function always returns 0).


    Fortify_ListAllMemory()   -   Outputs  the  entire  list  of  currently
allocated  memory.   For  each  block is output it's Address, Size, and the
SourceFile  and Line that allocated it.  If there is no memory on the list,
this function outputs nothing.  It returns the number of blocks on the list
(if Fortify has been disabled, this function always returns 0).


    Fortify_DumpAllMemory() - Outputs a hex dump of all currently allocated
memory.


    Fortify_EnterScope()  -  enters  a level of fortify scope.  Returns the
new scope level.


    Fortify_LeaveScope()  - leaves a level of fortify scope, it also prints
a  dump  of all unfreed memory allocated within the scope being left.  This
can  be  very  useful in tracking down memory leaks in a part of a program.
If  you  place  a EnterScope/LeaveScope pair around a set of functions that
should  have  no memory allocated when it's done, Fortify will let you know
if  this  isn't the case.  Fortify will also discard any deallocated memory
from the scope being left, if it is tracking deallocated memory.



    STATISTICAL FUNCTIONS
    ---------------------
    Fortify gathers some basic statistics about your programs memory usage.
It  will  keep  track  of  the total number of memory allocation operations
performed, and also the maximum amount of memory allocated at any one time.

    Fortify_OutputStatistics() - display the current statistics.

    Fortify: Statistics at test.c.70
             Maximum memory allocated at one time: 13633 bytes in 7 blocks
             There have been 9 allocations and 4 deallocations
             There was a total of 14343 bytes allocated
             The average allocation was 1593 bytes


    Fortify_GetCurrentAllocation()  -  returns  the  total amount of memory
currently  allocated  by  the  application  (if  Fortify  is disabled, this
function will always return 0).




    PROBLEMS WITH THE new AND delete MACROS
    ---------------------------------------
    Due  to  limitations  of the C preprocessor, getting caller source-code
information  to  new  and  delete  isn't  as easy as it is for malloc() and
free().   The macro for "new" which adds this information onto the new call
causes  syntax  errors  if  you  try to declare a custom new operator.  The
actual  Fortifying  works  fine, it's just the macro expansion which causes
problems.
    If  this  happens,  the  easiest  thing  to do is #ifdef out the custom
new/delete  operators  if  FORTIFY  is defined.  Alternatively, you can not
#include  "fortify.h"  for the offending file (and any files that use these
custom   operators,   but   remember   that  they  won't  have  source-code
information).

    eg.
    #ifndef FORTIFY *//* can't easily use custom new's with FORTIFY enabled */
/*    void *X::operator new(size_t size) { return malloc(size); }
    #endif

    Due  to a limitation with delete (it is illegal to declare a version of
delete  that  takes  different parameters), Fortify has limited information
about  where  delete  is  being called from, and so the the line and source
information  will  often  say  "delete.0". If  a delete is occurring from
within  another delete, Fortify is now able to maintain a 'delete stack',
and will output this stack after the main body of the Fortify hit.




    WHEN TO USE FORTIFY
    -------------------
    You  should  never  be without Fortify when you're developing software.
It will detect your bugs _as_you_write_them_, which makes them a lot easier
to find.
    Leave  Fortify  enabled  until  the  final  test  and  release  of your
software.   You  probably  won't  want  some of the slower options, such as
CHECK_ALL_MEMORY_ON_DEALLOCATE.   With  the  exception  of  those  options,
Fortify  doesn't have a great deal of overhead.  If posing a great problem,
this  overhead  can  be  reduced  by  cutting  down  on  the  size  of  the
fortifications, and turning off the pre/post fills, but each thing you turn
off gives Fortify less information to work with in tracking your bugs.
	(And besides, the slower your program runs while you're developing it,
the more efficient your algorithms are likely to be!).


    Dynamic Link Libraries
	----------------------
	Dynamic  Linking  of the standard libraries will not work with Fortify.
The  standard library DLL has it's own copy of memory management functions,
so any memory allocated by the DLL will be unknown to Fortify, and you will
get erroneous error messages.

	If  you are writing your own DLL's, or using a 3rd party one, it may be
possible  to  write  a callback module to get the DLL's to call the Fortify
routines  in  the  parent application.  If anyone does write a module to do
this, please send it to me so I can include it in the next version.

	If  the  DLL  doesn't  allocate any memory, or your application doesn't
call  free/delete/realloc  on any memory allocated by the DLL, then Fortify
should work fine.

	Another  alternative to the DLL problem is to use normal link libraries
while  you  are developing with Fortify, and then rebuild them as DLL's for
release.  This of course may not be appropriate in all situations.



    REVISION HISTORY
    ----------------

Changes from V2.1 to V2.2
	Added  FORTIFY_WARN_ON_ZERO_MALLOC, and FORTIFY_FAIL_ON_ZERO_MALLOC, as
some compilers do not allow a malloc(0) to succeed.
	Fixed a couple of incorrect #ifdef's.
	Improved some of the documentation.
	Fortify_LabelPointer() misbehaved when Fortify had been run-time
disabled.

Changes from V2.0 to V2.1
	Fixed Fortify_LabelPointer(), which was broken.


Changes from V2.0B to V2.0

    Moved  the  checksum  to  the  start  of the Header, to avoid alignment
problems (thanks to Ron Flory and Tim Taylor for finding this)
    Fixed a miscalcultation with FORTIFY_ALIGNED_BEFORE_SIZE (thanks to Tim
Taylor)
    Implemented  the  delete stack - Fortify is now aware of deletes inside
deletes, and outputs the full delete stack with all delete related hits.
    Implemented  the  new  and  improved  Fortify_Disable() - works even if
memory has already been allocated.
    Fixed a few problems with FORTIFY_TRACK_DEALLOCATED_MEMORY being turned
off.
    Fixed a couple of incorrect sprintfs.
	Added Fortify_LabelPointer (thanks to Steve Toal for this idea)
	FORTIFY_WARN_ON_ZERO_ALLOCATE  removed  as "new char[0]" is allowed, as
is malloc(0).
    free(0) is now accepted as harmless.



Changes from V1.0 to V2.0 B

    Added  FORTIFY_ALIGNMENT,  so that machines requiring special alignment
wouldn't break.
    Added  deallocated  memory  tracking,  and  loads  of  diagnostics made
possible by this.
    Added statistics.
    Merged Fortify and ZFortify.
    Each  memory  block  now  knows  which  allocator  function was used to
allocate  it,  and  uses this information to ensure the correct function is
being used to free it.
    Added support for strdup()
    Added support for versions of sprintf that don't support "%p".
    Fortify  will  now  supply  default values for configuration parameters
missing from "ufortify.h"
    A few minor portability bug fixes
    Fortify will now automatically configure itself for GCC and Borland C++
4.5.
    All  error  messages  and  warnings  tidied  up  so  they are easier to
understand.
    The new operators will now call the new handler if the allocation fails
(if there is a new handler installed, of course).


Changes from SafeMem to Fortify V1.0

    Completely rewrote it.
    Fortifies ANSI memory allocation functions rather than Amiga OS ones.
    Supports C++'s new and delete




    TO DO
    -----
    Make Fortify automatically configure itself for major compilers.

    Add support for non-standard new-handlers, such as Microsoft Visual C++
2.0, via FORTIFY_NEW_HANDLER_FUNC.

    Implement a stack for scope source-code info and scoped statistics.

    Better documentation.

    FAQ  -  installation  problems,  linking  problems,  "spurious output",
understanding the results, how to track down hits.

    Better test programs (with examples of obscure bugs).

    Memory  allocation  list could be implemented as a "skip list", so that
searching would be quicker.  "Paranoid" mode would be quite fast.

    CHECK_ALL_MEMORY_ON_  could take a percentage of the time to do it - it
could  be set to 50%, so that memory is only checked 1/2 of the time, or we
only  check 1/2 of the memory, or something like that, so that the checking
still  goes  on,  but less frequently, so there is less overhead.  Probably
overkill.

	Write  a  DLL  callback module so that user DLL's can share memory with
their parent applicatoins.

	Add a "pass-count" to source-code information.
 */
#endif

#endif
