#code abbey
#Jake Routh
#3/2/16
''' problem 1 '''
#a = int(input('input a: '))
#b = int(input('input b: '))
#c = (a+b)
#print(c)
''' problem 2 '''
#a = int(input())
#b = input().split()
#c = 0
#for i in range(a):
   #c = c + int(b[i])
#print(c)
''' problem 3 '''
#answers = []
#a = int(input())
#for i in range(0,a):
 #   b = input().split()
  #  if int(b[0]) > int(b[1]):
  #      answers.append(b[1])
   # else:
    #    answers.append(b[0])

#for i in answers:
 #   print(i ,end=' ')
'''problem 4'''
#answers = []
#a = int(input())
#for i in range(0,a):
 #   b = input().split()
 #  c = int(b[0]) + int(b[1])
 #   answers.append(c)
#for i in answers:
 #   print(i ,end=' ')
'''problem 5'''
#answers = []
#a = int(input())
#for i in range(0,a):
    #b = input().split()
   # if int(b[0]) > int(b[1]) and int(b[1]) < int(b[2]):
    #    answers.append(b[1])
   # elif int(b[0]) < int(b[1]) and int(b[0]) < int(b[2]):
     #   answers.append(b[0])
    #else:
        #answers.append(b[2])
#for i in answers:
    #print(i ,end=' ')
'''problem 6'''
#a = int(input())
#answers = []
#for i in range(0,a):
    #b = input()
    #answers.append(b.count('a') + b.count('e') + b.count('i') +
                   #b.count('u') + b.count('o') + b.count('y'))
#for i in answers:
    #print(i ,end=' ')
'''problem 7'''
#answers = []
#a = int(input())
#for i in range(0,a):
    #b = input().split()
    #c = round(int(b[0]) / int(b[1]))
    #answers.append(c)
#for i in answers:
    #print(i ,end=' ')
'''problem 8'''
#number = input().split()
#maxn= int(number[0])
#minn = int(number[0])
#for i in range(len(number)):
    #number[i] = int(number[i])
    #if number[i] > maxn:
        #maxn = number[i]
    #if number[i] < minn:
        #minn = number[i]
#print(maxn, minn)
'''problem 9''' 
#l =input(" ")
#print(l[::-1])
'''problem 10'''
#answers = ""
#data = int(input())
#for i in range(data):
    #pair = input().split()
    #weight = float(pair[0])
    #height = float(pair[1])
    #BMI = weight / (height**2)
    #if BMI < 18.5:
        #answer = "under"
    #if BMI >= 18.5 and BMI < 25.0:
        #answer = "normal"
    #if BMI >= 25.0 and BMI < 30.0:
        #answer = "over"
    #if BMI >= 30.0:
        #answer = "obese"
    #answers += str(answer) + " "
#print(answers)
'''problem 11'''
#answers = []
#l = input().split()
#for i in range(0,int(l[0])):
    #a = int(l[i+1])
    #b = (a-32)*5/9
    #answers.append(round(b))
#for i in answers:
    #print(i,end=' ')
'''problem 12'''
#answers = []
#a = int(input())
#for i in range(0,a):
    #b = input().split()
    #for i in range(len(b)):
        #b[i] = int(b[i])
    #b.sort()
    #answers.append(b[1])
#for i in answers:
    #print(i ,end=' ')
'''problem 13'''

