import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# 1. Фиксируем генератор случайных чисел для воспроизводимости
np.random.seed(42)

# 2. Генерируем точки данных в 3D пространстве (3 класса/категории)
X, y = make_blobs(
    n_samples=180,
    centers=[[2, 3, 5], [8, 2, 2], [4, 8, 3]],  # Центры 3-х кластеров
    cluster_std=0.8,  # Разброс точек
    random_state=42
)

# Цвета для классов (в стиле неоновой/темной темы)
colors = ['#FF4B4B', '#1E90FF', '#00E676']
class_labels = ['Category A (e.g. Text)', 'Category B (e.g. Audio)', 'Category C (e.g. Image)']

# 3. Настройка 3D графика
fig = plt.figure(figsize=(10, 8), facecolor='#0F172A')  # Темный фон контейнера
ax = fig.add_subplot(111, projection='3d', facecolor='#0F172A')

# Подготовка списка центроидов
centroids = []

# 4. Отрисовка точек для каждого кластера
for i in range(3):
    pts = X[y == i]
    # Считаем центроид (среднюю точку) кластера
    centroid = np.mean(pts, axis=0)
    centroids.append(centroid)

    # Рисуем сами точки
    ax.scatter(
        pts[:, 0], pts[:, 1], pts[:, 2],
        c=colors[i],
        s=45,
        alpha=0.8,
        edgecolors='none',
        label=class_labels[i]
    )

    # Рисуем яркие центральные узлы (центроиды)
    ax.scatter(
        centroid[0], centroid[1], centroid[2],
        c=colors[i],
        s=250,
        marker='o',
        edgecolors='white',
        linewidth=2,
        zorder=10
    )

# 5. Соединяем центроиды пунктирными связями (геометрия расстояний)
for i in range(len(centroids)):
    for j in range(i + 1, len(centroids)):
        p1, p2 = centroids[i], centroids[j]
        ax.plot(
            [p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]],
            color='#94A3B8',
            linestyle='--',
            linewidth=1.5,
            alpha=0.7
        )

# 6. Стилизация осей и сетки для современного/научного вида
ax.set_title("Vector Feature Space (3D Latent Projection)", color='white', fontsize=14, pad=20, fontweight='bold')

# Настройка подписей осей
ax.set_xlabel('Feature Axis $X_1$', color='#94A3B8', labelpad=10)
ax.set_ylabel('Feature Axis $X_2$', color='#94A3B8', labelpad=10)
ax.set_zlabel('Feature Axis $X_3$', color='#94A3B8', labelpad=10)

# Цвет делений осей
ax.tick_params(colors='#94A3B8')

# Прозрачные грани и деликатная сетка
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.xaxis.pane.set_edgecolor('#1E293B')
ax.yaxis.pane.set_edgecolor('#1E293B')
ax.zaxis.pane.set_edgecolor('#1E293B')

# Легенда
legend = ax.legend(facecolor='#1E293B', edgecolor='#334155', loc='upper left')
for text in legend.get_texts():
    text.set_color('white')

# Оптимальный угол обзора
ax.view_init(elev=22, azim=45)

plt.tight_layout()

# Сохранение в файл в высоком качестве (для вставки в статью на DEV.to)
plt.savefig('feature_space_3d.png', dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())

plt.show()