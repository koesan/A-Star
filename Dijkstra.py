def get_shortest_path(previous_nodes, start, target):
    path = []
    current_node = target
    
    while current_node is not None:
        path.insert(0, current_node)  # Düğümü başa ekle
        current_node = previous_nodes[current_node]  # Bir önceki düğüme git
    
    if path[0] == start:
        return path
    else:
        return []  # Eğer yol yoksa boş liste döner

def dijkstra(graph, start,target):
    # 1. Mesafe tablosu: Başlangıç düğümünden diğer düğümlere olan mesafeleri tutar
    mesafeler = {node: float('infinity') for node in graph}
    mesafeler[start] = 0

    # 2. Ziyaret edilen düğümleri tutan liste
    ziyaret_edilen = []

    # 3. Önceki düğümleri tutan tablo: En kısa yolu oluşturmak için
    önceki_düğümler = {node: None for node in graph}

    while len(ziyaret_edilen) < len(graph):
        # 4. Ziyaret edilmemiş düğümler arasında en kısa mesafeye sahip olanı seç
        en_kısa_yol_düğümü = None
        for node in mesafeler:
            if node not in ziyaret_edilen:
                if en_kısa_yol_düğümü is None:
                    en_kısa_yol_düğümü = node
                elif mesafeler[node] < mesafeler[en_kısa_yol_düğümü]:
                    en_kısa_yol_düğümü = node
        
        if en_kısa_yol_düğümü is None:
            break  # Tüm düğümler ziyaret edilmişse ya da ulaşılamayan düğümler kalmışsa döngüyü sonlandır

        # 5. Seçilen düğümün komşularının mesafelerini güncelle
        for ağırlık,komşu in graph[en_kısa_yol_düğümü]:

            yeni_mesafe = mesafeler[en_kısa_yol_düğümü] + ağırlık
            if yeni_mesafe < mesafeler[komşu]:
                mesafeler[komşu] = yeni_mesafe
                önceki_düğümler[komşu] = en_kısa_yol_düğümü

        # 6. Seçilen düğümü ziyaret edilmiş olarak işaretle
        ziyaret_edilen.append(en_kısa_yol_düğümü)

    return get_shortest_path(önceki_düğümler, start, target)
