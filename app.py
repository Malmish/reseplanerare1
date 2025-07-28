import streamlit as st

st.title("Reseplaneraren")
st.write("Hej! Denna app hjälper dig att planera din resebudget.")

def estimate_flight_cost(destination, season):
    base_prices = {
        "japan": 7000,
        "spanien": 3000,
        "usa": 6000,
        "thailand": 5000,
        "italien": 3500
    }
    season_multiplier = {
        "låg": 0.8,
        "mellan": 1.0,
        "hög": 1.3
    }
    base = base_prices.get(destination.lower(), 4000)
    multiplier = season_multiplier.get(season, 1.0)
    return round(base * multiplier)

def estimate_daily_cost(destination, level):
    costs = {
        "japan": {"snål": 400, "medel": 900, "lyx": 2000},
        "spanien": {"snål": 300, "medel": 700, "lyx": 1500},
        "usa": {"snål": 500, "medel": 1000, "lyx": 2500},
        "thailand": {"snål": 200, "medel": 500, "lyx": 1200},
        "italien": {"snål": 350, "medel": 800, "lyx": 1800},
    }
    default = {"snål": 300, "medel": 700, "lyx": 1500}
    return costs.get(destination.lower(), default)[level]

def estimate_accommodation_cost(level, days):
    hotel_prices = {
        "snål": 200,
        "medel": 600,
        "lyx": 2000
    }
    return hotel_prices[level] * days

def calculate_budget(destination, days, season):
    flight = estimate_flight_cost(destination, season)
    results = {}

    for level in ["snål", "medel", "lyx"]:
        daily = estimate_daily_cost(destination, level) * days
        hotel = estimate_accommodation_cost(level, days)
        total = flight + daily + hotel

        results[level] = {
            "flyg": flight,
            "boende": hotel,
            "övrigt": daily,
            "total": total
        }

    return results

st.title("✈️ Reseplanerare – Budgetkalkylator")

destination = st.text_input("Vart ska du resa?", "Thailand")
days = st.number_input("Hur många dagar ska du vara borta?", min_value=1, max_value=365, value=7)
season = st.selectbox("När reser du?", ["låg", "mellan", "hög"])

if st.button("Beräkna budget"):
    result = calculate_budget(destination, days, season)
    st.write(f"### Reseuppskattning för {destination.title()}")

    for level, data in result.items():
        st.write(f"**Budgetnivå: {level.capitalize()}**")
        st.write(f"✈️ Flyg: {data['flyg']} kr")
        st.write(f"🏨 Boende: {data['boende']} kr")
        st.write(f"🍜 Mat/Upplevelser: {data['övrigt']} kr")
        st.write(f"💰 Totalt: {data['total']} kr")
        st.write("---")
