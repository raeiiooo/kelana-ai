def calculate_daily_budget(budget, days):
    # Mengembalikan nilai pembagian budget / days
    return int(budget / days) if (budget / days).is_integer() else budget / days

def get_trip_category(budget):
    if budget < 1000:
        return "Backpacker"
    elif budget <= 3000:
        return "Standard"
    else:
        return "Luxury"

def get_travel_season(month):
    # Mengubah teks bulan ke format Title case
    month_clean = month.strip().capitalize()
    
    if month_clean == "December":
        return "Peak Season"
    elif month_clean == "June":
        return "Holiday Season"
    else:
        return "Regular Season"