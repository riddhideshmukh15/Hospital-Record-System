print("===== WELCOME TO HOSPITAL RECORD SYSTEM =====")

hospital_records = {}

while True:
    print("\n1. Add Patient Name")
    print("2. Add Disease Name")
    print("3. Add Doctor Name")
    print("4. Add Patient Mobile Number")
    print("5. Add Patient Address")
    print("6. View Patient Record")
    print("7. Update Record")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

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

        if len(mobile) == 10 and mobile.isdigit():
            hospital_records["mobile"] = mobile
            print("Mobile number added successfully!")
        else:
            print("Enter a valid 10-digit mobile number!")

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
        if hospital_records:
            print("\n===== UPDATE PATIENT RECORD =====")
            print("1. Update Name")
            print("2. Update Disease")
            print("3. Update Doctor")
            print("4. Update Mobile Number")
            print("5. Update Address")

            update_choice = input("Choose field to update (1-5): ")

            if update_choice == "1":
                new_name = input("Enter new patient name: ")
                hospital_records["name"] = new_name
                print("Patient name updated successfully!")

            elif update_choice == "2":
                new_disease = input("Enter new disease: ")
                hospital_records["disease"] = new_disease
                print("Disease updated successfully!")

            elif update_choice == "3":
                new_doctor = input("Enter new doctor's name: ")
                hospital_records["doctor"] = new_doctor
                print("Doctor name updated successfully!")

            elif update_choice == "4":
                new_mobile = input("Enter new mobile number: ")

                if len(new_mobile) == 10 and new_mobile.isdigit():
                    hospital_records["mobile"] = new_mobile
                    print("Mobile number updated successfully!")
                else:
                    print("Invalid mobile number!")

            elif update_choice == "5":
                new_address = input("Enter new address: ")
                hospital_records["address"] = new_address
                print("Address updated successfully!")

            else:
                print("Invalid update choice!")

        else:
            print("No patient record found. Add patient details first.")

    elif choice == "8":
        print("Thanks for using our hospital record system!")
        break

    else:
        print("Invalid choice! Try again.")