import keys
import praw
import pandas as pd
import os

# checking the credentials
reddit = praw.Reddit(client_id=keys.Keys.reddit_consumer_key,
                     client_secret=keys.Keys.reddit_secret_key,
                     user_agent=keys.Keys.user_agent,
                     username=keys.Keys.reddit_username,
                     password=keys.Keys.reddit_password)

subreddit_url = "https://www.reddit.com/r/confession/comments/13i0quy/i_threw_a_friends_photo_album_in_the_garbage_when/"  # <change>


#####################################################################
# for first time running this code, run this, if you want to keep track of your reddit post, after first time comment this out
# df_dict = {"ID": [],
#            "Title": [],
#            "URL": [],
#            'SubReddit': [],
#            'Description': []}


# df = pd.DataFrame(df_dict)
# df.to_csv('database.csv', index=False)
#####################################################################

# getting the comments


def get_comment(id, submission):
    post_id = id
    comment = []
    path = f'{os.getcwd()}\\assets\\{post_id}'

    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

    for top_level_comment in submission.comments:
        if (len(top_level_comment.body.split()) < 100):
            comment.append([top_level_comment.id, top_level_comment.body])

    comment_df = pd.DataFrame(comment, columns=['ID', 'Comment'])
    filename = path + '\comments.csv'
    comment_df.to_csv(filename, index=False)
########################################################################


# getting the data of the url and saving its data in a csv file
df = pd.read_csv('database.csv')


def subreddit_url_data(subreddit_url):
    submission = reddit.submission(url=subreddit_url)
    check_id = submission.id
#     print(check_id)
    i = len(df)
    # ~ is used to negate the value
    if ~(df.empty) and (check_id in df['ID'].unique()):
        print(
            f'The id from the reddit post {check_id} matched with our id in our database.')
    else:
        df.loc[i, 'ID'] = check_id
        df.loc[i, 'Title'] = submission.title
        df.loc[i, 'URL'] = submission.url
        df.loc[i, 'SubReddit'] = submission.subreddit
        df.loc[i, 'Description'] = submission.selftext
        get_comment(check_id, submission)
    df.to_csv('database.csv', index=False)


subreddit_url_data(subreddit_url)

# print(df)
