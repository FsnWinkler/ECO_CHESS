import os
import ChessOpening
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class Banner:
    def __init__(self, width, length, color):
        self.length = length
        self.width = width
        self.color = color

    def create_banner(self, filename, fonttype, title1, title2, title3):
        img = Image.new(mode="RGB", size=(self.width, self.length), color=self.color)
        self.width, self.length = img.size
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(fonttype, 18)
        font2 = ImageFont.truetype(fonttype, 22)
        w, h = draw.textsize(title1, font=font)
        w2, h2 = draw.textsize(title2, font=font)
        w3, h3 = draw.textsize(title3, font=font)
        draw.text(((self.width - w) / 2, 10), text=title1, fill="white", font=font2)
        draw.text(((self.width - w2) / 2, 40), text=title2, fill="white", font=font)
        draw.text(((self.width - w3) / 2, 70), text=title3, fill="white", font=font)
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


if __name__ == '__main__':
    pgn_file_path = os.path.join(os.getcwd(), "ECO PGN", "eco.pgn")
    chess_openings = ChessOpening.load_chess_openings(pgn_file_path)
    chess_opening = chess_openings[1516]



    pgn_string_full = chess_opening.pgn_string
    pgn_string_moves_only = chess_opening.pgn_string_moves_only
    moves_amount = chess_opening.half_moves_amount


    if len(pgn_string_moves_only) > 100:
        title1 = pgn_string_moves_only[0:80]
        title2 = pgn_string_moves_only[80:160]
        title3 = pgn_string_moves_only[160:len(pgn_string_moves_only)]

    else:
        title1 = chess_opening.pgn_string_moves_only
        title2 = " "
        title3 = " "


# longest opening 1516
# longest variation  2009
# longest moves 1463


   # if len(pgn_string_moves_only) > 100:



    Bn = Banner(720, 100, "black")
    Bn.create_banner("banner1.jpg", "arial.ttf", "{0} {1}".format(chess_opening.eco_code, chess_opening.opening), "{0}".format(chess_opening.variation))

    Bn2 = Banner(720, 100, "black")
    Bn2.create_banner_bot("banner2.jpg", "arial.ttf", title1, title2, title3)




#W, H = (720, 100)




