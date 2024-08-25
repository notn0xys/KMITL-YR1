def reverse(str):
   return str[::-1]
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

i = 1
row = 0
num = 13
while i <= 100:
    need_print = False
    if is_prime(num):
        reversed111 = int(reverse(str(num)))
        if is_prime(reversed111):
            need_print = True
    
    if need_print:
        i += 1
        if row < 10:
            print(f"{num} " ,end="")
        else:
            print(num)
            row = 0
        row += 1
    num += 1
