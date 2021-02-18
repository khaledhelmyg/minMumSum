# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
d = {}

for i in range(n):
    data = input().split(' ')
    d[data[0]] = data[1]
while 1:
    try:
        sheck=input()     
        if sheck in d:  
            print(sheck+"="+d[sheck])
        else:
            print("Not found")
    except:
        break      
              
