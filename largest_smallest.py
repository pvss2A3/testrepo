largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
            break
    try:
        x = float(num)
    except:
        print('Invalid input')
        continue
    if largest>x:
        largest = x
    if smallest<x:
        smallest=x
print("Maximum is", largest)
print("Minimum is", smallest)
