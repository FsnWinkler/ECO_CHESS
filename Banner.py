
import moviepy.editor as mpe


clip = mpe.VideoFileClip("video.avi")
music = mpe.AudioFileClip("audio.wav")
banner = (mpe.ImageClip("banner1.jpg")
          .set_duration(clip.duration)
          .margin(right=0, top=0, opacity=0)  # (optional) logo-border padding
          .set_pos(("right", "top")))


banner2 = (mpe.ImageClip("banner2.jpg")
          .set_duration(clip.duration)
          .margin(right=0, top=0, opacity=0)  # (optional) logo-border padding
          .set_pos(("right", "bottom")))

add_audio_clip = clip.set_audio(music)
final_clip = mpe.CompositeVideoClip([add_audio_clip, banner, banner2])

final_clip.write_videofile("output_final.mp4")
