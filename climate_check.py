import tkinter as tk
import requests

def get_weather():
    city = city_entry.get().strip()

    if city == "":
        result_label.config(text="Please enter a city name")
        return

    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    geo_data = requests.get(geo_url).json()

    if "results" not in geo_data:
        result_label.config(text="City not found")
        return

    lat = geo_data["results"][0]["latitude"]
    lon = geo_data["results"][0]["longitude"]

    weather_url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&current_weather=true"
    )
    weather_data = requests.get(weather_url).json()

    temp = weather_data["current_weather"]["temperature"]
    wind = weather_data["current_weather"]["windspeed"]

    result_label.config(
        text=f"{city}\n🌡 {temp} °C\n💨 Wind: {wind} km/h"
    )

# ---------------- UI ----------------
root = tk.Tk()
root.title("Weather App")
root.geometry("300x300")

tk.Label(root, text="Enter City").pack(pady=10)

city_entry = tk.Entry(root, font=("Helvetica", 14))
city_entry.pack(pady=5)

tk.Button(root, text="Check Weather", command=get_weather).pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

root.mainloop()

