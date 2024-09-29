import os

class MyData:
    def __repr__(self) -> str:
        pass

    def create_audio_folder(self, folder_name: str) -> None:
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"Folder {folder_name} created")

    def create_transcription_folder(self, folder_name: str) -> None:
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"Folder {folder_name} created")