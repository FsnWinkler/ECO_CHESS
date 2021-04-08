import multiprocessing
import mss
import pyaudio
import wave
import keyboard
import time
import datetime
import numpy
import cv2
import moviepy.editor as mpe


def record_audio():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    WAVE_OUTPUT_FILENAME = "audio.wav"
    dev_index = 3

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index=dev_index,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []
    while True:
        data = stream.read(CHUNK)
        frames.append(data)

        if keyboard.is_pressed('x'):
            print("Stoppe Aufnahme")
            break

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


def record_video():
    filename = "video"
    SCREEN_SIZE = (720, 920)

    print("Starte Aufnahme")
    print(datetime.datetime.now())

    frames = []
    while True:
        start = time.time()
        with mss.mss() as sct:
            # The screen part to capture
            region = {'top': 80, 'left': 581, 'width': 720, 'height': 920}

            # Grab the data
            img = sct.grab(region)

            # Save to the picture file
            #mss.tools.to_png(img.rgb, img.size, output='dummy.png')

        #img = pyautogui.screenshot(region=(600, 125, 680, 700))
        frames.append(img)
        if keyboard.is_pressed('x'):
            print("Stoppe Aufnahme")
            print(datetime.datetime.now())
            break
        time.sleep(max(1. / 24 - (time.time() - start), 0))

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    vid = cv2.VideoWriter(filename + ".avi", fourcc, 24.0, (SCREEN_SIZE))
    for img in frames:
        numpy_frame = numpy.array(img)
        frame = cv2.cvtColor(numpy_frame, cv2.COLOR_BGR2RGB)
        vid.write(frame)

    cv2.destroyAllWindows()
    vid.release()


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=record_audio)
    p2 = multiprocessing.Process(target=record_video)

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    clip = mpe.VideoFileClip("video.avi")
    music = mpe.AudioFileClip("audio.wav")

    final_clip = clip.set_audio(music)
    final_clip.write_videofile("output_final.mp4")
