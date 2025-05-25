# Analiza metod wielokryterialnego podejmowania decyzji (MCDM)

## Opis projektu
Projekt realizuje analizę porównawczą trzech metod MCDM: TOPSIS, SPOTIS oraz VIKOR.  
Celem jest wyznaczenie rankingu alternatyw na podstawie macierzy decyzyjnej zawierającej trzy kryteria: koszt, zysk oraz ryzyko.

## Struktura projektu
- `main.py` — skrypt wykonujący obliczenia metodami TOPSIS, SPOTIS i VIKOR, wyświetlający ranking oraz wykres porównawczy.
- `raport.md` — raport zawierający opis danych, metod, wyniki analizy oraz wnioski.

## Wymagania
- Python 3.x
- Biblioteki: numpy, pandas, pymcdm, matplotlib, scipy

Można je zainstalować poleceniem:

```bash
pip install numpy pandas pymcdm matplotlib scipy
```

## Uruchomienie
W terminalu, w katalogu projektu, uruchom:

```bash
python main.py
```

## Wyniki
Skrypt wypisuje ranking alternatyw oraz pokazuje wykres porównujący oceny według zastosowanych metod.

## Autor
Mariusz Mikołajczyk

## Licencja
MIT
