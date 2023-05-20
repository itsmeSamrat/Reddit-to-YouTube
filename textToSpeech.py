from gtts import gTTS
import pandas as pd
from mutagen.mp3 import MP3

length_of_speech = 0
count_comments = 1
df = pd.read_csv('database.csv')


# since we are primarily doing with url so every time we get something new, it will be at the end of our df.
post_title = df.iloc[-1, 1]
description_body = df.iloc[-1, -1]

full_title = post_title + description_body
post_id = df.iloc[-1, 0]


def textToSpeech(text, filename):
    length = 0
    tts = gTTS(text, lang='en')
    tts.save(f'assets/{post_id}/{filename}.mp3')
    length = MP3(f"assets/{post_id}/{filename}.mp3").info.length
    return length


length_of_speech += textToSpeech(full_title, 0)


comment_df = pd.read_csv(f'assets/{post_id}/comments.csv')

for i in (comment_df['Comment']):
    if length_of_speech > 50:
        break

    length_of_speech += textToSpeech(i, count_comments)
    # print(length_of_speech)
    # print(count_comments)
    count_comments += 1
