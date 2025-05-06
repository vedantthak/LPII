class MedicalExpertSystem:
    def __init__(self):
        self.rules = {
            "Flu": {
                "symptoms": ["fever", "cough", "sore throat", "fatigue", "body ache"],
                "treatment": "Rest, hydration, over-the-counter medications."
            },
            "COVID-19": {
                "symptoms": ["fever", "cough", "shortness of breath", "loss of taste", "loss of smell"],
                "treatment": "Isolation, oxygen support if severe, antiviral medications."
            },
            "Diabetes": {
                "symptoms": ["frequent urination", "excessive thirst", "fatigue", "blurry vision"],
                "treatment": "Lifestyle changes, insulin or oral medications."
            },
            "Hypertension": {
                "symptoms": ["headache", "dizziness", "chest pain", "shortness of breath"],
                "treatment": "Low-sodium diet, blood pressure medications."
            },
            "Migraine": {
                "symptoms": ["headache", "nausea", "sensitivity to light", "blurred vision"],
                "treatment": "Pain relief medications, rest in a dark room."
            }
        }
        
        self.resources = {
            "beds_available": 5,
            "doctors_available": 3
        }
        
        self.patient_history = {}  # Stores patient records

    def diagnose(self, symptoms):
        """Diagnose possible conditions based on symptoms."""
        scores = {disease: 0 for disease in self.rules}
        
        for disease, details in self.rules.items():
            scores[disease] = sum(1 for symptom in symptoms if symptom in details["symptoms"])
        
        best_match = max(scores, key=scores.get)
        if scores[best_match] > 0:
            return best_match, self.rules[best_match]["treatment"]
        else:
            return "Unknown Condition", "Consult a doctor for further diagnosis."

    def check_resources(self):
        """Check hospital resource availability."""
        return f"Beds Available: {self.resources['beds_available']}, Doctors Available: {self.resources['doctors_available']}"

    def emergency_alert(self, symptoms):
        """Trigger emergency alert for critical symptoms."""
        critical_conditions = ["chest pain", "shortness of breath", "severe headache"]
        if any(symptom in critical_conditions for symptom in symptoms):
            return " EMERGENCY ALERT! Immediate medical attention needed!"
        return "No emergency detected."

    def store_patient_history(self, name, symptoms, diagnosis, treatment):
        """Store patient history."""
        if name in self.patient_history:
            self.patient_history[name].append({"Symptoms": symptoms, "Diagnosis": diagnosis, "Treatment": treatment})
        else:
            self.patient_history[name] = [{"Symptoms": symptoms, "Diagnosis": diagnosis, "Treatment": treatment}]
        print(f" Patient history updated for {name}.")

    def get_patient_history(self, name):
        """Retrieve patient history."""
        if name in self.patient_history:
            print(f"\n Patient History for {name}:")
            for i, record in enumerate(self.patient_history[name], 1):
                print(f"\nRecord {i}:")
                print(f"Symptoms: {', '.join(record['Symptoms'])}")
                print(f"Diagnosis: {record['Diagnosis']}")
                print(f"Treatment: {record['Treatment']}")
        else:
            print(f"\n No history found for {name}.")

# Initialize the expert system
medical_system = MedicalExpertSystem()

while True:
    print("\n--- Medical Expert System ---")
    print("1. Diagnose a patient")
    print("2. View patient history")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        patient_name = input("Enter patient name: ")
        symptoms_input = input("Enter symptoms separated by commas: ").lower().split(", ")

        diagnosis, treatment = medical_system.diagnose(symptoms_input)
        resources_status = medical_system.check_resources()
        emergency_status = medical_system.emergency_alert(symptoms_input)

        # Store patient history
        medical_system.store_patient_history(patient_name, symptoms_input, diagnosis, treatment)

        # Display results
        print(f"\nPossible Diagnosis: {diagnosis}")
        print(f"Suggested Treatment: {treatment}")
        print(f"{resources_status}")
        print(f"{emergency_status}")

    elif choice == "2":
        name = input("Enter patient name to view history: ")
        medical_system.get_patient_history(name)

    elif choice == "3":
        print("Exiting the system. Stay healthy!")
        break  # Exit the loop

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")










# Let’s go through your Medical Expert System code line-by-line with detailed explanations:

# ✅ Class and Constructor
# python
# Copy
# Edit
# class MedicalExpertSystem:
# Declares a class to encapsulate all logic related to the medical expert system.

# python
# Copy
# Edit
#     def __init__(self):
# Initializes the class object. This constructor sets up rules, resources, and history.

# python
# Copy
# Edit
#         self.rules = {
# A dictionary of known diseases, each mapping to:

# a list of symptoms

# recommended treatment

# Example:

# python
# Copy
# Edit
# "Flu": {
#     "symptoms": ["fever", "cough", "sore throat", "fatigue", "body ache"],
#     "treatment": "Rest, hydration, over-the-counter medications."
# }
# python
# Copy
# Edit
#         self.resources = {
#             "beds_available": 5,
#             "doctors_available": 3
#         }
# Tracks hospital resource availability like beds and doctors.

# python
# Copy
# Edit
#         self.patient_history = {}  # Stores patient records
# Initializes a dictionary to store patient history (name → list of visits).

# 🧠 Diagnosis Logic
# python
# Copy
# Edit
#     def diagnose(self, symptoms):
# Accepts a list of patient symptoms and attempts to diagnose a disease.

# python
# Copy
# Edit
#         scores = {disease: 0 for disease in self.rules}
# Initializes a score for each disease to 0.

# python
# Copy
# Edit
#         for disease, details in self.rules.items():
#             scores[disease] = sum(1 for symptom in symptoms if symptom in details["symptoms"])
# For each disease, increase the score based on how many input symptoms match known symptoms.

# python
# Copy
# Edit
#         best_match = max(scores, key=scores.get)
# Finds the disease with the highest matching score.

# python
# Copy
# Edit
#         if scores[best_match] > 0:
#             return best_match, self.rules[best_match]["treatment"]
# If the match score is non-zero, return the diagnosis and its treatment.

# python
# Copy
# Edit
#         else:
#             return "Unknown Condition", "Consult a doctor for further diagnosis."
# If nothing matched, return a generic result.

# 🏥 Hospital Resource Check
# python
# Copy
# Edit
#     def check_resources(self):
#         return f"Beds Available: {self.resources['beds_available']}, Doctors Available: {self.resources['doctors_available']}"
# Simple status of how many beds/doctors are available.

# 🚨 Emergency Alert Detection
# python
# Copy
# Edit
#     def emergency_alert(self, symptoms):
#         critical_conditions = ["chest pain", "shortness of breath", "severe headache"]
# Critical symptoms that require immediate medical help.

# python
# Copy
# Edit
#         if any(symptom in critical_conditions for symptom in symptoms):
#             return " EMERGENCY ALERT! Immediate medical attention needed!"
#         return "No emergency detected."
# If any critical symptom is detected, trigger an alert.

# 🧾 Store Patient History
# python
# Copy
# Edit
#     def store_patient_history(self, name, symptoms, diagnosis, treatment):
# Stores a patient's visit including symptoms, diagnosis, and treatment.

# python
# Copy
# Edit
#         if name in self.patient_history:
#             self.patient_history[name].append(...)
#         else:
#             self.patient_history[name] = [...]
# Appends to existing history or initializes a new list.

# python
# Copy
# Edit
#         print(f" Patient history updated for {name}.")
# Confirmation message.

# 📜 Get Patient History
# python
# Copy
# Edit
#     def get_patient_history(self, name):
# Retrieves a patient's medical history.

# python
# Copy
# Edit
#         if name in self.patient_history:
# If history exists for the given patient:

# python
# Copy
# Edit
#             for i, record in enumerate(self.patient_history[name], 1):
# Iterate through the records and display each:

# python
# Copy
# Edit
#                 print(f"Symptoms: {', '.join(record['Symptoms'])}")
#                 print(f"Diagnosis: {record['Diagnosis']}")
#                 print(f"Treatment: {record['Treatment']}")
# Formats the stored information for output.

# python
# Copy
# Edit
#         else:
#             print(f"\n No history found for {name}.")
# No record case.

# 🔁 Main Menu Loop
# python
# Copy
# Edit
# # Initialize the expert system
# medical_system = MedicalExpertSystem()
# Creates an instance of the expert system.

# python
# Copy
# Edit
# while True:
# Infinite loop to interact with user until they choose to exit.

# python
# Copy
# Edit
#     print("1. Diagnose a patient")
#     print("2. View patient history")
#     print("3. Exit")
# Displays menu options.

# python
# Copy
# Edit
#     choice = input("Enter your choice: ")
# Takes the user’s input.

# 🩺 Diagnose a Patient
# python
# Copy
# Edit
#     if choice == "1":
# Starts diagnosis process.

# python
# Copy
# Edit
#         patient_name = input("Enter patient name: ")
#         symptoms_input = input("Enter symptoms separated by commas: ").lower().split(", ")
# Gets patient name and symptoms, converts to lowercase and splits by ", ".

# python
# Copy
# Edit
#         diagnosis, treatment = medical_system.diagnose(symptoms_input)
# Calls the diagnosis function.

# python
# Copy
# Edit
#         resources_status = medical_system.check_resources()
#         emergency_status = medical_system.emergency_alert(symptoms_input)
# Fetches resource availability and checks for emergencies.

# python
# Copy
# Edit
#         medical_system.store_patient_history(patient_name, symptoms_input, diagnosis, treatment)
# Saves the data in history.

# python
# Copy
# Edit
#         print(f"\nPossible Diagnosis: {diagnosis}")
#         print(f"Suggested Treatment: {treatment}")
#         print(f"{resources_status}")
#         print(f"{emergency_status}")
# Prints all results.

# 📖 View History
# python
# Copy
# Edit
#     elif choice == "2":
#         name = input("Enter patient name to view history: ")
#         medical_system.get_patient_history(name)
# ❌ Exit
# python
# Copy
# Edit
#     elif choice == "3":
#         print("Exiting the system. Stay healthy!")
#         break
# ⚠️ Invalid Choice
# python
# Copy
# Edit
#     else:
#         print("Invalid choice! Please enter 1, 2, or 3.")
# Would you like a dry run of this system using sample input?







# You said:
# give dry run


# ChatGPT said:
# Sure! Here's a dry run of your Medical Expert System code with sample input and a step-by-step walkthrough.

# 🔹 Sample Input
# Let's assume this user interaction:

# pgsql
# Copy
# Edit
# --- Medical Expert System ---
# 1. Diagnose a patient
# Enter your choice: 1
# Enter patient name: John
# Enter symptoms separated by commas: fever, cough, sore throat

# --- Medical Expert System ---
# 2. View patient history
# Enter your choice: 2
# Enter patient name to view history: John

# --- Medical Expert System ---
# 3. Exit
# Enter your choice: 3
# 🔸 Step-by-Step Execution
# ✅ Step 1: Initialization
# python
# Copy
# Edit
# medical_system = MedicalExpertSystem()
# rules, resources, and patient_history are initialized.

# beds_available = 5, doctors_available = 3

# ✅ Step 2: Diagnose John with ["fever", "cough", "sore throat"]
# python
# Copy
# Edit
# symptoms_input = ["fever", "cough", "sore throat"]
# ➤ Inside diagnose():
# scores initialized to {Flu: 0, COVID-19: 0, Diabetes: 0, Hypertension: 0, Migraine: 0}

# Now it calculates how many symptoms match each disease:

# Flu → matches fever, cough, sore throat → score = 3 ✅

# COVID-19 → matches fever, cough → score = 2

# Others → no matches or 0–1

# Best match: "Flu"
# Treatment: "Rest, hydration, over-the-counter medications."

# ➤ Check Resources:
# python
# Copy
# Edit
# "Beds Available: 5, Doctors Available: 3"
# ➤ Emergency Alert:
# Check for "chest pain", "shortness of breath", "severe headache"
# → None matched → "No emergency detected."

# ➤ Store History:
# python
# Copy
# Edit
# self.patient_history = {
#     "John": [
#         {
#             "Symptoms": ["fever", "cough", "sore throat"],
#             "Diagnosis": "Flu",
#             "Treatment": "Rest, hydration, over-the-counter medications."
#         }
#     ]
# }
# ➤ Output:
# yaml
# Copy
# Edit
# Possible Diagnosis: Flu
# Suggested Treatment: Rest, hydration, over-the-counter medications.
# Beds Available: 5, Doctors Available: 3
# No emergency detected.
# ✅ Step 3: View Patient History
# User inputs: John

# Inside get_patient_history():

# python
# Copy
# Edit
# for i, record in enumerate(patient_history["John"], 1):
# Output:

# yaml
# Copy
# Edit
# Patient History for John:

# Record 1:
# Symptoms: fever, cough, sore throat
# Diagnosis: Flu
# Treatment: Rest, hydration, over-the-counter medications.
# ✅ Step 4: Exit
# nginx
# Copy
# Edit
# Exiting the system. Stay healthy!
# Would you like this system to also handle multiple diagnoses (e.g., show all possible diseases ranked)?


# Viva Questions and Answers (Short)
# Q: What is the purpose of this system?
# A: To diagnose possible diseases based on symptoms and manage patient history and resource availability.

# Q: How does the system diagnose a disease?
# A: It compares input symptoms with predefined disease symptoms and picks the one with the highest match.

# Q: How are symptoms matched to diseases?
# A: Using a score system that counts the number of matching symptoms for each disease.

# Q: What happens if no symptoms match any disease?
# A: The system returns "Unknown Condition" and suggests consulting a doctor.

# Q: How are emergency cases handled?
# A: The system checks for critical symptoms like "chest pain" or "shortness of breath" and triggers an emergency alert.

# Q: What information is stored in patient history?
# A: Symptoms, diagnosis, and treatment are stored for each patient under their name.

# Q: How does the system handle multiple records for the same patient?
# A: It appends new records to the existing list under the patient’s name.

# Q: What is the use of check_resources()?
# A: It returns the number of beds and doctors available in the hospital.

# Q: Can a user retrieve their past medical data?
# A: Yes, using the "View patient history" option with the patient’s name.

# Q: What data structures are used in this system?
# A: Dictionaries (for rules and history) and lists (for symptoms and records).