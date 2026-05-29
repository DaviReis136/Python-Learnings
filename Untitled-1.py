largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    print(num)
    try: 
        number = float(num)
    except:
        print('Insira um número')
        continue
    count = 0
    count = count + 1
    if largest is None: 
        largest = number
    elif number > largest: 
        largest = number 
    if smallest is None: 
        smallest = number
    elif number < smallest : 
        smallest = number

print("Maximum", largest)
print('minimium', smallest)
