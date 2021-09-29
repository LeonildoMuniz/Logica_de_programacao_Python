a=1
b=1

num1 = int(input("Digite qual termo quer visualizar: "))


if (num1==1) or (num1==2):
    print("1")
else:
    for i in range(2,num1):
        result = a + b
        b = a
        a = result
        i += 1
    print(result)
