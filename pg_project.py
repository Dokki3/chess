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
    fullname = os.path.join('data/', name)
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
    image = load_image("b_p.png", -1)

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
        # кушаем
        if x + 1 <= 7 and board[y + 1][x + 1] != 0:
            if type(board[y + 1][x + 1]) not in black_f:
                sl['eat'].append((x + 1, y + 1))
        if x - 1 >= 0 and board[y + 1][x - 1] != 0:
            if type(board[y + 1][x - 1]) not in black_f:
                sl['eat'].append((x - 1, y + 1))
        if y == 7:
            pass
        return sl


class White_Pawn(pygame.sprite.Sprite):
    image = load_image("w_p.png", -1)

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = White_Pawn.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_cord(self, x, y):
        self.rect.x = 80 + x * 70
        self.rect.y = 10 + y * 70

    def true_xod(self, board, x, y):
        sl = {'xod': [], 'eat': []}  # проверка выхода за границы
        if y == 6:
            if board[y - 1][x] == 0 and board[y - 2][x] == 0:
                sl['xod'].append((x, y - 2))
        if board[y - 1][x] == 0:
            sl['xod'].append((x, y - 1))
        # кушаем
        if x + 1 <= 7 and board[y - 1][x + 1] != 0:
            if type(board[y - 1][x + 1]) not in white_f:
                sl['eat'].append((x + 1, y - 1))
        if x - 1 >= 0 and board[y - 1][x - 1] != 0:
            if type(board[y - 1][x - 1]) not in white_f:
                sl['eat'].append((x - 1, y - 1))
        if y == 0:
            pass
        return sl

######################
#####################


class Black_Knight(pygame.sprite.Sprite):
    image = load_image("b_kn.png", -1)

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
            # кушаем
        if (y + 2 < 8) and (x + 1 < 8) and (board[y + 2][x + 1] != 0):
            if type(board[y + 2][x + 1]) not in black_f:
                sl['eat'].append((x + 1, y + 2))
        if (y + 2 < 8) and (x - 1 >= 0) and board[y + 2][x - 1] != 0:
            if type(board[y + 2][x - 1]) not in black_f:
                sl['eat'].append((x - 1, y + 2))
        if (y + 1 < 8) and (x - 2 >= 0) and board[y + 1][x - 2] != 0:
            if type(board[y + 1][x - 2]) not in black_f:
                sl['eat'].append((x - 2, y + 1))
        if (y + 1 < 8) and (x + 2 < 8) and board[y + 1][x + 2] != 0:
            if type(board[y + 1][x + 2]) not in black_f:
                sl['eat'].append((x + 2, y + 1))
        if (y - 2 >= 0) and (x + 1 < 8) and board[y - 2][x + 1] != 0:
            if type(board[y - 2][x + 1]) not in black_f:
                sl['eat'].append((x + 1, y - 2))
        if (y - 2 >= 0) and (x - 1 >= 0) and board[y - 2][x - 1] != 0:
            if type(board[y - 2][x - 1]) not in black_f:
                sl['eat'].append((x - 1, y - 2))
        if (y - 1 >= 0) and (x - 2 >= 0) and board[y - 1][x - 2] != 0:
            if type(board[y - 1][x - 2]) not in black_f:
                sl['eat'].append((x - 2, y - 1))
        if (y - 1 >= 0) and (x + 2 < 8) and board[y - 1][x + 2] != 0:
            if type(board[y - 1][x + 2]) not in black_f:
                sl['eat'].append((x + 2, y - 1))
        return sl



class White_Knight(pygame.sprite.Sprite):
    image = load_image("w_kn.png", -1)

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = White_Knight.image
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
            # кушаем
        if (y + 2 < 8) and (x + 1 < 8) and (board[y + 2][x + 1] != 0):
            if type(board[y + 2][x + 1]) not in white_f:
                sl['eat'].append((x + 1, y + 2))
        if (y + 2 < 8) and (x - 1 >= 0) and board[y + 2][x - 1] != 0:
            if type(board[y + 2][x - 1]) not in white_f:
                sl['eat'].append((x - 1, y + 2))
        if (y + 1 < 8) and (x - 2 >= 0) and board[y + 1][x - 2] != 0:
            if type(board[y + 1][x - 2]) not in white_f:
                sl['eat'].append((x - 2, y + 1))
        if (y + 1 < 8) and (x + 2 < 8) and board[y + 1][x + 2] != 0:
            if type(board[y + 1][x + 2]) not in white_f:
                sl['eat'].append((x + 2, y + 1))
        if (y - 2 >= 0) and (x + 1 < 8) and board[y - 2][x + 1] != 0:
            if type(board[y - 2][x + 1]) not in white_f:
                sl['eat'].append((x + 1, y - 2))
        if (y - 2 >= 0) and (x - 1 >= 0) and board[y - 2][x - 1] != 0:
            if type(board[y - 2][x - 1]) not in white_f:
                sl['eat'].append((x - 1, y - 2))
        if (y - 1 >= 0) and (x - 2 >= 0) and board[y - 1][x - 2] != 0:
            if type(board[y - 1][x - 2]) not in white_f:
                sl['eat'].append((x - 2, y - 1))
        if (y - 1 >= 0) and (x + 2 < 8) and board[y - 1][x + 2] != 0:
            if type(board[y - 1][x + 2]) not in white_f:
                sl['eat'].append((x + 2, y - 1))
        return sl


#################
#################


class Black_Bishop(pygame.sprite.Sprite):
    image = load_image("b_b.png", -1)

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = Black_Bishop.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_cord(self, x, y):
        self.rect.x = 80 + x * 70
        self.rect.y = 10 + y * 70

    def true_xod(self, board, x, y):
        print(x, y)
        sl = {'xod': [], 'eat': []}  # проверка выхода за границы + еда чужих
        y1 = y
        for i in range(x + 1, 8):
            y1 += 1
            if y1 < 8 and board[y1][i] == 0:
                sl['xod'].append((i, y1))
            elif y1 < 8:
                if type(board[y1][i]) in black_f:
                    break
                else:
                    sl['eat'].append((i, y1))
                    break

        y1 = y
        for i in range(x + 1, 8):
            y1 -= 1
            if y1 >= 0 and board[y1][i] == 0:
                sl['xod'].append((i, y1))
            elif y1 >= 0:
                if type(board[y1][i]) in black_f:
                    break
                else:
                    sl['eat'].append((i, y1))
                    break

        y1 = y
        for i in range(x - 1, -1, -1):
            y1 += 1
            if y1 < 8 and board[y1][i] == 0:
                sl['xod'].append((i, y1))
                #print('x', board[y1][i], (i, y1))
            elif y1 < 8:
                if type(board[y1][i]) in black_f:
                    break
                else:
                    sl['eat'].append((i, y1))
                    #print('e', board[y1][i], (i, y1))
                    break

        y1 = y
        for i in range(x - 1, -1, -1):
            y1 -= 1
            if y1 >= 0 and board[y1][i] == 0:
                sl['xod'].append((i, y1))
            elif y1 >= 0:
                if type(board[y1][i]) in black_f:
                    break
                else:
                    sl['eat'].append((i, y1))
                    break
        return sl
###############################################################################


class White_Bishop(pygame.sprite.Sprite):
    image = load_image("w_b.png", -1)

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = White_Bishop.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_cord(self, x, y):
        self.rect.x = 80 + x * 70
        self.rect.y = 10 + y * 70

    def true_xod(self, board, x, y):
        print(x, y)
        sl = {'xod': [], 'eat': []}  # проверка выхода за границы + еда чужих
        y1 = y
        for i in range(x + 1, 8):
            y1 += 1
            if y1 < 8 and board[y1][i] == 0:
                sl['xod'].append((i, y1))
            elif y1 < 8:
                if type(board[y1][i]) in white_f:
                    break
                else:
                    sl['eat'].append((i, y1))
                    break

        y1 = y
        for i in range(x + 1, 8):
            y1 -= 1
            if y1 >= 0 and board[y1][i] == 0:
                sl['xod'].append((i, y1))
            elif y1 >= 0:
                if type(board[y1][i]) in white_f:
                    break
                else:
                    sl['eat'].append((i, y1))
                    break

        y1 = y
        for i in range(x - 1, -1, -1):
            y1 += 1
            if y1 < 8 and board[y1][i] == 0:
                sl['xod'].append((i, y1))
                #print('x', board[y1][i], (i, y1))
            elif y1 < 8:
                if type(board[y1][i]) in white_f:
                    break
                else:
                    sl['eat'].append((i, y1))
                    #print('e', board[y1][i], (i, y1))
                    break

        y1 = y
        for i in range(x - 1, -1, -1):
            y1 -= 1
            if y1 >= 0 and board[y1][i] == 0:
                sl['xod'].append((i, y1))
            elif y1 >= 0:
                if type(board[y1][i]) in white_f:
                    break
                else:
                    sl['eat'].append((i, y1))
                    break
        return sl

#################
#################


class Black_Rook(pygame.sprite.Sprite):
    image = load_image("b_r.png", -1)

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = Black_Rook.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_cord(self, x, y):
        self.rect.x = 80 + x * 70
        self.rect.y = 10 + y * 70

    def true_xod(self, board, x, y):
        print(x, y)
        sl = {'xod': [], 'eat': []}  # проверка выхода за границы + еда чужих

        for i in range(x + 1, 8):
            if board[y][i] == 0 and y < 8:
                sl['xod'].append((i, y))
            elif y < 8:
                if type(board[y][i]) in black_f:
                    break
                else:
                    sl['eat'].append((i, y))
                    break

        for i in range(x - 1, -1, -1):
            if board[y][i] == 0 and y >= 0:
                sl['xod'].append((i, y))
            elif y >= 0:
                if type(board[y][i]) in black_f:
                    break
                else:
                    sl['eat'].append((i, y))
                    break

        for i in range(y + 1, 8):
            if board[i][x] == 0 and x < 8:
                sl['xod'].append((x, i))
            elif x < 8:
                if type(board[i][x]) in black_f:
                    break
                else:
                    sl['eat'].append((x, i))
                    break

        for i in range(y - 1, -1, -1):
            if board[i][x] == 0 and x >= 0:
                sl['xod'].append((x, i))
            elif x >= 0:
                if type(board[i][x]) in black_f:
                    break
                else:
                    sl['eat'].append((x, i))
                    break
        return sl


class White_Rook(pygame.sprite.Sprite):
    image = load_image("w_r.png", -1)

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = White_Rook.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_cord(self, x, y):
        self.rect.x = 80 + x * 70
        self.rect.y = 10 + y * 70

    def true_xod(self, board, x, y):
        print(x, y)
        sl = {'xod': [], 'eat': []}  # проверка выхода за границы + еда чужих

        for i in range(x + 1, 8):
            if board[y][i] == 0 and y < 8:
                sl['xod'].append((i, y))
            elif y < 8:
                if type(board[y][i]) in white_f:
                    break
                else:
                    sl['eat'].append((i, y))
                    break

        for i in range(x - 1, -1, -1):
            if board[y][i] == 0 and y >= 0:
                sl['xod'].append((i, y))
            elif y >= 0:
                if type(board[y][i]) in white_f:
                    break
                else:
                    sl['eat'].append((i, y))
                    break

        for i in range(y + 1, 8):
            if board[i][x] == 0 and x < 8:
                sl['xod'].append((x, i))
            elif x < 8:
                if type(board[i][x]) in white_f:
                    break
                else:
                    sl['eat'].append((x, i))
                    break

        for i in range(y - 1, -1, -1):
            if board[i][x] == 0 and x >= 0:
                sl['xod'].append((x, i))
            elif x >= 0:
                if type(board[i][x]) in white_f:
                    break
                else:
                    sl['eat'].append((x, i))
                    break
        return sl


#################
#################


class Black_Queen(pygame.sprite.Sprite):
    image = load_image("b_q.png", -1)

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = Black_Queen.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_cord(self, x, y):
        self.rect.x = 80 + x * 70
        self.rect.y = 10 + y * 70

    def true_xod(self, board, x, y):
        print(x, y)
        sl = {'xod': [], 'eat': []}  # проверка выхода за границы + еда чужих
        y1 = y
        for i in range(x + 1, 8):
            y1 += 1
            if y1 < 8 and board[y1][i] == 0:
                sl['xod'].append((i, y1))
            elif y1 < 8:
                if type(board[y1][i]) in black_f:
                    break
                else:
                    sl['eat'].append((i, y1))
                    break

        y1 = y
        for i in range(x + 1, 8):
            y1 -= 1
            if y1 >= 0 and board[y1][i] == 0:
                sl['xod'].append((i, y1))
            elif y1 >= 0:
                if type(board[y1][i]) in black_f:
                    break
                else:
                    sl['eat'].append((i, y1))
                    break

        y1 = y
        for i in range(x - 1, -1, -1):
            y1 += 1
            if y1 < 8 and board[y1][i] == 0:
                sl['xod'].append((i, y1))
                #print('x', board[y1][i], (i, y1))
            elif y1 < 8:
                if type(board[y1][i]) in black_f:
                    break
                else:
                    sl['eat'].append((i, y1))
                    #print('e', board[y1][i], (i, y1))
                    break

        y1 = y
        for i in range(x - 1, -1, -1):
            y1 -= 1
            if y1 >= 0 and board[y1][i] == 0:
                sl['xod'].append((i, y1))
            elif y1 >= 0:
                if type(board[y1][i]) in black_f:
                    break
                else:
                    sl['eat'].append((i, y1))
                    break

        for i in range(x + 1, 8):
            if board[y][i] == 0 and y < 8:
                sl['xod'].append((i, y))
            elif y < 8:
                if type(board[y][i]) in black_f:
                    break
                else:
                    sl['eat'].append((i, y))
                    break

        for i in range(x - 1, -1, -1):
            if board[y][i] == 0 and y >= 0:
                sl['xod'].append((i, y))
            elif y >= 0:
                if type(board[y][i]) in black_f:
                    break
                else:
                    sl['eat'].append((i, y))
                    break

        for i in range(y + 1, 8):
            if board[i][x] == 0 and x < 8:
                sl['xod'].append((x, i))
            elif x < 8:
                if type(board[i][x]) in black_f:
                    break
                else:
                    sl['eat'].append((x, i))
                    break

        for i in range(y - 1, -1, -1):
            if board[i][x] == 0 and x >= 0:
                sl['xod'].append((x, i))
            elif x >= 0:
                if type(board[i][x]) in black_f:
                    break
                else:
                    sl['eat'].append((x, i))
                    break
        return sl


class White_Queen(pygame.sprite.Sprite):
    image = load_image("w_q.png", -1)

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = White_Queen.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_cord(self, x, y):
        self.rect.x = 80 + x * 70
        self.rect.y = 10 + y * 70

    def true_xod(self, board, x, y):
        print(x, y)
        sl = {'xod': [], 'eat': []}  # проверка выхода за границы + еда чужих
        y1 = y
        for i in range(x + 1, 8):
            y1 += 1
            if y1 < 8 and board[y1][i] == 0:
                sl['xod'].append((i, y1))
            elif y1 < 8:
                if type(board[y1][i]) in white_f:
                    break
                else:
                    sl['eat'].append((i, y1))
                    break

        y1 = y
        for i in range(x + 1, 8):
            y1 -= 1
            if y1 >= 0 and board[y1][i] == 0:
                sl['xod'].append((i, y1))
            elif y1 >= 0:
                if type(board[y1][i]) in white_f:
                    break
                else:
                    sl['eat'].append((i, y1))
                    break

        y1 = y
        for i in range(x - 1, -1, -1):
            y1 += 1
            if y1 < 8 and board[y1][i] == 0:
                sl['xod'].append((i, y1))
                #print('x', board[y1][i], (i, y1))
            elif y1 < 8:
                if type(board[y1][i]) in white_f:
                    break
                else:
                    sl['eat'].append((i, y1))
                    #print('e', board[y1][i], (i, y1))
                    break

        y1 = y
        for i in range(x - 1, -1, -1):
            y1 -= 1
            if y1 >= 0 and board[y1][i] == 0:
                sl['xod'].append((i, y1))
            elif y1 >= 0:
                if type(board[y1][i]) in white_f:
                    break
                else:
                    sl['eat'].append((i, y1))
                    break

        for i in range(x + 1, 8):
            if board[y][i] == 0 and y < 8:
                sl['xod'].append((i, y))
            elif y < 8:
                if type(board[y][i]) in white_f:
                    break
                else:
                    sl['eat'].append((i, y))
                    break

        for i in range(x - 1, -1, -1):
            if board[y][i] == 0 and y >= 0:
                sl['xod'].append((i, y))
            elif y >= 0:
                if type(board[y][i]) in white_f:
                    break
                else:
                    sl['eat'].append((i, y))
                    break

        for i in range(y + 1, 8):
            if board[i][x] == 0 and x < 8:
                sl['xod'].append((x, i))
            elif x < 8:
                if type(board[i][x]) in white_f:
                    break
                else:
                    sl['eat'].append((x, i))
                    break

        for i in range(y - 1, -1, -1):
            if board[i][x] == 0 and x >= 0:
                sl['xod'].append((x, i))
            elif x >= 0:
                if type(board[i][x]) in white_f:
                    break
                else:
                    sl['eat'].append((x, i))
                    break
        return sl

#################
#################


class Black_King(pygame.sprite.Sprite):
    image = load_image("b_k.png", -1)

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = Black_King.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_cord(self, x, y):
        self.rect.x = 80 + x * 70
        self.rect.y = 10 + y * 70

    def true_xod(self, board, x, y):
        sl = {'xod': [], 'eat': []}
        if (y + 1 < 8) and (x + 1 < 8) and (board[y + 1][x + 1] == 0):
            sl['xod'].append((x + 1, y + 1))
        if (y + 1 < 8) and board[y + 1][x] == 0:
            sl['xod'].append((x, y + 1))
        if (y + 1 < 8) and (x - 1 >= 0) and board[y + 1][x - 1] == 0:
            sl['xod'].append((x - 1, y + 1))
        if (x + 1 < 8) and board[y][x + 1] == 0:
            sl['xod'].append((x + 1, y))
        if (x - 1 >= 0) and board[y][x - 1] == 0:
            sl['xod'].append((x - 1, y))
        if (y - 1 >= 0) and (x - 1 >= 0) and board[y - 1][x - 1] == 0:
            sl['xod'].append((x - 1, y - 1))
        if (y - 1 >= 0) and board[y - 1][x] == 0:
            sl['xod'].append((x, y - 1))
        if (y - 1 >= 0) and (x + 1 < 8) and board[y - 1][x + 1] == 0:
            sl['xod'].append((x + 1, y - 1))
            # кушаем
        if (y + 1 < 8) and (x + 1 < 8) and (board[y + 1][x + 1] != 0):
            if type(board[y + 1][x + 1]) not in black_f:
                sl['eat'].append((x + 1, y + 1))
        if (y + 1 < 8) and board[y + 1][x] != 0:
            if type(board[y + 1][x]) not in black_f:
                sl['eat'].append((x, y + 1))
        if (y + 1 < 8) and (x - 1 >= 0) and board[y + 1][x - 1] != 0:
            if type(board[y + 1][x - 1]) not in black_f:
                sl['eat'].append((x - 1, y + 1))
        if (x + 1 < 8) and board[y][x + 1] != 0:
            if type(board[y][x + 1]) not in black_f:
                sl['eat'].append((x + 1, y))
        if (x - 1 >= 0) and board[y][x - 1] != 0:
            if type(board[y][x - 1]) not in black_f:
                sl['eat'].append((x - 1, y))
        if (y - 1 >= 0) and (x - 1 >= 0) and board[y - 1][x - 1] != 0:
            if type(board[y - 1][x - 1]) not in black_f:
                sl['eat'].append((x - 1, y - 1))
        if (y - 1 >= 0) and board[y - 1][x] != 0:
            if type(board[y - 1][x]) not in black_f:
                sl['eat'].append((x, y - 1))
        if (y - 1 >= 0) and (x + 1 < 8) and board[y - 1][x + 1] != 0:
            if type(board[y - 1][x + 1]) not in black_f:
                sl['eat'].append((x + 1, y - 1))
        return sl


class White_King(pygame.sprite.Sprite):
    image = load_image("w_k.png", -1)

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = White_King.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_cord(self, x, y):
        self.rect.x = 80 + x * 70
        self.rect.y = 10 + y * 70

    def true_xod(self, board, x, y):
        sl = {'xod': [], 'eat': []}
        if (y + 1 < 8) and (x + 1 < 8) and (board[y + 1][x + 1] == 0):
            sl['xod'].append((x + 1, y + 1))
        if (y + 1 < 8) and board[y + 1][x] == 0:
            sl['xod'].append((x, y + 1))
        if (y + 1 < 8) and (x - 1 >= 0) and board[y + 1][x - 1] == 0:
            sl['xod'].append((x - 1, y + 1))
        if (x + 1 < 8) and board[y][x + 1] == 0:
            sl['xod'].append((x + 1, y))
        if (x - 1 >= 0) and board[y][x - 1] == 0:
            sl['xod'].append((x - 1, y))
        if (y - 1 >= 0) and (x - 1 >= 0) and board[y - 1][x - 1] == 0:
            sl['xod'].append((x - 1, y - 1))
        if (y - 1 >= 0) and board[y - 1][x] == 0:
            sl['xod'].append((x, y - 1))
        if (y - 1 >= 0) and (x + 1 < 8) and board[y - 1][x + 1] == 0:
            sl['xod'].append((x + 1, y - 1))
            # кушаем
        if (y + 1 < 8) and (x + 1 < 8) and (board[y + 1][x + 1] != 0):
            if type(board[y + 1][x + 1]) not in white_f:
                sl['eat'].append((x + 1, y + 1))
        if (y + 1 < 8) and board[y + 1][x] != 0:
            if type(board[y + 1][x]) not in white_f:
                sl['eat'].append((x, y + 1))
        if (y + 1 < 8) and (x - 1 >= 0) and board[y + 1][x - 1] != 0:
            if type(board[y + 1][x - 1]) not in white_f:
                sl['eat'].append((x - 1, y + 1))
        if (x + 1 < 8) and board[y][x + 1] != 0:
            if type(board[y][x + 1]) not in white_f:
                sl['eat'].append((x + 1, y))
        if (x - 1 >= 0) and board[y][x - 1] != 0:
            if type(board[y][x - 1]) not in white_f:
                sl['eat'].append((x - 1, y))
        if (y - 1 >= 0) and (x - 1 >= 0) and board[y - 1][x - 1] != 0:
            if type(board[y - 1][x - 1]) not in white_f:
                sl['eat'].append((x - 1, y - 1))
        if (y - 1 >= 0) and board[y - 1][x] != 0:
            if type(board[y - 1][x]) not in white_f:
                sl['eat'].append((x, y - 1))
        if (y - 1 >= 0) and (x + 1 < 8) and board[y - 1][x + 1] != 0:
            if type(board[y - 1][x + 1]) not in white_f:
                sl['eat'].append((x + 1, y - 1))
        return sl


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
        self.coords_circle_xod = []
        self.coords_circle_eat = []

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
        if self.board[cell[1]][cell[0]] != 0:
            for i in self.board[cell[1]][cell[0]].true_xod(self.board, cell[0], cell[1])['xod']:
                self.coords_circle_xod.append(i)
            for i in self.board[cell[1]][cell[0]].true_xod(self.board, cell[0], cell[1])['eat']:
                self.coords_circle_eat.append(i)

        if self.xod_user[0] == 1:
            self.coords_circle_xod = []
            self.coords_circle_eat = []
            x = cell[0]
            y = cell[1]
            if (x, y) in self.xod_user[3]['xod']:
                self.board[y][x] = self.board[self.xod_user[2]][self.xod_user[1]]
                self.board[self.xod_user[2]][self.xod_user[1]] = 0
            elif (x, y) in self.xod_user[3]['eat']:
                self.board[y][x].kill()  # уничтожаем спрайт
                self.board[y][x] = self.board[self.xod_user[2]][self.xod_user[1]]
                self.board[self.xod_user[2]][self.xod_user[1]] = 0
            self.show()
            self.xod_user[0] = (self.xod_user[0] + 1) % 2
            self.calc_cord()
        else:
            self.xod_user[1] = cell[0]
            self.xod_user[2] = cell[1]
            if self.board[cell[1]][cell[0]] != 0:
                self.xod_user[3] = self.board[cell[1]][cell[0]].true_xod(self.board, cell[0], cell[1])
                print('!', self.board[cell[1]][cell[0]].true_xod(self.board, cell[0], cell[1]))
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

    def render(self, surface):  # 125, 147, 93    235, 236, 211
        colors = [(125, 147, 93), (235, 236, 211)]
        col = 0
        for y in range(self.height):
            col = (col + 1) % 2
            for x in range(self.width):
                pygame.draw.rect(screen, colors[col],
                    (self.x + self.size * x, self.y + self.size * y, self.size, self.size))
                pygame.draw.rect(screen, (0, 0, 0),
                    (self.x + self.size * x, self.y + self.size * y, self.size, self.size), 1)
                col = (col + 1) % 2


####################
####################


black_f = [Black_Pawn, Black_Knight, Black_Bishop, Black_Rook, Black_Queen, Black_King]
white_f = [White_Pawn, White_Knight, White_Bishop, White_Rook, White_Queen, White_King]
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
    board.render(screen)
    all_sprites.draw(screen)
    if board.coords_circle_xod != []:
        for i in board.coords_circle_xod:
            pygame.draw.circle(screen, (255, 255, 0), (board.x + board.size * i[0] + 35,
                                                 board.y + board.size * i[1] + 35), 35)
    if board.coords_circle_eat != []:
        for i in board.coords_circle_eat:
            pygame.draw.circle(screen, (255, 0, 0, 50), (board.x + board.size * i[0] + 35,
                                                       board.y + board.size * i[1] + 35), 35)
    pygame.display.flip()

pygame.quit()
