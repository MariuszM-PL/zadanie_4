# Raport z analizy metod MCDM – TOPSIS, SPOTIS i VIKOR

## 1. Wprowadzenie
Celem analizy było porównanie trzech metod wielokryterialnego podejmowania decyzji: TOPSIS, SPOTIS oraz VIKOR na podstawie przykładowej macierzy decyzyjnej.

## 2. Dane wejściowe
Analizowane są trzy alternatywy oceniane względem trzech kryteriów:

| Alternatywa | Koszt (min) | Zysk (max) | Ryzyko (min) |
|-------------|-------------|------------|--------------|
| A1          | 500         | 2000       | 3            |
| A2          | 680         | 2300       | 4            |
| A3          | 600         | 2200       | 2            |

Wagi kryteriów:
- Koszt: 0.3
- Zysk: 0.5
- Ryzyko: 0.2

Typy kryteriów:
- Koszt i ryzyko: minimalizacja
- Zysk: maksymalizacja

## 3. Metody analizy
- **TOPSIS** wykorzystuje normalizację min-max oraz oblicza odległość alternatyw od idealnego rozwiązania.
- **SPOTIS**  porównuje alternatywy względem ustalonych granic kryteriów.
- **VIKOR**  szuka kompromisowego rozwiązania w przypadku konfliktu między kryteriami.

## 4. Wyniki

| Alternatywa | TOPSIS | SPOTIS | VIKOR  |
|-------------|--------|--------|--------|
| A1          | 0.383  | 0.600  | 1.0000 |
| A2          | 0.581  | 0.500  | 0.5125 |
| A3          | 0.636  | 0.333  | 0.0000 |

Wyniki wskazują, że alternatywa **A3** jest najlepsza według wszystkich trzech metod.

## 5. Porównanie rankingów
Korelacja rang Spearmana pomiędzy metodami wynosi 1.0 dla wszystkich par, co oznacza pełną zgodność w kolejności alternatyw.

## 6. Wnioski
Analiza potwierdza, że alternatywa A3 jest najlepszym kompromisem pomiędzy kosztami, zyskiem i ryzykiem.  
Wszystkie trzy metody MCDM wskazują zgodnie tę samą kolejność, co zwiększa pewność podjętej decyzji.

---

