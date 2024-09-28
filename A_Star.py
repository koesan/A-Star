from heapq import *

# A* algoritmasında kullanılacak olan heuristik fonksiyon
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # A ile B arasındaki Manhattan mesafesi

# Yolu geri döndürmek için kullanılan fonksiyon
def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from and came_from[current] is not None:
        current = came_from[current]
        total_path.append(current)  # Yolun parçalarını sırayla ekle
    return total_path[::-1]  # Yolu ters çevir, böylece başlangıç -> hedef sırası olur

def a_star(graph, start, goal):
    queue = []
    heappush(queue, (0, start))  # Başlangıç düğümünü maliyet 0 ile kuyruğa ekle
    g_score = {start: 0}  # Başlangıç düğümünün maliyeti 0
    came_from = {start: None}  # Her düğümün nereden geldiğini takip etmek için

    while queue:
        _, current = heappop(queue)  # En düşük maliyetli düğümü al

        if current == goal:
            return reconstruct_path(came_from, goal)  # Hedefe ulaşıldıysa yolu geri döndür

        # Mevcut düğümün komşularını dolaş
        for neighbor_cost, neighbor in graph[current]:
            tentative_g_score = g_score[current] + neighbor_cost  # Komşuya ulaşmanın maliyetini hesapla

            # Daha düşük maliyet bulunursa güncelle
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score  # En iyi g_score güncelle
                f_score = tentative_g_score + heuristic(neighbor, goal)  # Toplam maliyeti hesapla (g + h)
                heappush(queue, (f_score, neighbor))  # Komşuyu öncelik sırasına ekle
                came_from[neighbor] = current  # Bu komşuya, mevcut düğümden gelindi

    return None  # Eğer hedefe ulaşılamazsa None döndür

