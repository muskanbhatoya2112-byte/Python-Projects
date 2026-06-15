# Contact Management System

contacts = {
    "Muskan": "9876543210",
    "Jasmeen": "9876543211"
}


contacts["Sannya"] = "9876543210"
print("After Adding:", contacts)


name = "Muskan"
print("Searched Number:", contacts[name])


contacts["Muskan"] = "9999999999"
print("After Updating:", contacts)


del contacts["Muskan"]
print("After Deleting:", contacts)


numbers = ["9999999999", "9876543211", "9999999999"]
unique_numbers = set(numbers)

print("Unique Numbers:", unique_numbers)