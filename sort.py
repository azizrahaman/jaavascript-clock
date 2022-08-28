from cmath import pi

## Function to calculate radians to Degree

# def radToDegree(x):
#     rad = x * (180/pi)
#     print(rad)

# print("Enter Rad value to convert into Degree: ", end=' ')
# radToDegree(int(input_x))

##Sorting an array funciotn

# def sort(Arr):
#     for i in range(len(Arr)-1,0,-1):
#         for j in range(i):
#             if(Arr[j]<Arr[j+1]):
#                 temp = Arr[j]
#                 Arr[j] = Arr[j+1]
#                 Arr[j+1] = temp

# Arr = [10,11,9,12,8,13,7]
# sort(Arr)
# print(Arr)

##Find average of a array 

# temp = 0
# for i in Arr:
#     temp = temp + i

# average = temp / len(Arr)
# print(average)

## Find product of real numbers

# product = 1
# count = int(input("Enter how many number to multiply: "))

# for i in range(count):
#     number = int(input("Enter Number: "))
#     product = product * number

# print("The product of those number is: ",product)

##Check a number is multiple of 5

# number = int(input("Enter a positive real number: "))
# if number % 5 == 0:
#     print(str(number) + " is completely divisable by 5")
# else:
#     print(str(number) + " is not divisable by 5")


## Reverse Number
# newNumber = 0
# number = int(input("Enter a positive real number: "))

# while number != 0:
#     first = number % 10
#     newNumber = newNumber * 10 + first
#     number = number // 10 
# print("New Number is: ", str(newNumber))

## Linar Searching

pos = -1

def search(list, n):
    i = 0
    while i < len(list):
        if list[i] == n:            
            globals()['pos'] = i
            return True
        i = i + 1

    return False

Arr = [2,4,6,8,10,12,14]
n = 10

print(Arr)

if search(Arr, n):
    print("Found The Number at index ", pos)
else:
    print("Not found!")