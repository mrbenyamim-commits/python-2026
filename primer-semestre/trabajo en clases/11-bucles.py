
"""   bucle infinito n°1:
while True:   
    sum += 2
    print(sum)   """
num = 0

while num <= 100:
    print(num)
    num +=2
print("fin del bucle n°1")

while num <= 200:
    print(num)
    num +=10
else:
    print("fin del bucle n°2")

while num <= 300:
    print(num)
    num +=5
    if num == 250:
        print("aqui cuando llega a 250")
print("fin del bucle n°1")