import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO

def get_weather():
    city = city_entry.get().strip() + ",IN"

    api_key = "0f5a49aa0f0c643c53fab0787fc8d493" 

    if city == "":
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"].capitalize()
        icon_code = data["weather"][0]["icon"]

        # Weather icon URL
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        icon_response = requests.get(icon_url)
        icon_img = Image.open(BytesIO(icon_response.content))
        icon_photo = ImageTk.PhotoImage(icon_img)

        icon_label.config(image=icon_photo)
        icon_label.image = icon_photo

        result_label.config(
            text=f"{city}\n🌡 {temp} °C\n☁ {weather}"
        )
    else:
        messagebox.showerror("Error", "City not found!")

# ---------------- UI Design ----------------
root = tk.Tk()
root.title("Weather App")
root.geometry("350x420")
root.configure(bg="#1e1e2f")
root.resizable(False, False)

title = tk.Label(
    root,
    text="🌦 Weather Checker",
    font=("Helvetica", 18, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title.pack(pady=15)

city_entry = tk.Entry(
    root,
    font=("Helvetica", 14),
    justify="center"
)
city_entry.pack(pady=10)
city_entry.insert(0, "Enter city name")

check_btn = tk.Button(
    root,
    text="Check Weather",
    font=("Helvetica", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=20,
    pady=5,
    command=get_weather
)
check_btn.pack(pady=15)

icon_label = tk.Label(root, bg="#1e1e2f")
icon_label.pack(pady=10)

result_label = tk.Label(
    root,
    text="",
    font=("Helvetica", 14),
    bg="#1e1e2f",
    fg="white"
)
result_label.pack(pady=10)

footer = tk.Label(
    root,
    text="Simple Python Weather App",
    font=("Helvetica", 9),
    bg="#1e1e2f",
    fg="gray"
)
footer.pack(side="bottom", pady=10)

root.mainloop()
