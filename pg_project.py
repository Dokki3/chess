import pygame
import sys
import os
from itertools import product

DISPLAY_SIZE = (800, 600)
pygame.init()
screen = pygame.display.set_mode(DISPLAY_SIZE)
all_sprites = pygame.sprite.Group()
#########################################################


def load_image(name, colorkey=None):
    fullname = os.path.join('', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image
#########################################################


class Black_Pawn(pygame.sprite.Sprite):
    image = load_image("Черная пешка.png", -1)

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = Black_Pawn.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_cord(self, x, y):
        self.rect.x = 80 + x * 70
        self.rect.y = 10 + y * 70

    def true_xod(self, board, x, y):
        sl = {'xod': [], 'eat': []} # проверка выхода за границы
        if y == 1:
            if board[y + 1][x] == 0 and board[y + 2][x] == 0:
                sl['xod'].append((x, y + 2))
        if board[y + 1][x] == 0:
            sl['xod'].append((x, y + 1))
        return sl


class White_Pawn(pygame.sprite.Sprite):
    image = load_image("Белая пешка.jpg", -1)

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = White_Pawn.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_cord(self, x, y):
        self.rect.x = 80 + x * 70
        self.rect.y = 10 + y * 70

######################
#####################


class Black_Knight(pygame.sprite.Sprite):
    image = load_image("Черный конь.png", -1)

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = Black_Knight.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_cord(self, x, y):
        self.rect.x = 80 + x * 70
        self.rect.y = 10 + y * 70

    def true_xod(self, board, x, y):
        sl = {'xod': [], 'eat': []} # проверка выхода за границы
        if (y + 2 < 8) and (x + 1 < 8) and (board[y + 2][x + 1] == 0):
            sl['xod'].append((x + 1, y + 2))
        if (y + 2 < 8) and (x - 1 >= 0) and board[y + 2][x - 1] == 0:
            sl['xod'].append((x - 1, y + 2))
        if (y + 1 < 8) and (x - 2 >= 0) and board[y + 1][x - 2] == 0:
            sl['xod'].append((x - 2, y + 1))
        if (y + 1 < 8) and (x + 2 < 8) and board[y + 1][x + 2] == 0:
            sl['xod'].append((x + 2, y + 1))
        if (y - 2 >= 0) and (x + 1 < 8) and board[y - 2][x + 1] == 0:
            sl['xod'].append((x + 1, y - 2))
        if (y - 2 >= 0) and (x - 1 >= 0) and board[y - 2][x - 1] == 0:
            sl['xod'].append((x - 1, y - 2))
        if (y - 1 >= 0) and (x - 2 >= 0) and board[y - 1][x - 2] == 0:
            sl['xod'].append((x - 2, y - 1))
        if (y - 1 >= 0) and (x + 2 < 8) and board[y - 1][x + 2] == 0:
            sl['xod'].append((x + 2, y - 1))
        return sl



class White_Knight(pygame.sprite.Sprite):
    image = load_image("Белый конь.png", -1)

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = White_Knight.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_cord(self, x, y):
        self.rect.x = 80 + x * 70
        self.rect.y = 10 + y * 70


#################
#################


class Black_Bishop(pygame.sprite.Sprite):
    image = load_image("Черный слон.png", -1)

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = Black_Bishop.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_cord(self, x, y):
        self.rect.x = 80 + x * 70
        self.rect.y = 10 + y * 70


class White_Bishop(pygame.sprite.Sprite):
    image = load_image("Белый слон.png", -1)

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = White_Bishop.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_cord(self, x, y):
        self.rect.x = 80 + x * 70
        self.rect.y = 10 + y * 70

#################
#################


class Black_Rook(pygame.sprite.Sprite):
    image = load_image("Черная ладья.png", -1)

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = Black_Rook.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_cord(self, x, y):
        self.rect.x = 80 + x * 70
        self.rect.y = 10 + y * 70


class White_Rook(pygame.sprite.Sprite):
    image = load_image("Белая ладья.png", -1)

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = White_Rook.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_cord(self, x, y):
        self.rect.x = 80 + x * 70
        self.rect.y = 10 + y * 70


#################
#################


class Black_Queen(pygame.sprite.Sprite):
    image = load_image("Черный ферзь.png", -1)

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = Black_Queen.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_cord(self, x, y):
        self.rect.x = 80 + x * 70
        self.rect.y = 10 + y * 70


class White_Queen(pygame.sprite.Sprite):
    image = load_image("Белый ферзь.png", -1)

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = White_Queen.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_cord(self, x, y):
        self.rect.x = 80 + x * 70
        self.rect.y = 10 + y * 70

#################
#################


class Black_King(pygame.sprite.Sprite):
    image = load_image("Черный король.png", -1)

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = Black_King.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_cord(self, x, y):
        self.rect.x = 80 + x * 70
        self.rect.y = 10 + y * 70


class White_King(pygame.sprite.Sprite):
    image = load_image("Белый король.png", -1)

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = White_King.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_cord(self, x, y):
        self.rect.x = 80 + x * 70
        self.rect.y = 10 + y * 70


################
################

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        for i in range(8):
            pawn1 = Black_Pawn(80 + i * 70, 80, all_sprites)
            self.board[1][i] = pawn1
        for i in range(8):
            pawn2 = White_Pawn(80 + i * 70, 430, all_sprites)
            self.board[6][i] = pawn2
        knight1 = Black_Knight(80 + 1 * 70, 10, all_sprites)
        self.board[0][1] = knight1
        knight1 = Black_Knight(80 + 6 * 70, 10, all_sprites)
        self.board[0][6] = knight1
        knight2 = White_Knight(80 + 1 * 70, 7 * 70 + 10, all_sprites)
        self.board[7][1] = knight2
        knight2 = White_Knight(80 + 6 * 70, 7 * 70 + 10, all_sprites)
        self.board[7][6] = knight2
        bishop1 = Black_Bishop(80 + 2 * 70, 10, all_sprites)
        self.board[0][2] = bishop1
        bishop1 = Black_Bishop(80 + 5 * 70, 10, all_sprites)
        self.board[0][5] = bishop1
        bishop2 = White_Bishop(80 + 2 * 70, 7 * 70 + 10, all_sprites)
        self.board[7][2] = bishop2
        bishop2 = White_Bishop(80 + 5 * 70, 7 * 70 + 10, all_sprites)
        self.board[7][5] = bishop2
        rook1 = Black_Rook(80 + 0 * 70, 10, all_sprites)
        self.board[0][0] = rook1
        rook1 = Black_Rook(80 + 7 * 70, 10, all_sprites)
        self.board[0][7] = rook1
        rook2 = White_Rook(80 + 0 * 70, 7 * 70 + 10, all_sprites)
        self.board[7][0] = rook2
        rook2 = White_Rook(80 + 7 * 70, 7 * 70 + 10, all_sprites)
        self.board[7][7] = rook2
        queen1 = Black_Queen(80 + 3 * 70, 10, all_sprites)
        self.board[0][3] = queen1
        queen2 = White_Queen(80 + 3 * 70, 7 * 70 + 10, all_sprites)
        self.board[7][3] = queen2
        king1 = Black_King(80 + 4 * 70, 10, all_sprites)
        self.board[0][4] = king1
        king2 = White_King(80 + 4 * 70, 7 * 70 + 10, all_sprites)
        self.board[7][4] = king2

        self.x = 10
        self.y = 10
        self.size = 30
        self.xod_user = [0, 0, 0, 0]

    def show(self):
        for i in self.board:
            for j in i:
                if j != 0:
                    print(1, end=' ')
                else:
                    print(0, end=" ")
            print()
        print()

    def set_view(self, left, top, cell_size):
        self.x = left
        self.y = top
        self.size = cell_size

    def get_cell(self, mouse_pos):
        board_x = (mouse_pos[0] - self.x) // self.size
        board_y = (mouse_pos[1] - self.y) // self.size
        if board_x < 0 or board_x > self.width or board_y < 0 or board_y > self.height:
            return None
        return board_x, board_y

    def on_click(self, cell):
        if self.xod_user[0] == 1:
            x = cell[0]
            y = cell[1]
            if (x, y) in self.xod_user[3]['xod']:
                self.board[y][x] = self.board[self.xod_user[2]][self.xod_user[1]]
                self.board[self.xod_user[2]][self.xod_user[1]] = 0
        else:
            self.xod_user[1] = cell[0]
            self.xod_user[2] = cell[1]
            print(self.board[cell[1]][cell[0]].true_xod(self.board, cell[0], cell[1]))
            self.xod_user[3] = self.board[cell[1]][cell[0]].true_xod(self.board, cell[0], cell[1])
        self.xod_user[0] = (self.xod_user[0] + 1) % 2
        self.calc_cord()

    def calc_cord(self):
        for i in range(8):
            for j in range(8):
                if self.board[i][j] != 0:
                    self.board[i][j].set_cord(j, i)

    def get_click(self, mouse_pos):
        cord = self.get_cell(mouse_pos)
        if cord is not None:
            self.on_click(cord)

    def render(self, surface):
        for x, y in product(range(self.width), range(self.height)):
            pygame.draw.rect(surface, 'black', (self.x + self.size * x, self.y + self.size * y,
                                                self.size, self.size), width=1)
####################
####################


board = Board(8, 8)
board.set_view(80, 10, 70)
board.show()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
        # elif event.type == pygame.KEYDOWN:
        #     board.show()

    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    board.render(screen)
    pygame.display.flip()

pygame.quit()
