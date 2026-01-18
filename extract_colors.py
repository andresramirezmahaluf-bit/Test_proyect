from PIL import Image
from collections import Counter
import sys

def get_palette(image_path):
    try:
        img = Image.open(image_path)
        img = img.convert("RGB")
        # Resize to speed up and simplify
        img = img.resize((100, 100))
        pixels = list(img.getdata())
        
        # Simple quantization: round to nearest 10 to group similar colors
        quantized = []
        for r, g, b in pixels:
            # Round to nearest 16 (hex-friendly ish)
            quantized.append((round(r/20)*20, round(g/20)*20, round(b/20)*20))
            
        counts = Counter(quantized)
        common = counts.most_common(10)
        
        print("Colores Dominantes (Aproximados):")
        for color, count in common:
            hex_col = '#{:02x}{:02x}{:02x}'.format(color[0], color[1], color[2])
            print(f"- {hex_col} (Frecuencia: {count})")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_palette(sys.argv[1])
    else:
        print("No file path provided")
