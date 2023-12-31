<h1>E-Commerce Sales Dataset Exploratory Data Analysis</h1> 
Data Source: https://www.kaggle.com/datasets/thedevastator/unlock-profits-with-e-commerce-sales-data
<br>last updated on 06/11/2023
<h2>Business Problem</h2>
<b>Objective:</b> To optimize the profitability of e-commerce sales across diverse channels and align inventory management with demand patterns.

<b>Background:</b> With the rapid growth of the e-commerce sector, understanding sales channels, inventory management, and profitability is pivotal for sustained business growth. Leveraging insights from detailed sales data can help improve decision-making, streamline operations, and maximize ROI.

<h2>About the Data</h2>
<b>Data Breakdown by Source:</b>
<ul>
<li>Cloud Warehouse Compersion Chart: It contains the information of services charged (Inbound, Outbound, Storage Fee and etc.) between Shiprocket and INCREFF </li>
<li>Sale Report: It contains the amount of stock, SKU Code, Design No., Category, Size, and Color.</li>
<li>P & L March 2021: Product price across third-party and other e-commerce platforms in March 2021.</li>
<li>P & L May 2022: Product price across third-party and other e-commerce platforms in March 2021.</li>
<li>Amazon Sales Report: Transaction Details, Status, and Customer Data Primarily from India.</li>
<li>International Sales Report: Transaction Overview, Status, and Customer Information for Global Sales.</li>
<li>Expense IIGF: It contains 2 tables, expense and amount received.</li>
</ul>

<h2>Question to be answer</h2>
<ol>
<li>How do SKU codes, design choices, and product categories influence sales performance across different channels?</li>
<li>How can we refine our pricing strategies across various e-commerce platforms to maximize profitability?</li>
<li>How can we better align our inventory with demand patterns to prevent stockouts and overstock situations?</li>
<li>Which sales channels (e.g., Shiprocket, INCREFF) are performing the best, and where should we reallocate resources for maximum efficiency?</li>
</ol>

<h2>Analysis</h2>
<h3>Information on general trend market on Amazon in India</h3>
About <b>27.8%</b> of shipped transactions on Amazon are fulfilled by merchants, contributing to <b>27.9%</b> of the platform’s shipped sales revenue. This indicates a relatively balanced distribution of product value between Amazon’s and merchants' sales, highlighting the substantial role of merchants in the Amazon ecosystem right from the start.
<br></br>
<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/e1f4a0f9-90b0-4e99-acf1-f2a11760be99">
</p>

Amazon accrued <b>₹50,324,255</b> in revenue from shipped transactions, outpacing merchants who earned <b>₹19,448,655</b>. Both saw comparable losses from cancellations and pending orders. However, merchants notably faced challenges, with returns, damages, or rejections affecting $1,278,075 worth of goods.

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/577be8e8-43a6-4a68-9dd1-0d64e33fafde">
</p>


The categories of Set, Kurta, and Western Dress constitute the top three revenue-generating segments, accounting for 89.374% of total Amazon sales in India. 
<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/f0baf9e2-cd44-49c5-b7dc-fc2b5da442b4">
</p>

The sales pattern seen here remains consistent across the top 10 countries with the highest purchase volumes on Amazon. Nonetheless, it's imperative to understand that these findings primarily illuminate current market inclinations and should not be solely used to make inventory stocking choices. The primary objective of presenting this information is to confirm and understand the existing trends in sales.

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/eba055d8-7648-489e-ac1e-d3d1ce971b37">
</p>

Merchants show competitive sales in Western Dresses compared to Amazon, performing notably well in this category, while Amazon dominates in other product areas.
<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/3e5f7779-877c-413a-8f95-b3ae6f7973cb">
</p>


Examining average earnings, Amazon surpasses in the majority of categories with only slight variations in revenue amounts. However, merchants demonstrate superior profitability in the 'SAREE' category. Additionally, it's noteworthy that the 'DUPATTA' category is exclusive to Amazon sales, as merchants have no transactions in that particular category. We can confidently deduce that generally, the item pricing is considerably stable across different categories. However, a thorough examination within each category is essential to pinpoint any potential anomalies or outliers that might exist.
<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/9f6ed031-03c0-4eb1-bbd9-8b4af3634119">
</p>


Both exhibit a comparable trend, with the majority of their customers falling within the XS to 3XL size range. There is lesser demand for sizes 4XL to 6XL, as well as for free sizes.
<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/1c627fad-cda4-4a17-893c-90064183cefc">
</p>

B2C sales significantly surpass B2B sales in terms of market value for both Amazon and Merchant.
<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/5fded3e1-cac3-4799-9a7f-bc06881b8ac2">
</p>

Examining the proportion of transactions that utilized discounts reveals that nearly 100% of transactions under Merchant, regardless of being B2B or B2C, have been discounted. On the other hand, Amazon displays varying percentages of discounted transactions across different categories for both B2B and B2C. This discrepancy suggests that Amazon might be employing a strategic approach to enhance its appeal to customers. The absence of data points for Merchant in either B2B or B2C categories can be attributed to the lack of transactions in those areas.
<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/40d47b72-340a-4e04-9027-4113afe6a81f">
</p>

<h3>Information on general trend market on International Sale</h3>
Kurta Set, Kurta, and Dress are the top revenue contributors in international sales, making up 85.148% of the overall revenue. This pattern is consistent with Amazon's sales trends, which also show these items as top sellers. To fully understand the comparison, we need to investigate whether the categories align exactly—for instance, whether 'Set' is synonymous with 'Kurta Set,' and if 'Dress' refers specifically to Western-style dresses.
<br></br>
<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/03e9151b-a342-4457-be16-ec5b4a9ce3b4">
</p>

Most of their clientele are within the XS to XXL size bracket, with a reduced demand for sizes 4XL to 6XL. Notably, there are no orders for Free Size or 3XL, a trend that somewhat resembles Amazon's sales pattern.

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/f369a2c7-451c-404b-b7b5-5e8c6cbe4b4b">
</p>

<h4>Summary of Sales Trends in Amazon India and Global Markets</h4>
<p>Analyzing both Amazon and international data, it's evident that focusing on <b>Kurta sets, sets, Kurtas, and Western Dresses/Dresses</b> could satisfy <b>80% to 90% of customer demand</b>. When considering stock sizes, maintaining an inventory ranging from <b>XS to 3XL</b> is advisable. Additionally, exploring the niche market of sizes 4XL to 6XL could attract a distinct customer base.</p>

<h3>Comparative Analysis of Pricing Across E-commerce Platforms</h3>
In the 2022 data, one third-party platform previously listed is notably absent, suggesting potential market shifts, alterations in strategic partnerships, or the platform's withdrawal from the competitive landscape.
<br></br>
We will examine the variations in pricing distribution across E-commerce platforms. Within categories like Kurta, Kurta Sets, and Tops that appear in both datasets, we've noted that Ajio, Amazon, Amazon FBA, and Flipkart exhibit a higher standard deviation than the average. This suggests that, during that particular month, these platforms may have engaged in strategic pricing, and promotions, or offered exclusive designs for these three categories. 
<br></br>
Additional data is required to thoroughly analyze the pricing distribution among e-commerce platforms.
<br></br>
<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/535d3b02-d9b7-4e59-995d-9f565d1a7782">
</p>

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/3a8561ff-fa43-419d-afe9-f8c39133146c">
</p>

During the review of Maximum Retail Prices (MRP) by category between March 2021 and May 2022, it was found that MRPs remain constant. The only notable variation detected was the disappearance of a third-party platform in the more recent data. Additionally, a significant price variation was identified on this third-party platform, where items were priced much lower, at times 4 to 5 times less, compared to other e-commerce platforms.

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/cadec952-254c-444b-9b0f-cb3bf66cef2b">
</p>

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/c3dacdac-2eab-4f6c-8574-4c0460672491">
</p>

<h3>Inventory for E-commerce Sales</h3>
We need to assess our inventory to determine which items are selling out and which are not. By merging Amazon and International sales data with our inventory reports, we've categorized products based on their sales performance and stock levels. Products with sales exceeding our stock are categorized as understocked, and those with significantly more inventory left than sold are overstocked. Additionally, we've identified products that are sold out, have no sales, or have balanced sales.

Our inventory composition reveals that 44.9% is tied up in overstocked items or products that have not achieved any sales. Moreover, 55% of our inventory suffers from a low turnover rate. Within this segment, approximately 10.1% of our products that are either balanced in stock or sold out may also be experiencing low turnover.

Ideally, we would aim for a turnover rate where at least 70% of our inventory is high-turning and no more than 30% is low-turning. Addressing the 10.1% segment with potential pricing strategy adjustments could enhance turnover rates. Concurrently, we need to focus on the remaining 20% to mitigate overstocking and zero sales situations.

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/6a0cd9e2-26ff-4a8c-8486-2a799e3c2c62">
</p>

We should prioritize managing our inventory for categories such as SAREE, SHARARA, KURTI, SKIRT, and BOTTOM, where the low turnover rates are most pronounced. Conversely, there is an opportunity for enhancement in categories like BLOUSE, LEGGINGS, and CARDIGAN, which currently exhibit a lower incidence of high turnover rates. 

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/634f8921-577d-43cc-be91-e14051ff9041">
</p>


<h3> Cloud Wharehouse - Shiprocket or  INCREFF </h3>



<!---!
<table cellspacing="0" cellpadding="0" border:none>
<tr>
  <th>Amazon</th>
  <th>Merchant</th>
</tr>

<tr>
  <td>1</td>
  <td>2</td>
</tr>
  
</table> --->

<h2>Conclusions</h2>


