import os
import io
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import render
from django.middleware.csrf import get_token
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from pydub import AudioSegment
import speech_recognition as sr


def index(request):
    csrf_token = get_token(request)
    return render(request, 'index.html')
    

def upload_video(request):
    if request.method == 'POST' and request.FILES.get('video'):
        video = request.FILES['video']

        file_path = os.path.join(settings.MEDIA_ROOT, "video.mp4")
        with default_storage.open(file_path, 'wb+') as destination:
            for chunk in video.chunks():
                destination.write(chunk)
                
        audio_path = mp4_to_wav(file_path)
        transcript = speech_to_text(audio_path)

        return JsonResponse({'message': 'Video uploaded successfully!', 'transcript': transcript})

    return JsonResponse({'error': 'No video file uploaded'}, status=400)


def get_video(request):
    if len(os.listdir(settings.MEDIA_ROOT)):
        return JsonResponse({'url': request.build_absolute_uri(settings.MEDIA_URL + "video.mp4")})
    return JsonResponse({})


def mp4_to_wav(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The video file at {file_path} does not exist")

    audio = AudioSegment.from_file(file_path, format='mp4')
    audio_path = file_path.replace('.mp4', '.wav')
    audio.export(audio_path, format='wav')
    return audio_path


def speech_to_text(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as audio:
        speech = recognizer.record(audio)
        return "Sample transcript"
        try:
            text = recognizer.recognize_google(speech, language='pl-PL')
            print("Transkrypt: " + text)
            return text

        except:
            return "Nie rozpoznano"