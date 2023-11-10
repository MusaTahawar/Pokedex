import pypokedex
from PIL import Image, ImageTk
import tkinter as tk
import urllib3
from io import BytesIO

window = tk.Tk()
window.geometry("800x800")
window.title("Musa Pokedex")
window.config(padx=10, pady=10)

title_label = tk.Label(window, text="Musa Pokedex")
title_label.config(font=("Arial", 32))
title_label.pack(padx=10, pady=10)

pokemon_image = tk.Label(window)
pokemon_image.pack(padx=10, pady=10)

pokemon_information = tk.Label(window)
pokemon_information.config(font=("Arial", 20))
pokemon_information.pack(padx=10, pady=10)

pokemon_types = tk.Label(window)
pokemon_types.config(font=("Arial", 20))
pokemon_types.pack(padx=10, pady=10)

pokemon_base_stats = tk.Label(window)
pokemon_base_stats.config(font=("Arial", 20))
pokemon_base_stats.pack(padx=10, pady=10)

pokemon_weight = tk.Label(window)
pokemon_weight.config(font=("Arial", 20))
pokemon_weight.pack(padx=10, pady=10)

pokemon_height = tk.Label(window)
pokemon_height.config(font=("Arial", 20))
pokemon_height.pack(padx=10, pady=10)

pokemon_ability = tk.Label(window)
pokemon_ability.config(font=("Arial", 20))
pokemon_ability.pack(padx=10, pady=10)

def load_pokemon():
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
        pokemon_information.config(text="Pokémon not found")
        return

    # Fetch and display the Pokémon image
    http = urllib3.PoolManager()
    response = http.request("GET", pokemon.sprites.front.get('default'))
    image_data = Image.open(BytesIO(response.data))
    img = ImageTk.PhotoImage(image_data)
    pokemon_image.config(image=img)
    pokemon_image.image = img

    # Update labels with Pokémon information
    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}".title())
    pokemon_types.config(text=" - ".join([t for t in pokemon.types]))
    pokemon_base_stats.config(text=f"Base Stats: {pokemon.base_stats}")
    pokemon_weight.config(text=f"Weight: {pokemon.weight}")
    pokemon_height.config(text=f"Height: {pokemon.height}")
    abilities = [ability.name for ability in pokemon.abilities]
    pokemon_ability.config(text=f"Abilities: {', '.join(abilities)}")

label_id_name = tk.Label(window, text="ID or Name")
label_id_name.config(font=("Arial", 20))
label_id_name.pack(pady=10, padx=10)

text_id_name = tk.Text(window, height=1)
text_id_name.config(font=("Arial", 20))
text_id_name.pack(pady=10, padx=10)

btn_load = tk.Button(window, text="Load Pokemon", command=load_pokemon)
btn_load.config(font=("Arial", 20))
btn_load.pack(pady=10, padx=10)

window.mainloop()
