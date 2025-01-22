print("""
NYC MetroCard Calculator
""")

pay_per_ride_cost = 2.90
unlimited_7day_cost = 34.00
unlimited_30day_cost = 132.00

ride_plan = int(input("Enter the number of rides you plan to take: "))
period = int(input("Enter the time period (in days) you plan to use the MetroCard: "))

pay_per_ride_total = ride_plan * pay_per_ride_cost

num_7day_passes = (period + 6) // 7
unlimited_7day_total = num_7day_passes * unlimited_7day_cost

num_30day_passes = (period // 7) + 1 if period % 7 != 0 else period // 7
unlimited_30day_total = num_30day_passes * unlimited_30day_cost

print("Calculating costs...")
print(f"""
Pay-per-Ride MetroCard:
- Total Cost: ${pay_per_ride_total:.2f}

Unlimited 7-Day MetroCard:
- Total Cost: ${unlimited_7day_total:.2f}

Unlimited 30-Day MetroCard:
- Total Cost: ${unlimited_30day_total:.2f}
""")

if pay_per_ride_total < unlimited_7day_total and pay_per_ride_total < unlimited_30day_total:
    print("Recommendation: The Pay-Per-Ride MetroCard is the most cost-effective option for you!")
elif unlimited_7day_total < unlimited_30day_total:
    print("Recommendation: The Unlimited 7-Day MetroCard is the most cost-effective option for you!")
else:
    print("Recommendation: The Unlimited 30-Day MetroCard is the most cost-effective option for you!")