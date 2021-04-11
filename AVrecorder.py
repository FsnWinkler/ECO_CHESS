import os
import glob
import multiprocessing
import mss
import pyaudio
import wave
import keyboard
import time
import datetime
import numpy
import cv2
import mss.tools
import moviepy.editor as mpe


def record_audio(start_time, record_sec=100):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    WAVE_OUTPUT_FILENAME = "audio.wav"
    RECORD_SECONDS = record_sec
    dev_index = 3

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index=dev_index,
                    frames_per_buffer=CHUNK)

    print("* recording")
    # sleep until start time
    time.sleep((start_time - datetime.datetime.now()).total_seconds())

    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

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


def record_video(start_time, capture_sec=100):
    filename = "video"
    SCREEN_SIZE = (720, 920)
    capture_duration = capture_sec

    print("Starte Aufnahme")
    # sleep until start time
    time.sleep((start_time - datetime.datetime.now()).total_seconds())

    print(datetime.datetime.now())

    frames = []

    start_time = time.time()

    while True:
        current_time = time.time()
        start = time.time()
        if current_time - start_time > capture_duration:
            break

        # The screen part to capture
        region = {'top': 80, 'left': 581, 'width': 720, 'height': 920}
        with mss.mss() as sct:
            # Grab the data
            img = sct.grab(region)
            # mss.tools.to_png(img.rgb, img.size, output=os.path.join(os.getcwd(), "cache", "img_{0}.png".format(i)))

            # Save to the picture file
            # mss.tools.to_png(img.rgb, img.size, output='dummy.png')

        # img = pyautogui.screenshot(region=(600, 125, 680, 700))
        frames.append(img)

        time.sleep(max(1. / 20 - (time.time() - start), 0))


    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    vid = cv2.VideoWriter(filename + ".avi", fourcc, 20.0, (SCREEN_SIZE))
    for img in frames:
        numpy_frame = numpy.array(img)
        frame = cv2.cvtColor(numpy_frame, cv2.COLOR_BGR2RGB)
        vid.write(frame)

    cv2.destroyAllWindows()
    vid.release()


def record_av(capture_time):
    p1 = multiprocessing.Process(target=record_audio, args=(capture_time,))
    p2 = multiprocessing.Process(target=record_video, args=(capture_time,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

