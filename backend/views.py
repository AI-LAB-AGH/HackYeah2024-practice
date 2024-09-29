import os
import json
import tempfile
import speech_recognition as sr
from django.http import JsonResponse
from moviepy.editor import VideoFileClip
from django.shortcuts import render
from django.middleware.csrf import get_token
from django.http import FileResponse, HttpResponseNotFound
from NLP_work.pipeline.pipeline_script import Pipeline
from Machine_learning.vision_module import get_vision_anomaly_timestamps
from Machine_learning.audio_analyze import AnalyzeAudio

def index(request):
    csrf_token = get_token(request)
    return render(request, 'index.html')


def serve_temp_file(request):
    temp_file_path = request.session['temp_file_path']
    
    if os.path.exists(temp_file_path):
        return FileResponse(open(temp_file_path, 'rb'), content_type='video/mp4')
    else:
        return HttpResponseNotFound('File not found')
    

def delete_video(request):
    temp_file_path = request.session['temp_file_path']
    
    if os.path.exists(temp_file_path):
        os.remove(temp_file_path)
    else:
        return HttpResponseNotFound('File not found')


def process_video(request):
    if request.method == 'POST' and request.FILES.get('video'):
        video = request.FILES['video']

        temp_dir = tempfile.gettempdir()
        temp_file_path = os.path.join(temp_dir, video.name)
        request.session['temp_file_path'] = temp_file_path

        with open(temp_file_path, 'wb+') as temp_file:
            for chunk in video.chunks():
                temp_file.write(chunk)

        # text
        pipeline = Pipeline(video_path=temp_file_path)
        pipeline.create_transcript()
        pipeline.load_transcript()
        pipeline.clean_transcripts()

        print(pipeline.transcript)
        print(pipeline.get_fog_index())
        print(pipeline.do_tasks_on_video())

        # video
        video_timestamps = get_vision_anomaly_timestamps(video_path=temp_file_path, frame_interval=0.5)

        # audio
        audio_path = mp4_to_wav(temp_file_path)
        analyze_audio = AnalyzeAudio(audio_path)
        


        return JsonResponse( { "transcript": pipeline.transcript,
                              "timestamps": pipeline.result['NBest'][0]['Words'],
                              "url": temp_file_path }.update(video_timestamps), status=201)

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
        

def write_to_temp_json_file():
    data = [{"timestamp": 3.12, "type": 1},
    {"timestamp": 6.12, "type": 2},
    {"timestamp": 9.12, "type": 0},
    {"timestamp": 12.12, "type": 0},
    {"timestamp": 15.12, "type": 2},]

    with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as temp_file:
        json.dump(data, temp_file)
        return temp_file.name


def serve_temp_json_data(request):
    temp_file_path = write_to_temp_json_file()
    
    with open(temp_file_path, 'r') as json_file:
        json_data = json.load(json_file)

    return JsonResponse(json_data, safe=False)
