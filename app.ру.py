import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 1. Настройка парадного интерфейса в стиле Лиги Плюща
st.set_page_config(page_title="Torus Clearing Simulator", layout="wide")
st.title("🌌 Глобальный финтех-симулятор 'Torus Clearing System'")
st.subheader("Математическая верификация обхода платформенных санкций на основе Индексов CPV")
st.write("---")

# 2. Интерактивная боковая панель управления (Ползунки для профессоров)
st.sidebar.header("🛠️ Параметры ИТ-ландшафта и макросистемы")

# Ползунок интенсивности атак ИИ ТНК (I_TNC)
I_TNC = st.sidebar.slider("Интенсивность атаки ИИ ТНК (I_TNC)", min_value=1.0, max_value=100.0, value=25.0)

# Ползунок силы и ширины санкций Запада (Width)
Width = st.sidebar.slider("Глубина финансовых санкций SWIFT (Width)", min_value=1.0, max_value=100.0, value=30.0)

# Главный управляющий ползунок — Твой Индекс Координации (CPV)
CPV = st.sidebar.slider("Ваш управляющий Индекс координации (CPV)", min_value=3.0, max_value=6.0, value=5.2, step=0.1)

st.sidebar.write("---")
st.sidebar.info("💡 Направлено для верификации в UPenn PPE и Harvard HAWC.")

# 3. Математический движок симулятора (Расчет твоих уравнений)
# Фиксированные константы твоей модели
alpha = 0.15   # Базовое техническое трение клиринга
i_cost = 0.85  # Издержки ТНК на попытки отслеживания платежей
hbar = 1.0     # Постоянная плотности закрытых цифровых сетей доверия
M_scale = 1000 # Масштаб емкости внутреннего рынка союза

# Расчет Формулы №2: Коэффициент квантового туннелирования ликвидности (T_Liquidity)
# T_Liquidity = exp( - (2 * alpha * i * Width) / (hbar * CPV) )
exponent = (2 * alpha * i_cost * Width) / (hbar * CPV)
T_Liquidity = np.exp(-exponent)

# Расчет Формулы №1: Совокупный очищенный выпуск союза (Y_MR)
# Упрощенная линейная проекция для графиков
C_I_G = 500 # Базовое внутреннее потребление союза
NX_base = 300 - (0.5 * I_TNC) # Чистый экспорт, проседающий от атак ИИ
F_CPV = 1.0 if CPV >= 5.2 else (0.1 * CPV) # Активация ковариантного Функтора Доверия
Y_MR = C_I_G + NX_base + F_CPV * (M_scale - alpha)

# 4. Вывод сочных макроэкономических показателей на экран
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="🛡️ Пропускная способность каналов (T_Liquidity)", 
        value=f"{round(T_Liquidity * 100, 2)} %",
        delta="ИДЕАЛ (100%)" if CPV >= 5.2 else "Требуется CPV = 5.2"
    )

with col2:
    st.metric(
        label="📈 Очищенный выпуск союза (Y_MR)", 
        value=f"{round(Y_MR, 2)} млрд у.е.",
        delta=f"+ {round(F_CPV * M_scale, 2)} от мотивной защиты"
    )

with col3:
    st.metric(
        label="⚖️ Текущий статус финансового контура", 
        value="Голографический Монолит" if CPV >= 5.2 else ("Локальный щит" if CPV >= 4.5 else "Хаос и вымывание ВРП")
    )

st.write("---")

# 5. Блок Live Charts: Генерация интерактивных графиков
st.write("### 📊 Визуализация Квантового перехода в некоммутативную геометрию тора")

# Генерируем массив данных по индексам для построения кривой
cpv_range = np.linspace(3.0, 6.0, 100)
t_range = np.exp(-(2 * alpha * i_cost * Width) / (hbar * cpv_range))

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(cpv_range, t_range, color="#1f77b4", linewidth=3, label="Траектория пробития санкций")
ax.scatter(CPV, T_Liquidity, color="#d62728", s=150, zorder=5, label="Ваша текущая точка CPV")

# Подсвечиваем твои критические пороговые константы
ax.axvline(x=4.5, color="#7f7f7f", linestyle="--", alpha=0.7)
ax.axvline(x=5.2, color="#2ca02c", linestyle="--", alpha=0.7)
ax.text(4.52, 0.2, "Порог РД (4.5)", color="#7f7f7f", fontsize=9, fontweight="bold")
ax.text(5.22, 0.8, "Монолит союза (5.2)", color="#2ca02c", fontsize=9, fontweight="bold")

ax.set_xlabel("Значение Вашего управляющего параметра (Индекс CPV)", fontsize=10)
ax.set_ylabel("Коэффициент туннелирования (T_Liquidity)", fontsize=10)
ax.grid(True, linestyle=":", alpha=0.6)
ax.legend(loc="lower right")

st.pyplot(fig)
