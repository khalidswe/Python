# try:
#     number1 = int(input())
#     print(number1+10)
# except NameError:
#     print("variable undefined")
#
# except:
#     print("enter an integer number")
#
# #try execpt with else :
# try:
#     number1 = int(input())
#     print(number1+10)
# except:
#     print("enter an integer number")
#
# else:
#    print("everthing allright")

# #try execpt with finally :

# try:
#     number1 = int(input("enter number: "))
#     print(100/number1)
# except Exception as k:  #caught exection as name
#     print("exeception : ",k)
#
# finally: #just give and output is this program finished or not
#    print("try execpt finish")

#learnvern assignment 3:
# try:
#     a = int(input("enter 1st input: "))
#     try:
#         b = int(input("enter 2nd input: "))
#         print("sum : ",a + b)
#     except Exception as l:
#         print("2nd number exception caught :",l)
# except Exception as k:
#          print("1st number exception is :",k)
# try:
#     number1 =int(input("enter number 1:"))
#     number2 =int(input("enter number 2:"))
#
#     print(number1+number2)
# except:
#     print("something wrong")
# else:
#     print("all ok")

try:
    if '1' != 1:
        raise "someError"
    else:
        print("someError has not occurred")
except "someError":
    print("someError has occurred")
