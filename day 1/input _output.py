name = input(" Enter the name:")
mobileno = int(input("Enter the mobile no:"))
product_1 = (input("Enter the product-1:"))
price_1 = float(input("Enter the price-1:"))
product_2 = (input("Enter the product-2:"))
price_2 = float(input("Enter the price-2:"))
product_3 = idle(input("Enter the product-3:"))
price_3 = float(input("Enter the price-3:"))

total_bill = price_1+price_2+price_3

print(f"{name} your bill")
print(f"{product_1} :${price_1}")
print(f"{product_2} :${price_2}")
print(f"{product_3} :${price_3}")
print(f"Total bill :{total_bill}")
