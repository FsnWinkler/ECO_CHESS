import os
from simple_youtube_api.Channel import Channel
from simple_youtube_api.LocalVideo import LocalVideo
import time
import datetime
import ChessOpening


def upload_video(file_path, title, description, publishing_time, playlist_id):
    """"
    publishing_time: str - (YYYY-MM-DDThh:mm:ss.sZ) format (UTC is used), e.g. 2020-03-20T01:31:12.467113+00:00
    """
    # setting up the video that is going to be uploaded
    video = LocalVideo(file_path=file_path)

    # setting snippet
    video.set_title(title)
    video.set_description(description)
    video.set_tags(["Encyclopaedia", "Chess", "Openings", "Educational", "Book", "Training", "FIDE", "shorts"])
    video.set_category("education")
    video.set_default_language("en-US")


    # setting status
    video.set_embeddable(True)
    video.set_license("creativeCommon")
    video.set_privacy_status("private")
    video.set_public_stats_viewable(True)

    """ Sets time that video is going to be published at in
    (YYYY-MM-DDThh:mm:ss.sZ) format
    """
    # publishing time
    video.set_publish_at(publishing_time)

    # setting thumbnail
    # video.set_thumbnail_path('test_thumb.png')

    # uploading video and printing the results
    youtube_video = channel.upload_video(video)

    # add video to playlist
    time.sleep(60)
    channel.add_video_to_playlist(playlist_id, youtube_video.id)
    print(youtube_video.id)
    print(youtube_video)

    # liking video
    youtube_video.like()


def get_file_path(base_path, chess_opening, i):
    variation = "" if chess_opening.variation == "?" else "_{}".format(chess_opening.variation)
    filename = "{0}_{1}_{2}{3}.mp4".format(i, chess_opening.eco_code, chess_opening.opening, variation).replace("/", " ")
    full_path = os.path.join(base_path, filename)
    return full_path


def get_description(chess_opening, i):
    description = """Moves: {0}

Here is a short joke for free:
{1}


Please visit our channel for a complete video library of the Encyclopaedia of Chess Openings (ECO)!
    """.format(chess_opening.pgn_string_moves_only, get_joke(i))
    return description


def get_title(chess_opening):
    title = "ECO " + chess_opening.eco_code

    if len(chess_opening.opening) > 1:
        title = title + " " + chess_opening.opening
    if len(chess_opening.variation) > 1:
        title = title + ", " + chess_opening.variation

    title = title + " (White perspective)"
    return title


def get_joke(i):
    jokes_path = os.path.join(os.getcwd(), "jokes.csv")
    jokes = np.loadtxt(jokes_path, delimiter="|", dtype=str)[1:]

    joke_index = i % len(jokes)  # 1650 % 1600 = 50
    return jokes[joke_index][1][1:-1]


def get_playlist(chess_opening, variation):
    if variation == "white":
        if "A" in chess_opening.eco_code:
            if int(chess_opening.eco_code[1:]) < 40:
                playlist_id = "PL9AGUBhOdsVATEDVSlh4Ot6qtph3m4QwC"
            elif int(chess_opening.eco_code[1:]) < 45:
                playlist_id = "PL9AGUBhOdsVD-ve2zDwk56LfHSQJ0xexE"
            elif int(chess_opening.eco_code[1:]) < 50:
                playlist_id = "PL9AGUBhOdsVBYmuPJAvMHr-T4vdgin4ea"
            elif int(chess_opening.eco_code[1:]) < 80:
                playlist_id = "PL9AGUBhOdsVDFv9G5hOBn1U928dQ61j28"
            elif int(chess_opening.eco_code[1:]) < 100:
                playlist_id = "PL9AGUBhOdsVCODzq2PFcM7VzKintC6-Q-"
        if "B" in chess_opening.eco_code:
            if int(chess_opening.eco_code[1:]) < 10:
                playlist_id = "PL9AGUBhOdsVBYMgbsmifgjMqqB6wsWN0b"
            if int(chess_opening.eco_code[1:]) < 20:
                playlist_id = "PL9AGUBhOdsVBG3kpKJppoTLhO2J21AQix"
            if int(chess_opening.eco_code[1:]) < 100:
                playlist_id = "PL9AGUBhOdsVBMCofT1rM6pyrVF7FCdrkt"
        if "C" in chess_opening.eco_code:
            if int(chess_opening.eco_code[1:]) < 20:
                playlist_id = "PL9AGUBhOdsVB22xh7gnHLL3pUQQidK0lP"
            if int(chess_opening.eco_code[1:]) < 100:
                playlist_id = "PL9AGUBhOdsVCzYECJxNVWBo_fnq6pHzGe"
        if "D" in chess_opening.eco_code:
            if int(chess_opening.eco_code[1:]) < 70:
                playlist_id = "PL9AGUBhOdsVB21A9_es7djW3PKw3rFYgI"
            if int(chess_opening.eco_code[1:]) < 100:
                playlist_id = "PL9AGUBhOdsVC6Sm01UoGqWL77qHB80Kbm"
        if "E" in chess_opening.eco_code:
            if int(chess_opening.eco_code[1:]) < 60:
                playlist_id = "PL9AGUBhOdsVBvO6j8tjbVXF39Y7GpeFxd"
            if int(chess_opening.eco_code[1:]) < 100:
                playlist_id = "PL9AGUBhOdsVAJFmrz0FeSOgDbLfow7PU3"

    return playlist_id


def move_file_to_uploaded_folder(file_path, destination_folder):
    file_name = os.path.basename(file_path)
    destination_path = os.path.join(destination_folder, file_name)
    os.rename(file_path, destination_path)


def load_last_scheduled_release():
    with open(os.path.join(os.getcwd(), 'last_scheduled_release.txt'), 'r') as file:
        last_scheduled_release = file.read().replace('\n', '')
    return last_scheduled_release


def write_last_scheduled_release(last_scheduled_release_string):
    with open(os.path.join(os.getcwd(), 'last_scheduled_release.txt'), 'w') as filetowrite:
        filetowrite.write(last_scheduled_release_string)


if __name__ == '__main__':
    BASE_PATH = "E:\\Users\\winkl\\PycharmProjects\\pythonProject\\ECO_Chess_Openings\\Videos_60fps"
    BASE_PATH_UPLOADED = "E:\\Users\\winkl\\PycharmProjects\\pythonProject\\ECO_Chess_Openings\\Videos_60fps_uploaded"

    # set up credential paths
    credentials_folder = os.path.join(os.getcwd(), "credentials")
    client_secret_path = os.path.join(credentials_folder, "client_secret.json")
    credentials_storage_path = os.path.join(credentials_folder, "credentials.storage")

    # logging into the channel
    channel = Channel()
    channel.login(client_secret_path, credentials_storage_path)

    pgn_file_path = os.path.join(os.getcwd(), "ECO PGN", "eco.pgn")
    chess_openings = ChessOpening.load_chess_openings(pgn_file_path)

    for i, chess_opening in enumerate(chess_openings):
        file_path = get_file_path(BASE_PATH, chess_opening, i)
        if not os.path.isfile(file_path):
            continue

        last_scheduled_release_string = load_last_scheduled_release()
        last_scheduled_release = datetime.datetime.strptime(last_scheduled_release_string, '%Y-%m-%dT%H:%M:%S.%f%z')
        datetime_now = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)

        if datetime_now > last_scheduled_release:
            last_scheduled_release_string = (datetime_now + datetime.timedelta(0, 180)).replace(tzinfo=datetime.timezone.utc).isoformat()
        else:
            last_scheduled_release_string = (last_scheduled_release + datetime.timedelta(0, 180)).replace(tzinfo=datetime.timezone.utc).isoformat()

        write_last_scheduled_release(last_scheduled_release_string)

        time_string = last_scheduled_release_string
        print(time_string)



        title = get_title(chess_opening)
        description = get_description(chess_opening, i)
        playlist_id = get_playlist(chess_opening, "white")

        upload_video(file_path, title, description, time_string, playlist_id)

        move_file_to_uploaded_folder(file_path, BASE_PATH_UPLOADED)


