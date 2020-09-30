def reply_to_comment(r, comment_id, comment_reply, dictionary_type, comment_subreddit, comment_author, comment_body):
    try:
        comment_to_be_replied_to = r.comment(id=comment_id)
        comment_to_be_replied_to.reply(comment_reply)
        print ("\nReply details:\nSubreddit: r/{}\nComment: \"{}\"\nUser: u/{}\a". format(comment_subreddit, comment_body, comment_author))

    # Probably low karma so can't comment as frequently
    except Exception as e:
        time_remaining = 15
        if (str(e).split()[0] == "RATELIMIT:"):
            for i in str(e).split():
                if (i.isdigit()):
                    time_remaining = int(i)
                    break
            if (not "seconds" or not "second" in str(e).split()):
                time_remaining *= 60

        print (str(e.__class__.__name__) + ": " + str(e))
        for i in range(time_remaining, 0, -5):
            print ("Retrying in", i, "seconds..")
            time.sleep(5)
