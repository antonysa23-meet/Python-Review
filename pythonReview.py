def create_youtube_video(title, description):
	youtubevideo = {"Title":title, "Description":description, "Likes":0, "Dislikes":0, "Comments":{},"Hashtag":[]}
	return youtubevideo


def like(youtubevideo):
	if "Likes" in youtubevideo:
		youtubevideo["Likes"] +=1

def dislike(youtubevideo):
	if "Dislikes" in youtubevideo:
		youtubevideo["Dislikes"] +=1

def add_comment(youtubevideo,username,comment_text):
	youtubevideo["Comments"][username]=comment_text

def add_hashtags(youtubevideo,hashtag):
	youtubevideo["Hashtag"] = hashtag

def similarity_to_video(Video_1,Video_2):
	x = 0
	for hashtag_1 in Video_1["Hashtag"]:
		for hashtag_2 in Video_2["Hashtag"]:
			if hashtag_1 ==hashtag_2:
				x+=1
	print("{0:.0%}".format(x / len(Video_1["Hashtag"])))

	
Video_no_1 = create_youtube_video("First Vid", "Amazing")
like(Video_no_1)
dislike(Video_no_1)
add_comment(Video_no_1,"antonio","Lets goooo")
add_hashtags(Video_no_1,["yes","wow","damn","challenge","eyy"])
print(Video_no_1)


Video_no_2 = create_youtube_video("Second Vid", "beaitful")
like(Video_no_2)
dislike(Video_no_2)
add_comment(Video_no_2,"fred","smh")
add_hashtags(Video_no_2,["no","wow","damn","easy","liked it"])
print(Video_no_2)
similarity_to_video(Video_no_1,Video_no_2)