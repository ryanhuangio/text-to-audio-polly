from gtts import gTTS
import os

# Read text from an input.txt file
input_file = "input.txt"

try:
    with open(input_file, "r") as file:
        text = file.read()
except FileNotFoundError:
    print(f"File '{input_file}' not found.")
    exit(1)

# Create a gTTS object
tts = gTTS(text)

# Specify the filename for the output MP3 file
output_file = "output-ggts.mp3"

# Save the MP3 file
tts.save(output_file)

# Provide feedback to the user
print(f"MP3 file saved as {output_file}")

# Optionally, you can play the generated MP3
# Uncomment the following lines to play the MP3 using a default media player
# import platform
# if platform.system() == "Darwin":  # macOS
#     os.system(f"open {output_file}")
# elif platform.system() == "Windows":
#     os.system(output_file)
# else:  # Linux
#     os.system(f"xdg-open {output_file}")
