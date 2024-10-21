LOOPING
1)The environmental eco club has discovered a new Amoeba that grows in the order of a Fibonacci series every month. They are exhibiting their amoeba in a national conference. They want to know the size of the amoeba at a particular time instant. If a particular month’s index is given, write a  program to displays the amoeba’s size……???. For Example, The size of the amoeba on month 1, 2, 3, 4, 5, 6, ..will be 0, 1, 1, 2, 3, 5, 8 respectively.
Input format:
The first input containing an integer which denotes the number of the month
Output format:
Print the amoeba size.
Refer the sample output for formatting.
Sample Input:
7
Sample Output:
8
Ans:
n=int(input())
a=0
b=1
for i in range (3,n+1):
	c=a+b
	a=b
	b=c
print (c)



2)Write a program to determine whether 'n' is a factorial number or not. Factorial of a number is the product of all positive numbers from 1 to 'n'.
Input format:
The input containing an integer 'n' which denotes the given number.
Output format:
If the given number is factorial, print "Yes". Otherwise, print "No".
Refer the sample output for formatting.
Sample Input:
6
Sample Output:
Yes
3) a = 0, b=0, c=1 are the 1st three terms. All other terms in the Lucas sequence are generated by the sum of their 3 most recent predecessors. Write a program to generate the first n terms of a Lucas Sequence.
Input format:
The input containing an integer 'n' which denotes the given number
Output format:
Print the  'n' terms of the Lucas Sequence, separated by a single space. There are no leading or trailing spaces in the output.
Refer the sample output for formatting.
Sample Input:
5
Sample Output:
0 0 1 1 2
Ans:
n=int(input())
a=0
b=0
c=1
print(a,end=’ ‘)
print(b,end=’ ‘)
print(c,end=’ ‘)
for i in range (4,n+1):
	d=a+b+c
	a=b
	b=c
	c=d
	print(d,end=’ ‘)
4)The rules for generating Collatz Sequence are:
If n is even:   n = n / 2
If n is odd:    n = 3n + 1
For example, if the starting number is 5 the sequence is:
5 -> 16 -> 8 -> 4 -> 2 -> 1
It has been proved for almost all integers, the repeated application of the above rule will result in a sequence that ends at 1.
Input format:
The input containing an integer 'n' which denotes the given number
Output format:
Print the numbers in the sequence and also print the number of times the rule has to be applied in order to reach 1.
Refer the sample output for formatting.
Sample Input:
5
Sample Output:
5
16
8
4
2
1
5
5)Write a program to check whether the given number is a trendy number or not. A number is said to be a trendy number if and only if it has 3 digits and the middle digit is divisible by 3.
Input format:
The input containing an integer 'n' which denotes the given number
Output format:
If the given number is a trendy number, then print "Trendy Number". Otherwise, print "Not a Trendy Number".
Refer the sample output for formatting.
Sample Input:
791
Sample Output:
Trendy Number
Ans :
n=int(input())
if(n>=100 and n<=999):
    a=n//10
    b=a%10
    if(b%3==0):
        print("Trendy Number")
    else:
        print("Not a Trendy number")
else:
    print("Not a Trendy Number")
