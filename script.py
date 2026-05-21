# def display():
#     n="Neha"
#     a=21
#     b="Female"
#     print(f"name:{n}")
#     print(f"age:{a}")
#     print(f"gender:{b}")
# display()

# def fun(*a):
#     print(a)
#     print(*a)
# fun(10,20,30,40,60)

# def fun3(a,b,c,d):
#     print(a,b,c,d)
#
#
# # def fun2(**b):
# #     print(b)
# #     print(**b)
# fun3(a=75 , b=23, c=24, d=10)

# def fun5(*a,**b):
#     print(a,b,sep ="\n")
# fun5(10,7,a=30,75,b=50)
#
# def fun6(*a):
#     print(sum(a))
# fun6(10,20,30,40)

# def fun7(*a):
#     i=0;s=0;
#     while i<len(a):
#         if a[i]%2==0:
#             s+=a[i]
#         i+=1
#     print(s)
# fun7(1,7,8,25,30,60,70)


# def fun8(*a):
#     i = 0
#     s = 0
#
#     while i < len(a):
#         s += a[i]
#         i += 2   # skips one element (alternate numbers)
#
#     print(s)
#
# fun8(1,2,3,4,5,7,8,8,10)


# def fun9(*a):
#      i=0
#      s=0
#      while i<len(a):
#          if i%2==0:
#              s+=a[1]
#          i+=1
 #      print(s)
# fun9(1,2,3,4,5,7,8,8,10)

def fun10(*a):
    print(sum(a[::2]))
fun10(1,2,3,4,5,7,7,8,8,10)