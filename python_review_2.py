def create_youtube_video(title, description):
	video = {"title" : title, "description" : description, "likes" : 0, "dislikes" : 0, "comments" : {}} 

	return video

def like(video):
	if "likes" in video:
		video["likes"] = video["likes"]+1
	return video

def dislike(video):
	if "dislikes" in video:
		video["dislikes"] = video["dislikes"]+1
	return video
	
def add_comment(youtubevideo, username, comment_text):
	youtubevideo["comments"][username] = comment_text
	return video

video = create_youtube_video("hadar","hadar cohen")
like(video)
dislike(video)
add_comment(video,"hadar2","hadar cohen2")
print(video)



