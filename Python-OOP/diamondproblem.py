class A:
    def method(self):
        print("this method belongs to class A")
#if just had this oe showing this statemtant would print
class B(A):
    def method(self):
        print("this method belongs to class B")
#can have this one and class A showing but this statement would print 
class C(A):
    def method(self):
        print("this method belongs to class C")
#class D(B,C):#this shows class B because of the order in this class bracket
 #   pass
class D(C,B):#this one shows class C because of the order
    pass
#if had class C and A showing class C would print, but all 3 depends on order in class D brackets.


d=D()
d.method()