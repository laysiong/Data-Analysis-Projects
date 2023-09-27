<h1>PSPD Bank Credit Card Exploratory Data Analysis </h1> 

<h2>Business Statment</h2>
In order to effectively produce quality decisions in the modern credit card industry, knowledge
must be gained through effective data analysis and modeling. Through the use of dynamic data-driven decision-making tools and procedures, information can be gathered to successfully evaluate all aspects of credit card operations. PSPD Bank has banking operations in more than 50 countries across the globe. Mr. Jim Watson, CEO, wants to <b>evaluate areas of bankruptcy, fraud, and collections, and respond to customer requests for help with proactive offers and service.</b>

<h2>About the Data</h2>
<b>This book has the following sheets:</b>
  <li>Customer Acquisition: At the time of card issuing, the company maintains the details of customers.</li>
  <li>Spend (Transaction data): Credit card spend for each customer</li>
  <li>Repayment: Credit card Payment done by customer</li>

<h2>Question to be answer</h2>
Based on the business statement, here is a list of questions that helped us to tackle those areas.

<ol>
<li> Who are our clients? </li>
<li> What is their spending habit? monthly? overall? </li>
<li> Are they repaying their credit card on time?</li>
<li> Did they spend over the credit limit or spend amount per month?and overall?</li>
<li> What is their risk profile? </li>
<li> Who are will more exposed to Fraud? </li>
<li> What can inform us if there is any suspicion of transactions?</li>
</ol>

<h2>Analysis</h2>
<h3>Who are the cilents?</h3>
<p>There is 3 tier for the Credit Card User. It is Silver, Gold, and Platinum. Among 3 the tiers, Gold spent the most and also had the highest number of users. Surprising, there are 5.6% of credit card user that is below 20 years old.</p>
 
<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/bb6a0d8a-6bd3-445a-a0fb-d507bc3b8337">
</p>

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/ad34315a-64a5-47dd-85c7-2b9bbb4cfdba">
</p>


<h3>Countries where our clients are from</h3>
<p>The Top 3 Countries the client are from is Bangalore, Cochin and Calcutta.</p>

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/4de9e33d-04f4-4f6e-992a-337bd617c45a">  
</p>

<h3>What is their spending habit? </h3>
<p>Across all tiers, they spend on similar expenses such as  petrol, food, camera, air ticket, train ticket, and shopping. </p>

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/ee319557-c8ce-48c9-8b42-e248a97b346f">
</p>
<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/3db902a9-b5d7-40f5-9097-d043b91cb84e">
</p>

<!---![image](https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/41083519-6e79-4500-9852-9fd2cda6e970)--->


<h3> Are they repaying their credit card on time?</h3>
<p>The number of our clients who late payments on credit bills is almost half of the total amount of clients. The number continues to increase through the 3 years. </p>

<!--- Pie Chart of % of Clients repaid on time monthly--->
<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/d8b12207-cd5a-44aa-970a-56a30c1b8688">
</p>

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/248ae11a-c181-4fd5-8abf-45221ae1595f">
</p>

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/b02f0ab2-82c6-4039-946a-06b1491cb46f">
</p>

<p>A reason for the increased number of late payments to Credit bills could be the number of Customer growth over time.</p>

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/c315361b-3d62-4159-bc5e-6b72a0885ed9">
</p>

<p>The reason for the increase in late payments, is our longer-time client (2 years). The pattern also forms of late payment on every Jan to May Period</p>

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/31aada88-9bbf-4d6e-9128-673192fd1fb99">
</p>


<h3>Did they spend over the credit limit or spend amount per month?and overall?</h3>
<p> Currently, there is 45% are in debt with their credit card.</p>

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/b54a3645-d549-4909-83a7-adc6dc579bc3">
</p>

<h3> What is their risk profile? </h3>
<p> I created a risk profile based on 2 factors, first are the payments on time, and did the spent pass their credit limit monthly? Based on that, we will assign a score to each client to determine its risk profile. 

Distribution of Repay to Spend Amount Raito across Ages, there is a number of people that are in debt but they are quite close to paying up debt. There are few clients that pay amounts that exit further from what they spend on. It could be a repayment of their previous debt that is not recorded in the data. 

Distribution of Risk Groups Across Ages, there seems to be a group of clients under 60 who fall into the high-risk profile. 
</p>

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/75efc4cd-bcab-4311-a97b-65618e06d581">
</p>

<p align="center">
  <!---<img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/5770bde9-2aac-4321-adbf-9dccc2224c0b">--->
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/67950f43-af72-4c4c-a197-818bc38aefe0">
</p>

<h2>Conclusions</h2>




