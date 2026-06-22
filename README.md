# 🏥 Hospital Management System

A simple Python CLI app to manage hospital patient records. All data is saved in a `data.json` file so records stay even after closing the program.

## Features

- Register new patients (name, age, disease, doctor)
- View all patient records in a numbered list
- Search for a patient by name
- Update patient status — Admitted, Under Treatment, or Discharged
- Delete a patient record
- Input validation on all fields

## How to Run

```bash
git clone https://github.com/thesohailahmad/hospital-management-system.git
cd hospital-management-system
hospital_mangment_system.py
```

No extra libraries needed — only Python built-ins (`json`, `os`).

## Project Structure

```
hospital-management-system/
├── main.py       # Main application
├── data.json     # Patient data (auto-created on first run)
└── README.md
```

## Concepts Used

- Functions, loops, and conditionals
- Dictionaries and lists
- JSON file handling for persistent storage
- Input validation and error handling

## Author

**Sohail Ahmad** — [github.com/thesohailahmad](https://github.com/thesohailahmad)
