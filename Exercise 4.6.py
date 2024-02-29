def computepay(fhours,frate) :
    if fhours > 40 :
        overtime = fhours - 40
        pay = (40 * frate) + (1.5 * overtime * frate)
    else:
        pay = fhours * frate
    return pay

hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
try:
    x = float(hours)
    y = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

print("Pay",computepay(x,y))
