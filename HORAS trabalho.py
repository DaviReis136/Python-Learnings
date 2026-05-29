def computepay():
    if hrs < 40: 
        PAY = hrs * hed
        return(PAY)
    elif hrs > 40:
        PAY = 40 * hed + ((hrs - 40) * 1.5 * hed)
        return(PAY)
        
hrs = input("Enter Hours: ")
hrs = float(hrs)
hed = input("Enter rate: ")
hed = float(hed)

print("Pay", computepay())
