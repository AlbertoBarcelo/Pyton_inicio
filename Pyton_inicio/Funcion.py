import sys, traceback

def fun1():
    print("Fun1_in")
    fun2()
    print ("fun1_out")

def fun2():
    print("Fun2_in")
    fun3()
    print ("fun2_out")

def fun3():
    print("Fun3_in")
    #print(3/0)
    raise(Exception("Este error es porque si"))
    print ("fun3_out")

try:
    fun1()
except Exception as err:
    print(str(err))
    print("="*10)
    traceback.print_exc()