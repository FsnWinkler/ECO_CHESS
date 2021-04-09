import os
from simple_youtube_api.Channel import Channel
from simple_youtube_api.LocalVideo import LocalVideo

# set up credential paths
credentials_folder = os.path.join(os.getcwd(), "credentials")
client_secret_path = os.path.join(credentials_folder, "client_secret.json")
credentials_storage_path = os.path.join(credentials_folder, "credentials.storage")

# loggin into the channel
channel = Channel()
channel.login(client_secret_path, credentials_storage_path)

# setting up the video that is going to be uploaded
video = LocalVideo(file_path="output_final.mp4")

# setting snippet
video.set_title("My Title")
video.set_description("This is a description")
video.set_tags(["this", "tag"])
video.set_category("gaming")
video.set_default_language("en-US")

# setting status
video.set_embeddable(True)
video.set_license("creativeCommon")
video.set_privacy_status("private")
video.set_public_stats_viewable(True)

# setting thumbnail
# video.set_thumbnail_path('test_thumb.png')

# uploading video and printing the results
video = channel.upload_video(video)
print(video.id)
print(video)

# liking video
video.like()
