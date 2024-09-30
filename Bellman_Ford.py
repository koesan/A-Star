# kaynak: https://www.youtube.com/watch?v=24HziTZ8_xo

def bellman_ford(graph,başlangıç,hedef):
   # Mesafeleri sonsuz olarak başlat
   mesafeler = {node: float('infinity') for node in graph}
   önceki = {node: None for node in graph}  # Her düğümün öncesini kaydet

   # Başlangıç düğümünün mesafesini sıfır olarak ayarla
   mesafeler[başlangıç] = 0

   # Döngü graftaki düğümlerin sayısının 1 eksiği kadar devam etmeli.
   for _ in range(len(graph) - 1):  # Düğüm sayısı - 1 kadar tekrar et
       for i in graph:  # Her düğüm üzerinde dolaş
           for j in graph[i]:  # Düğümün komşularına bak
               hedef_dugum = j[1]  # Hedef düğümü al
               maliyet = j[0]  # Kenar maliyetini al

               # Eğer mevcut düğümün mesafesi sonsuz değilse ve komşuya olan mesafe daha düşükse güncelle
               if mesafeler[i] != float('infinity') and (mesafeler[i] + maliyet < mesafeler[hedef_dugum]):
                   mesafeler[hedef_dugum] = mesafeler[i] + maliyet
                   önceki[hedef_dugum] = i  # Önceki düğümü güncelle

   # Negatif ağırlıklı döngü kontrolü
   for i in graph:
       for j in graph[i]:
           hedef_dugum = j[1]
           maliyet = j[0]

           # Eğer hala bir iyileştirme yapılabiliyorsa negatif döngü vardır
           if mesafeler[i] != float('infinity') and (mesafeler[i] + maliyet < mesafeler[hedef_dugum]):
               return None  # Negatif döngü bulunduktan sonra işlevi sonlandırın.


   # En kısa yolu bulmak için hedeften başlangıca doğru git
   yol = []
   geçerli_dugum = hedef

   while geçerli_dugum is not None:
       yol.append(geçerli_dugum)
       geçerli_dugum = önceki[geçerli_dugum]

   # Yolu ters çevir ve döndür.
   yol.reverse()
   return yol