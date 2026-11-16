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