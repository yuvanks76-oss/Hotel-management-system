# Hospital Management System

A menu-driven Python console application to manage hospital patient records (add, view, search, update, delete). Data is kept in memory while the program runs.

**Rungta International Skills University, School of Computer Science and Engineering. PS No. 62**

## Repository Contents

| File | Description |
|------|-------------|
| `one.py` | Main project file (the complete program) |
| `README.md` | Describes this repository |
| `summary.md` | Project summary and test case screenshots |
| `screenshots/` | Screenshots of the four test cases |

## Features

- Add a patient with Name, Age, Disease and Doctor
- Patient IDs are generated automatically: P101, P102, P103, ...
- View all patients
- Search a patient by ID
- Update a patient's disease
- Delete a patient
- Input validation: name must not be empty, age must be a number from 0 to 120
- Clear messages when an ID is not found or there are no records

## Requirements

- Python 3.x (no external libraries)

## How to Run

```bash
git clone https://github.com/<your-username>/hospital-management-system.git
cd hospital-management-system
python one.py
```

## Menu

```
1. Add Patient
2. View All Patients
3. Search Patient by ID
4. Update Patient
5. Delete Patient
6. Exit
```

## Design

- Each patient is a dictionary: `{"name", "age", "disease", "doctor"}`
- All patients are stored in one main dictionary keyed by patient ID
- Separate functions handle each operation: `add_patient()`, `view_patients()`, `search_patient()`, `update_patient()`, `delete_patient()`

TEST CASE - 01
<img width="370" height="84" alt="testcase1" src="https://github.com/user-attachments/assets/88b4a833-6a2f-4587-b658-13cf774c1b3c" />
TEST CASE - 02
<img width="348" height="90" alt="test case 2" src="https://github.com/user-attachments/assets/d3623423-af4f-4eef-95ae-0ec69f3665c7" />
TEST CASE 3
<img width="376" height="63" alt="test case 3" src="https://github.com/user-attachments/assets/077e2075-be43-4beb-9c28-b6f8830de4f6" />
TEST CASE - 04
<img width="265" height="68" alt="test case 4 a" src="https://github.com/user-attachments/assets/94ab2c16-3ee9-424a-a4fe-be7987c09394" />
<img width="244" height="48" alt="TEST CASE 4 B" src="https://github.com/user-attachments/assets/4a472acb-7a1c-40be-81b0-e7bd0bfab475" />
<img width="237" height="42" alt="TEST CASE 4 C" src="https://github.com/user-attachments/assets/1b552c9b-66aa-4116-8839-c7ea67be6c44" />





