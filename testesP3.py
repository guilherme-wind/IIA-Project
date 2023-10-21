s = ProblemaGrafo()
print('---------------- IDA* ----------------')
f=lambda n: n.path_cost + s.h1(n)
res_IDAstar,visitados=ida_star_graph_search_count(s,f)
if res_IDAstar:
    print("\nSolução:",res_IDAstar.solution(),'com custo',res_IDAstar.path_cost)
else:
    print('\nSem Solução')
print('Visitados:',visitados)

# ---------------- IDA* ----------------

# Solução: ['ir de I para B', 'ir de B para F2'] com custo 12
# Visitados: 14

s = ProblemaGrafo()
print('---------------- IDA* pedagógico ----------------')
f=lambda n: n.path_cost + s.h1(n)
res_IDAstar,visitados=ida_star_graph_search_count(s,f,True)
if res_IDAstar:
    print("\nSolução:",res_IDAstar.solution(),'com custo',res_IDAstar.path_cost)
else:
    print('\nSem Solução')
print('Visitados:',visitados)

# ---------------- IDA* pedagógico ----------------
# ------Cutoff at 10

# I
# Cost: 0 f= 10

# A
# Cost: 3 f= 8

# C
# Cost: 4 f= 7

# D
# Cost: 9 f= 16
# Out of cutoff -- minimum out: 16

# B
# Cost: 3 f= 8

# E
# Cost: 4 f= 8

# F2
# Cost: 12 f= 12
# Out of cutoff -- minimum out: 12


# ------Cutoff at 12

# I
# Cost: 0 f= 10

# A
# Cost: 3 f= 8

# C
# Cost: 4 f= 7

# D
# Cost: 9 f= 16
# Out of cutoff -- minimum out: 16

# B
# Cost: 3 f= 8

# E
# Cost: 4 f= 8

# F2
# Cost: 12 f= 12
# Goal found within cutoff!

# Solução: ['ir de I para B', 'ir de B para F2'] com custo 12
# Visitados: 14

grafoDuploLimpo= {'I':{'A':3,'B':3},
             'A':{'C':1,'D':6},
             'B':{'E':1,'F2':9},
             'C':{'D':4},
             'D':{'B':3,'F1':6},
             'F1':{'C':2},
             'E':{'F2':5},
             'F2':{}}

hDuploLimpo = {'A':5,'B':5,'C':3,'D':7,'E':4,'F1':0,'F2':0, 'I':10 }

s = ProblemaGrafo('I',['X'],grafoDuploLimpo,hDuploLimpo)
print('---------------- IDA* ----------------')
f=lambda n: n.path_cost + s.h1(n)
res_IDAstar,visitados=ida_star_graph_search_count(s,f)
if res_IDAstar:
    print("\nSolução:",res_IDAstar.solution(),'com custo',res_IDAstar.path_cost)
else:
    print('\nSem Solução')
print('Visitados:',visitados)

# ---------------- IDA* ----------------

# Sem Solução
# Visitados: 22

grafoDuploLimpo= {'I':{'A':3,'B':3},
             'A':{'C':1,'D':6},
             'B':{'E':1,'F2':9},
             'C':{'D':4},
             'D':{'B':3,'F1':6},
             'F1':{'C':2},
             'E':{'F2':5},
             'F2':{}}

hDuploLimpo = {'A':5,'B':5,'C':3,'D':7,'E':4,'F1':0,'F2':0, 'I':10 }

s = ProblemaGrafo('I',['X'],grafoDuploLimpo,hDuploLimpo)
print('---------------- IDA* ----------------')
f=lambda n: n.path_cost + s.h1(n)
res_IDAstar,visitados=ida_star_graph_search_count(s,f,True)
if res_IDAstar:
    print("\nSolução:",res_IDAstar.solution(),'com custo',res_IDAstar.path_cost)
else:
    print('\nSem Solução')
print('Visitados:',visitados)

# ---------------- IDA* ----------------
# ------Cutoff at 10

# I
# Cost: 0 f= 10

# A
# Cost: 3 f= 8

# C
# Cost: 4 f= 7

# D
# Cost: 9 f= 16
# Out of cutoff -- minimum out: 16

# B
# Cost: 3 f= 8

# E
# Cost: 4 f= 8

# F2
# Cost: 12 f= 12
# Out of cutoff -- minimum out: 12


# ------Cutoff at 12

# I
# Cost: 0 f= 10

# A
# Cost: 3 f= 8

# C
# Cost: 4 f= 7

# D
# Cost: 9 f= 16
# Out of cutoff -- minimum out: 16

# B
# Cost: 3 f= 8

# E
# Cost: 4 f= 8

# F2
# Cost: 12 f= 12


# ------Cutoff at 16

# I
# Cost: 0 f= 10

# A
# Cost: 3 f= 8

# C
# Cost: 4 f= 7

# D
# Cost: 9 f= 16

# F1
# Cost: 15 f= 15

# B
# Cost: 3 f= 8

# E
# Cost: 4 f= 8

# F2
# Cost: 12 f= 12

# Sem Solução
# Visitados: 22

parametros="T=15\nM=6\nP=10"
linha1= "= = = = = =\n"
linha2= "= * F @ * =\n"
linha3= "= . . . . =\n"
linha4= "= . = . . =\n"
linha5= "= . = . . =\n"
linha6= "= = = = = =\n"
grelha=linha1+linha2+linha3+linha4+linha5+linha6
mundoStandard2=parametros + "\n" + grelha
gx=MedoTotal(mundoStandard2)
print('---------------- IDA* ----------------')
f=lambda n: n.path_cost + gx.minimal_h(n)
res_IDAstar,visitados=ida_star_graph_search_count(gx,f)
if res_IDAstar:
    print("\nSolução:",res_IDAstar.solution(),'com custo',res_IDAstar.path_cost)
else:
    print('\nSem Solução')
print('Visitados:',visitados)

# ---------------- IDA* ----------------

# Solução: ['E', 'S', 'S', 'S', 'W', 'N', 'N', 'W', 'W', 'N', 'S', 'S', 'S', 'N', 'S'] com custo 18
# Visitados: 1919

parametros="T=45\nM=6\nP=10"
linha1= "= = = = = = = = = =\n"
linha2= "= @ . * . . * . . =\n"
linha3= "= . = = = = = = . =\n"
linha4= "= . = F * . . . . =\n"
linha5= "= . = = = = = = . =\n"
linha6= "= . = . . . . . . =\n"
linha7= "= . = . . . . . . =\n"
linha8= "= * . . . . . . . =\n"
linha9= "= . . . . . . . . =\n"
linha10="= = = = = = = = = =\n"
grelha=linha1+linha2+linha3+linha4+linha5+linha6+linha7+linha8+linha9+linha10
mundoStandardx=parametros + "\n" + grelha
gx=MedoTotal(mundoStandardx)

print('---------------- IDA* ----------------')
f=lambda n: n.path_cost + gx.minimal_h(n)
res_IDAstar,visitados=ida_star_graph_search_count(gx,f)
if res_IDAstar:
    print("\nSolução:",res_IDAstar.solution(),'com custo',res_IDAstar.path_cost)
else:
    print('\nSem Solução')
print('Visitados:',visitados)

# ---------------- IDA* ----------------

# Solução: ['S', 'S', 'S', 'S', 'S', 'S', 'E', 'W', 'N', 'N', 'N', 'N', 'N', 'N', 'E', 'E', 'W', 'W', 'E', 'E', 'E', 'E', 'W', 'E', 'E', 'E', 'W', 'E', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'E', 'E', 'E', 'E', 'S', 'S', 'W', 'W', 'W', 'W'] com custo 66
# Visitados: 144987

parametros="T=23\nM=7\nP=8"
linha1= "= = = = = = = = = =\n"
linha2= "= @ . . . . * . . =\n"
linha3= "= . = = = = . = . =\n"
linha4= "= . = F * = . . . =\n"
linha5= "= = = = . = . = . =\n"
linha6= "= * = . . . . . . =\n"
linha7= "= . = = = = . = = =\n"
linha8= "= * . . . . . = . =\n"
linha9= "= * . . . . . . . =\n"
linha10="= = = = = = = = = =\n"
grelha=linha1+linha2+linha3+linha4+linha5+linha6+linha7+linha8+linha9+linha10
mundoStandardx=parametros + "\n" + grelha
gx=MedoTotal(mundoStandardx)
print('---------------- IDA* ----------------')
f=lambda n: n.path_cost + gx.minimal_h(n)
res_IDAstar,visitados=ida_star_graph_search_count(gx,f)
if res_IDAstar:
    print("\nSolução:",res_IDAstar.solution(),'com custo',res_IDAstar.path_cost)
else:
    print('\nSem Solução')
print('Visitados:',visitados)

# ---------------- IDA* ----------------

# Solução: ['S', 'N', 'E', 'E', 'E', 'E', 'E', 'S', 'S', 'S', 'S', 'W', 'W', 'N', 'N', 'S', 'S', 'E', 'E', 'E', 'E', 'N', 'N'] com custo 28
# Visitados: 2342

parametros="T=6\nM=4\nP=10"
linha1= "= = = = = =\n"
linha2= "= * F @ . =\n"
linha3= "= . = . . =\n"
linha4= "= . . . . =\n"
linha5= "= . = . . =\n"
linha6= "= = = = = =\n"
grelha=linha1+linha2+linha3+linha4+linha5+linha6
mundoStandardx=parametros + "\n" + grelha
gx=MedoTotal(mundoStandardx)
print('---------------- IDA* ----------------')
f=lambda n: n.path_cost + gx.minimal_h(n)
res_IDAstar,visitados=ida_star_graph_search_count(gx,f)
if res_IDAstar:
    print("\nSolução:",res_IDAstar.solution(),'com custo',res_IDAstar.path_cost)
else:
    print('\nSem Solução')
print('Visitados:',visitados)

# ---------------- IDA* ----------------

# Sem Solução
# Visitados: 10

	
parametros="T=23\nM=7\nP=8"
linha1= "= = = = = = = = = =\n"
linha2= "= @ . . . . * . . =\n"
linha3= "= . = = = = . = . =\n"
linha4= "= . = F * = . . . =\n"
linha5= "= = = = . = . = . =\n"
linha6= "= * = . . . . . . =\n"
linha7= "= . = = = = . = = =\n"
linha8= "= * . . . . . = . =\n"
linha9= "= * . . . . . . . =\n"
linha10="= = = = = = = = = =\n"
grelha=linha1+linha2+linha3+linha4+linha5+linha6+linha7+linha8+linha9+linha10
mundoStandardx=parametros + "\n" + grelha
gx=MedoTotal(mundoStandardx)
print('---------------- IDA* ----------------')
f=lambda n: n.path_cost + gx.minimal_h(n)
res_IDAstar,visitados=ida_star_graph_search_count(gx,f)
if res_IDAstar:
    print("\nSolução:",res_IDAstar.solution(),'com custo',res_IDAstar.path_cost)
else:
    print('\nSem Solução')
print('Visitados:',visitados)

# ---------------- IDA* ----------------

# Solução: ['S', 'N', 'E', 'E', 'E', 'E', 'E', 'S', 'S', 'S', 'S', 'W', 'W', 'N', 'N', 'S', 'S', 'E', 'E', 'E', 'E', 'N', 'N'] com custo 28
# Visitados: 2342