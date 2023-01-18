print("Hello word")

if 7 >4:
    #Soy un comentario
    print("Veo que se cumple la condición")

if True:
    print("Si o si")


i=1
while i<10:
    print ("Num", i)
    i= i+1


a=[]
i = 0
while i<10:
    a.append(i+2)

i = 0
while i<10:
    print("La psoicion", i, "contiene el valor", a[i])

b=[None]*10
print (b[0])

for item in b:
    print(item)

for i in range (0,10):
    print (i)

for i in range (1,30,2):
    print (i)
    
print("Adios")

if 7<5:
    print("Si 1")
elif 6<8:
    print("Si 2")
else:
    print("no o no")