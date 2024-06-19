import pandas as pd
import matplotlib.pyplot as plt

def get_data_in_date_range(main_df, start_date, end_date):
    # Convert the date column to datetime format
    main_df['Date'] = pd.to_datetime(main_df['Date'])

    # Filter the DataFrame based on the date range
    filtered_df = main_df[(main_df['Date'] >= start_date) & (main_df['Date'] <= end_date)]

    # Print the filtered DataFrame
    return filtered_df

def get_plot(main_df):
    if not pd.api.types.is_datetime64_any_dtype(main_df['Date']):
        main_df['Date'] = pd.to_datetime(main_df['Date'])
    
    main_df['YearMonth'] = main_df['Date'].dt.to_period('M')

    # Membership Fee includes connects cost
    membership_df = main_df[main_df['Type'] == 'Membership Fee']
    subscription_df = main_df[(main_df['Description'] == 'Fees for Freelancer Plus membership') | (main_df['Description'] == 'Subscription Renewal Charges')]
    withdrawal_df = main_df[main_df['Type'] == 'Withdrawal']
    withdrawal_fees_df = main_df[main_df['Type'] == 'Withdrawal Fee']
    service_df = main_df[main_df['Type'] == 'Service Fee']
    fixed_price_df = main_df[main_df['Type'] == 'Fixed Price']
    hourly_df = main_df[main_df['Type'] == 'Hourly']
    bonus_df = main_df[main_df['Type'] == 'Bonus']

    monthly_data = main_df.groupby('YearMonth').sum(numeric_only=True)
    # Plotting the data
    plt.figure(figsize=(12, 6))
    plt.plot(monthly_data.index.astype(str), monthly_data['Amount'], label='Total Amount')
    
    for category, df in [('Earnings (Fixed Price)', fixed_price_df), 
                         ('Earnings (Hourly)', hourly_df), 
                         ('Earnings (Bonuses)', bonus_df), 
                         ('Service Fees', service_df), 
                         ('Withdrawal Fees', withdrawal_fees_df), 
                         ('Subscription Cost', subscription_df), 
                         ('Membership Fees', membership_df)]:
        monthly_category_data = df.groupby('YearMonth').sum(numeric_only=True)
        plt.plot(monthly_category_data.index.astype(str), monthly_category_data['Amount'], label=category)
    
    plt.xlabel('Month')
    plt.ylabel('Amount ($)')
    plt.title('Monthly Distribution of Upwork Transactions')
    plt.legend()
    plt.grid(True)
    plt.show()

def get_summary(main_df):
    # Membership Fee includes connects cost
    membership_df = main_df[main_df['Type'] == 'Membership Fee']
    subscription_df = main_df[(main_df['Description'] == 'Fees for Freelancer Plus membership') | (main_df['Description'] == 'Subscription Renewal Charges')]
    withdrawal_df = main_df[main_df['Type'] == 'Withdrawal']
    withdrawal_fees_df = main_df[main_df['Type'] == 'Withdrawal Fee']
    service_df = main_df[main_df['Type'] == 'Service Fee']
    fixed_price_df = main_df[main_df['Type'] == 'Fixed Price']
    hourly_df = main_df[main_df['Type'] == 'Hourly']
    bonus_df = main_df[main_df['Type'] == 'Bonus']

    total_earning = fixed_price_df['Amount'].sum() + hourly_df['Amount'].sum() + bonus_df['Amount'].sum()
    total_withdrawal = withdrawal_df['Amount'].sum()
    total_withdrawal_fees = withdrawal_fees_df['Amount'].sum()
    total_service_fees = service_df['Amount'].sum()
    total_membership_fees = membership_df['Amount'].sum()
    total_subscription_cost  = subscription_df['Amount'].sum()

    print(f"Total Earnings from fixed price contracts: ${fixed_price_df['Amount'].sum()}")
    print(f"Total Earnings from hourly contracts: ${hourly_df['Amount'].sum()}")
    print(f"Total Earnings from bonuses: ${bonus_df['Amount'].sum()}")
    print()
    print(f"Total Earning from Upwork without cost: ${total_earning}")
    print()
    print(f"Total Service Fees: ${total_service_fees}")
    print(f"Total Withdrawal Fees: ${total_withdrawal_fees}")
    print(f"Total Subscriptions Cost: ${total_subscription_cost}")
    print(f"Total Connects Cost: ${ total_membership_fees}")
    print(f"Connects + Membership Cost: ${total_membership_fees + total_subscription_cost}")
    print(f"Total Cost on Upwork: ${total_withdrawal_fees + total_service_fees + total_membership_fees}")
    print()
    print(f"Total Withdrawal: ${abs(total_withdrawal)}")
    print()
    print(f"Total Earning from Upwork without Service Fees: ${total_earning + total_withdrawal_fees + total_service_fees}")
    print(f"Total Earning from Upwork - WD Fees - Service Fees - Membership Fees: ${total_earning + total_withdrawal_fees + total_membership_fees + total_service_fees}")
    print()
    print(f"Return On Investment (ROI): {(abs(total_withdrawal))/abs(total_withdrawal_fees + total_service_fees + total_membership_fees)}x")

# Specify the path to your CSV file
# In case you place it in the same folder as the script and the CSV file is named 'analysis.csv'
csv_file = 'analysis.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file)

# Common pandas operations to explore the table 
# print(df.head())
# print(df.columns)
# print(df.dtypes)
# print(df.describe())

# Remove unnecessary columns
columns_to_remove = ['Currency', 'Enhanced PO Number', 'AWS Study Name - number', 'Agency', 'Freelancer', 'Amount in local currency', 'Balance', 'PO', 'Team', 'Ref ID', 'Account Name']
main_df = df.drop(columns=columns_to_remove)

# Get summary on the whole dataset
print()
print("Summary for the whole dataset")
print()
get_summary(main_df)


# Get summary on a date range'
start_date = 'Jan 20 2023'
end_date = 'Jan 01 2024'

data_in_date_range = get_data_in_date_range(main_df, start_date, end_date)
# Print the list of data in the date range
# print(data_in_date_range)

print()
print(f"Summary for the date range: {start_date} - {end_date}")
print()
get_summary(data_in_date_range)
get_plot(data_in_date_range)
