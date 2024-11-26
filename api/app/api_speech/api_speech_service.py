import os
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv


load_dotenv()
SPEECH_APIKEY = os.getenv('SPEECH_APIKEY')
SPEECH_REGION = os.getenv('SPEECH_REGION')

speech_config = speechsdk.SpeechConfig(subscription=SPEECH_APIKEY, region=SPEECH_REGION)
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

def speech_text(text) -> None:
    speech_config.speech_synthesis_voice_name='en-US-AvaMultilingualNeural'
    # file_name = "output.wav"
    # file_config = speechsdk.audio.AudioOutputConfig(filename= file_name)
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()
    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}]".format(text))
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")

