# Upwork Transaction Analysis Script

## Problem:
Upwork doesn't provide any way to filter transactions based on preferences, such as calculating spending only on connects or subscription.

## Solution:
I created a Python Script that provides summary on the Transaction history you download from Upwork which you also are able to analyse by date. 

### Summary Includes:
- Total Earnings from hourly contracts
- Total Earnings from fixed price contracts
- Total Earnings from bonuses
- Total Earning from Upwork without cost
- Total Service Fee
- Total Withdrawal Fees
- Total Subscriptions Cost
- Total Connects Cost
- Connects + Membership Cost
- Total Cost on Upwork
- Total Withdrawal
- Total Earning from Upwork without Service Fees
- Total Earning from Upwork - Withdrawal Fees - Service Fees - Membership Fees

## How to Use:
1. Go to Upwork -> Reports -> Transaction History. Select a custom date for the statement period and download your whole transaction history on Upwork by clicking **Download CSV**.

<p align="center">
  <img src="https://github.com/shanto-datta/upwork-analysis/assets/55149956/10945da8-497a-4f0c-9777-0a1a5f24ffaa" alt="Upwork statement" style="width: 50%; height: 40%;">
</p>

2. Go to your desired directory in the command line and clone this git repository using the command: `git clone https://github.com/shanto-datta/upwork-analysis.git`

3. Navigate into the folder using: `cd upwork-analysis` on Linux or macOS.

4. Let's create a virtual environment that will take care of the dependencies we install: `python -m venv upwork`

5. Activate the virtual environment: `source upwork/bin/activate` (or on Windows: `source pilot-env/bin/activate`)

6. When you run this command in your terminal, you’ll notice that the prompt changes to include the name of the activated virtual environment. This indicates that the virtual environment is now active, and any Python commands you run will use the environment’s settings and packages.

7. Install pandas: `pip3 install pandas`

8. Copy the CSV file you downloaded in the first step to the current directory and rename it to `analysis.csv`

9. Run the Python script: `python3 upwork.py`.

10. Additionally, tweak with the date in `upwork.py` by changing code in these variables:

    ![Date variables](https://github.com/shanto-datta/upwork-analysis/assets/55149956/93178d35-9eb7-4725-af61-88d1640028e6)

11. **Rest Assured, Happy Hacking!**

#### Later, I will be adding some graphs for further investigation.
