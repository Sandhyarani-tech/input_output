10)
 Distance Between Two Points
Problem Statement
Ajay, Binoy, and Chandru decide to play a game of distance calculation. Each of them will give their house coordinates and they need to calculate the distance between Ajay's house and Chandru's house. Given the coordinates of the 2 endpoints of a line (x1,y1)(x_1, y_1)(x1​,y1​) and (x2,y2)(x_2, y_2)(x2​,y2​), write a Python program to find the distance between the points.
Input Format
Input consists of 4 integers. The first integer corresponds to x1x_1x1​. The second integer corresponds to y1y_1y1​. The third and fourth integers correspond to x2x_2x2​ and y2y_2y2​ respectively.
Output Format
Refer to the Sample Input and Output for exact formatting specifications. [All floating point values are displayed correct to 2 decimal places]
Sample Input
3
4
6
8

Sample Output
The distance between Ajay's house and Chandru's house is 5.00

Solution
import math

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"The distance between Ajay's house and Chandru's house is {distance:.2f}")





11)
Finding the Area of a Triangle
Problem Statement
Ajay, Binoy, and Chandru decide to test their geometry skills. They want to calculate the area of the triangle formed by their house coordinates. Given the coordinates of the 3 vertices of a triangle (x1,y1)(x_1, y_1)(x1​,y1​), (x2,y2)(x_2, y_2)(x2​,y2​), and (x3,y3)(x_3, y_3)(x3​,y3​), write a Python program to find the area of the triangle.
Formula
Area=1/2​∣x1​(y2​−y3​)+x2​(y3​−y1​)+x3​(y1​−y2​)∣
Input Format
Input consists of 6 integers. The first two integers correspond to (x1,y1)(x_1, y_1)(x1​,y1​). The next two integers correspond to (x2,y2)(x_2, y_2)(x2​,y2​). The last two integers correspond to (x3,y3)(x_3, y_3)(x3​,y3​).
Output Format
Refer to the Sample Input and Output for exact formatting specifications. [All floating point values are displayed correct to 2 decimal places]
Sample Input

0
0
4
0
0
3

Sample Output

The area of the triangle is 6.00

Solution
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2

print(f"The area of the triangle is {area:.2f}")

12)
 Finding the Slope of a Line
Problem Statement
Ajay and Binoy are curious about the slope of the line joining their houses. Given the coordinates of the 2 endpoints of a line (x1,y1)(x_1, y_1)(x1​,y1​) and (x2,y2)(x_2, y_2)(x2​,y2​), write a Python program to find the slope of the line.
Formula:
slope=x2​−x1/​y2​−y1​​
Input Format
Input consists of 4 integers. The first integer corresponds to x1x_1x1​. The second integer corresponds to y1y_1y1​. The third and fourth integers correspond to x2x_2x2​ and y2y_2y2​ respectively.
Output Format
Refer to the Sample Input and Output for exact formatting specifications. [All floating point values are displayed correct to 2 decimal places]
Sample Input

1
2
3
6

Sample Output

The slope of the line joining Ajay's house and Binoy's house is 2.00

Solution

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x2 != x1:
    slope = (y2 - y1) / (x2 - x1)
    print(f"The slope of the line joining Ajay's house and Binoy's house is {slope:.2f}")
else:
    print("The line is vertical, slope is undefined")

Decision Making
1)Get two integers x and y from the user and write a program to relate 2 integers as equal to, less than or greater than.
Input format:
Input consist of 2 integers
The first input corresponds to  the first number.(a)
The second input corresponds to the second number.(b)
Output format:
If the first number is equal to the second number, print "x and y are equal". Otherwise, print "x greater than y" or "x less than y"
Sample Input:
6
8
Sample Output:
6 less than 8

2)Write a program to check whether the given character is vowel or consonant.
Input format:
The input consist of a character
Output format:
The output consists of a below-given string
“Vowel” / “Consonant” / “Not an alphabet”
Sample Input:
e

Sample Output:
Vowel
Ans:
a=input()
if(a=='a' or a=='e' or a=='i' or a=='o' or a=='u'):
    print('Vowel')
elif(a>'a' and 'a'<a):
    print("Consonant")
else:
    print("Not an alphabet")
3)The newly appointed Vice-Chancellor of Anna University wanted to create an automated grading system for the students to check their grade. When a student enters a mark, the grading system displays the corresponding grade.
Write a program to solve the given problem.
  Marks scored  
  Grade 
100
S
90 - 99
A
80 - 89
B
70 - 79
C
60 - 69
D
50 - 59
E
<50
F

Input format:
The input consists of one integer which corresponds to the marks scored by the student

Output format:
If a student marks greater than 100, print "Invalid Input". Otherwise, print the grade.
Sample Input:
78
Sample Output:C

4) A fruit seller buys a dozen of banana at Rs.X. He sells 1 banana at Rs.Y. Write a program to determine the profit or loss in Rs. for the fruitseller.
Input format:
Input consists of 2 floating point numbers
The first input corresponds to the total cost(X)
The second input corresponds to the sold cost(Y)
Output format:
Print "Profit or Loss" with Rupees.
Sample Input:
60
4
Sample Output:
Loss : Rs.12.00

5) 
Write a program to determine the fee amount to be collected from a student. 
Refer the table below for fee details.
  Student Type  
  Student Type denoted as  
  Fee Details  
Merit Seat Day Scholar
MSDS

Tuition fee + Bus fee



Merit Seat Hosteller
MSH
Tuition fee + Hostel fee

Management Seat Day Scholar



MGSDS

150% of Tuition fee + Bus fee



Management Seat Hosteller
MGSH

150% of Tuition fee + Hostel fee




Input format:
The first input corresponds to the student type
The second input corresponds to the tuition fee
The third input corresponds to the bus fee or hostel fees
Output format:
Print the total fee amount of the corresponding student with 2 decimal places.
Refer below sample output for formatting
Sample Input:
MSH
40000
50000
Sample Output:
90000.00

6)
Ask a user for their birth year encoded as two digits (like "62") and for the current year, also encoded as two digits (like "99"). Write a program to find the users current age in years.
Input format:
Input consists of 2 integers
The first integer corresponds to the last 2 digits of the birth year
The second integer corresponds to the last 2 digits of the current year
Output format:
Print the user's current age
Refer below sample output for formatting.
Sample Input:
62
00
Sample Output:
38
7)
There are 3 labs in the CSE department(L1, L2, and L3) with a seating capacity of x, y, and z respectively. Find the lab which has minimal seating capacity.  
Input format:
Input consists of 3 integers
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
Output format:
Print the minimal seating lab capacity
Refer the Sample output for formatting
Sample Input:
30
40
20
Sample Output:
L3
Ans :

L1=int(input())
L2=int(input())
L3=int(input())
if((L1<L2) and (L1<L3)):
    print("L1")
elif(L2<L3 and L2<L1):
    print("L2")
else:
    print("L3")

8)
There are 3 labs in the CSE department are L1, L2, and L3 with a seating capacity of x, y, and z respectively. One of the 3 labs has been allocated for ACE training. Out of the available labs, find the lab which has minimal seating capacity.
Input format:
Input consists of 3 integers and a string
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
The fourth input denotes the lab which is allocated for ACE training
Output format:
Print the minimal seating capacity lab amongst the available labs.
Refer the Sample output for formatting
Sample Input:
30
40
20
L3
Sample Output:
L1
9)
There are 3 labs in the CSE department are L1, L2, and L3 with a seating capacity of x, y, and z. A single lab needs to be allocated to a class of 'n' students. How many of the 3 labs can accommodate 'n' students?
Input format:
Input consists of 4 integers
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
The fourth input denotes the number of students(x)
Output format:
Print the number of labs which can accommodate the 'n' number of students
Refer the Sample output for formatting
Sample Input:
30
40
20
25
Sample Output:
2 
10)


 There are 3 labs in the CSE department. The labs are L1, L2, and L3 with a seating capacity of x, y, and z respectively. A single lab needs to be allocated to a class of 'n' students. The labs need to be utilized to the maximum i.e the number of systems used should not be minimal. Which lab needs to be allocated to this class?
Input format:
Input consists of 4 integers
The first input denotes 'x'
The second input denotes 'y'
The third input denotes 'z'
The fourth input denotes 'n'
Output format:
Print the lab which is suitable for  'n' number of students
Refer the Sample output for formatting
Sample Input:
30
40
20
25
Sample Output:
L1
