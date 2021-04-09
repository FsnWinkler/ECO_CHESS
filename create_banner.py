import os
import ChessOpening
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import moviepy.editor as mpe


class Banner:
    def __init__(self, width, length, color):
        self.length = length
        self.width = width
        self.color = color

    def create_banner(self, filename, fonttype, title1, title2, title3):
        img = Image.new(mode="RGB", size=(self.width, self.length), color=self.color)
        self.width, self.length = img.size
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(fonttype, 20)
        font2 = ImageFont.truetype(fonttype, 22)
        w, h = draw.textsize(title1, font=font2)
        w2, h2 = draw.textsize(title2, font=font)
        w3, h3 = draw.textsize(title3, font=font)
        draw.text(((self.width - w) / 2, 5), text=title1, fill="white", font=font2)
        draw.text(((self.width - w2) / 2, 35), text=title2, fill="white", font=font)
        draw.text(((self.width - w3) / 2, 65), text=title3, fill="white", font=font)
        img.show()
        img.save(filename)

    def create_banner_bot(self, filename, fonttype, title1, title2, title3):
        img = Image.new(mode="RGB", size=(self.width, self.length), color=self.color)
        self.width, self.length = img.size
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(fonttype, 18)
        w, h = draw.textsize(title1, font=font)
        w2, h2 = draw.textsize(title2, font=font)
        w3, h3 = draw.textsize(title3, font=font)
        draw.text(((self.width - w) / 2, 10), text=title1, fill="white", font=font)
        draw.text(((self.width - w2) / 2, 40), text=title2, fill="white", font=font)
        draw.text(((self.width - w3) / 2, 70), text=title3, fill="white", font=font)
        img.show()
        img.save(filename)

    def create_final_vid(self):
        if "7." not in pgn_string_moves_only:
            title1 = chess_opening.pgn_string_moves_only
            title2 = " "
            title3 = " "

        elif "7." in pgn_string_moves_only and "13." not in pgn_string_moves_only:
            title1 = pgn_string_moves_only[0:pgn_string_moves_only.index("7.")]
            title2 = pgn_string_moves_only[pgn_string_moves_only.index("7."):len(pgn_string_moves_only)]
            title3 = " "

        elif "13." in pgn_string_moves_only:
            title1 = pgn_string_moves_only[0:pgn_string_moves_only.index("7.")]
            title2 = pgn_string_moves_only[pgn_string_moves_only.index("7."):pgn_string_moves_only.index("13.")]
            title3 = pgn_string_moves_only[pgn_string_moves_only.index("13."):len(pgn_string_moves_only)]

        opening = chess_opening.opening
        variation = chess_opening.variation

        if len(opening) < 2:
            opening = " "

        if len(variation) < 2:
            variation = " "

        # longest opening 1516
        # longest variation  2009
        # longest moves 1463

        # if len(pgn_string_moves_only) > 100:

        Bn = Banner(720, 100, "black")
        Bn.create_banner("banner1.jpg", "arial.ttf", chess_opening.eco_code, opening, variation)

        Bn2 = Banner(720, 100, "black")
        Bn2.create_banner_bot("banner2.jpg", "arial.ttf", title1, title2, title3)

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


if __name__ == '__main__':
    pgn_file_path = os.path.join(os.getcwd(), "ECO PGN", "eco.pgn")
    chess_openings = ChessOpening.load_chess_openings(pgn_file_path)
    chess_opening = chess_openings[1463]

    pgn_string_full = chess_opening.pgn_string
    pgn_string_moves_only = chess_opening.pgn_string_moves_only
    moves_amount = chess_opening.half_moves_amount
    Bn = Banner(720, 100, "black")
    Bn.create_final_vid()
