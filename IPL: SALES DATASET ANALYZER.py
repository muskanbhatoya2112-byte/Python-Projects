import pandas as pd

def load_dataset():
    file = input("Enter CSV file name (ipl.csv / sales.csv): ")

    try:
        data = pd.read_csv(file)
        return data
    except:
        print("File not found!")
        return None


def show_data(data):
    print("\nDataset:")
    print(data)


def show_columns(data):
    print("\nColumns:")
    print(data.columns)


def describe_data(data):
    print("\nSummary:")
    print(data.describe())


def missing_values(data):
    print("\nMissing Values:")
    print(data.isnull().sum())


def top_records(data):
    n = int(input("Enter number of records: "))
    print(data.head(n))


def total_sales(data):
    if "Price" in data.columns:
        data["Total"] = data["Price"] * data["Quantity"]
        print(data)
        print("\nTotal Sales =", data["Total"].sum())
    else:
        print("Not a Sales Dataset")


def highest_run_scorer(data):
    if "Runs" in data.columns:
        player = data.loc[data["Runs"].idxmax()]
        print("\nHighest Run Scorer")
        print(player)
    else:
        print("Not an IPL Dataset")


def highest_wicket_taker(data):
    if "Wickets" in data.columns:
        player = data.loc[data["Wickets"].idxmax()]
        print("\nHighest Wicket Taker")
        print(player)
    else:
        print("Not an IPL Dataset")


def main():

    data = load_dataset()

    if data is None:
        return

    while True:

        print("\n========== MENU ==========")
        print("1. Show Dataset")
        print("2. Show Columns")
        print("3. Dataset Summary")
        print("4. Missing Values")
        print("5. Top Records")
        print("6. Total Sales")
        print("7. Highest Run Scorer")
        print("8. Highest Wicket Taker")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_data(data)

        elif choice == "2":
            show_columns(data)

        elif choice == "3":
            describe_data(data)

        elif choice == "4":
            missing_values(data)

        elif choice == "5":
            top_records(data)

        elif choice == "6":
            total_sales(data)

        elif choice == "7":
            highest_run_scorer(data)

        elif choice == "8":
            highest_wicket_taker(data)

        elif choice == "9":
            print("Thank You!")
            break

        else:
            print("Invalid Choice")


main()