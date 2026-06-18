import csv

def grade(m):
    if m >= 80:
        return "A"
    elif m >= 60:
        return "B"
    else:
        return "C"

with open("students.csv", "r") as f, open("result.csv", "w", newline="") as r:
    reader = csv.reader(f)
    writer = csv.writer(r)

    for row in reader:
        try:
            name = row[0]
            marks = int(row[1])
            writer.writerow([name, marks, grade(marks)])
        except:
            pass

print("Results saved")