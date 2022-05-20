import numpy as np


def filtriraj_mono(signal, b, a):
    # y(n) = b(1)*x(n) + b(2)*x(n-1) + ... + b(nb+1)*x(n-nb) - a(2)*y(n-1) - ... - a(na+1)*y(n-na)
    # iteriramo prvo za koeficient b nato a
    y_n = np.zeros((np.size(signal), 1))
    sizeSignal = np.arange(0, np.size(signal))
    a_size = np.arange(np.shape(a)[0])
    b_size = np.arange(np.shape(b)[0])

    # for iteration in sizeSignal:
    #   for i in b_size:
    #      if iteration - i < 0:
    #           continue
    #   else:
    #         y_n[iteration] = y_n[iteration] + b[i] * signal[iteration - i]

    # for iteration in sizeSignal:
    #  if a[0][0] != 1:
    #     y_n[n] = y_n[n] / a[0][0]
    # for i in a_size:
    #   if 0 > iteration - i:
    #      continue
    # else:
    #    y_n[iteration] = y_n[iteration] - a[i] * y_n[iteration - i]

    for iteration in sizeSignal:
        for i in b_size:
            if iteration - i >= 0:
                y_n[iteration] = y_n[iteration] + b[i] * signal[iteration - i]

    for iteration in sizeSignal:  # OPOZORILO: niste upoštevali koeficienta a[0] - v kolikor ta ni enak 1, morate ustrezno pomnožiti/deliti rezultat
        if a[0][0] != 1:
            y_n[iteration] = y_n[iteration] / a[0][0]
        for i in a_size:
            if iteration - i >= 0:
                y_n[iteration] = y_n[iteration] - a[i] * y_n[iteration - i]

    return y_n

def filtriraj_stereo(signal, b, a):
    y_n = np.zeros(signal.shape)
    sizeSignal = np.arange(0, np.size(signal))
    a_size = np.arange(np.shape(a)[0])
    b_size = np.arange(np.shape(b)[0])
    # y(n) = b(1)*x(n) + b(2)*x(n-1) + ... + b(nb+1)*x(n-nb) - a(2)*y(n-1) - ... - a(na+1)*y(n-na)
    #Razlika: dimenziji [0] in [1]

    for iteration in sizeSignal:
        for j in b_size:
            if iteration - j >= 0:
                y_n[iteration][0] = y_n[iteration][0] + b[j][0] * signal[iteration - j][0]
                y_n[iteration][1] = y_n[iteration][1] + b[j][0] * signal[iteration - j][1]

        for j in a_size:
            if iteration - j >= 0:
                y_n[iteration][0] = y_n[iteration][0] - a[j][0] * y_n[iteration - j][0]
                y_n[iteration][1] = y_n[iteration][1] - a[j][0] * y_n[iteration - j][1]
        y_n[iteration][0] = y_n[iteration][0] / a[0][0]
        y_n[iteration][1] = y_n[iteration][1] / a[0][0]

    return y_n

if __name__ == '__main__':
    print("Modul za filtriranje signala!")
