
import os

def generate_sun_icon():
    # Gold color: #C6A75E
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#C6A75E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-sun"><circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/></svg>"""
    return svg_content

def generate_moon_icon():
    # Strong Blue color: #1C2A3A (Brand Blue)
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#1C2A3A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-moon"><path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/></svg>"""
    return svg_content

def main():
    target_dir = r"c:\Users\spart\Streaming de Google Drive\Mi unidad\Asesorías\Integrales\assets"
    os.makedirs(target_dir, exist_ok=True)
    
    with open(os.path.join(target_dir, "sun_icon.svg"), "w", encoding="utf-8") as f:
        f.write(generate_sun_icon())
        print(f"Generated {os.path.join(target_dir, 'sun_icon.svg')}")

    with open(os.path.join(target_dir, "moon_icon.svg"), "w", encoding="utf-8") as f:
        f.write(generate_moon_icon())
        print(f"Generated {os.path.join(target_dir, 'moon_icon.svg')}")

if __name__ == "__main__":
    main()
