import time
fibonachi = [1,2]
while (len(fibonachi) <= 20):
    print(fibonachi[-1])
    fibonachi.append(fibonachi[-1] + fibonachi[-2])
    time.sleep(0.1)