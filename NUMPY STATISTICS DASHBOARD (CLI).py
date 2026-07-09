import numpy as np
from collections import Counter


def mode(data):
    count = Counter(data)
    max_count = max(count.values())
    modes = [k for k, v in count.items() if v == max_count]

    if max_count == 1:
        return "No Mode"
    return modes


def dashboard():
    print("=" * 45)
    print("      NUMPY STATISTICS DASHBOARD (CLI)")
    print("=" * 45)

    numbers = input("Enter numbers separated by space: ")

    try:
        data = np.array(list(map(float, numbers.split())))
    except:
        print("Invalid Input!")
        return

    while True:
        print("\n----------- MENU -----------")
        print("1. Display Dataset")
        print("2. Mean")
        print("3. Median")
        print("4. Mode")
        print("5. Maximum")
        print("6. Minimum")
        print("7. Sum")
        print("8. Standard Deviation")
        print("9. Variance")
        print("10. Percentiles")
        print("11. Sort Data")
        print("12. Add New Data")
        print("13. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            print("Dataset:", data)

        elif choice == "2":
            print("Mean =", np.mean(data))

        elif choice == "3":
            print("Median =", np.median(data))

        elif choice == "4":
            print("Mode =", mode(data))

        elif choice == "5":
            print("Maximum =", np.max(data))

        elif choice == "6":
            print("Minimum =", np.min(data))

        elif choice == "7":
            print("Sum =", np.sum(data))

        elif choice == "8":
            print("Standard Deviation =", np.std(data))

        elif choice == "9":
            print("Variance =", np.var(data))

        elif choice == "10":
            print("25th Percentile =", np.percentile(data, 25))
            print("50th Percentile =", np.percentile(data, 50))
            print("75th Percentile =", np.percentile(data, 75))

        elif choice == "11":
            print("Sorted Data =", np.sort(data))

        elif choice == "12":
            new_numbers = input("Enter new numbers separated by space: ")
            try:
                new_data = np.array(list(map(float, new_numbers.split())))
                data = np.concatenate((data, new_data))
                print("Data Added Successfully!")
            except:
                print("Invalid Input!")

        elif choice == "13":
            print("Thank you for using NumPy Statistics Dashboard!")
            break

        else:
            print("Invalid Choice! Try Again.")


dashboard()