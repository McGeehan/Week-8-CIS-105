# Input salesperson's ID number
salesperson_id = input("Enter the salesperson's ID number: ")

# Input the number of items sold
num_items_sold = int(input("Enter the number of items sold: "))

# Input the total value of the items sold
total_value_sold = float(input("Enter the total value of the items sold: $"))

# Check if the salesperson is a high performer
if num_items_sold > 200:
    performance_status = "high performer"
else:
    performance_status = "not a high performer"

# Display the data message
print(f"Salesperson ID: {salesperson_id}")
print(f"Number of items sold: {num_items_sold}")
print(f"Total value of items sold: ${total_value_sold:.2f}")
print(f"Performance status: {performance_status}")
