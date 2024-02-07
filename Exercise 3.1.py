hrs = input('Enter hours: ')
hrs = float(hrs)
rate = input('Enter rate: ')
rate = float (rate)
if hrs > 40 :
    overtime = hrs - 40
    pay = (40 * rate) + (1.5 * overtime * rate)
else :
    pay = hrs * rate
print("Pay:",pay)
