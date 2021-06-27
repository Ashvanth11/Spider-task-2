# Algos task-2
## Questions:
***A)*** 
A company hires Inderraj as a typewriter. His work is to type proper bracket strings. However Inderraj is so lazy that he does not really take his job seriously and ends with messing up.

Now the company hires you to find the longest proper bracket sequence from starting that is perfectly written by inderraj.

More formally find the longest proper prefix bracket sequence written by him.

[Proper prefix of a string is the balanced string bracket sequence starting from first position of the given expression. It will be more clear by looking at sample test case.]

**Input Format**

Input will consist of an integer T denoting the number of test cases to follow.

Then, T strings follow, each on a single line, representing a string of bracket.

**Constraints**
1<=T<=500
1<=The length of a single expression<10^6

The total size of all the input expressions is no more than 5.10^6

**Output Format**

Output T lines containing the length of the longest prefix that is valid or 0 if there's no such a prefix.
<br />
<hr />

***B)*** 

There exist an integer array A of length N whose values are unknown to us. We are given an integer sequence B of length N−1 as input. We also know that : Bi≥max(Ai,Ai+1) (i.e., every value of B array at ith  index ,will be greater than values at Ai  and Ai+1  , for every i from 0 to N-1).

Find the maximum possible sum of the elements of A.

**Input Format**

First line will have an integer N, the length of A array.

second line will have N-1 spaced integers, representing the elements of B array.



B1  B2  B3  ........ BN-1.

**Constraints**

All values in input are integers.

2 ≤ N ≤ 100

0 ≤ Bi  ≤ 10^5

**Output Format**

Print the maximum possible sum of the elements of A
<br />
<hr />

***C)***
Anuj has to climb up stairs to reach the first floor of his home. He can either climb up one step or two steps at a time. However there is a catch. There are some stairs that are not safe to step on. You have to count the number of ways that Anuj can reach the nth stair. He is initially on the ground floor, i.e. 0th step. Since the number of ways can be a large number, find the count modulo 1000000007.

**Input Format**

-   The first line has integers n, the number of stairs and m, the number of broken stairs
-   The next m lines have the positions, brokeni  of the broken steps.

**Constraints**

-   1 <= n <= 105
-   0 <= m <= n-1
-   1 <= brokeni  <= n-1

**Output Format**

Print the number of ways, modulo 1000000007.
<br/>
<hr/>

***D)*** 
You are given with an array of integers with size  **n**  , where a[i]=i. You will be given with  **q**  queries. In each query you have to add a value '**v**' to each of the array element between the given indices (_l_,_r_) inclusive of both the indices. As a result, you have to return the maximum element of the resultant array after  **q**  operations.

**Input Format**

-   The first line contains number of elements in the array,  **n**
-   The second line contains number of queries to be performed,  **q**
-   Each of the next  **q**  lines contains 3 space separated integers -  _l, r,val_- denoting left index,right index of the range and the value to be added.

**Constraints**
1<=n<=10^5

and 1<=q<=10^2

Left and Right indices for query: 1<=L<=R<=n
Value to be added, v: 1<=v<=10^9

**Output Format**

-   Print the maximum element in the array after  _q_  operations.
<br/>
<hr/>

***E)*** 
You are given with an array of integers with size  **n**  , where a[i]=i. You will be given with  **q**  queries. In each query you have to add a value '**v**' to each of the array element between the given indices (_l_,_r_) inclusive of both the indices. As a result, you have to return the maximum element of the resultant array after  **q**  operations.

**Input Format**

-   The first line contains number of elements in the array,  **n**
-   The second line contains number of queries to be performed,  **q**
-   Each of the next  **q**  lines contains 3 space separated integers -  _l, r,val_- denoting left index, right index of the range and the value to be added.

**Constraints**
1<=n<=10^5

and 1<=q<=10^5

Left and Right indices for query: 1<=L<=R<=n
Value to be added, v: 1<=v<=10^9
**Output Format**

-   Print the maximum element in the array after  _q_  operations.
## Explanation:
TASK 2-A 
FIND THE LENGTH
- define a function prefix_length() which takes in a string
  - we create variables x, ans and set them to 0 initially.
  - we check all the characters of the string and increment x by 1 if its '<' and decrement x by 1 if its '<'.
  - if x becomes 0( perfect set of brackets) we add ans by the position of the current character which is the current length of proper prefix bracket.
 - we check the entire string unless number of '>' exceeds '<'(x becomes -ve)
 - we print the answer(ans)
- we take in the number of test cases(t) and store each test case in a list(s)
- we call the function prefix_length() for each test case

TASK 2-B
MAXIMUM POSSIBLE SUM
- we take in the length of array A(n) and array B(b[])
- we create a variable ans to find the maximum sum
- B[i]>=max(A[i],A[i+1])
  so, B[0]>=A[0]
   which implies,  B[0]=A[0] (since we are finding maximum sum)
  similarly,
      B[n-2]=A[n-1]

- we add A[0] and A[n-1] to ans
- for other elements,
   since B[i]>=max(A[i],A[i+1]),
               A[i]=min(B[i-1],B[i])

-using this we find the total answer and print it

TASK 2-C
STAIRS PROBLEM
- define a function fibonnacci() which returns the fibonacci sum of the given number
- we take in number of stairs(n) and number of broken stairs(m)
- for easier calculation lets assume 2 imaginary broken steps, step[-1](below 0th step) and step[n+1](above last step)
- take in all the positions of the broken steps in b[]

{the number of ways to climb n continuous stairs with 1 or 2 steps at a time is same the nth element of the fibonacci series}

- using this we find the ways to climb n continuous steps between two broken steps
- we do this every interval(every successive pair of broken steps) and multiply every value in totways(multiplication theorem)
- totways=0 if two consecutive stairs are broken
- we print the answer(totways)

TASK 2-D
MAXIMUM ELEMENT IN ARRAY
- take in number of elements in array(n) and number of queries(q)
- create a[] initially with given condition
- for each query, take in l,r,val and update the array using given range range and val
- finally print maximum element of a[] using max() function

TASK 2-E
MAXIMUM ELEMENT IN ARRAY-2
- due to increase in constraint's range , we have to optimize last problem's code
- initially create a[] with every element being 0. 
- for each query , instead of adding val over the entire range, we can val to a[l-1] and -val to a[r]
- to get the original updated list, we have to find the prefix sum list of the list we have 
- finally we add every element of the list with its postion to meet the initial condition(a[i]=i)
- print maximum element of a[] using max() function
