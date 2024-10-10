import time
import os
import random
print("Password Cracker zzzzz")
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ", "A","B","C","D","E","F","G","H","I","J","K","L","M","N",'O',"P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","!","@","#","$","%","&","*","(",")","^","+","_"]
target_string = input("Enter password: ")
current = ""
i = 0
for i in range(len(target_string)):
    while True:
        x = random.choice(alphabet)
        print(current + x)
        if x == target_string[i]:
            current += x
            break
        time.sleep(0.025)

        
