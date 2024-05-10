from elevenlabs import play, save

class AudioGenerator:
    def __init__(self, client, voice="Sally Ford", model="eleven_multilingual_v2"):
        """
        Initializes the AudioGenerator with a specified client, voice, and model.

        :param client: The ElevenLabs client for generating audio.
        :param voice: The voice to use for audio generation (default: "Sally Ford").
        :param model: The model to use for audio generation (default: "eleven_multilingual_v2").
        """
        self.client = client
        self.voice = voice
        self.model = model

    def generate_audio(self, text: str, filename: str = "my-file.mp3"):
        """
        Generates audio from text and saves it to a file.

        :param text: The text to generate audio from.
        :param filename: The filename to save the generated audio (default: "my-file.mp3").
        """
        audio = self.client.generate(
            text=text,
            voice=self.voice,
            model=self.model
        )
        save(audio, filename)

# client = initialize_client()  # You'll need to initialize the client object.
# audio_generator = AudioGenerator(client)
# audio_generator.generate_audio("Hello, world!")
