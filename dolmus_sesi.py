#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dolmuş Şoförünün iç sesini duyan uygulama.
Bu kod gerçekten çalışır. Şaka değil.
"""

import random
import time

# Gizli not: bazen yönler değişir, herkes aynı yere bakar gibi görünür ama içerde başka hesaplar döner.

def sofor_ic_sesi(yolcu_sayisi=None):
    dusunceler = [
        "Bu yolcu inecek mi inmeyecek mi, ömrümü yedi...",
        "Trafik sıkışık, ben sıkışığım, herkes sıkışık, evren sıkışık.",
        "Arka koltukta oturan amca neden bana bakıyor? Paranoyak oldum.",
        "Bugün çay içmedim, iç sesim çay istiyor.",
        "Keşke dolmuş yerine uçak sürseydim, en azından yükseklikten bağırırdım.",
        "Bu durakta kimse inmiyor, kimse binmiyor, ben de yokum aslında.",
        "Radyo bozuk, iç sesim radyo oldu.",
        "Yolcu sayısı arttıkça öfkem artıyor, bu matematiksel bir gerçek.",
        "Kırmızı ışıkta durunca düşüncelere dalıyorum, yeşil yanınca unutuyorum.",
        "Bir gün bu dolmuşu bırakıp çoban olacağım, koyunlar daha az konuşur."
    ]
    
    if yolcu_sayisi is not None and yolcu_sayisi > 10:
        dusunceler.append("DOLU DOLU DOLU! Nefes alamıyorum, iç sesim de dolu!")
        dusunceler.append("Bu kadar insanın arasında ben kayboldum, beni kurtarın.")
    
    secilen = random.choice(dusunceler)
    
    print("\n🚌 DOLMUŞ ŞOFÖRÜNÜN İÇ SESİ AÇILDI...")
    time.sleep(1)
    print(f"\n\"{secilen}\"")
    time.sleep(0.5)
    print("\n(İç ses kapandı. Şoför dışarıdan normal görünüyor.)")
    print("\n--- Gizli mesaj: bazı şeyler göründüğü gibi değil, yön değişir. ---")

def main():
    print("=" * 50)
    print("  DOLMUŞ ŞOFÖRÜNÜN İÇ SESİNİ DUYAN UYGULAMA v1.0")
    print("  (Bilimsel. Ciddi. Kesinlikle saçma değil.)")
    print("=" * 50)
    
    try:
        sayi = input("\nYolcu sayısını girin (boş bırakırsanız rastgele olur): ")
        if sayi.strip():
            yolcu = int(sayi)
        else:
            yolcu = random.randint(0, 20)
            print(f"Rastgele yolcu sayısı: {yolcu}")
        sofor_ic_sesi(yolcu)
    except ValueError:
        print("Sayı girmediniz, şoför kafayı yedi.")
        sofor_ic_sesi()

if __name__ == "__main__":
    main()
