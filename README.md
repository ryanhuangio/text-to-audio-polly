# Text to Audio using Amazon AWS Polly

1. Edit `input.txt`
2. Install dependencies

```
pip install awscli
pip install python-decouple
pip install boto3
```

3. Rename `.env.sample` to `.env` and enter your credentials (you don't have to store it in your `.env`, you can store it anywhere)
4. Run `aws configure` and copy your credentials from `.env`
5. Run `python3 audio-polly.py`

# Text to Audio using Google Text to Speech (gTTS)

1. Edit `input.txt`
2. Install dependency

```
pip install gTTS
```

3. Run `python3 audio-gtts.py`
