from decouple import config
import boto3

# Load AWS credentials from .env file
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')

# Create a Polly client
polly_client = boto3.client('polly', region_name='us-west-2')  # Set your AWS region

# Read text from an input.txt file
input_file = "input.txt"

try:
    with open(input_file, "r") as file:
        text = file.read()
except FileNotFoundError:
    print(f"File '{input_file}' not found.")
    exit(1)

# Specify the voice ID (e.g., 'Joanna') and text type (e.g., 'text')
voice_id = "Joanna"  # You can choose from various voices available in your region
text_type = "text"

# Define a maximum text length per request (adjust as needed)
max_text_length = 3000  # You can change this value based on your needs

# Split the text into smaller chunks
text_chunks = [text[i:i + max_text_length] for i in range(0, len(text), max_text_length)]

# Initialize an empty list to store the audio streams
audio_streams = []

# Generate speech for each text chunk
for chunk in text_chunks:
    response = polly_client.synthesize_speech(
        Text=chunk,
        OutputFormat="mp3",
        VoiceId=voice_id,
        TextType=text_type
    )
    audio_streams.append(response["AudioStream"].read())

# Concatenate the audio streams
combined_audio = b''.join(audio_streams)

# Save the combined MP3 file
output_file = "output.mp3"

with open(output_file, "wb") as file:
    file.write(combined_audio)

# Provide feedback to the user
print(f"MP3 file saved as {output_file}")
