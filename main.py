import pygame as pg
from heapq import *
from A_Star import a_star
from Dijkstra import dijkstra
from Bellman_Ford import bellman_ford

# Konumun merkezine yerleştirilen çemberin pozisyonunu döndürüyor
def get_circle(x, y):
    return (x * TILE + TILE // 2, y * TILE + TILE // 2), TILE // 7  # Çemberin merkezini ve yarıçapını döndür

# Komşu hücreleri kontrol ediyor
def neighbor_control(x, y):
    # Komşuların hangi yönlerde olduğunu belirleyen liste (sol, yukarı, sağ, aşağı)
    ways = [-1, 0], [0, -1], [1, 0], [0, 1]
    neighbor = []

    for dx, dy in ways:
        new_dx, new_dy = x + dx, y + dy
        # Komşu hücrelerin oyun alanı sınırları içinde olup olmadığını kontrol et
        if cols > new_dx >= 0 and rows > new_dy >= 0:
            neighbor.append((grid[new_dy][new_dx], (new_dx, new_dy)))  # Geçerli komşuyu listeye ekle
    return neighbor

# Fare ile tıklanan hücreyi seçiyor.
def get_click_mouse_pos():
    x, y = pg.mouse.get_pos()  # Fare imlecinin konumunu al
    grid_x, grid_y = x // TILE, y // TILE  # Imlecin bulunduğu grid hücresini bul
    pg.draw.circle(sc, pg.Color('black'), * ((grid_x * TILE + TILE // 2, grid_y * TILE + TILE // 2), TILE // 7))  # Hücrede kırmızı çember çiz
    click = pg.mouse.get_pressed()  # Fare tıklaması kontrolü
    return (grid_x, grid_y) if click[0] else False  # Sol tıklama yapılmışsa pozisyonu döndür, aksi halde False döndür

# Oyun alanının boyutları (kolonlar, satırlar ve hücre boyutu)
cols, rows = 12, 8
TILE = 70  # Her bir hücrenin piksel boyutu

# Pygame başlatma ve ekran ayarlama
pg.init()
sc = pg.display.set_mode([cols * TILE, rows * TILE])  
clock = pg.time.Clock()

# Oyun alanı için grid oluşturma (her hücrede maliyetler)
grid = [[4, 4, 4, 4, 4, 4, 4, 2, 3, 2, 4, 2], 
        [4, 4, 4, 4, 9, 9, 3, 2, 2, 4, 4, 4], 
        [4, 4, 2, 4, 2, 2, 2, 1, 1, 9, 9, 4], 
        [4, 2, 2, 4, 2, 2, 1, 1, 1, 4, 4, 2], 
        [1, 1, 2, 1, 1, 1, 1, 9, 1, 1, 1, 1], 
        [4, 1, 2, 1, 9, 2, 1, 1, 1, 9, 2, 2], 
        [4, 1, 4, 1, 2, 4, 4, 1, 1, 4, 4, 2], 
        [1, 1, 1, 1, 2, 4, 2, 2, 1, 2, 3, 2]]

# Oyun alanı için graph oluşturma (komşuluk ilişkileri ile)
graph = {}
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        graph[(x, y)] = graph.get((x, y), []) + neighbor_control(x, y)

# Başlangıç ve hedef konum
start = (0, 7)
goal = start
visited = []

# Arka plan resmi yükleme ve ölçeklendirme
bg = pg.image.load('./resim/map.jpg').convert()
bg = pg.transform.scale(bg, (cols * TILE, rows * TILE))

# Oyun döngüsü
while True:

    sc.blit(bg, (0, 0))  
    mouse_pos = get_click_mouse_pos() 
    if mouse_pos:
        #visited = a_star(graph, start, mouse_pos)  # A* algoritmasını çalıştır ve yolu bul
        #visited = dijkstra(graph, start, mouse_pos)  # dijkstra algoritmasını çalıştır ve yolu bul
        visited = bellman_ford(graph, start, mouse_pos)  # bellman_ford algoritmasını çalıştır ve yolu bul


        goal = mouse_pos  # Hedefi fare ile tıklanan pozisyona ayarla

    if visited:
        for path_segment in visited:
            pg.draw.circle(sc, pg.Color('blue'), *get_circle(*path_segment))  # Bulunan yol üzerindeki hücreleri maviyle işaretle
    pg.draw.circle(sc, pg.Color('green'), *get_circle(*start))  # Başlangıç hücresini yeşille işaretle
    pg.draw.circle(sc, pg.Color('red'), *get_circle(*goal))  # Hedef hücresini kırmızı işaretle

    [exit() for event in pg.event.get() if event.type == pg.QUIT]  
    pg.display.flip()  
    clock.tick(30) 
