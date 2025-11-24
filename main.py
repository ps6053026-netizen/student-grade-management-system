"""
Student Grade Management System
Simple version - All code in one file
Author: [Your Name]
"""

import json
import os

# Global list to store students
students = []

def clear_screen():
    """Clear console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate_grade(marks):
    """Calculate grade based on marks"""
    if marks >= 90:
        return 'A+'
    elif marks >= 80:
        return 'A'
    elif marks >= 70:
        return 'B+'
    elif marks >= 60:
        return 'B'
    elif marks >= 50:
        return 'C'
    elif marks >= 40:
        return 'D'
    else:
        return 'F'

def add_student():
    """Add a new student"""
    print("\n--- Add New Student ---")
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    
    # Check if roll number already exists
    for student in students:
        if student['roll_no'] == roll_no:
            print(f"Error: Roll number {roll_no} already exists!")
            return
    
    try:
        marks = float(input("Enter marks (0-100): "))
        if marks < 0 or marks > 100:
            print("Error: Marks must be between 0 and 100!")
            return
    except ValueError:
        print("Error: Please enter valid marks!")
        return
    
    subject = input("Enter subject name: ")
    grade = calculate_grade(marks)
    
    student = {
        'name': name,
        'roll_no': roll_no,
        'marks': marks,
        'subject': subject,
        'grade': grade
    }
    
    students.append(student)
    print(f"\nSuccess! Student {name} added with grade {grade}")

def view_all_students():
    """Display all students"""
    print("\n--- All Students ---")
    if not students:
        print("No students in the system yet!")
        return
    
    print(f"{'Name':<20} {'Roll No':<12} {'Subject':<15} {'Marks':<8} {'Grade':<5}")
    print("-" * 70)
    
    for student in students:
        print(f"{student['name']:<20} {student['roll_no']:<12} {student['subject']:<15} {student['marks']:<8.2f} {student['grade']:<5}")

def search_student():
    """Search for a student by roll number"""
    print("\n--- Search Student ---")
    roll_no = input("Enter roll number to search: ")
    
    for student in students:
        if student['roll_no'] == roll_no:
            print("\nStudent Found:")
            print(f"Name: {student['name']}")
            print(f"Roll No: {student['roll_no']}")
            print(f"Subject: {student['subject']}")
            print(f"Marks: {student['marks']}")
            print(f"Grade: {student['grade']}")
            return
    
    print(f"No student found with roll number: {roll_no}")

def update_marks():
    """Update student marks"""
    print("\n--- Update Student Marks ---")
    roll_no = input("Enter roll number: ")
    
    for student in students:
        if student['roll_no'] == roll_no:
            try:
                new_marks = float(input("Enter new marks (0-100): "))
                if new_marks < 0 or new_marks > 100:
                    print("Error: Marks must be between 0 and 100!")
                    return
            except ValueError:
                print("Error: Please enter valid marks!")
                return
            
            student['marks'] = new_marks
            student['grade'] = calculate_grade(new_marks)
            print(f"\nSuccess! Updated marks to {new_marks} (Grade: {student['grade']})")
            return
    
    print(f"No student found with roll number: {roll_no}")

def delete_student():
    """Delete a student"""
    print("\n--- Delete Student ---")
    roll_no = input("Enter roll number to delete: ")
    
    for i, student in enumerate(students):
        if student['roll_no'] == roll_no:
            confirm = input(f"Delete {student['name']}? (yes/no): ")
            if confirm.lower() == 'yes':
                students.pop(i)
                print("Student deleted successfully!")
            else:
                print("Deletion cancelled.")
            return
    
    print(f"No student found with roll number: {roll_no}")

def show_statistics():
    """Calculate and display class statistics"""
    print("\n--- Class Statistics ---")
    if not students:
        print("No students in the system yet!")
        return
    
    marks_list = [s['marks'] for s in students]
    pass_count = sum(1 for m in marks_list if m >= 40)
    
    print(f"Total Students: {len(students)}")
    print(f"Average Marks: {sum(marks_list) / len(marks_list):.2f}")
    print(f"Highest Marks: {max(marks_list)}")
    print(f"Lowest Marks: {min(marks_list)}")
    print(f"Pass Percentage: {(pass_count / len(students)) * 100:.2f}%")

def save_data():
    """Save student data to file"""
    try:
        with open('students_data.txt', 'w') as file:
            json.dump(students, file, indent=4)
        return True
    except Exception as e:
        print(f"Error saving data: {e}")
        return False

def load_data():
    """Load student data from file"""
    global students
    if os.path.exists('students_data.txt'):
        try:
            with open('students_data.txt', 'r') as file:
                students = json.load(file)
        except:
            students = []

def display_menu():
    """Display main menu"""
    print("\n" + "="*50)
    print("   STUDENT GRADE MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add New Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Show Class Statistics")
    print("7. Save and Exit")
    print("="*50)

def main():
    """Main program"""
    load_data()
    print("\nWelcome to Student Grade Management System!")
    print(f"Loaded {len(students)} existing records.")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_all_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_marks()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            show_statistics()
        elif choice == '7':
            print("\nSaving data...")
            save_data()
            print("Data saved! Thank you for using the system!")
            break
        else:
            print("Invalid choice! Please enter 1-7.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
