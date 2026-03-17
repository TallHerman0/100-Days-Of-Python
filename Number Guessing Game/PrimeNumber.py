def is_prime(num):
    square = round(num**0.5)
    prime = True
    for i in range(2,square+1):
        if num % i == 0:
            prime = False
        
    if prime == False:
        return "False"
    else:
        return "True"
            
num = int(input("input number: "))
print(is_prime(num))

# for i in range(2,(round(75**0.5))+1):
#     if 75 & i == 0:
#         print(f"{i}. Yes")
#     else:
#         print(f"{i}. No")