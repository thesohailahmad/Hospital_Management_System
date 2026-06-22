import json
import os
# Hospital managment system 
#include storage of  patient data
# by the use of file handling 

print("---Welcome to Hospital managment system---")
patients = []
#  This Function save patient data

def save_patient_data():
    with open("data.json", "w") as file:
        json.dump(patients, file)
#  This Function load patient data

def load_patient_data():
    global patients
    if os.path.exists("data.json"):
        with open("data.json", "r") as file:
            patients = json.load(file)
# This Function show menu to the user 
#syntax use 
#functions
#loops
#conditions
def view_menu():
    while True:
        print("1- Register New Patient")
        print("2- View Patient Data")
        print("3- Search Patient by name")
        print("4- Update Patient Status")
        print("5- Delete Patient Data")
        print("6- Exit")
        user = input(" Please enter your number: ")
        if user == "1":
            register_patient() 
        elif user == "2":
            view_data()
        elif user == "3":
            search_patient() 
        elif user == "4":
            update_status()
        elif user == "5":
            delete_patient()
        elif user == "6":
            print("You Exit Successfully...")
            break
        else:
            print("∆Invalid Number please enter valid name")
# This Function store data of patient 
#syntax use 
#functions
#Error hanndling 
#dictionary
#list methods
#conditions
def register_patient():
    
    patient_name = input("Please enter the name of patient: ").capitalize()
    if patient_name == "" or not patient_name.replace(" ", "").isalpha():
        print("∆Invalid name!! Please enter a valid name..")
        return

    
    patient_age = input("Please enter the age of patient: ")
    if not patient_age.isdigit():
        print("∆Invalid age!! Please enter a valid number..")
        return
    if int(patient_age) < 1 or int(patient_age) > 120:
        print("∆Invalid age!! Age must be between 1 and 120..")
        return

    
    patient_disease = input("Please enter the Disease: ").capitalize()
    if patient_disease == "" or not patient_disease.replace(" ", "").isalpha():
        print("∆Invalid disease!! Please enter a valid disease name..")
        return

    
    patient_doctor = input("Enter the Doctor name of patient: ").capitalize()
    if patient_doctor == "" or not patient_doctor.replace(" ", "").isalpha():
        print("∆Invalid doctor name!! Please enter a valid name..")
        return

    data = {
        "Name": patient_name,
        "Age": patient_age,
        "Disease": patient_disease,
        "Doctor Name":patient_doctor,
        "Status":"Admitted"
    } 
    patients.append(data)
    save_patient_data()
    print("Your Patient data added Successfully!!")            
# This Function for showing data with numbers
#syntax use 
#functions
#Enumerate function
#len()method
#conditions
def view_data():
    if len(patients) == 0:
        print("No Data yet!!")
    else:
        for number, item in enumerate(patients, 1):
             print(number, item["Name"],":",item["Age"],":",item["Disease"],":",item["Doctor Name"],":",item["Status"] )

# This Function for searching patient 
#syntax use 
#functions
#loops
#len()method
#conditions
#error handling
def search_patient():
    if len(patients) == 0:
        print("No information of patient add yet..")
        return
    search = input ("Please Enter the name of Patient: ").capitalize()
    found = False
    for item in patients:
        if item["Name"] == search:
         print("Name:" ,item["Name"])
         print("Age:" , item["Age"])
         print("Disease:" , item["Disease"])
         print("Doctor Name:" , item["Doctor Name"])
         print("Status:" , item["Status"])
         found = True
    if found == False:
        print("Patient not found")
 #This Function for updating status of patient
#syntax use 
#functions
#loops
#len()method
#conditions
#error handling
#enumerate function
def update_status():
    if len(patients) == 0:
        print("No Data yet!!")
        return
    for number, item in enumerate(patients, 1):
        print(number, item["Name"], ":", item["Status"])
    choice = input("Enter patient number to update status: ")
    if not choice.isdigit():
        print("∆Invalid input. Please enter a number..")
        return
    index = int(choice) - 1
    if index < 0 or index >= len(patients):
        print("∆Patient number not found..")
        return
    print("1. Admitted")
    print("2. Under Treatment")
    print("3. Discharged")
    status_choice = input("Enter status number: ")
    if status_choice == "1":
        patients[index]["Status"] = "Admitted"
    elif status_choice == "2":
        patients[index]["Status"] = "Under Treatment"
    elif status_choice == "3":
        patients[index]["Status"] = "Discharged"
    else:
        print("∆Invalid choice!!")
        return
    save_patient_data()    
    print("Status updated successfully!!")
#This Function for deleting data of patient
#syntax use 
#functions
#loops
#len()method
#conditions
#error handling
#enumerate function
def delete_patient():
    if len(patients) == 0:
        print("No Data yet!!")
        return
    for number, item in enumerate(patients, 1):
        print(number, item["Name"], ":", item["Status"])
    choice = input("Enter patient number to delete: ")
    if not choice.isdigit():
        print("∆Invalid input. Please enter a number..")
        return
    index = int(choice) - 1
    if index < 0 or index >= len(patients):
        print("∆Patient number not found..")
        return
    patient_name = patients[index]["Name"]
    patients.pop(index)
    save_patient_data()
    print(f"{patient_name} record deleted successfully!!")    

load_patient_data()
view_menu() 




