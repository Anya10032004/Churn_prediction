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
 - Revenue throughout 2020 to 2023 remains relatively stable. Although there are slight increases and decreases each year, the changes are not really significant.
 - West Java Province contribute the most in profit/revenue and total sales in Kimia Farma
 - Top contributing products in profit but low in sales are mostly symptom-relief medications, such as sedatives and anxiolytics for relaxation and sleep, antihistamines for allergies, drugs for obstructive airway diseases (respiratory issues), and analgesics for pain and fever.
 - Top 5 Kimia Farma branches with the highest customer ratings but relatively low transaction ratings are located in Bangka Belitung, South Sulawesi, North Kalimantan, North Sumatra, and Nusa Tenggara Barat. If we zoom in to their city, Lower transaction ratings may be influenced by a relatively smaller amount customer base compared to other cities within the same province—such as Pangkalpinan from Bangka Belitung and Tarakan from North Kalimantan—or by lower transaction quality in certain cities, including Pematangsiantar, Tomohon, and Bima
 - Although West Java generates the highest total revenue, the cities with the highest average profit per transaction are mostly outside West Java—and even outside Java. Several of these cities also contribute strongly to their province’s revenue and transaction volume, this cities are Lubuklinggau (South Sumatra), Bontang (East Kalimantan), Malang and Madiun (East Java), Medan (North Sumatra), Pekanbaru (Riau), Tomohon (North Sulawesi), and Banda Aceh (Aceh). Meanwhile, others like Tangerang (Banten) and Palu (Central Sulawesi) have high profit per transaction but relatively low overall transactions and revenue. 

## 💡 Business recommendation
So based on the evaluation of the performance of Kimia Farma year 2020-2023, so in order so that the revenue of the Kimia farma increases, some business recommendations that helps are:
- For cities that has lower revenue and transaction volume, but has high profit in each transactions:
  Tangerang and Palu:
  Increase the number of customers in branches with lower revenue and transaction volume . This can be achieved by improving visibility and conducting location assessments—for example, evaluating whether the branch is in a low-traffic
  area or lacks sufficient customer exposure.
  
- Focus on “underated” branches, which has high customer ratings, but low transaction rating

  Branches with lower number of customers:
  Focus on increase the number of customer  → Ex: Local promotion or improve the exposure of the branch

  More likely because of Transaction quality:
  Increase payment flexibility →  Such as add more payment methods
  
- Focus on products that generates high profits, but low sales
  - Increase product visibility → Ex: placement in-store or highlight the products through displays and recommendations.
  - Do some promotion to the products → Ex: offering promotions such as bundling with related products.
  - Educate customers on product benefits  → Provide clear information about the product’s value and benefits, as low sales may be due to limited customer awareness.
- For west Java
  Because West Java contributes the highest revenue, profit, and total sales, the strategy should focus on maintaining and further improving its performance through the following actions:
   - Make each customer to spend more → Ex: Offer bundle or recommend additional products
   - Focus on products that give the most profit → So because West Java has the most number of transactions and generates the most profits/revenue, we can try to leverage the condition by promoting and selling high-margin products, not just the most popular ones.
   - Reward repeat customers → Ex: Make loyalty programs, Discounts for repeat buyers 



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
