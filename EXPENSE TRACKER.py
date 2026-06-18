file = "expense.txt"

try:
    d = {}

    for i in range(3):   # 3 expenses
        c = input("Category: ")
        a = float(input("Amount: "))
        d[c] = d.get(c, 0) + a

    with open(file, "w") as f:
        for k, v in d.items():
            f.write(k + " " + str(v) + "\n")

    print("\nSummary:")
    for k, v in d.items():
        print(k, "=", v)

except ValueError:
    print("Invalid Input")