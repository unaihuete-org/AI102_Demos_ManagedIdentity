# Python console app to test azure speech regonition and synthesis
from dotenv import load_dotenv
from datetime import datetime
import os
from azure.identity import DefaultAzureCredential
from playsound import playsound

# Import namespaces
import azure.cognitiveservices.speech as speech_sdk



def main():
    try:
        global speech_config

        # Get Configuration Settings
        # load_dotenv()
        cog_key = os.environ['COG_SERVICE_KEY_SPEECH']
        cog_region = 'eastus'

        # Configure speech service
        speech_config = speech_sdk.SpeechConfig(cog_key, cog_region)
        print('Ready to use speech service in:', speech_config.region)

        # Get spoken input
        command = TranscribeCommand()
        if command.lower() == 'what time is it?':
            TellTime()

    except Exception as ex:
        print(ex)

def TranscribeCommand():
    command = ''

    # Configure speech recognition
    # audio_config = speech_sdk.AudioConfig(use_default_microphone=True)
    # speech_recognizer = speech_sdk.SpeechRecognizer(speech_config, audio_config)
    # print('Speak now...')
    print('Transcribing audio file...') 
    audioFile = 'files/time.wav'
    print(audioFile)
    # playsound(audioFile)
    # print('Playing audio file...')
    audio_config = speech_sdk.AudioConfig(filename=audioFile)
    speech_recognizer = speech_sdk.SpeechRecognizer(speech_config, audio_config)

    # Process speech input
     # Process speech input
    speech = speech_recognizer.recognize_once_async().get()
    if speech.reason == speech_sdk.ResultReason.RecognizedSpeech:
        command = speech.text
        print(command)
    else:
        print(speech.reason)
        if speech.reason == speech_sdk.ResultReason.Canceled:
            cancellation = speech.cancellation_details
            print(cancellation.reason)
            print(cancellation.error_details)

    # Return the command
    return command


def TellTime():
    now = datetime.now()
    response_text = 'The time is {}:{:02d}'.format(now.hour,now.minute)

    print('telling time')
    # Configure speech synthesis
    # Configure speech synthesis
    speech_config.speech_synthesis_voice_name = "en-GB-RyanNeural"
    audio_config = speech_sdk.AudioConfig(filename="files/time-out.wav")
    speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config, audio_config)

    # Synthesize spoken output
     # Synthesize spoken output
    speak = speech_synthesizer.speak_text_async(response_text).get()
    if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
        print(speak.reason)

    # Print the response
    print(response_text)


if __name__ == "__main__":
    main()
