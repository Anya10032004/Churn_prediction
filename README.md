# Churn_prediction

## 📌 Project Description
This project focuses on predicting customer churn using machine learning techniques in the banking industry. The goal is to analyze customer behavior and identify which customers are likely to leave the bank. The project includes data preprocessing, exploratory data analysis, machine learning model development, and business recommendation insights.

## 🎯 Objectives
The main objectives of this project are:
- Predict whether a customer will churn or stay using machine learning models.
- Analyze customer behavior patterns related to churn.
- Compare multiple machine learning algorithms to find the best-performing model.
- Identify important factors influencing customer churn.
- Provide business recommendations to improve customer retention and customer engagement.

## 🗂️ Dataset Information

The dataset contains customer-related information from a banking company. Several important features are used to analyze customer churn behavior, including:
 - customer_id -->	Unique ID assigned to each customer
 - credit_score --> 	Customer credit score that reflects financial credibility
 - country	--> Country where the customer is located (e.g., France, Spain, Germany)
 - gender	--> Customer gender (Male/Female)
 - age	--> Customer age
 - tenure --> 	Number of years the customer has stayed with the bank
 - balance	--> Customer bank account balance
 - products_number	--> Number of bank products used by the customer
 - credit_card	--> Whether the customer owns a credit card (1 = Yes, 0 = No)
 - active_member --> 	Whether the customer is an active bank member (1 = Active, 0 = Not Active)
 - estimated_salary	--> Estimated customer salary/income
 - churn --> 	Target variable indicating whether the customer left the bank (1 = Churn, 0 = Stay)
    
## ⚙️ Tools & Technologies
 - 💻 Google Colab
 - 🐍 Python
 - 🐼 Pandas
 - 📊 Matplotlib
 - 🤖 Scikit-learn (sklearn)

## 🔄 Project Workflow
 1. Import datasets into Google Colab
 2. Data review and cleaning
 3. Exploratory Data Analysis (EDA)
 4. Feature engineering
 5. Data preparation and Data pipeline
 6. Prepare the Machine Learning models
 7. Conclution:
    - Finale insights
    - Better model explanation
    - Business Insights

      
## 📊 Key Features / Analysis

- Analyze the profit distribution across provinces in Indonesia
- Identify the top 10 branches with the highest number of transactions in each province in Indonesia
- Determine the top 10 cities based on average profit per transaction
- Identify the top 5 branches with the highest branch ratings but the lowest transaction ratings
- Determine the top 5 most profitable products
- Analyze annual revenue trends
- Identify the top 10 provinces with the highest net sales

## 📈 Dashboard

🔗 Dashboard Link: 
https://datastudio.google.com/reporting/8dc7a40e-a571-4f57-99bf-5d41f31f8cb2/page/oYLwF

## 🔍 Business insights
Final Insights

Around 79.6% of customers remain with the bank, while 20.4% have churned. Customer churn is strongly influenced by age, with customers between 38–51 years old showing the highest churn rate. Customers in this age group also tend to have higher account balances compared to non-churn customers, particularly within the balance range of 38,340.02–131,433.33. In terms of gender, female customers are more likely to churn than male customers.

When analyzed by country, customers from Germany have the highest churn rate compared to customers from other countries.

The main characteristics of churned customers in Germany are:

 - Female customers
 - Aged between 38–51 years old
 - Have higher account balances compared to the overall churned
 - customer balance range, specifically between 107,521.59–132,900.18

Further analysis of customers with these characteristics shows several additional patterns:
- Churned customers generally have a longer tenure, indicating that many customers who leave the bank are actually long-term customers.
- Both churned and non-churned customers mostly own 1–2 banking products, showing that the number of products does not create a significant difference between the two groups.
- Most churned customers already have a credit card. Although churned customers tend to stay longer with the bank, many of them are not active members.
- Churned customers generally have lower estimated salaries compared to non-churned customers.
- Churned customers also tend to have lower credit scores than non-churned customers, indicating a higher financial risk and a greater possibility of delayed loan repayments.

## 💡 Business recommendation

1. Develop retention programs for long-tenure customers, since many churned customers are long-term customers who may feel undervalued despite their long relationship with the bank.

  Example:

     - Loyalty rewards
     - Reduced banking fees
     - Exclusive financial products
    
2. Improve customer engagement and membership benefits, since many churned customers are inactive members despite having long tenure and existing banking products.
   - Reward Active Membership(ex: Cashback for frequent transactions, Lower transfer/admin fees)
   - Re-engagement Campaigns(ex: Email or SMS reminders, "We miss you" promotions)
   - Personalized Financial Recommendations(ex: High-balance customer suggest for
   - investment or savings products, Salary account holder suggest for loan recommendations)
   - Activity-Based Incentives(ex: Make 10 transactions can get cashback, Maintain active account usage get fee discount)
    

3. Prioritize churn prevention strategies in Germany, where customer churn is highest, particularly among high-risk customer segments.

## 📂 Repository Structure
```
├── SQL/

| └── analysis_query.sql

├── Dataset/

| └── Analysis_table(sample_10_rows)

├── Dashboard/

| └── Finale_project_rankamin (1)

| └── Link to the dashboard in google studio.txt

├── README.md

```

## Additional Links
 - 📂 GitHub Repository: https://github.com/Anya10032004/Rankamin_finale_project
 - 📄 Presentation (PPT): https://docs.google.com/presentation/d/1xc19aI7Nb05oyQ8OTsxjSikXMAus8RmPXcZe8Ob7sQI/edit?usp=sharing
 - 🎥 Video Explanation: https://youtu.be/U92kj4zlHn0
