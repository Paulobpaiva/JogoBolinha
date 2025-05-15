import pygame
import random
import sys

pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clicker Game - Níveis Progressivos")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Fonte
font = pygame.font.SysFont(None, 36)

# Relógio
clock = pygame.time.Clock()

# Variáveis do jogo
score = 0
level = 1
target_radius = 30
target_spawn_time = 2000
target_timer = 0

# Função para desenhar texto
def draw_text(text, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

# Função para gerar um novo alvo
def new_target():
    x = random.randint(target_radius, WIDTH - target_radius)
    y = random.randint(target_radius, HEIGHT - target_radius)
    return pygame.Rect(x - target_radius, y - target_radius, target_radius * 2, target_radius * 2)

# Inicializa o primeiro alvo
target = new_target()

while True:
    screen.fill(WHITE)

    # Verifica eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if target.collidepoint(event.pos):
                score += 1
                target = new_target()

    # Aumenta a dificuldade progressivamente
    if score % 5 == 0 and score != 0:
        level += 1
        target_spawn_time = max(500, target_spawn_time - 200)
        target_radius = max(10, target_radius - 2)
        score += 1  # Evita subir múltiplos níveis de uma vez

    # Desenha o alvo
    pygame.draw.circle(screen, RED, target.center, target_radius)

    # Exibe pontuação e nível
    draw_text(f"Score: {score}", BLACK, 10, 10)
    draw_text(f"Level: {level}", BLACK, 10, 50)

    pygame.display.flip()
    clock.tick(60)
