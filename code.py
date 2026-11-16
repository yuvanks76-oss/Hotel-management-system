patients = {}
next_id_number = 101


def generate_id():
    global next_id_number
    patient_id = f"P{next_id_number}"
    next_id_number += 1
    return patient_id


def format_patient(patient_id, record):
    return (f"{patient_id} | {record['name']} | {record['age']} | "
            f"{record['disease']} | {record['doctor']}")


def add_patient():
    name = input("Name: ").strip()
    if not name:
        print("Invalid name. Name cannot be empty. Patient not added.")
        return

    age_text = input("Age: ").strip()
    try:
        age = int(age_text)
    except ValueError:
        print("Invalid age. Enter a number between 0 and 120. Patient not added.")
        return
    if age < 0 or age > 120:
        print("Invalid age. Enter a number between 0 and 120. Patient not added.")
        return

    disease = input("Disease: ").strip()
    doctor = input("Doctor: ").strip()

    patient_id = generate_id()
    patients[patient_id] = {
        "name": name,
        "age": age,
        "disease": disease,
        "doctor": doctor,
    }
    print(f"Patient added. ID: {format_patient(patient_id, patients[patient_id])}")


def view_patients():
    if not patients:
        print("No patient records found.")
        return
    for patient_id, record in patients.items():
        print(format_patient(patient_id, record))


def search_patient():
    if not patients:
        print("No patient records found.")
        return
    patient_id = input("Enter Patient ID: ").strip().upper()
    if patient_id not in patients:
        print(f"Patient ID {patient_id} not found.")
        return
    print(format_patient(patient_id, patients[patient_id]))


def update_patient():
    if not patients:
        print("No patient records found.")
        return
    patient_id = input("Enter Patient ID: ").strip().upper()
    if patient_id not in patients:
        print(f"Patient ID {patient_id} not found.")
        return
    new_disease = input("New Disease: ").strip()
    if not new_disease:
        print("Disease cannot be empty. Patient not updated.")
        return
    patients[patient_id]["disease"] = new_disease
    print(f"Patient {patient_id} updated. Disease: {new_disease}")


def delete_patient():
    if not patients:
        print("No patient records found.")
        return
    patient_id = input("Enter Patient ID: ").strip().upper()
    if patient_id not in patients:
        print(f"Patient ID {patient_id} not found.")
        return
    del patients[patient_id]
    print(f"Patient {patient_id} deleted. Total patients: {len(patients)}")


def show_menu():
    print("\n===== Hospital Management System =====")
    print("1. Add Patient")
    print("2. View All Patients")
    print("3. Search Patient by ID")
    print("4. Update Patient")
    print("5. Delete Patient")
    print("6. Exit")


def main():
    actions = {
        "1": add_patient,
        "2": view_patients,
        "3": search_patient,
        "4": update_patient,
        "5": delete_patient,
    }
    while True:
        show_menu()
        try:
            choice = input("Enter your choice: ").strip()
        except EOFError:
            print("\nExiting.")
            break
        if choice == "6":
            print("Thank you. Exiting.")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid option. Please choose 1-6.")


if __name__ == "__main__":
    main()