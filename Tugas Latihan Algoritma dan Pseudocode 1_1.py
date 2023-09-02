print("Hitunglah KPK dari 3 dan 4")

x = 3
y = 4

num1 = x
num2 = y 

while x!=y :
    if x>y :
        y = num2 + y
    else :
        x = num1 + x
        
print("Nilai KPK dari 3 dan 4 adalah", x)