cost_price = float(input("Please enter the cost price:"))
selling_price = float(input("Please enter the selling price:"))
if(cost_price<selling_price):
    print("You get the Profit of Rupees:",selling_price - cost_price,"/- 😊")
elif(cost_price>selling_price):
    print("You get the Loss of Rupees:",cost_price-selling_price,"/- 😔")
else:
    print("No Loss & No Profit")