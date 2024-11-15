def fonc():
    print ("hello world")
def change_fonc(fonc):
    def my_warpper():
        print ("wait for hello world")
        fonc()
        print("Bye Bye world")
    return my_warpper()
obj=change_fonc(fonc)    
obj