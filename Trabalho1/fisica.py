import numpy as np

# for k in range(tam-1):
# Sistema de controle

# PARÂMETROS DE SIMULAÇÃO
finished = False
h = 0.001  # passo da simulação de tempo continuo
Ts = 0.01  # intervalo de atuação do controlador
fTh = Ts / h
maxT = 600
tc = np.arange(0, maxT, h)  # k
td = np.arange(0, maxT, Ts)  # j
tam = len(tc)
j = 0

# Vetor de estados
x = np.zeros([8, tam])
k = 0
x[:, 0] = np.array([0., 0.,
                    0.5, 3.5,
                    0., .0,
                    0 * np.pi / 180.,
                    0 * np.pi / 180.])

# Constanstes do modelo
m = 0.25  # massa
g = 9.81  # aceleração da gravidade
l = 0.1  # tamanho
kf = 1.744e-08  # constante de força
Iz = 2e-4  # momento de inércia
tal = 0.05
Fe = np.array([-m * g])

# Restrições do controle
phi_max = 15 * np.pi / 180.  # ângulo máximo

w_max = 15000
Fc_max = kf * w_max ** 2  # Força de controle máximo
Tc_max = l * kf * w_max ** 2

# Waypoints
r_ = np.array([[0.5, 3.5],
               [0.5, 0.2],
               [6., 0.2],
               [6., 3.5],
               [3.25, 1.75]]).transpose()

r_points = np.array([[0.5, 3.5],
                     [0.5, 0.2],
                     [6., 0.2],
                     [6., 3.5],
                     [3.25, 1.75]]).transpose()

r_ID = 0
r_IDN = 5

w_ = np.zeros([2, 2])
ref = np.array([0.5, 3.5])

# Processamento de variáveis intermediárias
"""
# obtem a força aplicada por cada rotor
f = np.zeros([3, tam])

for k in range(tam):
    w = x[0:2, k]
    f[0:2, k] = np.array([kf * w[0] ** 2, kf * w[1] ** 2])
    f[2, k] = f[0, k] + f[1, k]  # Força total em B
"""

def x_dot(t, x, w_):
    # Parâmetros
    w_max = 15000.  # velocidade máxima do motor
    m = 0.25  # massa
    g = 9.81  # aceleração da gravidade
    l = 0.1  # tamanho
    kf = 1.744e-08  # constante de força
    Iz = 2e-4  # momento de inércia
    tal = 0.005
    Fg = np.array([[0], [-m * g]])

    ## Estados atuais
    w = x[0:2]
    r = x[2:4]
    v = x[4:6]
    phi = x[6]
    ome = x[7]

    ## Variáveis auxiliares
    # forças
    f1 = kf * w[0] ** 2
    f2 = kf * w[1] ** 2

    # Torque
    Tc = l * (f1 - f2)

    # Força de controle
    Fc_B = np.array([[0], [(f1 + f2)]])

    # Matriz de atitude
    D_RB = np.array([[np.cos(phi), -np.sin(phi)], [np.sin(phi), np.cos(phi)]])

    ## Derivadas
    w_dot = (-w + w_) / tal
    r_dot = v
    v_dot = (1 / m) * (D_RB @ Fc_B + Fg)
    v_dot = v_dot.reshape(2, )
    phi_dot = np.array([ome])
    ome_dot = np.array([Tc / Iz])

    xkp1 = np.concatenate([w_dot,
                           r_dot,
                           v_dot,
                           phi_dot,
                           ome_dot])

    return xkp1


def rk4(tk, h, xk, uk):
    k1 = x_dot(tk, xk, uk)
    k2 = x_dot(tk + h / 2.0, xk + h * k1 / 2.0, uk)
    k3 = x_dot(tk + h / 2.0, xk + h * k2 / 2.0, uk)
    k4 = x_dot(tk + h, xk + h * k3, uk)
    xkp1 = xk + (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
    return xkp1

#função para gravar novos waypoints
def gravar(reset):
    global r_, r_ID, r_IDN, r_points
    if not reset:
        r_ID = 0
        r_IDN = 0
    elif r_IDN == 0:
        r_points = np.array(x[2:4, k - 1], ndmin=2).transpose()
        r_IDN += 1
    elif r_IDN > 0:
        r_points = np.concatenate((r_points,
                                   np.array(x[2:4, k - 1], ndmin=2).transpose()), axis=1)
        r_IDN += 1
    r_ = r_points
    print(r_IDN)
    print(r_)


def movimenta(esquerda, direita, cima, baixo, comando):
    global k
    global r_ID
    global r_IDN
    global w_
    global r_
    global ref

    # Extrai os dados do  vetor
    r_k = x[2:4, k]
    # print(r_k)
    v_k = x[4:6, k]
    phi_k = x[6, k]
    ome_k = x[7, k]

    # Comando de posição
    v_ = np.array([0, 0])

    # Controle de Posição
    kpP = np.array([0.7])
    kdP = np.array([0.6])

    # Colocar os way points na referencia
    if not comando:
        r_ = r_points
        ref = r_[:, r_ID]
        eP = ref - r_k
        if np.linalg.norm(eP) < .1 and r_ID < r_IDN:
            r_ID += 1
        if np.linalg.norm(eP) < .1 and r_ID >= r_IDN:
            r_ID = 0
        if r_ID == r_IDN:
            ref = r_[:, r_ID]
    # setar as referencias pelo teclado
    if comando:
        r_ID = 0
        if esquerda and ref[0] >= 0:
            ref += [-0.05, 0]
            if ref[0] < 0:
                ref[0] = 0
        if direita and ref[0] <= 6:
            ref += [0.05, 0]
            if ref[0] > 6:
                ref[0] = 6
        if cima and ref[1] >= -0.4:
            ref += [0, -0.05]
            if ref[1] < -0.4:
                ref[1] = -0.4
        if baixo and ref[1] <= 3.5:
            ref += [0, 0.05]
            if ref[1] > 3.5:
                ref[1] = 3.5
    # erro de posição
    eP = ref - r_k

    # limitar a ação de controle
    if comando == 0:
        if abs(eP[0]) > 2:
            eP[0] = 2*np.sign(eP[0])
        if abs(eP[1]) > 2:
            eP[1] = 2*np.sign(eP[1])
    else:
        if abs(eP[0]) > 1.5:
            ref[0] = r_k[0] + 1.5 * np.sign(eP[0])
        if abs(eP[1]) > 1.5:
            ref[1] = r_k[1] + 1.5 * np.sign(eP[1])

    # erro de velocidade
    eV = v_ - v_k

    # calculo das forças
    Fx = kpP * eP[0] + kdP * eV[0]
    Fy = kpP * eP[1] + kdP * eV[1] - Fe
    Fy = np.maximum(0.2 * Fc_max, np.minimum(Fy, 0.8 * Fc_max))

    # Controle de Atitude
    phi_ = np.arctan2(-Fx, Fy)

    if np.abs(phi_) > phi_max:
        # print(phi_*180/np.pi)
        signal = phi_ / np.absolute(phi_)
        phi_ = signal * phi_max

        # Limitando o ângulo
        Fx = Fy * np.tan(phi_)

    Fxy = np.array([Fx, Fy])
    Fc = np.linalg.norm(Fxy)
    f12 = np.array([Fc / 2.0, Fc / 2.0])

    # Constantes Kp e Kd
    kpA = np.array([0.3])
    kdA = np.array([0.1])
    ePhi = phi_ - phi_k
    eOme = 0 - ome_k

    # calculo do torque
    Tc = kpA * ePhi + kdA * eOme
    Tc = np.maximum(-0.4 * Tc_max, np.minimum(Tc, 0.4 * Tc_max))

    # Delta de forças
    df12 = np.absolute(Tc) / 2.0

    if (Tc >= 0.0):
        f12[0] = f12[0] + df12
        f12[1] = f12[1] - df12
    else:
        f12[0] = f12[0] - df12
        f12[1] = f12[1] + df12

    # Limitadores
    w1_ = np.sqrt(f12[0] / (kf))
    w2_ = np.sqrt(f12[1] / (kf))

    # Limitando o comando do motor entre 0 - 15000 rpm
    w1 = np.maximum(0., np.minimum(w1_, w_max))
    w2 = np.maximum(0., np.minimum(w2_, w_max))

    # Determinação do comando de entrada
    w_ = np.array([w_[1, :],
                   [w1, w2]])


    #Ajuste de tempos entre simulação e controle
    for j in range(10):
        x[:, k + 1 + j] = rk4(tc[k + j], h, x[:, k + j], w_[0, :])
    k += 10


    #Extração da posição e do angulo do vetor x
    pos = x[2:4, k]
    angle = x[6, k]
    return pos, angle
