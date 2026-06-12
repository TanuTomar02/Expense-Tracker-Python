def expense_tracker():
    total_spent = 0
    print("--- Expense Tracker ---")
    print("Enter your expenses one by one. Type 'done' to finish.")

    while True:
        user_input = input("Enter expense amount: ")

        if user_input.lower() == 'done':
            break

        # Defensive coding to handle invalid data inputs
        try:
            # Transformation mechanism: converting input to integer
            expense = int(user_input)
            
            # Logic for accumulating the total
            total_spent = total_spent + expense
            print(f"Current Total: {total_spent}")
            
        except ValueError:
            # Shield interface for invalid input
            print("Invalid Data. Please enter a valid numerical amount.")

    print(f"\nFinal Total Spent: {total_spent}")

# Run the tracker
expense_tracker()