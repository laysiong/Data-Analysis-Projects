<h1>PSPD Bank Credit Card Exploratory Data Analysis </h1>
Data Source: https://www.kaggle.com/datasets/darpan25bajaj/credit-card-exploratory-data-analysis
<br>last updated on 23/10/2023
<h2>Business Problem</h2>
In order to effectively produce quality decisions in the modern credit card industry, knowledge
must be gained through effective data analysis and modeling. Through the use of dynamic data-driven decision-making tools and procedures, information can be gathered to successfully evaluate all aspects of credit card operations. PSPD Bank has banking operations in more than 50 countries across the globe. Mr. Jim Watson, CEO, wants to <b>evaluate areas of bankruptcy, fraud, and collections, and respond to customer requests for help with proactive offers and service.</b>

<h2>About the Data</h2>
<b>This book has the following sheets:</b>
<ul>
  <li>Customer Acquisition: At the time of card issuing, the company maintains the details of customers.</li>
  <li>Spend (Transaction data): Credit card spend for each customer</li>
  <li>Repayment: Credit card Payment done by customer</li>
</ul>

<h2>Question to be answer</h2>
Based on the business problem, here is a list of questions that helped us to evaluate all aspects of credit card operation. 

<ol>
<li> Who are our customers? </li>
<li> What is their spending habit?</li>
<li> Are they repaying their credit card on time?</li>
<li> How many customers are in debt? </li>
<li> What is their Credit Score? </li>
<li> Who is more likely to go bankrupt? </li>
<li> Which transaction could potentially be a fraud?</li>
</ol>

<h2>Analysis</h2>
<h3>1. Who are the cilents?</h3>
<p>In a pool of 100 clients, the credit card users are divided into three tiers: Silver, Gold, and Platinum. The Gold tier not only reports the highest spending but also comprises the most substantial segment of users. Notably, 0.3%, which may equate to just one to two users in that tier, could have a significant influence on the results given our small sample size.</p>
 
<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/bb6a0d8a-6bd3-445a-a0fb-d507bc3b8337">
</p>

<p>Interestingly, 5.6% of credit card users under 20 years old mostly possess either Gold or Platinum tier cards.</p>

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/ad34315a-64a5-47dd-85c7-2b9bbb4cfdba">
</p>

<h3>Customer Locations: A Breakdown</h3>
<p>The top three cities our customers hail from are Bangalore, Cochin, and Calcutta.</p>

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/4de9e33d-04f4-4f6e-992a-337bd617c45a">  
</p>

<h3>2. What is their spending habit? </h3>
<p>The spending habits of our customers, regardless of tier, show consistency in preferences such as petrol, food, cameras, air tickets, train tickets, and shopping. This trend remains consistent across various age groups. The top five expenditure categories emerging prominently are petrol, cameras, food, air tickets, and train tickets.</p>

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/ee319557-c8ce-48c9-8b42-e248a97b346f">
</p>

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/3db902a9-b5d7-40f5-9097-d043b91cb84e">
</p>

<!---![image](https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/41083519-6e79-4500-9852-9fd2cda6e970)--->


<h3>3. Are they repaying their credit card on time?</h3>
<p>Nearly half of our customers, accounting for 48.4%, are late on their credit bill payments.</p>

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/e6038b10-ee93-4375-b92d-26882b7f0792">
</p>

Over the past three years, we've seen a rising trend in customers who are late on their credit bill payments. Notably, between February and July of 2006, there was a significant spike in late payments. One possible reason for this could be the influx of newer customers during this period.

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/7e8d9320-5ff8-4a59-999d-774e14593f22">
</p>

<!---!<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/d3dcd5fc-04e2-4503-b81e-f07edbcd79e8">
</p> --->

<p> Indeed, while our customer base has been expanding over the years, it isn't the driving factor behind the surge in late payments. Other underlying issues might be at play, warranting a deeper investigation.</p>

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/ada5fa2a-b876-4218-94d2-cf210a0df87b"> 
</p>

<p> When segmenting customers based on their tenure with us, it's evident that late payments have notably risen among our long-standing customers of 2 years or more. Furthermore, post-2006, there's a discernible uptick in late payments, particularly in the first half of the year. This trend warrants further investigation to understand the underlying causes. </p>

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/366f72e3-0cc5-4fa3-b44d-12dcef5b8327">
</p>

<h3>4.How many customers are in debt?</h3>
<p>At present, 45% of our customers carry a balance on their credit cards. While this might initially raise concerns, it's essential to note that this doesn't inherently signify a financial strain on their part. Some customers may just need an extended period to settle their balances.</p>

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/ecde6d90-a278-4959-87b5-24ebe9d83ea9">
</p>

<h3>5.What is their Credit Score?</h3>
<p> We've developed a risk profile for each customer based on two critical factors: the timeliness of their payments and whether they exceed their monthly credit limit. Using the information at our disposal, we assign a score to each customer, helping us determine their risk profile. Based on this metric system, 45% of clients fall into negative credit scores.
</p>

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/c701aad8-9a47-4de4-8d4a-d152e30bedb0">
</p>

<p>
When we look at the 'Repay to Spend Amount Ratio' for different age groups, many people have debt but are close to finishing their payments. Some customers are paying much more than they recently spent. This might mean they're clearing old debts.

Looking at credit scores by age, there's a worry: many customers under 60 are high-risk.

By card tier, silver and platinum cardholders often have lower credit scores.

Lastly, Bangalore, Calcutta, and Cochin have a higher number of people with low credit scores. This is likely because most of our users are from these areas.
</p>

</p>
<p align="center">
  <!---<img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/5770bde9-2aac-4321-adbf-9dccc2224c0b">--->
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/eb36ac16-9c0a-4560-aeea-92fd2e53600f">
</p>

<h3>6.Who is more likely to go bankrupt?</h3>
<p> Currently, our data shows that no customers have declared bankruptcy. To identify potential bankruptcy risks, we need to first establish our criteria for what would be considered a "bankrupt" profile. For this analysis, we define a customer as being on the verge of bankruptcy if:
  
<ol>
<li>They are unable to repay their outstanding debts.</li>
<li>Their outstanding debts are double the amount they've repaid.</li>
<li>There's a consistent monthly decrease in their repayment-to-spending ratio.</li>
<li>They have a poor credit score.</li>
</ol>

Based on these factors, we will assign merit or demerit points to each customer to assess their likelihood of declaring bankruptcy.

Out of our 100 clients, 17% fall into the high-risk category and are likely to declare bankruptcy based on our three defined factors. However, if we exclude those who made only a single transaction and then became inactive, this percentage might change.
</p>

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/8c6e2e56-5566-4d0a-841b-c64180b29570">
</p>

<p>Excluding clients who made only a single transaction and then became inactive, 3.2% of the remaining 63 clients, who frequently use the card, are at a high risk of bankruptcy.</p>
<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/5dc7e751-7abc-4202-84ef-f972da0df7fe">
</p>

<h3>7.Which transaction could potentially be a fraud?</h3>
<p> To determine the likelihood of transaction fraud, we'll consider several factors: the transaction location, the card user's origin location, whether the transaction has been fully repaid, and the consistency of the client's spending amount throughout the month. Based on these metrics, 36% of transactions are categorized as high-risk for fraud.
</p>

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/6f0f90de-7434-4306-adad-3e555ae12d6a">
</p>

<p>Of the transactions identified as high-risk for fraud, they account for 46.5% of the total spending amount across all transactions.</p>

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/ff86470c-c9f5-47cd-b161-bd5d76f73ebd">
</p>

<p>The three most common spending categories within these transactions are Train Tickets, Shopping, and Sandals.</p> 
<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/2f630f9f-5f34-4720-84e4-5eed765a1b89">
  <!---<img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/037cfb79-7d24-4dfa-aa30-f37b0fa0b476">--->
</p>

<p> Upon analyzing the high-risk transactions, 78.3% involve clients from the adult age group. However, given that 71.9% of our total clientele falls within the adult age bracket, this distribution is roughly proportional. Thus, it suggests a minimal likelihood of any age-specific targeted fraud.</p>

<p align="center">
  <img src="https://github.com/laysiong/Data-Analysis-Projects/assets/65546211/4a2c7a92-d424-4b1d-8cd0-246c27a01e86">
</p>

<h2>Conclusions</h2>

<h3>Bankruptcy</h3>
<p></p>Currently, none of our clients have filed for bankruptcy. Yet, our analysis reveals that 48.4% face challenges in settling their monthly credit debt. Alarmingly, a significant chunk of these late payments comes from loyal customers who have been with us for over two years.
<br></br>
While 45% of our client base is in debt, it's essential to shed light on the potential repercussions of their ongoing expenditure behaviors. If unchecked, many might be on a direct path to financial insolvency. From our predictive metrics, 17% of our total clientele is likely on the brink of bankruptcy. When we filter out those who have had only one transaction and ceased activity, 3.2% of the active 63 clients remain in the high-risk zone.
<br></br>
<b>Proposed Interventions:</b>
<ol>
<li><b>Financial Literacy Campaign</b>: Launch educational initiatives on wealth management to enlighten our clients about prudent financial behaviors.</li>
<li><b>Reminders</b>: Implement timely notifications towards the end of every month to alert clients about upcoming payments, thus preventing inadvertent delays.</li>
<li><b>Personalized Counseling</b>: Offer financial counseling sessions for high-risk clients to guide them through effective debt management strategies.</li>
</ol>
</p>

<h3>Fraud</h3>
<p>The data currently available to us is somewhat limited, hindering our ability to effectively identify fraudulent transactions. For a more holistic analysis, we'd benefit from a dataset that encompasses specifics like customers' spending behaviors, transaction locations (especially specific shops), and history of reported fraudulent activities.

Applying our existing fraud metric system to this data, we consider factors such as transaction and origin locations, repayment status, and the client's monthly spending consistency. Based on these criteria, 36% of the transactions are flagged as high risk, accounting for 46.5% of the total transactional value. Notably, the primary sectors these transactions fall into are Train Tickets, Shopping, and Sandals. These sectors might warrant extra vigilance on our part.

Interestingly, 78.3% of clients who fall into the adult age group are tagged as high-risk. Given that this demographic represents the majority of our client base, it's somewhat reassuring, suggesting there's a minimal likelihood of targeted scams.

For a more granular understanding, we need specifics such as the nature of the transaction (online or in-store), the exact order location, and, crucially, for our younger customers, details about the authorization of their card usage. Given that they are minors, discerning who granted them credit card access is vital. Their legal accountability being potentially limited raises concerns, as they might inadvertently become conduits for malicious activities, including fraud.
<br></br>
<b>Recommendations:</b>
<ol>
<li><b>Educate Clients</b>: Share information about common types of fraud, both online and offline, to heighten awareness. Offering guidelines on how to prevent such incidents can empower them to make safer transaction choices.</li>
<li><b>Enhanced Verification</b>: For accounts that display unusual spending patterns, implement a two-step verification process for purchases to add an extra layer of security.</li>
<li><b>Parental Control</b>: For accounts belonging to underage clients, consider introducing parental controls or guardian-approved transaction limits to prevent misuse. </li>
</ol>
</p>


<h3>Proactive Offers and Service</h3>
<p>In our continuous endeavor to better serve our customers, we've analyzed their spending habits. The most popular spending categories include Petrol, Camera, Food, Air Tickets, and Train Tickets. Digging deeper, we see a clear trend: a majority of these expenses are related to 'Transport'. Given this insight, introducing offers in these categories stands out as a smart strategy to boost customer loyalty.
<br></br>
<b>Solution:</b>
To capitalize on these spending patterns, we propose expanding our rewards program to give special emphasis on these categories. Additionally, partnering with businesses in these sectors could offer our customers exclusive deals, further promoting the use of our bank's credit card and enhancing customer retention.</p>
