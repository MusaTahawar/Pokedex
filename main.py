import pypokedex
from PIL import Image, ImageTk
import tkinter as tk
import urllib3
import random as rd
from io import BytesIO
from tkinter import Listbox


window = tk.Tk()
window.geometry("900x800")
window.title("Unidex")
window.config(padx=10, pady=10)

# Create a modern color scheme
background_color = "#303030"
text_color = "white"
button_color = "#4CAF50"

# Set a custom font for the entire application
custom_font = ("Helvetica", 14)

# Update the window background color
window.configure(bg=background_color)

title_label = tk.Label(window, text="Unidex", font=("Arial", 32), bg=background_color, fg=button_color)
title_label.pack(padx=10, pady=10)

pokemon_image = tk.Label(window, bg=background_color)
pokemon_image.pack(padx=10, pady=10)

pokemon_information = tk.Label(window, font=custom_font, bg=background_color, fg=text_color)
pokemon_information.pack(padx=10, pady=10)

pokemon_types = tk.Label(window, font=custom_font, bg=background_color, fg=text_color)
pokemon_types.pack(padx=10, pady=10)

# pokemon_base_stats = tk.Label(window, font=custom_font, bg=background_color, fg=text_color)
# pokemon_base_stats.pack(padx=10, pady=10)

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

shiny_mode = False  # Added variable to track shiny mode

#type advantages and disadvantages

def load_pokemon():
    random_weight = rd.randint(10,20)
    random_height = rd.randint(1,9)
    random_expirience = rd.randint(55,75)
    random_stats = rd.randint(20,50)
  
    
    global shiny_mode  # Make shiny_mode variable global

    # Clear the existing image and labels
    pokemon_image.config(image=None)
    pokemon_information.config(text="")
    pokemon_types.config(text="")

    # Get the Pokemon data
    pokemon_name = text_id_name.get(1.0, "end-1c")
    try:
        pokemon = pypokedex.get(name=pokemon_name)
    except Exception as e:
        # Handle the case where the Pokémon is not found
        pokemon_information.config(text="Pokémon not found", fg="red")
        return
    
    hp_stat = pokemon.base_stats.hp
    attack_stat = pokemon.base_stats.attack
    defense_stat = pokemon.base_stats.defense
    special_attack_stat = pokemon.base_stats.sp_atk
    special_defense_stat = pokemon.base_stats.sp_def
    speed_stat = pokemon.base_stats.speed
    
    # Fetch and display the Pokémon image (shiny if shiny_mode is True)
    
    sprite_key = 'shiny' if shiny_mode else 'default'
    http = urllib3.PoolManager()
    response = http.request("GET", pokemon.sprites.front.get(sprite_key))
    image_data = Image.open(BytesIO(response.data))
    img = ImageTk.PhotoImage(image_data)
    pokemon_image.config(image=img)
    pokemon_image.image = img

    # Update labels with Pokémon information
    
    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}".title(), fg="yellow")
    pokemon_types.config(text=" - ".join([t for t in pokemon.types]))
    # pokemon_base_stats.config(text=f"Base Stats: {pokemon.base_stats}")
    pokemon_weight.config(text=f"Weight: {pokemon.weight}")
    pokemon_height.config(text=f"Height: {pokemon.height}")
    pokemon_expirience.config(text=f"Expirience: {pokemon.base_experience}")
    abilities = [ability.name for ability in pokemon.abilities]
    pokemon_ability.config(text=f"Abilities: {', '.join(abilities)}")
    pokemon_stats.config(text=f"Base Stats: HP: {hp_stat} Attack: {attack_stat} Defense: {defense_stat} Special Attack: {special_attack_stat} Special Defense: {special_defense_stat} Speed: {speed_stat}")
    
    if sprite_key == 'shiny':
        
        pokemon_information.config(text=f"{pokemon.dex} - Shiny {pokemon.name}".title(), fg="red")
        pokemon_types.config(text=" - ".join([t for t in pokemon.types]))
        pokemon_weight.config(text=f"Weight: {pokemon.weight + random_weight}")
        pokemon_height.config(text=f"Height: {pokemon.height + random_height:.2f}")
        pokemon_expirience.config(text=f"Expirience: {pokemon.base_experience + random_expirience}")
        
        pokemon_stats.config(text=f"Base Stats: HP: {hp_stat + random_stats:.1f} Attack: {attack_stat + random_stats:.1f} Defense: {defense_stat + random_stats:.1f} Special Attack: {special_attack_stat + random_stats:.1f} Special Defense: {special_defense_stat + random_stats:.1f} Speed: {speed_stat + random_stats:.1f}")

def toggle_shiny_mode():
    global shiny_mode
    shiny_mode = not shiny_mode
    load_pokemon()  # Reload the Pokemon image with the updated shiny mode

def prevent_enter_key(event):
    return "break"

# Create a modern label for the input field

label_id_name = tk.Label(window, text="ID or Name:", font=custom_font, bg=background_color, fg=text_color)
label_id_name.pack(pady=10, padx=10)

text_id_name = tk.Text(window, height=1, font=custom_font)
text_id_name.pack(pady=10, padx=10)
text_id_name.bind("<Return>", prevent_enter_key)

# Create a modern button to load Pokemon

btn_load = tk.Button(window, text="Load Pokemon", command=load_pokemon, font=custom_font, bg=button_color, fg="white")
btn_load.pack(pady=10, padx=10)
btn_load.bind("<Return>", prevent_enter_key)

# Create a button to toggle shiny mode

btn_toggle_shiny = tk.Button(window, text="Toggle Shiny", command=toggle_shiny_mode, font=custom_font, bg="red", fg="white")
btn_toggle_shiny.pack(pady=10, padx=10)

window.mainloop()

# Last Commit and edited 11/23/2023
