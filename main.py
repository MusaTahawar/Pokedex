# Import necessary libraries
import pypokedex
from PIL import Image, ImageTk
import tkinter as tk
import urllib3
import random as rd
from io import BytesIO

# Constants for random values
WEIGHT_MIN = 10
WEIGHT_MAX = 20
HEIGHT_MIN = 1
HEIGHT_MAX = 9
EXPERIENCE_MIN = 55
EXPERIENCE_MAX = 75
STATS_MIN = 20
STATS_MAX = 50

# Create the main Tkinter window
window = tk.Tk()
window.geometry("900x800")
window.title("Unidex")
window.config(padx=10, pady=10)

# Define color scheme
background_color = "#303030"
text_color = "white"
button_color = "#4CAF50"

# Set a custom font for the entire application
custom_font = ("Helvetica", 14)

# Update the window background color
window.configure(bg=background_color)

# Create and pack labels for title, Pokemon image, and information
title_label = tk.Label(window, text="Unidex", font=("Arial", 32), bg=background_color, fg=button_color)
title_label.pack(padx=10, pady=10)

pokemon_image = tk.Label(window, bg=background_color)
pokemon_image.pack(padx=10, pady=10)

pokemon_information = tk.Label(window, font=custom_font, bg=background_color, fg=text_color)
pokemon_information.pack(padx=10, pady=10)

pokemon_types = tk.Label(window, font=custom_font, bg=background_color, fg=text_color)
pokemon_types.pack(padx=10, pady=10)

pokemon_weight = tk.Label(window, font=custom_font, bg=background_color, fg=text_color)
pokemon_weight.pack(padx=10, pady=10)

pokemon_height = tk.Label(window, font=custom_font, bg=background_color, fg=text_color)
pokemon_height.pack(padx=10, pady=10)

pokemon_ability = tk.Label(window, font=custom_font, bg=background_color, fg=text_color)
pokemon_ability.pack(padx=10, pady=10)

pokemon_expirience = tk.Label(window, font=custom_font, bg=background_color, fg=text_color)
pokemon_expirience.pack(padx=10, pady=10)

pokemon_stats = tk.Label(window, font=custom_font, bg=background_color, fg=text_color)
pokemon_stats.pack(padx=10, pady=(0, 0))

# Initialize shiny mode
shiny_mode = False

# Function to clear display labels
def clear_display():
    pokemon_image.config(image=None)
    pokemon_information.config(text="")
    pokemon_types.config(text="")
    pokemon_weight.config(text="")
    pokemon_height.config(text="")
    pokemon_ability.config(text="")
    pokemon_expirience.config(text="")
    pokemon_stats.config(text="")

# Function to fetch Pokemon data from pypokedex
def fetch_pokemon_data(pokemon_name):
    try:
        return pypokedex.get(name=pokemon_name)
    except Exception as e:
        print(f"Error fetching Pokémon data: {e}")
        return None

# Function to display Pokemon image using urllib3 and PIL
def display_pokemon_image(selected_sprite_key, url):
    http = urllib3.PoolManager()
    with http.request("GET", url, preload_content=False) as response:
        image_data = Image.open(BytesIO(response.data))
        img = ImageTk.PhotoImage(image_data)
        pokemon_image.config(image=img)
        pokemon_image.image = img

# Function to update labels with Pokemon information
def update_labels(pokemon, random_weight, random_height, random_expirience, random_stats):
    hp_stat = pokemon.base_stats.hp
    attack_stat = pokemon.base_stats.attack
    defense_stat = pokemon.base_stats.defense
    special_attack_stat = pokemon.base_stats.sp_atk
    special_defense_stat = pokemon.base_stats.sp_def
    speed_stat = pokemon.base_stats.speed

    # Update labels with Pokemon information
    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}".title(), fg="yellow")
    pokemon_types.config(text=" - ".join([t for t in pokemon.types]))
    pokemon_weight.config(text=f"Weight: {pokemon.weight + random_weight}")
    pokemon_height.config(text=f"Height: {pokemon.height + random_height:.2f}")
    pokemon_expirience.config(text=f"Experience: {pokemon.base_experience + random_expirience}")
    abilities = [ability.name for ability in pokemon.abilities]
    pokemon_ability.config(text=f"Abilities: {', '.join(abilities)}")
    pokemon_stats.config(
        text=f"Base Stats: HP: {hp_stat + random_stats:.1f} Attack: {attack_stat + random_stats:.1f} Defense: {defense_stat + random_stats:.1f} Special Attack: {special_attack_stat + random_stats:.1f} Special Defense: {special_defense_stat + random_stats:.1f} Speed: {speed_stat + random_stats:.1f}")

# Function to load Pokemon data and update UI
def load_pokemon():
    clear_display()
    random_weight = rd.randint(WEIGHT_MIN, WEIGHT_MAX)
    random_height = rd.randint(HEIGHT_MIN, HEIGHT_MAX)
    random_expirience = rd.randint(EXPERIENCE_MIN, EXPERIENCE_MAX)
    random_stats = rd.randint(STATS_MIN, STATS_MAX)

    global shiny_mode
    pokemon_name = text_id_name.get(1.0, "end-1c")
    pokemon = fetch_pokemon_data(pokemon_name)

    if pokemon:
        sprite_key = 'shiny' if shiny_mode else 'default'
        display_pokemon_image(sprite_key, pokemon.sprites.front.get(sprite_key))
        update_labels(pokemon, random_weight, random_height, random_expirience, random_stats)
    else:
        pokemon_information.config(text="Pokémon not found", fg="red")

# Function to toggle shiny mode and reload Pokemon image
def toggle_shiny_mode():
    global shiny_mode
    shiny_mode = not shiny_mode
    load_pokemon()

# Function to prevent Enter key from triggering the default action
def prevent_enter_key(event):
    return "break"

# Create labels and buttons for user interaction
label_id_name = tk.Label(window, text="ID or Name:", font=custom_font, bg=background_color, fg=text_color)
label_id_name.pack(pady=10, padx=10)

text_id_name = tk.Text(window, height=1, font=custom_font)
text_id_name.pack(pady=10, padx=10)
text_id_name.bind("<Return>", prevent_enter_key)

btn_load = tk.Button(window, text="Load Pokemon", command=load_pokemon, font=custom_font, bg=button_color, fg="white")
btn_load.pack(pady=10, padx=10)
btn_load.bind("<Return>", prevent_enter_key)

btn_toggle_shiny = tk.Button(window, text="Toggle Shiny", command=toggle_shiny_mode, font=custom_font, bg="red", fg="white")
btn_toggle_shiny.pack(pady=10, padx=10)

# Start the Tkinter event loop
window.mainloop()

# Last Commit and edited 28/01/2023
