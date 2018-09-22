f = open("logs/bruteforce","w")
fact = 1
for i in range(1,13):
    fact *= i
    f.write(str(i)+" "+str(i*fact)+"\n")
f = open("logs/backtrack","w")
fact = 1
for i in range(1,13):
    fact *= i
    f.write(str(i)+" "+str(fact)+"\n")
