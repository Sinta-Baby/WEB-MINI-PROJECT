# Canine Care Recommendation Web Application

A Django-based web application that provides **personalized canine care and nutrition recommendations** using a **Random Forest Machine Learning model**.

This project is developed as a **college mini-project** and is also suitable for **resume and internship evaluation**.

---

## Project Overview

The Canine Care Web Application helps dog owners by suggesting proper care and nutrition based on dog-related inputs such as:
- Breed
- Age
- Health-related parameters

The backend uses a **trained Random Forest model** to generate predictions, which are displayed through a web-based interface.

---

##  Objectives

- To integrate **Machine Learning with Web Development**
- To provide data-driven canine care recommendations
- To understand real-world ML model deployment using Django

---

##  Technologies Used

- **Programming Language:** Python  
- **Web Framework:** Django  
- **Frontend:** HTML, CSS, JavaScript, Bootstrap  
- **Machine Learning:** Scikit-learn (Random Forest Algorithm)  
- **Database:** SQLite  
- **Version Control:** Git & GitHub  
- **Large File Handling:** Git Large File Storage (Git LFS)

---

##  Key Features

- User-friendly web interface
- Machine learning–based recommendations
- Backend integration of trained ML model
- Admin panel for managing data
- Clean and modular project structure

---

##  Machine Learning Model Details

- **Algorithm Used:** Random Forest Classifier  
- **Reason for Selection:**  
  - Handles complex data well  
  - Reduces overfitting compared to single decision trees  
  - Provides better accuracy and robustness  

###  Model Files
Due to large file size, trained ML models are stored using **Git LFS**:
- `random_forest_model.joblib`
- `encoder.joblib`

---

##  How the System Works

1. User provides dog-related input through the web interface  
2. Input data is preprocessed and encoded  
3. The trained Random Forest model makes predictions  
4. Care and nutrition recommendations are displayed to the user  

---

## How to Run the Project Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Sinta-Baby/WEB-MINI-PROJECT.git
cd WEB-MINI-PROJECT

