try:
    my_file = open("Funcion2.py", "r")
except Exception as err:
    print(err)

for line in my_file:
    print(line)

my_file.close()