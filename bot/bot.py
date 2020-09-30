import praw
import time
import os
import requests
import json
import bot_login
import re
from com_reply import reply_to_comment
target = "!q"

def run_bot(r, created_utc):
    try:
        comment_url = f"""https://api.pushshift.io/reddit/search/comment/?q={target}&sort=desc&size=50&fields=author,body,created_utc,id,subreddit&after=""" + created_utc

        parsed_comment_json = requests.get(comment_url).json()

        if (len(parsed_comment_json["data"]) > 0):
            created_utc = parsed_comment_json["data"][0]["created_utc"]

            for comment in parsed_comment_json["data"]:

                comment_author = comment["author"]
                comment_body = comment["body"]
                comment_id = comment["id"]
                comment_subreddit = comment["subreddit"]

                if (target in comment_body.lower() and comment_author != "queybot"):
                    print ("\n\nFound a comment!")

                    # action here

                    comment_reply += "\n\n\n\n---\n\n^(Beep boop. I am a bot. If there are any issues, contact my) [^Main ](https://www.reddit.com/message/compose/?to=queybot&subject=/u/q)\n\n^(Want to make a similar reddit bot? Check out: ) [^GitHub ](https://github.com/kylelobo/Reddit-Bot)"

                    reply_to_comment(r, comment_id, comment_reply, comment_subreddit, comment_author, comment_body)

                    print ("\nFetching comments..")

    except Exception as e:
        print (str(e.__class__.__name__) + ": " + str(e))

    return str(created_utc)

if __name__ == "__main__":
    while True:
        try:
            r = bot_login.bot_login()

            created_utc = ""

            print ("\nFetching comments..")
            while True:
                # Fetching all new comments that were created after created_utc time
                created_utc = run_bot(r, created_utc)
                time.sleep(10)

        except Exception as e:
            print (str(e.__class__.__name__) + ": " + str(e))
            cur.close()
            conn.close()
            time.sleep(15)
