import numpy as np
import pandas as pd
from pymcdm.methods import TOPSIS, SPOTIS, VIKOR
from scipy.stats import spearmanr
import matplotlib.pyplot as plt

# --- Dane ---
decision_matrix = np.array([
    [500, 2000, 3],
    [680, 2300, 4],
    [600, 2200, 2]
])

weights = np.array([0.3, 0.5, 0.2])
types = np.array([-1, 1, -1])

bounds = [
    (np.min(decision_matrix[:, 0]), np.max(decision_matrix[:, 0])),
    (np.min(decision_matrix[:, 1]), np.max(decision_matrix[:, 1])),
    (np.min(decision_matrix[:, 2]), np.max(decision_matrix[:, 2]))
]

# --- Metody ---
topsis = TOPSIS()
spotis = SPOTIS(bounds)
vikor = VIKOR()

# --- Obliczenia ---
topsis_scores = topsis(decision_matrix, weights, types)
spotis_scores = spotis(decision_matrix, weights, types)
vikor_scores = vikor(decision_matrix, weights, types)

# --- Tworzenie DataFrame z wynikami ---
results = pd.DataFrame({
    'Alternatywa': ['A1', 'A2', 'A3'],
    'TOPSIS': topsis_scores,
    'SPOTIS': spotis_scores,
    'VIKOR': vikor_scores
})

print(results)

# --- Porównanie rankingów ---
def rank_scores(scores, reverse=False):
    order = -scores if not reverse else scores
    return np.argsort(np.argsort(-order)) + 1

r_topsis = rank_scores(topsis_scores)
r_spotis = rank_scores(spotis_scores, reverse=True)
r_vikor = rank_scores(vikor_scores, reverse=True)

print("\nKorelacje Spearmana między rankingami:")
print("TOPSIS vs SPOTIS:", spearmanr(r_topsis, r_spotis).correlation)
print("TOPSIS vs VIKOR:", spearmanr(r_topsis, r_vikor).correlation)
print("SPOTIS vs VIKOR:", spearmanr(r_spotis, r_vikor).correlation)

# --- Wizualizacja ---
labels = results['Alternatywa']
x = np.arange(len(labels))
width = 0.25

fig, ax = plt.subplots()
ax.bar(x - width, topsis_scores, width, label='TOPSIS')
ax.bar(x, spotis_scores, width, label='SPOTIS')
ax.bar(x + width, vikor_scores, width, label='VIKOR')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Ocena')
ax.set_title('Porównanie ocen alternatyw w metodach MCDM')
ax.legend()

plt.tight_layout()
plt.show()
