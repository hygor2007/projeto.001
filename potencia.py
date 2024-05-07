b= int(input("digite o valor da base:"))

e= int(input("digite o valor do expoente:"))

r =b

for g in range(1,e):
   r =r * b
print("resultado:" , "{:.2f}".format(r))
