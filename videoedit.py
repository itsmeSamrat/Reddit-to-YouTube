import glob
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips, VideoFileClip, CompositeVideoClip
import pandas as pd
from mutagen.mp3 import MP3
import os

length_of_audio = []

df = pd.read_csv('database.csv')
post_id = df.iloc[-1, 0]
comment_df = pd.read_csv(f'assets/{post_id}/comments.csv')
post_title = df.iloc[-1, 1]

list_of_images = glob.glob(f'assets/{post_id}/*.png')
list_of_audio = glob.glob(f'assets/{post_id}/*.mp3')

for i in list_of_audio:
    length = MP3(i).info.length
    length_of_audio.append(length)

clip = []
# height = 1920
# width = 1080

path = f'C:/Users/tsamr/Desktop/everything/reddit to youtube/assets/{post_id}/picAudio'
if not os.path.exists(path):
    os.makedirs(path)


def createClip(screenshotFile, voiceOverFile, duration, i, post_id):
    imageClip = ImageClip(screenshotFile, duration=duration,
                          transparent=True).set_position(("center", "center"))
    audioClip = AudioFileClip(voiceOverFile)
    videoClip = imageClip.set_audio(audioClip)
#     videoClip_resized = videoClip.resize((x,y))
    # videoClip.write_videofile(f'assets/{post_id}/picAudio/{i}.mp4', fps=30)
    clip.append(videoClip)


for i in range(len(list_of_images)):
    createClip(list_of_images[i], list_of_audio[i],
               length_of_audio[i], i, post_id)


linking_clips = concatenate_videoclips(clip, method='compose')
# linking_clips.write_videofile(
#     f'assets/{post_id}/picAudio/linked_video.mp4', fps=30)
# linking_clips.preview(fps=30)

background = VideoFileClip(
    'background/GTA_1.mp4').subclip(5, sum(length_of_audio)).without_audio()

# # # background.write_videofile(f'test.mp4',fps=30)

finalVideo = CompositeVideoClip(
    clips=[background, linking_clips], use_bgclip=True)
# finalVideo.preview(fps=30)

output_file = f'assets/{post_id}/final_video.mp4'

finalVideo.write_videofile(output_file, codec='mpeg4',
                           threads=12, bitrate="8000k")
