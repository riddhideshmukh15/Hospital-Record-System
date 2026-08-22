print("===== WELCOME TO HOSPITAL RECORD SYSTEM =====")

hospital_records = {}

while True:
    print("\n1. Add Patient Name")
    print("2. Add Disease Name")
    print("3. Add Doctor Name")
    print("4. Add Patient Mobile Number")
    print("5. Add Patient Address")
    print("6. View Patient Record")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        name = input("Enter patient name: ")
        hospital_records["name"] = name
        print(f"{name} added successfully!")

    elif choice == "2":
        disease = input("Enter disease name: ")
        hospital_records["disease"] = disease
        print(f"{disease} added successfully!")

    elif choice == "3":
        doctor = input("Enter doctor's name: ")
        hospital_records["doctor"] = doctor
        print(f"{doctor} added successfully!")

    elif choice == "4":
        mobile = input("Enter patient mobile number: ")
        hospital_records["mobile"] = mobile
        print("Mobile number added successfully!")

    elif choice == "5":
        address = input("Enter patient's address: ")
        hospital_records["address"] = address
        print("Address added successfully!")

    elif choice == "6":
        print("\n===== PATIENT RECORD =====")

        if hospital_records:
            for key, value in hospital_records.items():
                print(f"{key.title()}: {value}")
        else:
            print("No patient record found.")

    elif choice == "7":
        print("Thanks for using our hospital record system!")
        break

    else:
        print("Invalid choice! Try again.")