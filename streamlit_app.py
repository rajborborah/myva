import streamlit as st
from gtts import gTTS
import openai
import os
import tempfile

# Set up your OpenAI API key
openai.api_key = "your_openai_api_key"

def generate_response(prompt):
    """Generate response using OpenAI's GPT."""
    try:
        response = openai.Completion.create(
          engine="davinci",  # or another engine as needed
          prompt=prompt,
          temperature=0.7,
          max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        st.error("Failed to generate response from OpenAI.")
        return f"An error occurred: {str(e)}"

def text_to_speech(text, lang='en'):
    """Convert text to speech."""
    tts = gTTS(text=text, lang=lang)
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
        tts.save(fp.name)
        return fp.name

def main():
    st.title("Virtual Assistant with Voice")

    # Using a mockup GIF for dynamic display example
    st.image("https://media.giphy.com/media/3o7bu3XilJ5BOiSGic/giphy.gif", caption="Dynamic Display")

    user_input = st.text_input("How can I assist you today?")

    if user_input:
        # Generate a response using OpenAI's GPT
        response_text = generate_response(user_input)
        
        if response_text:
            # Display the generated text response
            st.write(response_text)

            # Convert the response to speech and play it
            audio_file_path = text_to_speech(response_text)
            st.audio(audio_file_path, format='audio/mp3', start_time=0)

            # Clean up
            os.remove(audio_file_path)

if __name__ == "__main__":
    main()
