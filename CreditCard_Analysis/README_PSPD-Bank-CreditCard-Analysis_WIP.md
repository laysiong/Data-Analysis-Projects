<h1>PSPD Bank Credit Card Exploratory Data Analysis </h1> 

<h2>Business Problem</h2>
In order to effectively produce quality decisions in the modern credit card industry, knowledge
must be gained through effective data analysis and modeling. Through the use of dynamic data-driven decision-making tools and procedures, information can be gathered to successfully evaluate all aspects of credit card operations. PSPD Bank has banking operations in more than 50 countries across the globe. Mr. Jim Watson, CEO, wants to <b>evaluate areas of bankruptcy, fraud, and collections, and respond to customer requests for help with proactive offers and service.</b>

<h2>About the Data</h2>
<b>This book has the following sheets:</b>
  <li>Customer Acquisition: At the time of card issuing, the company maintains the details of customers.</li>
  <li>Spend (Transaction data): Credit card spend for each customer</li>
  <li>Repayment: Credit card Payment done by customer</li>

<h2>Question to be answer</h2>
Based on the business problem, here is a list of questions that helped us to evaluate all aspects of credit card operation. 

<ol>
<li> Who are our clients? </li>
<li> What is their spending habit? monthly? overall? </li>
<li> Are they repaying their credit card on time?</li>
<li> How often do they spend over the credit card limit? </li>
<li> How many have the ability to repay? How many have large outstanding debts? </li>
<li> What is their Credit Score? </li>
<li> Who is more likely to go bankrupt? </li>
<li> Who and what transactions are will more exposed to Fraud? </li>
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
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/c701aad8-9a47-4de4-8d4a-d152e30bedb0">
</p>

<p align="center">
  <!---<img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/5770bde9-2aac-4321-adbf-9dccc2224c0b">--->
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/eb36ac16-9c0a-4560-aeea-92fd2e53600f">
</p>

<h3> Who might get Bankrupt? </h3>
<p> Currently, there is no cilent who had declared Bankrupt in the data. So for us to find out who could potentially bankrupt, we will first define what is consider as Bankrupt. The <b>definition of Bankrupt</b> for this case, is when cilents is unable to repay outstanding debts or outstanind debts is twice on what cilents had repay, decrease in repay to spending amount monthly and bad credit score. Those will be 3 factor we will acesss merit or dermit point to the cilent to gauge if they will likely to declared bankrupt.
</p>

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/8c6e2e56-5566-4d0a-841b-c64180b29570">
</p>
17% of our 100 cilents are in the high-risk and likely to bankrupt based on our 3 consider factors. If we will to filter out some of only use for 1 transaction and stop.

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/5dc7e751-7abc-4202-84ef-f972da0df7fe">
</p>
3.2% of 63 cilents are likely to brankrupt. This are cilents who use the card often.


<h3> Which transaction could potentially be fraud? </h3>
<p> The factor we wil consider to check if transaction fraud will be location on card use, user origin location, have the transaction be repay full and is there usual spending amount through out the month from same cilents. Based on those mertrix, we can see their 36% of transaction are High Risk to fraud.
</p>

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/6f0f90de-7434-4306-adad-3e555ae12d6a">
</p>

If we look amount spend amounting on 36% compare all transaction, it is 46.5% of spent amount in transaction. The top 3 transaction area that is being spent are Train Ticket, Shopping and Sandals.

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/e9536e5b-0b70-4533-bf41-566378194c5a">
</p>
<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/2f630f9f-5f34-4720-84e4-5eed765a1b89">
  <!---<img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/037cfb79-7d24-4dfa-aa30-f37b0fa0b476">--->
</p>

<h2>Conclusions</h2>

<h3>Bankruptcy</h3>
<p>At present, none of our clients have declared bankruptcy. However, from our analysis, we've identified that 48.4% of them struggle with their monthly credit debt payments. A significant portion of these late payments emanates from our long-standing clients who have been associated with us for 2 years or more.
<br></br>
Although 45% of our clientele is in debt, it's crucial to highlight the potential risks associated with their current spending patterns. If they persist in these habits, there's an elevated likelihood of them facing bankruptcy in the future.</p>

<h3>Fraud</h3>
<p>The current data set is not comprehensive enough to detect fraudulent transactions effectively. A more detailed dataset encompassing client spending habits, transaction locations (such as shops), and previously reported fraud incidents would significantly enhance our analysis.
<br></br>
From the information available, we note that all transactions have occurred within the clients' countries of birth. An area that merits closer scrutiny is the segment of our clientele under the age of 19, representing 5.6% of the total. For a more in-depth analysis, we would need additional details, like who authorized their credit card usage and which guardian or parent consented to these teenagers having a credit card. There's a potential risk here; since these individuals are underage, they might be less accountable legally, making them potential targets for illicit activities, including fraud.</p>

<h3>Proactive Offers and Service</h3>
<p>As part of our initiative for proactive offers and services, we've delved into analyzing our clients' spending patterns. The top five categories where expenditure is highest are: Petrol, Camera, Food, Air Tickets, and Train Tickets. On closer inspection, a predominant theme emerges—most of these expenses can be categorized under 'Transport'. In light of these findings, we suggest introducing offers related to these categories, as it would be a strategic move to enhance client retention.</p>
