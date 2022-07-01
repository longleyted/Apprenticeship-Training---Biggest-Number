biggestNumber = 0
x = 0
while True:
    x+=1
    answer = int(input("Please input a number: "))
    if biggestNumber < answer:
        biggestNumber = answer
    if x == 5:
        print("Here is the biggest number you input... ",biggestNumber)
        break
