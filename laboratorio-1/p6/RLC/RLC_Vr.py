import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def gigante(freq):
    df_tensoes = pd.read_csv(f'./data{str(freq)}_pc_RLC0.csv')
    df_tensoes.columns = ['Time(s)', 'VG', 'VC']
    df_tensoes['VR'] = df_tensoes['VG'] - df_tensoes['VC']

    time_data = df_tensoes['Time(s)'].values
    VG_data = df_tensoes['VG'].values
    VC_data = df_tensoes['VC'].values
    VR_data = df_tensoes['VR'].values

    ## AJUSTE Vg

    def senoidal(t, VGoffset, VG0, VGomega, VGphi):
        return VG0 * np.sin(VGomega * t + VGphi) + VGoffset

    initial_guess = [2.3, 2.5, 2 * np.pi * (freq), 0]

    params_Vg, params_Vg_covariance = curve_fit(senoidal, time_data, VG_data, p0=initial_guess)

    plt.plot(time_data, VG_data, label='Dados Originais', color='navy', marker = '.', markersize=8)

    plt.gca().xaxis.set_major_formatter(ticker.ScalarFormatter(useMathText=True))
    plt.gca().xaxis.get_major_formatter().set_scientific(True)
    plt.gca().xaxis.get_major_formatter().set_powerlimits((-1,1))

    plt.plot(time_data, senoidal(time_data, *params_Vg), label='Senoidal Ajustada', color='#FF2400')

    plt.title(f'VG(t) para {freq} Hz')
    plt.xlabel('Tempo(s)')
    plt.ylabel('Tensão(V)')
    plt.legend(loc='upper right')
    plt.grid()
    plt.ylim(VG_data.min() - 1, VG_data.max() + 1)
    plt.show()

    VGoffset, VG0, VGomega, VGphi = params_Vg
    print(f'VGoffset: {np.round(VGoffset, 2)}, VG0: {np.round(VG0, 2)}, VGOmega: {np.round(VGoffset, 2)}, VGPhi: {np.round(VGphi, 2)}\n')
    print(f'A senoidal ajustada é: {np.round(VG0, 2)} * sin({np.round(VGoffset, 2)} * t + {np.round(VGphi, 2)}) + {np.round(VGoffset, 2)}')


    ## AJUSTE Vr
    def senoidal(t, VRoffset, VR0, VRomega, VRphi):
        return VR0 * np.sin(VRomega * t + VRphi) + VRoffset

    initial_guess = [2.3, 2.5, 2 * np.pi * (freq), 0]

    params_Vr, params_Vr_covariance = curve_fit(senoidal, time_data, VR_data, p0=initial_guess)

    plt.plot(time_data, VR_data, label='Dados calculados', color='darkorange', marker = 'o')

    plt.gca().xaxis.set_major_formatter(ticker.ScalarFormatter(useMathText=True))
    plt.gca().xaxis.get_major_formatter().set_scientific(True)
    plt.gca().xaxis.get_major_formatter().set_powerlimits((-1,1))

    plt.plot(time_data, senoidal(time_data, *params_Vr), label='Senoidal Ajustada', color='yellow')

    VRoffset, VR0, VRomega, VRphi = params_Vr

    plt.title(f'VR(t) para {freq} Hz')
    plt.xlabel('Tempo(s)')
    plt.ylabel('Tensão(V)')
    plt.legend(loc='upper right')
    plt.ylim(VR_data.min() - 1, VR_data.max() + 1)
    plt.grid()
    plt.show()

    print(f'VRoffset: {np.round(VRoffset, 2)}, VR0: {np.round(VR0, 2)}, VROmega: {np.round(VRomega, 2)}, VRPhi: {np.round(VRphi, 2)}\n')
    print(f'A senoidal ajustada é: {np.round(VR0, 2)} * sin({np.round(VRoffset, 2)} * t + {np.round(VRphi, 2)}) + {np.round(VRoffset, 2)}')
    
    return [VG0, params_Vg_covariance[1][1]**(1/2), \
            VGphi, params_Vg_covariance[3][3]**(1/2), \
            VR0, params_Vr_covariance[1][1]**(1/2), \
            VRphi, params_Vr_covariance[3][3]**(1/2)]

freqs = [228, 456, 912, 1824, 3648, 7296, 14592, 29184, 58368]
res = []

for freq in freqs:
    res.append(gigante(freq))

df = pd.DataFrame(res)
df.columns = ['VG0', 'VG0_uncertainty', 'VGphi', 'VGphi_uncertainty', 'VR0', 'VR0_uncertainty', 'VRphi', 'VRphi_uncertainty']
    
df.to_csv('output.csv')

