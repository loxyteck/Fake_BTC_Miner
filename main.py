from colorama import Fore
import time
import secrets
from random import randint
from pystyle import *
import ctypes

btcval = 64000.42

input(Fore.CYAN + "Entre ton adresse BITCOIN : ")

Fails = 0
Success = 0

try:
  with open("money.txt", "r") as file:
    total_balance = float(file.read().strip())
except ValueError:
  total_balance = 0
total_balance = float(open("money.txt", "r").read().strip())
while True:
  ctypes.windll.kernel32.SetConsoleTitleW(f"BITCOIN MINER | Success : {Success} | Fails : {Fails} |")
  with open("money.txt", "w") as file:
    file.write(str(total_balance))
  time.sleep(0.008)
  ranInt = randint(0, 50000)
  if ranInt <= 1:
    randomBTC = randint(1,50000)/100000
    balance = round(btcval * randomBTC, 2) 
    total_balance += balance 
    print(Fore.WHITE + "> 0x" + secrets.token_hex(20) + Fore.GREEN + " > " + str(randomBTC) + " BTC ($" + str("{:,}".format(balance)) + ") Total Balance: $" + str("{:,}".format(round(total_balance,2))))
    Success += 1
    input()
    time.sleep(1)
  else:
    print(Fore.WHITE + "> 0x" + secrets.token_hex(20) + Fore.RED + " > 0.00 BTC ($0.00)")
    Fails += 1
