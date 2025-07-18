# Step 1: Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "AMZN": 3400,
    "MSFT": 300
}

# Step 2: Take user input for number of stocks
portfolio = {}
num_stocks = int(input("How many different stocks do you want to add? "))

# Step 3: Get stock name and quantity from user
for i in range(num_stocks):
    stock_name = input(f"Enter stock name #{i+1} (e.g., AAPL): ").upper()
    if stock_name not in stock_prices:
        print(f"Sorry, {stock_name} is not in our database.")
        continue
    quantity = int(input(f"Enter quantity of {stock_name}: "))
    portfolio[stock_name] = quantity

# Step 4: Calculate total investment
total_investment = 0
print("\n----- Portfolio Summary -----")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
    print(f"{stock}: {qty} shares x ${price} = ${value}")

print(f"\nTotal Investment Value: ${total_investment}")

# Step 5: (Optional) Save to file
save_option = input("\nDo you want to save the portfolio summary to a file? (yes/no): ").lower()

if save_option == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("----- Portfolio Summary -----\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock}: {qty} shares x ${price} = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}\n")
    print("Portfolio summary saved to 'portfolio_summary.txt'.")
