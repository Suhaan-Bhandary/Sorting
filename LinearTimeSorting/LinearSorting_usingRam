### In this We will be taking a look at how to sort a data in linear time ###

# We will be using ram to achieve this task.

=> We are assuming that the given input are integers,(if not you can use mapping to convert them)
=> We have to also assume a boundary to the data e.g. [0,1,2,3....n] where n is a finite number.
=> the integer should fit in a word.
# Tip : In this context, a word is the unit that a machine uses
  when working with memory. For example, on a 32 bit machine,
  the word is 32 bits long and on a 64 bit is 64 bits long.
  The word size determines the address space.
  Tip : This topic is still in research and the best solution is O(n*sqrt(loglog(n)))

Lets get started :
1.We can do lot of things other than comparison.
2.If the data contains k[maximum possible value in array] which is not very big in size then we can sort them in linear time.

!!!!!!!---!!!!!!!
# First Algorithm : Counting Sort.

=> First Approach : make a array with k indexes and allocate the elements
   with the key same to the value and again traverse over it to get the output.
:( ->But in this approach we will sort the list but we are not taking other values attached to it or its identity.
eg. if i have a list of students participating in event by their roll number, in this approach we will only sort
    all roll numbers but not the name with it as we are only storing value in this method.

    To solve it we will pass value in the list.
    Check : counter_sort for the code.

    Counter sort is not the end !!, As it is a mediocre way to think but useful in the next algorithm.

# Second Algorithm : Radix Sort
=> Radix sort uses Counting Sort as sub algorithm.
=> it gets a much wider range, so k = n^O(1) [O(1) denotes the constant]

!=> Start :
1.Imagine each integer as base b.
digits = d = logbk +1 # It tell us how many digits we have.
we will take b = 2 as computer scientist take.

2.sort ints by least significant digit
  :
  :
  sort ints by most significant digit

3.Runtime : O((n+b)*d)
          : O[(n+b)*(logbk +1)]
          To make it minimun b = n
          : O[(n+n)*(lognk +1)]
          and on line 34 we mentioned that k = n^O(1)
          : O[(n+n)*(lognn^O(1) +1)]
