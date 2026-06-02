# Smart Campus Information System
# Simple Integrated Mini Project

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

students = []

# -------------------------------
# 1. Student Registration
# -------------------------------
def register_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    marks = int(input("Enter Marks: "))

    # Grade Calculation
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "F"

    student = {
        "name": name,
        "age": age,
        "marks": marks,
        "grade": grade
    }

    students.append(student)
    print("Student Added Successfully")

# -------------------------------
# 2. Display Student Records
# -------------------------------
def display_students():
    print("\n--- Student Records ---")

    if not students:
        print("No records found.")
    else:
        for s in students:
            print(s)

# -------------------------------
# 3. Course Enrollment
# -------------------------------
def enroll_course():
    courses = []

    while True:
        course = input("Enter Course Name (done to stop): ")

        if course.lower() == "done":
            break

        credits = int(input("Enter Credits: "))
        courses.append((course, credits))

    print("\nCourses Enrolled:")
    print(courses)

# -------------------------------
# 4. Sorting and Searching
# -------------------------------
def search_sort():
    ids = [105, 102, 110, 101]

    print("Original IDs:", ids)

    ids.sort()

    print("Sorted IDs:", ids)

    search = int(input("Enter ID to Search: "))

    if search in ids:
        print("ID Found")
    else:
        print("ID Not Found")

# -------------------------------
# 5. Fee Calculation
# -------------------------------
def calculate_fee():
    tuition = int(input("Enter Tuition Fee: "))
    hostel = int(input("Enter Hostel Fee: "))
    transport = int(input("Enter Transport Fee: "))

    total = tuition + hostel + transport

    print("Total Fee =", total)

# -------------------------------
# 6. File Handling
# -------------------------------
def file_handling():
    file = open("students.txt", "w")

    for s in students:
        file.write(s["name"] + " " + str(s["marks"]) + "\n")

    file.close()

    print("Data Written to File")

    file = open("students.txt", "r")

    print("\nFile Data:")
    print(file.read())

    file.close()

# -------------------------------
# 7. Directory Scanning
# -------------------------------
def scan_directory():
    path = input("Enter Folder Path: ")

    try:
        files = os.listdir(path)

        print("\nFiles in Folder:")
        for f in files:
            print(f)

    except:
        print("Invalid Folder Path")

# -------------------------------
# 8. Performance Analysis
# -------------------------------
def performance_analysis():
    if not students:
        print("No student data available.")
        return

    names = []
    marks = []

    for s in students:
        names.append(s["name"])
        marks.append(s["marks"])

    arr = np.array(marks)

    print("Average Marks =", np.mean(arr))
    print("Highest Marks =", np.max(arr))

    df = pd.DataFrame({
        "Name": names,
        "Marks": marks
    })

    print("\nStudent Data")
    print(df)

    plt.bar(names, marks)
    plt.title("Student Performance")
    plt.xlabel("Students")
    plt.ylabel("Marks")
    plt.show()

# -------------------------------
# Main Program
# -------------------------------
while True:

    print("\n===== SMART CAMPUS SYSTEM =====")
    print("1. Register Student")
    print("2. Display Students")
    print("3. Course Enrollment")
    print("4. Search and Sort")
    print("5. Fee Calculation")
    print("6. File Handling")
    print("7. Directory Scan")
    print("8. Performance Analysis")
    print("9. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        register_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        enroll_course()

    elif choice == "4":
        search_sort()

    elif choice == "5":
        calculate_fee()

    elif choice == "6":
        file_handling()

    elif choice == "7":
        scan_directory()

    elif choice == "8":
        performance_analysis()

    elif choice == "9":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")