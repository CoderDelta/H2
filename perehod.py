from math import *
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from numpy import *
import numpy as np
import xlrd
from scipy import integrate
from phy import *
from matplotlib import rcParams

WIDER = 0.06
z = []
book1 = xlrd.open_workbook("energiy_perekhodu.xlsx")
sheet_name = book1.sheet_names()
rm = []
rk = []

"---------------------------------  Функції  ---------------------------------"

plt.style.use('ggplot')
def laguerre(s, n, x):
    if (s==0):
        return 1
    if (s==1):
        return 1+n-x
    m = 1
    while(m<s):
        lag = ((2*m+n+1-x)*laguerre(m, n, x)-(m+n)*laguerre(m-1, n, x))/(m+1)
        m+=1
    return lag

def wavefun_morze(s, J, r):
    nu = J
    T, w, wx, r0 = s
    x = r  - r0
    E = w*(nu + 1/2) - wx*(nu + 1/2)**(2)
    k = int(w/wx)
    B = sqrt(2*wx)
    N = sqrt(B*factorial(nu)*(k-2*nu-1)/factorial(k-nu-1))
    kexp = k*exp(-B*x)
    n = k-J*2-1
    return ((N*exp(-1/2.0*kexp)*kexp**(n/2)*laguerre(J, n, kexp))**2)*100

def wavefun_Xmorze(s, J, r):
    T, w, wx, r0 = s
    x = r  - r0
    k = int(w/wx)
    B = sqrt(2*wx)
    N = sqrt(B*factorial(J)*(k-2*J-1)/factorial(k - J - 1))
    kexp = k*exp(-B*x)
    n = k-J*2-1
    return (N*exp(-1/2.0*kexp)*kexp**(n/2)*laguerre(J, n, kexp))**2


def findXmorze(s, J):
    T, w, wx, r0 = s
    B = sqrt(2*wx)
    E = w*(J+1/2)-wx*(J+1/2)**(2)
    D = w**2/4.0/wx
    r1 = -1.0/B*math.log(1+math.sqrt(E/D))+r0
    r2 = -1.0/B*math.log(1-math.sqrt(E/D))+r0
    return (r1, r2)


"-----------------------------------------------------------------------------"
col = ['red','deepskyblue','yellow','green','purple','brown','grey']
k = 0 
for i in range(0,len(sheet_name)):
    fig = plt.figure(figsize=(15, 7.5))
    gs = gridspec.GridSpec(1, 2, width_ratios=[2,1])

    gs.update(left=0.1, right=0.96, wspace=0.1)
    
    theor_sheet = book1.sheet_by_index(i)
    num = theor_sheet.row_values(8)
    num_1 = theor_sheet.row_values(4)
    sp_0 = [num[0], num[1], num[2], num[9]]
    sp_1 = [num_1[0], num_1[1], num_1[2], num_1[9]]
    sp = [sp_0,sp_1]
    print(sheet_name[i])
    index = 0
    energy = 0
    plt.subplot(gs[0])
    for s in sp:
        T,w,wx,r0 = s
        print(s)
        if index != 0:
            energy = 20000
        if wx == 0:
            wx = 14
            s[2] = 14

        rg = findXmorze(s, 6)
        r = linspace(rg[0]-WIDER, rg[1]+WIDER, 10000)
        for nu in range(0,7):
            y = wavefun_morze(s, nu, r)
            E = w*(nu + 1/2) - wx*(nu + 1/2)**(2)
            plt.plot(r, y +  energy + E, color =col[k])
            k +=1
        k = 0
        ln = 5000
        B = sqrt(2*wx)
        xa = [ i*0.001 for i in range(0,ln)]
        ya = [(w**2/(4*wx))*(1 - exp(-B*(x*0.001 - r0)))**2 + energy  for x in range(0,ln) ]
        stan =  sheet_name[i]
        if stan == 'd->a':
            stan = r'$3_{П_{u} 3 p \pi} \mapsto 3_{\sum_{g}^{+} 2 s \sigma} $'
            enrg_1 =  r'$3_{П_{u} 3 p \pi}$'
            enrg_2 = r'$3_{\sum_{g}^{+} 2 s \sigma} $'
            
        elif stan == 'G->C':
            stan = r'$l_{\sum_{g}^{+} 3 d \sigma} \mapsto l_{П_{u} 2 p \pi} $'
            enrg_1 =  r'$l_{\sum_{g}^{+} 3 d \sigma} $'
            enrg_2 = r' $l_{П_{u} 2 p \pi} $'
            
        elif stan == 'R->C':
            stan = r'$l_{П_{g} 4 d \pi} \mapsto l_{П_{u} 2 p \pi}$'
            enrg_1 =  r'$l_{П_{u} 2 p \pi} $'
            enrg_2 = r' $l_{П_{u} 2 p \pi}$'
            
        elif stan == 'n->c':
           stan = r'$3_{П_{u}5 p \pi} \mapsto 3_{П_{u} 2 p \pi}$'
           enrg_1 =  r'$3_{П_{u}5 p \pi} $'
           enrg_2 = r'$3_{П_{u} 2 p \pi}$'
            
        fig.suptitle(stan, fontsize=20)

        plt.plot(xa,ya,color ='blue')
        lg = plt.plot(xa,ya,color ='blue')
        plt.axis([0.85, 1.4, 0, 50000])
        plt.grid(True)
        plt.xlabel('r, A')
        plt.ylabel('U, 1/cm')

        if energy == 20000:
            energy = 0
            index = 0
        else:
            index += 1
    for j1 in range(7):
        for j2 in range(7):
            f = lambda x: wavefun_Xmorze(sp_0,j1,x)*wavefun_Xmorze(sp_1,j2,x)
            r1 = min( findXmorze(sp_1,j1)[0], findXmorze(sp_0,j2)[0] )
            r2 = max( findXmorze(sp_1,j1)[1], findXmorze(sp_0,j2)[1] )
            r = integrate.quad(f, r1-0.1, r2+0.1)[0]
            z.append(r*int(abs(j1-j2)<=1))
    dzarr = array(z).reshape(7,7,order='F')
    
    plt.text(1.24, 10000, 'зверху - '+ enrg_1, fontsize=20)
    plt.text(1.24, 5000, 'знизу - '+ enrg_2, fontsize=20)

    num = np.amax(dzarr)
    j2,j1 = np.where(dzarr == num)# індекси знайдені
    rm.append(findXmorze(sp_1, int(j2)))
    rm.append(findXmorze(sp_0, int(j1)))
    rk.append(linspace(rm[0][0], rm[0][1], 10000))
    rk.append(linspace(rm[1][0], rm[1][1], 10000))
    

    resultx = linspace(rk[0][0], rk[1][-1], 10000)
    nu = int(j2)
    nu1 = int(j1)
    enrg1 = wavefun_morze(sp_1, nu, resultx) + 20000 + sp_1[1]*(nu + 1/2) - sp_1[2]*(nu + 1/2)**(2)
    enrg2 = wavefun_morze(sp_0, nu1, resultx)  + sp_0[1]*(nu1 + 1/2) - sp_0[2]*(nu1 + 1/2)**(2)
    index = np.where(enrg1 == np.amax(enrg1))
    index = int(index[0])

    mx = np.amax(enrg1) - enrg2[index]
    plt.arrow(resultx[index], enrg1[index]   , 0.0, mx*(-1) + 1000, head_width=0.006, head_length=1000, fc='k', ec='k')

    
    print('--------------------------------------')
    rk = []
    rm = []

 
    plt.subplot(gs[1])
    
    imgplot = plt.imshow(dzarr, interpolation='nearest')
    imgplot.set_cmap('gray')
    z = []
    fig = fig.colorbar(imgplot)

    plt.xlabel(r'$\nu_1$, '+str(sheet_name[i][3]))
    plt.ylabel(r'$\nu_2$, '+str(sheet_name[i][0]))
    plt.savefig(sheet_name[i]+ '.png', dpi=200)



    



plt.show()

