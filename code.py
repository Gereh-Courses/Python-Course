import pygame
import random
import numpy as np
import sys

pygame.init()

size = 400
cell_count = 4
cell_size = size // cell_count
background_color = (187, 173, 160)
cell_colors = {
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}
font = pygame.font.SysFont('arial', 20, bold=True)

score = 0
best_score = 0


def initialize_game():
    global score
    board = np.zeros((cell_count, cell_count), dtype=int)
    add_new_tile(board)
    add_new_tile(board)
    score = 0
    return board


def add_new_tile(board):
    free_positions = [(i, j) for i in range(cell_count) for j in range(cell_count) if board[i][j] == 0]
    if free_positions:
        i, j = random.choice(free_positions)
        board[i][j] = 2 if random.random() < 0.9 else 4


def compress(board):
    new_board = np.zeros((cell_count, cell_count), dtype=int)
    for i in range(cell_count):
        position = 0
        for j in range(cell_count):
            if board[i][j] != 0:
                new_board[i][position] = board[i][j]
                position += 1
    return new_board


def merge(board):
    global score
    for i in range(cell_count):
        for j in range(cell_count - 1):
            if board[i][j] == board[i][j + 1] and board[i][j] != 0:
                board[i][j] *= 2
                board[i][j + 1] = 0
                score += board[i][j]
    return board


def reverse(board):
    return np.array([row[::-1] for row in board])


def transpose(board):
    return np.transpose(board)


def move_left(board):
    board = compress(board)
    board = merge(board)
    board = compress(board)
    return board


def move(board, direction):
    if direction == 'LEFT':
        board = move_left(board)
    elif direction == 'RIGHT':
        board = reverse(move_left(reverse(board)))
    elif direction == 'UP':
        board = transpose(move_left(transpose(board)))
    elif direction == 'DOWN':
        board = transpose(reverse(move_left(reverse(transpose(board)))))
    add_new_tile(board)
    return board


def is_game_over(board):
    if 0 in board:
        return False
    for i in range(cell_count):
        for j in range(cell_count - 1):
            if board[i][j] == board[i][j + 1] or board[j][i] == board[j + 1][i]:
                return False
    return True


def draw_reset_button(screen):
    button_color = (142, 135, 123)
    button_rect = pygame.Rect(size - 120, 10, 100, 40)
    pygame.draw.rect(screen, button_color, button_rect)
    text = font.render('Reset', True, (255, 255, 255))
    screen.blit(text, (button_rect.x + 5, button_rect.y + 10))
    return button_rect


def draw_board(screen, board):
    screen.fill(background_color)
    for y in range(cell_count):
        for x in range(cell_count):
            value = board[y][x]
            color = cell_colors.get(value, (205, 193, 180))
            pygame.draw.rect(screen, color, (x * cell_size + 5, y * cell_size + 5, cell_size - 10, cell_size - 10))
            if value != 0:
                text = font.render(str(value), True, (0, 0, 0))
                text_rect = text.get_rect(center=(x * cell_size + cell_size // 2, y * cell_size + cell_size // 2))
                screen.blit(text, text_rect)

    global score, best_score
    best_score = max(score, best_score)
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    best_score_text = font.render(f'Best: {best_score}', True, (255, 255, 255))
    screen.blit(score_text, (20, 10))
    screen.blit(best_score_text, (180, 10))
    reset_button = draw_reset_button(screen)
    return reset_button

def main():
    global board, score, best_score
    screen = pygame.display.set_mode((size, size))
    pygame.display.set_caption('2048 Game')
    board = initialize_game()

    reset_button = draw_reset_button(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and reset_button.collidepoint(event.pos):
                board = initialize_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    board = move(board, 'UP')
                elif event.key == pygame.K_DOWN:
                    board = move(board, 'DOWN')
                elif event.key == pygame.K_LEFT:
                    board = move(board, 'LEFT')
                elif event.key == pygame.K_RIGHT:
                    board = move(board, 'RIGHT')

                if is_game_over(board):
                    print("Game Over!")

        reset_button = draw_board(screen, board)
        pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
