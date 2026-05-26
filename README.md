# Churn_prediction

## 📌 Project Description
This project analyzes the business performance of Kimia Farma from 2020 to 2023 using BigQuery and Google Looker Studio. The goal is to transform raw data into meaningful insights such as sales trends, branch performance, and customer ratings. The data is processed using SQL in BigQuery and visualized through an interactive dashboard.

## 🎯 Objectives
- Analyze revenue performance trends from 2020 to 2023 to understand overall business stability and growth patterns.
- Identify top-performing provinces and branches based on revenue, profit, and transaction volume.
- Detect high-profit but low-sales products (underrated products) that have strong margins but low transaction frequency.
- Evaluate profit contribution by province to determine which regions generate the highest business value.
- Analyze city-level performance within each province by calculating the average profit per transaction.
- Identify underrated branches—branches with high customer ratings but relatively low transaction volumes—and explore possible causes.
- Examine profit and sales distribution patterns across regions, branches, and products to uncover key business insights.
- Generate data-driven business insights to support strategic decision-making and performance improvement.
- Provide actionable business recommendations to increase revenue, improve transaction volume, and optimize product and branch performance.

## 🗂️ Dataset Information

The analysis_table column information:
  - transaction_id: transaction ID
  - date: transaction date
  - branch_id: Kimia Farma branch ID
  - branch_name: branch name
  - kota (city): city where the branch is located
  - provinsi (province): province where the branch is located
  - rating_cabang (branch_rating): customer rating of the branch
  - customer_name: name of the customer who made the transaction
  - product_id: product ID
  - product_name: product (medicine) name
  - actual_price: product price
  - discount_percentage: discount percentage applied to the product
  - persentase_gross_laba (gross profit percentage)
    
     -- Price ≤ Rp 50,000 → 10%
    
     -- Rp 50,000 < Price ≤ Rp 100,000 → 15%
    
     -- Rp 100,000 < Price ≤ Rp 300,000 → 20%
    
     -- Rp 300,000 < Price ≤ Rp 500,000 → 25%
    
     -- Price > Rp 500,000 → 30%
    
  - nett_sales: price after discount (net sales / revenue after discount
     - nett_profit: net profit earned by Kimia Farma
       
  - rating_transaksi (transaction_rating): customer rating of the transaction

The analysis_table table is actually made by merging 4 datasets

1. kf_final_transaction.csv
     - transaction_id: transaction ID
     - product_id: product ID (medicine)
     - branch_id: Kimia Farma branch ID
     - customer_name: name of the customer who made the transaction
     - date: transaction date
     - price: product price
     - discount_percentage: percentage of discount applied to the product
     - rating: customer rating for the transaction
2. kf_product.csv
     - product_id: product ID (medicine)
     - product_name: product name (medicine)
     - product_category: product category (medicine)
     - price: product price
3. kf_inventory.csv
    - inventory_ID: inventory ID for the medicine product
    - branch_id: Kimia Farma branch ID
    - product_id: product ID (medicine)
    - product_name: product name (medicine)
    - opname_stock: total stock of the product
6. kf_kantor_cabang.csv
    - branch_id: Kimia Farma branch ID
    - branch_category: branch category
    - branch_name: branch office name
    - kota: city of the branch
    - provinsi: province of the branch
    - rating: customer rating for the branch

## ⚙️ Tools & Technologies
 - Google BigQuery (SQL)
 - Google Cloud Platform (GCP)
 - Google Looker Studio
 - GitHub

## 🔄 Project Workflow
 1. Import datasets into BigQuery
 2. Clean and transform data
 3. Create an analysis table by joining
 4. Calculate metrics (nett sales, profit, etc.)
 5. Build a dashboard in Looker Studio

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
