import math

mes = input("give measurements number:")
mes = int(mes)

# average value
sumo = []
sum1 = 0.0
for i in range(0, mes):
    x = input("give value of measurement in Amperes:")
    x = float(x)
    sumo.append(x)
    sum1 += x
mo = sum1 / mes
print("the average value of the measured current values is:", mo, "Ampere")

# standard deviation
dev = 0.0
for x in sumo:
    dev += (x - mo) ** 2
mo2 = math.sqrt(dev / (mes - 1))
print("Standard deviation of current values is:", mo2, "Ampere")

# accuracy of the average value
acav = mo2 / math.sqrt(mes)
acav = acav * 1000
print("the accuracy of the average value is:", acav, "mA")

# possible 50% error
e = mo2 * 0.6745
e = e * 1000
print("the 50% possible error is:", e, "mA")
