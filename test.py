import os
from NLP_work.pipeline.pipeline_script import Pipeline

root_dir = 'C:/Users/slota/Downloads/wetransfer_hackyeah-2024-breakwordtraps_2024-09-28_0449'
tgt_dir = 'C:/Users/slota/Desktop/transcript'

for video_path in os.listdir(root_dir):
    pipeline = Pipeline(video_path=os.path.join(root_dir, video_path))
    pipeline.create_transcript()
    pipeline.load_transcript()
    with open(os.path.join(tgt_dir, video_path.split('.')[0] + '.txt'), "w") as f:
        f.write(pipeline.transcript)