<div align="center">

# Path Finding Algorithms

[](https://www.python.org/)
[](https://www.pygame.org/)
[](https://en.wikipedia.org/wiki/A*_search_algorithm)
[](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
[](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm)

Visual comparison of A*, Dijkstra, and Bellman-Ford algorithms with Pygame

https://github.com/user-attachments/assets/b8624274-dfc7-42a4-901d-85c8734f3065

## 🚀 Live Demo

[![Open in Spaces](https://img.shields.io/badge/🤗%20Hugging%20Face-Open%20in%20Spaces-yellow?style=for-the-badge&logo=huggingface&logoColor=white)](https://huggingface.co/spaces/koesan/pathfinding-algorithms)

**Try the interactive web version!** Click the button above to explore pathfinding algorithms in your browser - no installation required.

---

**[English](#english)** | **[Türkçe](#turkish)**

</div>

---

## <a name="english"></a>🇬🇧 English

# Path Finding Algorithms Visualizer

This project implements and visualizes three popular pathfinding algorithms: **A\***, **Dijkstra**, and **Bellman-Ford**. Built with Python and Pygame, it provides an interactive way to understand how different algorithms find the shortest path on a weighted grid.

## 🎯 Algorithms

### ⚡ A* (A-Star)

**Smart and Fast**

Uses both past cost and estimated distance to goal. Focuses toward the target, avoiding unnecessary exploration.

**Advantages:**

- ✅ Fastest algorithm
- ✅ Always finds optimal path
- ✅ Very efficient when goal is known

---

### 🔵 Dijkstra

**Classic and Guaranteed**

Finds shortest path from start to all nodes. Explores equally in all directions without focusing on goal.

**Advantages:**

- ✅ Always correct results
- ✅ Finds shortest paths to all nodes
- ✅ Simple and clear logic

---

### 🔴 Bellman-Ford

**Flexible and Robust**

Handles negative edge weights and detects negative cycles. Slower but more general-purpose.

**Advantages:**

- ✅ Supports negative edge weights
- ✅ Can detect negative cycles
- ✅ Works with complex graphs

---

## 🚀 How to Run

### Requirements

```bash
pip install pygame
```

### Run the Program

```bash
python main.py
```

### How to Use

1. **Click** on the grid to set a target destination
2. The algorithm will automatically calculate and display the shortest path
3. **Green circle** = Start position
4. **Red circle** = Target position
5. **Blue circles** = Shortest path

### Change Algorithm

Open `main.py` and uncomment the algorithm you want to use (lines 72-74):

```python
visited = a_star(graph, start, mouse_pos)        # A* Algorithm
# visited = dijkstra(graph, start, mouse_pos)    # Dijkstra Algorithm
# visited = bellman_ford(graph, start, mouse_pos) # Bellman-Ford Algorithm
```

## 📊 Features

- **Interactive Visualization** - Real-time pathfinding
- **Weighted Grid** - Different terrain costs (1-9)
- **Multiple Algorithms** - A*, Dijkstra, Bellman-Ford
- **Visual Feedback** - Color-coded paths and nodes

---

## <a name="turkish"></a>🇹🇷 Türkçe

# Yol Bulma Algoritmaları Görselleştirici

Bu proje, üç popüler yol bulma algoritmasını uygular ve görselleştirir: **A\***, **Dijkstra** ve **Bellman-Ford**. Python ve Pygame ile oluşturulmuş, farklı algoritmaların ağırlıklı bir grid üzerinde en kısa yolu nasıl bulduğunu anlamak için interaktif bir yol sunar.

## 🎯 Algoritmalar

### ⚡ A* (A-Star)

**Akıllı ve Hızlı**

Hem geçmiş maliyeti hem de hedefe tahmini mesafeyi kullanır. Hedefe doğru odaklanarak gereksiz yolları keşfetmez.

**Avantajları:**

- ✅ En hızlı algoritma
- ✅ Her zaman optimal yolu bulur
- ✅ Hedef bilinen durumlarda çok verimli

---

### 🔵 Dijkstra

**Klasik ve Garantili**

Başlangıçtan her noktaya en kısa yolu bulur. Tüm yönlere eşit şekilde yayılarak ilerler, hedefe odaklanmaz.

**Avantajları:**

- ✅ Her zaman doğru sonuç verir
- ✅ Tüm noktalara en kısa yolu bulur
- ✅ Basit ve anlaşılır mantık

---

### 🔴 Bellman-Ford

**Esnek ve Güçlü**

Negatif maliyetli yolları destekler ve negatif döngüleri tespit eder. Daha yavaş ama daha genel amaçlı.

**Avantajları:**

- ✅ Negatif ağırlıklı kenarları destekler
- ✅ Negatif döngü tespiti yapabilir
- ✅ Karmaşık graflar için uygundur

---

## 🚀 Nasıl Çalıştırılır

### Gereksinimler

```bash
pip install pygame
```

### Programı Çalıştırın

```bash
python main.py
```

### Nasıl Kullanılır

1. Grid üzerinde **tıklayarak** hedef konumu belirleyin
2. Algoritma otomatik olarak en kısa yolu hesaplayıp gösterecektir
3. **Yeşil çember** = Başlangıç noktası
4. **Kırmızı çember** = Hedef noktası
5. **Mavi çemberler** = En kısa yol

### Algoritma Değiştirme

`main.py` dosyasını açın ve kullanmak istediğiniz algoritmayı aktif edin (72-74. satırlar):

```python
visited = a_star(graph, start, mouse_pos)        # A* Algoritması
# visited = dijkstra(graph, start, mouse_pos)    # Dijkstra Algoritması
# visited = bellman_ford(graph, start, mouse_pos) # Bellman-Ford Algoritması
```

## 📊 Özellikler

- **İnteraktif Görselleştirme** - Gerçek zamanlı yol bulma
- **Ağırlıklı Grid** - Farklı arazi maliyetleri (1-9)
- **Çoklu Algoritmalar** - A*, Dijkstra, Bellman-Ford
- **Görsel Geri Bildirim** - Renkle kodlanmış yollar ve düğümler
