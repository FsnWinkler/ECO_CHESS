import ChessOpening
import CreateVideo
import BrowserHandling
import datetime
import multiprocessing
import os
import copy
import AVrecorder


if __name__ == '__main__':
    pgn_file_path = os.path.join(os.getcwd(), "ECO PGN", "eco.pgn")
    chess_openings = ChessOpening.load_chess_openings(pgn_file_path)

    i = 0
    chess_opening = chess_openings[1463]  # 1463
    # if i > 4:
    #     break

    time_now_plus_min = datetime.datetime.now() + datetime.timedelta(0, 30)  # days, seconds, then other fields
    p1 = multiprocessing.Process(target=BrowserHandling.start_browser, args=(chess_opening.pgn_string,
                                                                             chess_opening.half_moves_amount,
                                                                             time_now_plus_min))
    p2 = multiprocessing.Process(target=AVrecorder.record_audio, args=(time_now_plus_min,
                                                                       chess_opening.half_moves_amount * 2.5 + 5))
    p3 = multiprocessing.Process(target=AVrecorder.record_video, args=(time_now_plus_min,
                                                                       chess_opening.half_moves_amount * 2.5 + 5))
    # p2 = multiprocessing.Process(target=CreateVideo.film, args=(chess_opening, time_now_plus_half_min))

    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()

    variation = "" if chess_opening.variation == "?" else "_{}".format(chess_opening.variation)
    filename = "{0}_{1}_{2}{3}.mp4".format(i, chess_opening.eco_code, chess_opening.opening, variation)

    CreateVideo.create_final_vid(filename, chess_opening)

    i += 1

    # pro1 = multiprocessing.Process(target=AVrecorder.record_audio, args=(10,))
    # pro2 = multiprocessing.Process(target=AVrecorder.record_video, args=(10,))
    # pro3 = multiprocessing.Process(target=BrowserHandling.start_clicking, args=(chess_opening,))

    # pro1.start()
    # pro2.start()
    # pro3.start()
    # pro1.join()
    # pro2.join()
    # pro3.join()
    




