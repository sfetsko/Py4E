hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
try:
    fhours = float(hours)
    frate = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

if fhours > 40 :
    overtime = fhours - 40
    pay = (40 * frate) + (1.5 * overtime * frate)
else:
    pay = hrs * rate
print("Pay:",pay)
