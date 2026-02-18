from PIL import Image

def generate_codex(text):
    letter_size = 64
    spacing = 8
    padding = 40

    text = text.upper()

    text_width = len(text) * (letter_size + spacing) - spacing
    text_height = letter_size

    width = text_width + padding * 2
    #height = text_height + padding * 2


    final_image = Image.new("RGBA", (width, 720), (255, 255, 255, 0))

    x = padding
    y = padding

    for char in text:
        if char == " ":
            x += letter_size + spacing
            continue
        if (x + letter_size + spacing) > 800:
            x = padding
            y += letter_size + spacing
        symbol = Image.open(f"fonts/Penguin_{char}.png")

        final_image.paste(symbol, (x, y), symbol)
        x += letter_size + spacing

    final_image.save("output.png")


generate_codex("This is the test of a longer sentence to test wrapping")