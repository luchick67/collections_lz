import math  # Импортируем математику для экспоненты и логарифма
import matplotlib.pyplot as plt  # Импортируем библиотеку для графиков
# Создаем пустые списки для координат X и Y
x_points = []
x_points_ln = []  # Отдельный список для логарифма, так как ему нельзя минус и ноль
# Наполняем списки числами от -2.5 до 3.5 с маленьким шагом 0.01, чтобы линии были гладкими
i = -2.5
while i <= 3.5:
    x_points.append(i)
    if i > 0:  # Логарифм работает только если x больше нуля
        x_points_ln.append(i)
    i += 0.01
# Считаем Y для каждого графика по простым формулам
y_x2 = []
for x in x_points:
    y_x2.append(x**2)  # Икс в квадрат
y_ex = []
for x in x_points:
    y_ex.append(math.exp(x))  # Экспонента
y_ln = []
for x in x_points_ln:
    y_ln.append(math.log(x))  # Натуральный логарифм
y_x3 = []
for x in x_points:
    y_x3.append(x**3)  # Икс в кубе
# Список целых иксов по заданию
x_ints = [-2, -1, 0, 1, 2, 3]
x_ints_ln = [1, 2, 3]  # Для логарифма только целые больше нуля
# Считаем целые игреки для каждого графика
y_ints_x2 = []
for x in x_ints:
    y_ints_x2.append(x**2)
y_ints_ex = []
for x in x_ints:
    y_ints_ex.append(math.exp(x))
y_ints_ln = []
for x in x_ints_ln:
    y_ints_ln.append(math.log(x))
y_ints_x3 = []
for x in x_ints:
    y_ints_x3.append(x**3)
# 1. График x^2 (Синяя линия, маркеры — кружочки 'o')
plt.plot(x_points, y_x2, color="blue", label="x^2")
plt.scatter(x_ints, y_ints_x2, color="blue", marker="o", s=100)
# 2. График e^x (Зеленая линия, маркеры — крестики 'x')
plt.plot(x_points, y_ex, color="green", label="e^x")
plt.scatter(x_ints, y_ints_ex, color="green", marker="x", s=100)
# 3. График ln(x) (Красная линия, маркеры — треугольники '^')
plt.plot(x_points_ln, y_ln, color="red", label="ln(x)")
plt.scatter(x_ints_ln, y_ints_ln, color="red", marker="^", s=100)
# 4. График x^3 (Оранжевая линия, маркеры — квадраты 's')
plt.plot(x_points, y_x3, color="orange", label="x^3")
plt.scatter(x_ints, y_ints_x3, color="orange", marker="s", s=100)
plt.grid(True)  # Включаем обычную сетку
plt.legend()  # Показываем окошко со списком графиков
plt.ylim(-5, 25)  # Ограничиваем высоту, чтобы графики не улетали слишком высоко
# Показываем результат на экране
plt.show()