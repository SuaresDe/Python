ground_weight = 8.4

if ground_weight <= 2:
    ground_rate_per_pound = 1.50
elif ground_weight > 2 and ground_weight <= 6:
    ground_rate_per_pound = 3.00
elif ground_weight > 6 and ground_weight <= 10:
    ground_rate_per_pound = 4.00
else:
    ground_rate_per_pound = 4.75

ground_flat_charge = 20.00

total_ground_cost = (ground_weight * ground_rate_per_pound) + ground_flat_charge

premium_ground_cost = 125.00


drone_weight = 1.5

if drone_weight <= 2:
    drone_rate_per_pound = 4.50
elif drone_weight > 2 and drone_weight <= 6:
    drone_rate_per_pound = 9.00
elif drone_weight > 6 and drone_weight <= 10:
    drone_rate_per_pound = 12.00
else:
    drone_rate_per_pound = 14.25

total_drone_cost = drone_weight * drone_rate_per_pound

print(f"|||Shipping Cost Estimates|||")
print("")
print(f"Package 1 (Weight: {ground_weight} lbs):")
print(f"Standard Ground Shipping Cost: ${total_ground_cost:.2f}")
print(f"Premium Ground Shipping Cost: ${premium_ground_cost:.2f}")
print(f"")
print(f"Package 2 (Weight: {drone_weight} lbs):")
print(f"Drone Shipping Cost: ${total_drone_cost:.2f}")