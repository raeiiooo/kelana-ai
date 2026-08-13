def print_trip_summary(destination, country, days, budget, currency, travel_month):
        print("========================")
        print("KelanaAI")
        print("========================")
        print(f"Destination : {destination}")
        print(f"Country : {country}")
        print(f"Days        : {days}")
        print(f"Budget      : {budget}")
        print(f"Currency       : {currency}")
        print(f"Travel Month       : {travel_month}")

# Ask the user for the details tripwh
destination                 = input("Destination : ")
country                     = input("Country : ")
days                        = int(input("Days : "))
budget                      = float(input("Budget : "))
currency                    = input("Currency : ")
travel_month                = input("Travel Month : ")

# # Total Estimated Cost
# total_estimated_cost = hotel_cost + transportations_cost + food_cost + miscellaneous_cost

# Print the trip summary
print_trip_summary(destination, country, days, budget, currency, travel_month)
