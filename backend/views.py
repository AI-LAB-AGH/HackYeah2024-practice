import os
import tempfile
import speech_recognition as sr
from django.http import JsonResponse
from moviepy.editor import VideoFileClip
from django.shortcuts import render
from django.middleware.csrf import get_token


def index(request):
    csrf_token = get_token(request)
    return render(request, 'index.html')
    

def process_video(request):
    if request.method == 'POST' and request.FILES.get('video'):
        video = request.FILES['video']

        temp_dir = tempfile.gettempdir()
        temp_file_path = os.path.join(temp_dir, video.name)

        with open(temp_file_path, 'wb+') as temp_file:
            for chunk in video.chunks():
                temp_file.write(chunk)

        audio_path = mp4_to_wav(temp_file_path)
        transcript = speech_to_text(audio_path)

        os.remove(temp_file_path)

        return JsonResponse( { "transcript": transcript }, status=201)

    return JsonResponse({'error': 'No video file uploaded'}, status=400)


def upload_video(request):
    if request.method == 'POST' and request.FILES.get('video'):
        video = request.FILES['video']
        blob_service_client = BlobServiceClient.from_connection_string("DefaultEndpointsProtocol=https;AccountName=hub17610921168;AccountKey=CASOXObgv/Qksm76gp2ps0kBvzZ910pKuYi2j0RILLdQjSKHMr0/I+PcE7NqWZKaM9VlphaKfGz2+AStAvJImg==;EndpointSuffix=core.windows.net")
        blob_client = blob_service_client.get_blob_client(container='hackathon', blob=video.name)
        blob_client.upload_blob(video.read(), overwrite=True)
        return JsonResponse( { "url": "url" }, status=201)

    return JsonResponse({'error': 'No video file uploaded'}, status=400)


def mp4_to_wav(file_path):
    audio_path = os.path.splitext(file_path)[0] + '.wav'
    with VideoFileClip(file_path) as video:
        video.audio.write_audiofile(audio_path)
    return audio_path


def speech_to_text(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as audio:
        speech = recognizer.record(audio)
        try:
            text = recognizer.recognize_google(speech, language='pl-PL')
            print("Transkrypt: " + text)
            return text

        except:
            return "Nie rozpoznano"