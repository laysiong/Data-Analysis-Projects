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
<p>There is 3 tier for the Credit Card User. It is Silver, Gold, and Platinum. Among 3 the tiers, Gold spent the most and also had the highest number of users. Surprisingly, there are 5.6% of credit card users that is below 20 years old.</p>
 
<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/bb6a0d8a-6bd3-445a-a0fb-d507bc3b8337">
</p>

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/ad34315a-64a5-47dd-85c7-2b9bbb4cfdba">
</p>

<h3>Countries where our clients are from</h3>
<p>The top 3 countries that our clients are from Bangalore, Cochin, and Calcutta.</p>

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/4de9e33d-04f4-4f6e-992a-337bd617c45a">  
</p>

<h3>What is their spending habit? </h3>
<p>Across all tiers, they spend on similar expenses such as  petrol, food, camera, air ticket, train ticket, and shopping. A similar spending pattern is shown across the age group. The top 5 categories that are most spent on are Petrol, Camera, Food, Air Ticket and Train Ticket.</p>

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
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/e6038b10-ee93-4375-b92d-26882b7f0792">
</p>

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/7e8d9320-5ff8-4a59-999d-774e14593f22">
</p>

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/d3dcd5fc-04e2-4503-b81e-f07edbcd79e8">
</p>

<p> The number of Customers continues to grow through the years. It was not the contributor to the increasing in late payment.</p>

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/c315361b-3d62-4159-bc5e-6b72a0885ed9">
</p>


<p>The number of late payments has increased among our long-term clients who have been with us for 2 years. There's also a pattern of increasing late payments observed every year during the January to May period.</p>

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/3619e041-fa20-4938-99b5-f7e135762b4d">
</p>

<h3>Did they spend over the credit limit or spend amount per month?and overall?</h3>
<p> Currently, 45% of customers are in debt with their credit cards. However, this doesn't necessarily indicate an inability to pay; it might suggest that some customers simply require more time. </p>

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/ecde6d90-a278-4959-87b5-24ebe9d83ea9">
</p>

<h3> What is their risk profile? </h3>
<p> We've developed a risk profile for each client based on two critical factors: the timeliness of their payments and whether they exceed their monthly credit limit. Using the information at our disposal, we assign a score to each client, helping us determine their individual risk profile.

In observing the distribution of the 'Repay to Spend Amount Ratio' across different age groups, we notice that many individuals are in debt. However, they're nearing the completion of their debt repayment. A smaller subset of clients appears to be paying amounts significantly higher than their recent spending. This discrepancy might be due to them settling previously unrecorded debts.

When examining the distribution of risk groups by age, a concerning trend emerges. A considerable number of clients below the age of 60 fall into the high-risk category.

Regarding geographic patterns, cities like Bangalore, Calcutta, Cochin, Patna, and Chennai have a notably higher number of individuals with lower credit scores.

Lastly, when segmented by tier, both the silver and platinum categories show a tendency towards lower credit scores.
</p>

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/f36e1052-fa53-4d78-b898-5101f678b4ca">
</p>

<p align="center">
  <!---<img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/5770bde9-2aac-4321-adbf-9dccc2224c0b">--->
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/67950f43-af72-4c4c-a197-818bc38aefe0">
</p>

<h2>Conclusions</h2>

**Bankruptcy**
At present, none of our clients have declared bankruptcy. However, from our analysis, we've identified that 48.4% of them struggle with their monthly credit debt payments. A significant portion of these late payments emanates from our long-standing clients who have been associated with us for 2 years or more.

Although 45% of our clientele is in debt, it's crucial to highlight the potential risks associated with their current spending patterns. If they persist in these habits, there's an elevated likelihood of them facing bankruptcy in the future.

**Fraud**
The current data set is not comprehensive enough to detect fraudulent transactions effectively. A more detailed dataset encompassing client spending habits, transaction locations (such as shops), and previously reported fraud incidents would significantly enhance our analysis.

From the information available, we note that all transactions have occurred within the clients' countries of birth. An area that merits closer scrutiny is the segment of our clientele under the age of 19, representing 5.6% of the total. For a more in-depth analysis, we would need additional details, like who authorized their credit card usage and which guardian or parent consented to these teenagers having a credit card. There's a potential risk here; since these individuals are underage, they might be less accountable legally, making them potential targets for illicit activities, including fraud.


**Proactive Offers and Service**
As part of our initiative for proactive offers and services, we've delved into analyzing our clients' spending patterns. The top five categories where expenditure is highest are: Petrol, Camera, Food, Air Tickets, and Train Tickets. On closer inspection, a predominant theme emerges—most of these expenses can be categorized under 'Transport'. In light of these findings, we suggest introducing offers related to these categories, as it would be a strategic move to enhance client retention.