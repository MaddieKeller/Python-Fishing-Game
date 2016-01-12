import datetime, calendar, math, numpy
from fractions import gcd
import matplotlib.pyplot as plt

#Exercise 40 - distance between two points (lat1, lon1) and (lat2, lon2)
point1 = (5,5)
point2 = (8,0)

def distanceCal(p1, p2):
    #Spherical in radians
    degRadian = math.pi/180.0

    #phi = 90-latitude
    phi1 = (90-p1[0])*degRadian
    phi2 = (90-p2[0])*degRadian

    #theta = longitute
    theta1 = p1[1]*degRadian
    theta2 = p2[1]*degRadian

    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1-theta2)+math.cos(phi1)*math.cos(phi2))
    arc = math.acos(cos)

    return arc
miles = 3960
kilometers = 6373
dist = distanceCal(point1, point2)

print ("The distance between them is " + str(miles*dist) + " miles or " + str(kilometers*dist) +" kilometers.")

#Exercise 39 - compute the future value of interest principal and years
amt = 10000
interest = 3.5
years = 7

x = 0
while x < years:
    amt = amt + (amt* (interest/100))
    x += 1

print amt

#Exercise 38 - solve (x + y) * (x+Y)
x = 4
y = 3

def exer38(x, y):
    return (x + y)*(x+y)

print exer38(x,y)

#Exercise 36 - Add two objects if both are integer
obj1 = 7
obj2 = 'fred'

if type(obj1).__name__ == 'int' and type(obj2).__name__ == 'int':
    print obj1 + obj2
else:
    print "These are not both integers. They are " + type(obj1).__name__ + " and a " + type(obj2).__name__

#Exercise 35 - return true if the two integers are equal or their sum or difference is 5
int1 = 1
int2 = 4

def ex35(a, b):
    if (a+b == 5 or a-b ==5 or a == b):
        return True
    else:
        return False

print ex35(int1, int2)

#Exercise 34 - sum two integers except if between 15 and 20 will sum zero

def exer34(a, b):
    if (a + b)>= 15 and (a + b) <=20:
        return 20
    else:
        return a + b

print exer34(int1, int2)



#Exercise 33 - sum of three given integers but if two are equal it will sum zero

int3 = 5

def exer3(a, b, c):
    if (a == b or a == c or b == c):
        return 0
    else:
        return a + b + c

print exer3(int1, int2, int3)


#Exercise 32 - least common multiple of two positive integers
int1 = 15
int2 = 17

def leastCommon(a,b):
    return ((a*b)//gcd(a,b))

print leastCommon(int1,int2)

#Exercise 31 - compute the greatest common divisor of two integers

print gcd(int1, int2)

#Exercise 30 - base and height of a triangle and compute the area
base = raw_input('Enter the triangle\'s base: ')
height = raw_input('Enter the triangle\'s height: ')

def triangleArea(b,h):
    area = (float(b) * float(h))/2.0
    return area

print ('Area = ' + str(triangleArea(base, height)))

#Exercise 29 print out all results from 1 not in 2
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
missingColors = set([])

for color in color_list_1:
    if color not in color_list_2:
        missingColors.add(color)

print missingColors
print color_list_1.difference(color_list_2)

#Exercise 28 print all even numbers list and stop printing if number is after 237

numbers = [\
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, \
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, \
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, \
    958,743, 527]

def exercise28(numbers):
    for number in numbers:
        if (number != 237 and number%2 == 0):
            print number
        elif (number ==237):
            break
        else:
            pass

exercise28(numbers)

#Exercise 27 - concatenate all elements in a list into a string
n = [3,4,6,20,39,44]
s = ''
for item in n:
    s = s + str(item)

print s

#Exercise 26 - histogram

n = [3,4,6,20,39,44]

plt.hist(n)
plt.title("Some Numbers, dude")
plt.xlabel("X-Range")
plt.ylabel("Y-Range")
plt.show()

for item in n:
    output = ''
    times = item
    while (times>0):
        output +='*'
        times -=1
    print output

#Exercise 25 - is a value in a group of values?

def valueCheck(values, n):
    return n in values

list1 = [1,5,8,3]

print valueCheck(list1, 3)
print valueCheck(list1, 9)

#Exercise 24 - check for letter is vowel

def checkVowel(letter):
    lcLetter = letter.lower()
    if (lcLetter == 'a' or lcLetter == 'e' or lcLetter == 'u' or lcLetter == 'i' or lcLetter == 'o'):
        print (letter.upper() + " is a vowel.")
    else:
        print (letter.upper() + " is a consenant.")

checkVowel('a')
checkVowel('q')
checkVowel('y')

#Exercise 23 - get n copies of first 2 characters of a string

def getCopiesFirst2(s,n):
    strNew = ""
    if len(s)<2:
        strNew = s
    else:
        for i in range(n):
            strNew = strNew + s[:2]

    return strNew

print getCopiesFirst2('abcdef',2)
print getCopiesFirst2('p',3)


#Exercise 22 - count the number 4 in a list

def count(nums):
    count = 0
    for num in nums:
        if num == 4:
            count +=1
    return count

list1 = [1,4,5,6,4,9,0]
list2 = [9,8,4,5,6,2,4,1,4,0]

print count(list1)
print count(list2)

#Exercise 21 is a given number odd or even
n = raw_input('Enter a number to find out if is odd or even: ')

if (int(n)%2 == 0):
    print "Your number is even."
else:
    print "Your number is odd."

#Exercise 20 get a string which is n copies of a given string

s = raw_input('Input some text:  ')
n = raw_input('Enter a number: ')
strNew = ''
x=0
while (x < int(n)):
    strNew = strNew+s
    x += 1


print strNew

#Exercise 19 get a new string from a given string [:2] method

string1 = raw_input('Input some text: ')

def stringExtract(str):
    if (str[:2] == 'Is'):
        return str
    else:
        str = 'Is ' + str
        return str

print stringExtract(string1)


#Exercise 17 - test if number is within 100 of 1000 or 2000
answer = raw_input('Enter a number to test:  ')


def testNumber(d):
    if ((d>=9000 and d<=1100) or (d>=1900 and d<=2100)):
        return True
    else:
        return False

print (testNumber(int(answer)))


#Exercise 16 - difference between given number and 17 if greater than 17 give double
answer = raw_input('Enter a number:   ')
def Difference(answer):
    if (float(answer) <=17.0):
        return (17.0-float(answer))
    else:
        return((int(answer)-17)*2)

print Difference(answer)

#Exercise 15 - volume of a sphere
radius = raw_input('Input the sphere\'s radius')

volume = (4.0/3.0)*math.pi*float(radius)**3

print ('The volume of the sphere is: '+ str(volume))

#Exercise 14 - difference in two dates
date1 = '2014,7,2'
date2 = '2014,7,11'

def dayFind(d):
    return datetime.datetime.strptime(d,'%Y,%M,%d')

endTime = dayFind(date2)
startTime = dayFind(date1)

delta = endTime - startTime

print (str(delta.days) + ' days.')

date3 = (2014,7,2)
date4 = (2014,7,11)

def tupleDayFind(d):
    return datetime.date(d[0],d[1],d[2])

endTime = tupleDayFind(date4)
startTime = tupleDayFind(date3)

print (str((endTime-startTime).days) + ' days.')