import json
import azure.cognitiveservices.speech as speechsdk


def transcribe_audio_with_timestamps(audio_file_path):
    speech_key = "9cf400b6a7a3492c90b1ad0f6bd640f6"
    service_region = "westeurope"  # e.g., westus, eastus
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_config.request_word_level_timestamps()

    # Set the language to Polish
    speech_config.speech_recognition_language = "pl-PL"

    # Set up the audio input
    audio_input = speechsdk.AudioConfig(filename=audio_file_path)

    # Create a recognizer with detailed output format
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)
    speech_config.output_format = speechsdk.OutputFormat.Detailed

    # Perform the recognition
    result = speech_recognizer.recognize_once()

    # Check the result status
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print(f"Transcription: {result.text}")

        # Parse the JSON result for detailed information
        detailed_result = json.loads(result.json)

        # Extract word-level timestamps from the 'NBest' section of the result
        nbest_result = detailed_result['NBest'][0]
        words = nbest_result['Words']

        # Iterate through each word and print timestamps
        for word_info in words:
            word = word_info['Word']
            start_time = word_info['Offset'] / 10_000_000  # Convert from 100-nanosecond units to seconds
            duration = word_info['Duration'] / 10_000_000  # Convert from 100-nanosecond units to seconds
            print(f"Word: '{word}', Start Time: {start_time}s, Duration: {duration}s")
    
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized.")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print(f"Speech Recognition canceled: {cancellation_details.reason}")
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print(f"Error details: {cancellation_details.error_details}")

# Example usage with Polish language
transcribe_audio_with_timestamps("HY_2024_film_01.wav")
