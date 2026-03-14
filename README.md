# 🚀 ChurnSense.AI

**Automated Customer Churn Prediction & Retention System**

ChurnSense.AI is an **end-to-end automated churn detection and customer retention system** that analyzes telecom customer data, predicts churn probability using machine learning, and automatically triggers retention actions such as sending personalized email offers.

This project demonstrates how **data analytics, machine learning, and workflow automation** can work together to reduce customer churn and improve customer retention strategies.

---

# 📊 Problem Statement

Customer churn is one of the biggest challenges for telecom companies. Losing customers results in:

* Reduced revenue
* Higher customer acquisition costs
* Lower customer lifetime value

Traditional churn analysis is often **manual and reactive**.

ChurnSense.AI solves this by creating an **automated churn intelligence pipeline** that predicts churn early and automatically triggers retention actions.

---

# 🎯 Project Objectives

* Build an **automated churn prediction pipeline**
* Predict **customer churn probability using machine learning**
* Trigger **automated retention offers via email**
* Demonstrate **AI + automation for business analytics**

---

# 🧠 Key Features

✔ Automated data ingestion
✔ Automated data cleaning pipeline
✔ Logistic Regression churn prediction model
✔ Customer churn probability calculation
✔ Automated retention email system
✔ End-to-end automation workflow

---

# ⚙️ System Architecture

Customer Data Input (Excel / Google Sheets)
↓
Automated Data Cleaning
↓
Machine Learning Model (Logistic Regression)
↓
Churn Probability Calculation
↓
Customer Risk Classification
↓
Retention Automation Workflow
↓
Automated Email Offers

---

# 🔄 End-to-End Workflow

## 1️⃣ Customer Data Entry

Customer data is entered into the dataset (Excel / Google Sheets).

Example attributes include:

* Customer tenure
* Monthly charges
* Contract type
* Payment method
* Internet services
* Customer demographics

---

## 2️⃣ Automated Data Processing

Once new data is added, the automation pipeline automatically:

* Cleans missing values
* Standardizes data formats
* Prepares features for machine learning

---

## 3️⃣ Churn Prediction Model

A **Logistic Regression model** calculates churn probability for each customer.

Example output:

| Customer ID | Churn Probability |
| ----------- | ----------------- |
| C101        | 0.78              |
| C102        | 0.15              |
| C103        | 0.62              |

---

## 4️⃣ Risk Identification

Customers are categorized based on churn probability:

* **High Risk:** > 0.7
* **Medium Risk:** 0.4 – 0.7
* **Low Risk:** < 0.4

---

## 5️⃣ Automated Retention System

For high-risk customers, the system automatically triggers retention actions such as:

* Promotional discounts
* Loyalty offers
* Contract upgrade incentives
* Customer support outreach

Retention offers are automatically sent via **email automation**.

---

# 🤖 Automation Workflow

The automation pipeline is built using **n8n workflow automation**.

Workflow capabilities include:

* Data ingestion
* Automated data processing
* Machine learning model execution
* Email retention triggers

Workflow file included in this repository:

Churn.json

This workflow can be imported directly into n8n.

---

# 🛠 Technologies Used

Python — Data processing and machine learning
Logistic Regression — Churn prediction model
n8n — Workflow automation
Excel / Google Sheets — Data source
SMTP / Email service — Automated email notifications
Data Analytics — Business insights

---

# 📂 Repository Structure

churnSense.AI
│
├── Churn.json
│   n8n automation workflow
│
├── README.md
│   Project documentation
│
└── assets
Screenshots / demo materials

---

# 🚀 Getting Started

## 1️⃣ Clone the Repository

git clone https://github.com/ashishamith/churnSense.AI.git

---

## 2️⃣ Import the Workflow

Open n8n and import the workflow file:

Churn.json

---

## 3️⃣ Configure Credentials

Configure the required credentials for:

* Google Sheets access
* Email service (SMTP)

---

## 4️⃣ Run the Workflow

Execute the workflow to start the **automated churn prediction and retention pipeline**.

---

# 📈 Business Impact

ChurnSense.AI enables telecom companies to:

* Detect churn risk early
* Automate retention campaigns
* Improve customer lifetime value
* Reduce revenue loss

---

# 🔮 Future Improvements

* Advanced machine learning churn prediction models
* Real-time churn monitoring pipeline
* Customer segmentation analytics
* Interactive dashboards (Power BI / Streamlit)
* AI-generated retention recommendations

---

# 👨‍💻 Author

**Ashish Amith R**

Data Analytics & Generative AI Enthusiast
Building practical AI, automation, and analytics solutions.

---

# ⭐ Support

If you found this project useful, consider giving the repository a **star ⭐**.
