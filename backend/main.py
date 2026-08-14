from services.trip_service import (
    calculate_daily_budget, 
    get_trip_category, 
    get_travel_season
)

def print_trip_summary(destination, days, budget, travel_month, recommended_places):
    # Hitung nilai dari logika bisnis
    category = get_trip_category(budget)
    daily_budget = calculate_daily_budget(budget, days)
    season = get_travel_season(travel_month)

    # Cetak ringkasan sesuai format tampilan target
    print("==================================")
    print("KelanaAI")
    print("==================================")
    print(f"Destination  : {destination}")
    print(f"Days         : {days}")
    print(f"Budget       : {int(budget)} USD")
    print(f"Category     : {category}")
    print(f"Daily Budget : {daily_budget} USD/Day")
    print(f"Travel Month : {travel_month}")
    print(f"Season : {season}")
    print()
    print("Recommended Places")
    for place in recommended_places:
        print(f"- {place}")

# List tempat rekomendasi
recommended_places = [
    "Tokyo Tower",
    "Shibuya",
    "Mount Fuji"
]

# Mengambil masukan (input) dari pengguna
destination  = input("Destination  : ")
days         = int(input("Days         : "))
budget       = float(input("Budget       : "))
travel_month = input("Travel Month : ")
print()

# Menampilkan hasil ringkasan
print_trip_summary(destination, days, budget, travel_month, recommended_places)