'''
# 1009
name=str(input())
b=float(input())
c=float(input())

med = b  + (c*(15/100))
print ('TOTAL = R$ %.2f'%(med))

# 1012

a,b,c = list(map(float,input().split()))

triangle = (.5)* (a * c)
circle = (3.14159) * (c * c)
trapezium = ((a+b)/2) * c
sqare = b**2
recatangle = (a*b)

print('TRIANGULO: %.3f\nCIRCULO: %.3f\nTRAPEZIO: %.3f\nQUADRADO: %.3f\nRETANGULO: %.3f'%(triangle,circle,trapezium,sqare,recatangle))

n = int(input("enter range of star : "))
for i in range(0,n+1):
    for j in range(0,i):
        print("*", end="")
    print()
'''
x = ['ab', 'cd']
for i in x:    
    i.upper() 
    print(x)