# Variables store the trip data
# destination  = "Japan"
# days         = 5
# budget       = 1500
# travel_style = "Family"

# # Reuse them anywhere
# print(destination)        # → Japan
# print(days)               # → 5

# print()

# # Readable, labeled
# print(f"Destination : {destination}")
# print(f"Days        : {days}")
# print(f"Budget      : {budget}")
# print(f"Style       : {travel_style}")

# print()

# # Ask the user for trip details
# destination  = input("Destination : ")
# days         = int(input("Days : "))
# budget       = float(input("Budget : "))
# travel_style = input("Travel Style : ")

# # Now use them
# print(f"Destination : {destination}")
# print(f"Days        : {days}")
# print(f"Budget      : {budget}")

# print()

def print_trip_summary(destination, days, budget, travel_style, hotel_cost, transportations_cost, food_cost, miscellaneous_cost, total_estimated_cost):
        print("========================")
        print("KelanaAI")
        print("========================")
        print(f"Destination : {destination}")
        print(f"Days        : {days}")
        print(f"Budget      : {budget}")
        print(f"Style       : {travel_style}")
        print(f"Hotel Cost       : {hotel_cost}")
        print(f"Transportation Cost       : {transportations_cost}")
        print(f"Food Cost       : {food_cost}")
        print(f"Miscellaneous Cost       : {miscellaneous_cost}")
        print(f"Total Estimated Cost       : {total_estimated_cost}")

# Ask the user for the details tripwh
destination                 = input("Destination : ")
days                        = int(input("Days : "))
budget                      = float(input("Budget : "))
travel_style                = input("Travel Style : ")
hotel_cost                  = float(input("Hotel Cost : "))
transportations_cost        = float(input("Transportations Cost : "))
food_cost                   = float(input("Food Cost : "))
miscellaneous_cost          = float(input("Miscellaneous Cost : "))

# Total Estimated Cost
total_estimated_cost = hotel_cost + transportations_cost + food_cost + miscellaneous_cost

# Print the trip summary
print_trip_summary(destination, days, budget, travel_style, hotel_cost, transportations_cost, food_cost, miscellaneous_cost, total_estimated_cost)
