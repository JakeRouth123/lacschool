#Jake Routh
#Function programs
#3/17/16
import random


def min3(a,b,c):
    answers = []

    for i in range(0,a):

        if int(a) > int(b) and int(b) < int(c):
            answers.append(b)
        elif int(a) < int(b) and int(a) < int(c):
            answers.append(a)
        else:
            answers.append(c)
    for i in answers:
        print(i ,end=' ')
    return i 


def box(height, width):
    for i in range(height):
        print(width*"*")

        
        
def find(mylist, key):
    for i in range(len(mylist)):
        if mylist[i] == key:
            print('Found', str(mylist[i]), 'at position', str(i))


def create_list(num):
    numlist = []
    for i in range(num):
        numlist.append(random.randint(1,6))
    return numlist



def count_list(numlist, num):
    out = 0
    for i in numlist:
        if i == num:
            out += 1
    return out


def average_list(numlist):
    out = 0
    for i in numlist:
        out += i
    out /= len(numlist)
    return out


tl = create_list(10000)
for i in range(1, 7):
    print(count_list(tl,i))
print(average_list(tl))









