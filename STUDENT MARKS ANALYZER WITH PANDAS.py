import pandas as pd

# Empty DataFrame
df = pd.DataFrame(columns=["Name", "Math", "Science", "English"])


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"


while True:
    print("\n========== STUDENT MARKS ANALYZER ==========")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Analyze Marks")
    print("4. Find Topper")
    print("5. Subject-wise Average")
    print("6. Save to CSV")
    print("7. Load from CSV")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        math = float(input("Math Marks: "))
        science = float(input("Science Marks: "))
        english = float(input("English Marks: "))

        new_row = {
            "Name": name,
            "Math": math,
            "Science": science,
            "English": english
        }

        df.loc[len(df)] = new_row
        print("Student Added Successfully!")

    elif choice == "2":
        if df.empty:
            print("No Records Found!")
        else:
            print("\nStudent Records")
            print(df)

    elif choice == "3":
        if df.empty:
            print("No Data Available!")
        else:
            analysis = df.copy()
            analysis["Total"] = analysis[["Math", "Science", "English"]].sum(axis=1)
            analysis["Percentage"] = analysis["Total"] / 3
            analysis["Grade"] = analysis["Percentage"].apply(calculate_grade)

            print("\nStudent Performance")
            print(analysis)

    elif choice == "4":
        if df.empty:
            print("No Data Available!")
        else:
            analysis = df.copy()
            analysis["Total"] = analysis[["Math", "Science", "English"]].sum(axis=1)

            topper = analysis.loc[analysis["Total"].idxmax()]

            print("\nTopper Details")
            print(topper)

    elif choice == "5":
        if df.empty:
            print("No Data Available!")
        else:
            print("\nSubject-wise Average")
            print("Math Average:", df["Math"].mean())
            print("Science Average:", df["Science"].mean())
            print("English Average:", df["English"].mean())

    elif choice == "6":
        df.to_csv("students.csv", index=False)
        print("Data Saved to students.csv")

    elif choice == "7":
        try:
            df = pd.read_csv("students.csv")
            print("Data Loaded Successfully!")
        except FileNotFoundError:
            print("students.csv file not found!")

    elif choice == "8":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")