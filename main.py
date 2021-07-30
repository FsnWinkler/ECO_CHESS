import ChessOpening
import CreateVideo
import BrowserHandling
import datetime
import multiprocessing
import os
import time
import AVrecorder
import sys


if __name__ == '__main__':
    pgn_file_path = os.path.join(os.getcwd(), "ECO PGN", "eco.pgn")
    chess_openings = ChessOpening.load_chess_openings(pgn_file_path)
    errors = []
    y = 0
    i = 0
    while True:
        chess_opening = chess_openings[i]
    # longest opening 1516
    # longest variation  2009
    # longest moves 1463
        if i > 6000:
            break
        try:
            time_now_plus_min = datetime.datetime.now() + datetime.timedelta(0, 30)  # days, seconds, then other fields
            p1 = multiprocessing.Process(target=BrowserHandling.start_browser, args=(chess_opening.pgn_string,
                                                                                     chess_opening.half_moves_amount,
                                                                                     time_now_plus_min))
            p2 = multiprocessing.Process(target=AVrecorder.record_audio, args=(time_now_plus_min,
                                                                               chess_opening.half_moves_amount * 2.5 + 5))
            p3 = multiprocessing.Process(target=AVrecorder.record_video, args=(time_now_plus_min,
                                                                               chess_opening.half_moves_amount * 2.5 + 5))

            p1.start()
            p2.start()
            p3.start()
            p1.join()
            p2.join()
            p3.join()

            variation = "" if chess_opening.variation == "?" else "_{}".format(chess_opening.variation)
            filename = "{0}_{1}_{2}{3}.mp4".format(i, chess_opening.eco_code, chess_opening.opening, variation).replace("/", " ")
            full_path_filename = os.path.join("E:\\Users\\winkl\\PycharmProjects\\pythonProject\\ECO_Chess_Openings\\Videos_60fps", filename)

            if os.path.isfile(full_path_filename):
                filename = "{0}_{1}_{2}{3}_new.mp4".format(i, chess_opening.eco_code, chess_opening.opening, variation).replace("/", " ")
                full_path_filename = os.path.join("E:\\Users\\winkl\\PycharmProjects\\pythonProject\\ECO_Chess_Openings\\Videos_60fps", filename)
            CreateVideo.create_final_vid(full_path_filename, chess_opening)
            i += 1
            print(errors)
            time.sleep(5)

        except:
            errors.append(i)
            errors.append(sys.exc_info()[y])
            print(errors)
            print("Next entry.")
            y += 1
            i += 1
            time.sleep(5)
            continue

        # finally:
        #     time.sleep(5)
        #     print("failed and continue")
        #     continue

