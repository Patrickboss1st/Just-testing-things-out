name = input("Whats the name of your item?: ")
price = float(input("Whats the price of your itme?: "))
quant = int(input("How many of set item did you get?: "))
total = price * quant
print(f"Your total of {quant} {name} is {total}")