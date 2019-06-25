start = int(input("Enter a starting number: "))
end = int(input("Enter an ending number: "))
amount = int(input("Enter the amount by which to count: "))
for i in range(start, end, amount):
    print(i)
