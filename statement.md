# Project Statement: Student Grade Management System

## 1. Problem Definition
Educational institutions and instructors often struggle with the manual management of student records. Traditional paper-based methods or disconnected spreadsheets are prone to errors, difficult to update, and risk data loss. There is a need for a streamlined, digital solution to efficiently manage student details, academic performance, and grading logic in a centralized manner.

## 2. Proposed Solution
The **Student Grade Management System** is a Python-based command-line application designed to digitize the entire process of student record keeping. It allows administrators to perform essential operations (CRUD) while automating grade calculations and providing class-wide statistical insights.

## 3. Key Objectives
* **Automation:** Eliminate manual grade calculation errors by implementing a standard grading algorithm.
* **Efficiency:** Provide quick search and retrieval mechanisms for specific student records.
* **Persistence:** Ensure data integrity by saving records to a local storage file (`.json`), preventing data loss between sessions.
* **Analysis:** Offer immediate insight into class performance through statistical summaries (averages, pass percentages).

## 4. Functional Requirements
The system is built to handle the following core functions:

### A. Student Management
* **Registration:** Add new students with validation to prevent duplicate Roll Numbers.
* **Modification:** Update existing marks, which automatically triggers a re-calculation of the student's grade.
* **Deletion:** Remove obsolete records securely with user confirmation.

### B. Academic Processing
* **Auto-Grading:** Automatically maps numerical marks (0-100) to letter grades (A+ to F) based on predefined thresholds.
* **Validation:** Ensures input integrity (e.g., marks cannot exceed 100 or be negative).

### C. Reporting & Persistence
* **View & Search:** Display all students in a formatted table or search individually by unique Roll Number.
* **Statistics:** Calculate and display the Class Average, Highest/Lowest scores, and Pass Percentage.
* **Data Storage:** Automatically load data on startup and save data to a text file upon exit.

## 5. Technology Stack
* **Language:** Python 3.x
* **Data Storage:** JSON (JavaScript Object Notation) for lightweight, structured file storage.
* **Interface:** CLI (Command Line Interface) for ease of use and minimal resource consumption.

## 6. Scope
This project is currently designed as a standalone desktop utility. Future iterations may include graphical user interfaces (GUI), multi-subject support, and database integration (SQL).
