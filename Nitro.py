import random, string
import webbrowser
import time
import requests

Num = input("Enter Number : ")

f = open("Nitro Codes.txt", 'w', encoding='utf-8')

print("Wait, Generating Nitro Codes")

for n in range(int(Num)):
    y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
    f.write('https://discord.gift/')
    f.write(y)
    f.write("\n")

f.close()

with open("Nitro Codes.txt") as f:
    for line in f:
        nitro = line.strip("\n")
        url = 'https://discordapp.com/api/v6/entitelemnts/gift-codes/' + nitro + "?with_application=false&with_subscription_plan=true"
        r = requests.get(url)

print("Check 'Discord Nitro Code.txt'")