def checkPrime(x):
    for item in range(1,x+1):
        if x % item == 0:
            count = count +1
    if count == 2:        
        return True
    return False
def findPrimeNumber(arr):
    prime_array = []
    for num in arr:
        if checkPrime(num) == True:
            prime_array.append(num)
    return prime_array



def findOddNumber(arr):
    odd_array = []
    for num in arr:
        if num %2 !=0:
            odd_array.append(num)
    return odd_array


if __name__ =="__main__":

    # username = input("Enter your name: \n")
    # age = int(input("Enter your age: \n"))
    # print("Your name: "+ username)
    # print("Your age:"+ str(age))

    # number1 = int(input("Enter number1"))
    # number2 = int(input("Enter number2"))
    # number3 = int(input("Enter number3"))
    # number4 = int(input("Enter number4"))

    # max = number1
    # if number2 > max:
    #     max = number2
    # if number3 > max:
    #     max = number3
    # if number4 > max:
    #     max = number4
    # print(max)

    # array1 = [1,2,3,4,5,6,7,8,9,10]
    # arrayStr = ['123', 1,2,3,4, "ahahhaa123", "234"]
    # s = array1 + arrayStr
    
    # print(array1[3:7])
    # print(array1[3:])
    # print(array1[:4])
    # print(s)
    array1 = [1,2,3,4,5,6,7,8,9,10]
    arrayResult = findOddNumber(array1)
    print(arrayResult)
    arrayResult1 = findPrimeNumber(array1)
    print(arrayResult1)

        
    


    