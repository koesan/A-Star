# Path Finding

***Bu projede, en kısa yolu bulan algoritmaların Python kodlarını yazıp projeye ekliyorum.***

***

## A* Algoritması

A* algoritması, graf teorisi ve yol bulma problemleri için kullanılan etkili bir arama algoritmasıdır. Hedefe ulaşmak için en kısa ve en düşük maliyetli yolu bulur. A* algoritması, iki temel bileşeni birleştirir:

- **G maliyeti (g)**: Başlangıç noktasından mevcut noktaya olan mesafe.
- **H maliyeti (h)**: Mevcut noktadan hedef noktaya olan tahmini mesafe.

A* algoritması, bu iki değeri birleştirerek toplam maliyeti (f = g + h) hesaplar ve en düşük maliyetli yolu bulmak için bu toplamı kullanır.

---

## Dijkstra Algoritması

Dijkstra algoritması, bir grafikteki bir başlangıç düğümünden diğer düğümlere olan en kısa yolları bulmak için kullanılan etkili bir yol bulma algoritmasıdır.

### Temel Adımlar:

1. **Başlangıç Düğümünü Seçme**: Başlangıç düğümünün mesafesi 0, diğer tüm düğümlerin mesafesi "sonsuz" olarak ayarlanır.

2. **Mesafeleri Güncelleme**: İşlem sırasındaki düğümlerden en düşük mesafeye sahip olan düğüm seçilir ve bu düğümden komşularına olan mesafeleri güncellenir.

3. **Düğümleri İşleme**: Seçilen düğüm işlenir ve daha önce hesaplanan mesafeler üzerinden komşulara geçiş yapılarak mesafeler güncellenir.

4. **Tekrar Etme**: Tüm düğümler işlenene kadar bu adımlar tekrarlanır.

### Sonuç:

Başlangıç düğümünden diğer düğümlere olan en kısa yollar ve mesafeler elde edilir.


https://github.com/user-attachments/assets/b8624274-dfc7-42a4-901d-85c8734f3065

