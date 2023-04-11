#sudo apt install python3-pip
#python.exe -m pip install --upgrade pip 

import random
from collections import Counter

# Funcion que busca
def busca(mesaa,carton):
    for i in range(len(mesaa)-1):
        #print(mesaa[len(mesaa)-1][:1],mesaa[i][:1])
        if mesaa[len(mesaa)-1]==mesaa[i]:
            carton+=2
            mesaa.pop(i)
            # Elimina carta tirada
            mesaa.pop(len(mesaa)-1)
            break
    return mesaa,carton

# Cuanto carton llevaria al sumar cartas
def sumarcartas(mesa,aux,aux_sumar,aux_suman):
    carton=0
    cont=0
    for i in range(len(mesa)-1):
        for j in range(i+1,len(mesa)-1):
            if mesa[i] in aux_sumar and mesa[j] in aux_sumar and aux in aux_suman and int(mesa[i])+int(mesa[j])<=7:
                if int(mesa[i])+int(mesa[j])==int(aux) and cont<1:
                    cont+=1
                    carton+=2
                    con=1
                    while str(int(aux)+con) in mesa:
                        con+=1
                        carton+=1
    #print('Cuanto sumocartas: ',carton)
    return carton

def buscacuenta(mesaa,aux):
    carton=0
    for i in range(len(mesaa)-1):
        if mesaa[len(mesaa)-1]==mesaa[i]:
            carton+=1
            break
    return carton

def buscamain(mesa,carton,score,auxcp1,auxcp2):
    # Cartas a Numeros
    for i in range(len(mesa)):
        if mesa[i]=='A':
            mesa[i]='1'
        elif mesa[i]=='J':
            mesa[i]='8'
        elif mesa[i]=='Q':
            mesa[i]='9'
        elif mesa[i]=='K':
            mesa[i]='10'
    
    # Carta tirada
    aux=mesa[len(mesa)-1]
    # Si la carta anterior es igual a la que tiro
    #print('AAAA',mesa,mesa[len(mesa)-2],mesa[len(mesa)-1],auxcp1,auxcp2)
    if mesa[len(mesa)-2]==mesa[len(mesa)-1] and auxcp1==auxcp2 and len(mesa)>1:
        #print('Caida')
        score+=2
    aux_len_mesa=len(mesa)
    # Elegir sumar o siguiente
    aux_a_llevar=sumarcartas(mesa,aux,aux_sumar,aux_suman)
    aux_in=buscacuenta(mesa,aux)
    eleccion=0
    #print('Antes de todo',mesa)
    if aux_a_llevar>0 and aux_in>0:
        #print('Llevar')
        #print('1: ',aux_a_llevar+1)
        #print('2: ',aux_a_llevar)
        eleccion=1
    if eleccion==1 or eleccion==0:
        # Suma con siguiente
        for i in range(len(mesa)-1):
            for j in range(i+1,len(mesa)-1):
                if mesa[i] in aux_sumar and mesa[j] in aux_sumar and aux in aux_suman and int(mesa[i])+int(mesa[j])<=7:
                    #print(mesa[i]+mesa[j])
                    if int(mesa[i])+int(mesa[j])==int(aux):
                        #print(int(mesa[i])+int(mesa[j]))
                        mesa.pop(i)
                        mesa.pop(j-1)
                        #print('Despues de eliminar la suma',mesa)
                        carton+=2
                        # Siguiente
                        con=1
                        while str(int(aux)+con) in mesa:
                            #print('mesa WHILE',mesa)
                            #print('aux WHILE',aux)
                            index = mesa.index(str(int(aux)+con))
                            mesa.pop(index)
                            con+=1
                            carton+=1
                            #print('Siguiente',mesa)

                        # Eliminar carta tirada
                        #print('mesa elimi',mesa)
                        #print('aux elimi',aux)
                        if aux in mesa:
                            index = mesa.index(str(aux))
                        else:
                            break
                        #print('index',index)
                        mesa.pop(index)
                        carton+=1
                        #print('Despues de eliminar siguiente', mesa)
                        break
    if eleccion==2 or eleccion==0:
        # Una-Siguiente
        con=1
        if aux in mesa:
            index = mesa.index(aux)
            while str(int(aux)+con) in mesa and index!=len(mesa)-1:
                index = mesa.index(str(int(aux)+con))
                mesa.pop(index)
                con+=1
                carton+=1
                #print('Siguiente',mesa)
                #Actualiza
                index = mesa.index(aux)
        #print('Despues de eliminar Una-Siguiente', mesa)

    # Una
    mesa,carton=busca(mesa,carton)

    # Numeros a cartas
    for i in range(len(mesa)):
        if mesa[i]=='1':
            mesa[i]='A'
        elif mesa[i]=='8':
            mesa[i]='J'
        elif mesa[i]=='9':
            mesa[i]='Q'
        elif mesa[i]=='10':
            mesa[i]='K'
    '''
    # Elimina carta tirada
    index = mesa.index(str(aux))
    mesa.pop(index)
    carton+=1
    '''
    # Si mesa queda limpia
    if len(mesa)==0 and score<30:
        score+=2
        #print('Limpia')
    return mesa,carton,score


# Cartas que se pueden sumar
aux_sumar=['1','2','3','4','5','6']
# Cartas que suman a otras
aux_suman=['3','4','5','6','7']


for xy in range(10):
    winplayer1=0
    winplayer1list=[]
    winplayer2=0
    winplayer2list=[]
    for hh in range(1000):
        scorep1=0
        scorep2=0
        aux_turno=0
        while scorep1<40 and scorep2<40:
            T=['A','A','A','A','2','2','2','2','3','3','3','3',
               '4','4','4','4','5','5','5','5','6','6','6','6',
               '7','7','7','7','J','J','J','J','Q','Q','Q','Q',
               'K','K','K','K']
            random.shuffle(T)
            #print(T)
            #T=['6', '7', 'J', '3', '2', '5', '7', '2', 'K', '7', 'A', 'A', 'J', '2', '6', '4', '5', 'Q', '3', '6', '7', '4', 'Q', '2', 'Q', 'K', '4', '5', 'A', '6', 'K', '3', 'J', '4', 'K', 'J', '5', 'Q', '3', 'A']
            cartonp1=0
            cartonp2=0

            mesa=[]

            cuenta={}
            
            
            #mesa=['K', '3', 'J', 'A']
            
            for i in range(4):
                aux1=[]
                aux2=[]

                auxcp1=0
                auxcp2=0
                for j in range(5):
                    #print("Player 1 ",T[0])
                    aux1.append(T[0])
                    T.pop(0)
                    #print("Player 2 ",T[0])
                    aux2.append(T[0])
                    T.pop(0)
                #aux=1

                # Verificar si hay ronda
                conteo=Counter(aux1)
                aux_ronda1=0
                for ii in aux1:
                    if conteo[ii]==3:
                        aux_ronda1=1
                        break
                if aux_ronda1==1:
                    #print("Ronda Player 1")
                    scorep1+=2

                conteo=Counter(aux2)
                aux_ronda2=0
                for ii in aux2:
                    if conteo[ii]==3:
                        aux_ronda2=1
                        break
                if aux_ronda2==1:
                    #print("Ronda Player 2")
                    scorep2+=2
                
                # Si tiene 38 y le sale ronda
                if scorep1==40 or scorep2==40:
                    break
                
                #print("---------- RONDA",i+1," ----------")
                while len(aux2)!=0 and scorep1<40 and scorep2<40:
                    #print("Ronda",aux)
                    #aux+=1
                    if aux_turno%2==0:
                        comparalen=len(mesa)
                        #print("Player 1")
                        #print("MESA:", mesa)
                        #print("Que juegas?")
                        #print(aux1)
                        #print('Cartas player 2',aux2)
                        # AAA
                        if len(cuenta)==0:
                            # Mira si las frecuencias de las cartas en mi
                            # mano son las mismas
                            aux_dic_cont=Counter(aux1)
                            #print(aux_dic_cont)
                            veri=list(aux_dic_cont.values())
                            #print(veri)
                            veri_count=Counter(veri)
                            #print(veri_count)
                            condi=0
                            # Si es 1 que escoga randomicamente
                            if len(veri_count)==1:
                                condi=1
                            #print(condi)
                            aux_mayo=0
                            aux_comp=0
                            for i in aux_dic_cont:
                                if condi!=1:
                                    # Hay mas de 1 carta igual en mi mano
                                    if aux_mayo<aux_dic_cont[i]:
                                        aux_mayo=aux_dic_cont[i]
                                        aux_comp=i
                                        #print(i)
                            #print('aaa',aux_comp)
                            # Si las frecuencias son diferentes
                            if aux_comp!=0:
                                for iii in range(len(aux1)):
                                    if aux_comp==aux1[iii]:
                                        mesa.append(aux1[iii])
                                        auxcp1=aux1[iii]
                                        aux_indexv=iii
                                        #print('Deb imprimir solo una vez mesa',mesa)
                                        break
                            # Si son las mismas escoge un random
                            else:
                                tirar_random=random.randint(0,len(aux1)-1)
                                valor_tirar=aux1
                                #print('Lista',valor_tirar,'Carta a tirar', valor_tirar[tirar_random])
                                auxx_index=-1
                                for i in aux1:
                                    auxx_index+=1
                                    if i==valor_tirar[tirar_random]:
                                        #print(auxx_index)
                                        break
                                #print(auxx_index)
                                mesa.append(aux1[auxx_index])
                                auxcp1=aux1[auxx_index]
                                #print(mesa)
                                #print(auxcp2)
                                aux_indexv=auxx_index
                        else:
                            # -----------------------------------------------------------------------------------------------
                            aux_indexv=-1
                            # ------------------------------------------------------------------
                            # Agente experto
                            # ------------------------------------------------------------------
                            #print('----------------------------------------------------')
                            # Verifica si puedo caerle, pero ene este caso la ultima carta de la mesa no necesariamente
                            # es la carta tirada en el turno anterior. Entonces la prioridad no seria de "si se puede caer"
                            # seria la suma de cartas, si siguiente, al menos me llevo una
                            #print('SI SE PUEDE CAER')
                            #print('----------------------------------------------------')
                            if len(mesa)>0:
                                for i in aux1:
                                    aux_indexv+=1
                                    #print('CAERLE',i,mesa[len(mesa)-1])
                                    if i==mesa[len(mesa)-1] and auxcp2==i:
                                        #print('ENTRA')
                                        mesa.append(i)
                                        auxcp1=i
                                        #aux2.pop(aux_indexv)
                                        break
                                    else:
                                        None
                                #print('Mano player 2',aux2)
                                #print('----------------------------------------------------')
                            # ------------------------------------------------------------------*
                            if comparalen==len(mesa):
                                aux_indexv=0
                                # Verifica si alguna suma
                                #print('SI ALGUNA SUMA')
                                #print('----------------------------------------------------')
                                for i in aux1:
                                    svalor=sumarcartas(mesa,i,aux_sumar,aux_suman)
                                    #print("Si alguna suma, cuantos suma",svalor)
                                    # if svalor> algo: tire esa carta y llevese las cartas
                                    # elimine la carta tirada de aux2.pop(aux_indexv)
                                #print('Mano player 2',aux2)
                                #print('----------------------------------------------------')
                            # ------------------------------------------------------------------
                            if comparalen==len(mesa):
                                aux_indexv=-1
                                # Verificar si me puedo llevar Una-Siguiente
                                #print('SI ALMENOS ME LLEVO UNA')
                                #print('----------------------------------------------------')
                                # Ordenar las cartas de la mano
                                # Cartas a Numeros
                                for i in range(len(aux1)):
                                    if aux1[i]=='A':
                                        aux1[i]=1
                                    elif aux1[i]=='J':
                                        aux1[i]=8
                                    elif aux1[i]=='Q':
                                        aux1[i]=9
                                    elif aux1[i]=='K':
                                        aux1[i]=10
                                    else:
                                        aux1[i]=int(aux1[i])
                                #print('Sin ordenar',aux1)
                                aux1.sort()
                                #print('Ordenado',aux2)
                                # Numeros a cartas
                                for i in range(len(aux1)):
                                    if aux1[i]==1:
                                        aux1[i]='A'
                                    elif aux1[i]==8:
                                        aux1[i]='J'
                                    elif aux1[i]==9:
                                        aux1[i]='Q'
                                    elif aux1[i]==10:
                                        aux1[i]='K'
                                    else:
                                        aux1[i]=str(aux1[i])
                                #print('Vuelta',aux2)
                                
                                for i in aux1:
                                    aux_indexv+=1
                                    if i in mesa:
                                        mesa.append(i)
                                        auxcp1=i
                                        #aux2.pop(aux_indexv)
                                        break
                                # Programar llevarme la que tenga mas o menos frecuencias
                                #print('Mano player 2',aux2)
                                #print('index ',aux_indexv)
                                #print('----------------------------------------------------')
                            # ------------------------------------------------------------------*
                            if comparalen==len(mesa):
                                aux_indexv=-1
                                # Si no hay carta similar, tirar la carta con mas frecuencias
                                #print('TIRAR BASADO EN FRECUENCIAS')
                                #print('----------------------------------------------------')
                                aux_dic={}
                                aux_mayor=0
                                aux_mayor_n=0
                                for i in aux1:
                                    if i in cuenta:
                                        # Obtener carta con mas frecuencia
                                        if cuenta[i]>aux_mayor_n:
                                            aux_mayor_n=cuenta[i]
                                            aux_mayor=i
                                        # Meter valores a aux_dic
                                        aux_dic[i]=cuenta[i]
                                #print(aux_dic)
                                #obtener la carta con mas frecuencia
                                #print(aux_mayor)
                                #print(aux_mayor_n)
                                # Buscar cartas que tienen la misma frecuencia
                                aux_dic2={}
                                for i in aux_dic:
                                    if aux_dic[i]==aux_mayor_n:
                                        aux_dic2[i]=aux_mayor_n
                                #print('Lista frecuencias mayores encontradas que esten en mi mano',aux_dic2)
                                # Elegir randomicamente que carta votar
                                if len(aux_dic2)>0:
                                    # Mira si las frecuencias de las cartas en mi
                                    # mano son las mismas
                                    aux_dic_cont=Counter(aux1)
                                    #print(aux_dic_cont)
                                    veri=list(aux_dic_cont.values())
                                    veri_count=Counter(veri)
                                    #print(veri_count)
                                    condi=0
                                    # Si es 1 que escoga randomicamente
                                    if len(veri_count)==1:
                                        condi=1
                                    #print(condi)
                                    aux_mayo=0
                                    aux_comp=0
                                    for i in aux_dic_cont:
                                        if condi!=1:
                                            if aux_mayo<aux_dic_cont[i]:
                                                aux_mayo=aux_dic_cont[i]
                                                aux_comp=i
                                                #print(i)
                                    #print('aaa',aux_comp)
                                    #print(aux_dic2)
                                    if aux_comp!=0:
                                        #print('ENTRA')
                                        # Si son las mismas y es K, Q o J tirar la que no suma
                                        if 'K' in aux_dic2:
                                            for it in range(len(aux1)):
                                                if aux1[it]=='K':
                                                    mesa.append(aux1[it])
                                                    auxcp1=aux1[it]
                                                    aux_indexv=it
                                                    #print('2-1 K',mesa, it)
                                                    break
                                        elif 'Q' in aux_dic2:
                                            for it in range(len(aux1)):
                                                if aux1[it]=='Q':
                                                    mesa.append(aux1[it])
                                                    auxcp1=aux1[it]
                                                    aux_indexv=it
                                                    #print('2-1 Q',mesa, it)
                                                    break
                                        elif 'J' in aux_dic2:
                                            for it in range(len(aux1)):
                                                if aux1[it]=='J':
                                                    mesa.append(aux1[it])
                                                    auxcp1=aux1[it]
                                                    aux_indexv=it
                                                    #print('2-1 J',mesa, it)
                                                    break
                                        else:
                                            # Si son las mismas pero son numeros escoge un random
                                            tirar_random=random.randint(0,len(aux_dic2)-1)
                                            valor_tirar=list(aux_dic2.keys())
                                            #print('Lista',valor_tirar,'Carta a tirar', valor_tirar[tirar_random])
                                            auxx_index=-1
                                            for i in aux1:
                                                auxx_index+=1
                                                if i==valor_tirar[tirar_random]:
                                                    #print(auxx_index)
                                                    break
                                            #print(auxx_index)
                                            mesa.append(aux1[auxx_index])
                                            auxcp1=aux1[auxx_index]
                                            #print(mesa)
                                            #print(auxcp2)
                                            aux_indexv=auxx_index
                                            #print('2-2',mesa)
                                    else:
                                        #print('ENTRA 2')
                                        # Si son las mismas pero son numeros escoge un random
                                        tirar_random=random.randint(0,len(aux_dic2)-1)
                                        valor_tirar=list(aux_dic2.keys())
                                        #print('Lista',valor_tirar,'Carta a tirar', valor_tirar[tirar_random])
                                        auxx_index=-1
                                        for i in aux1:
                                            auxx_index+=1
                                            if i==valor_tirar[tirar_random]:
                                                #print(auxx_index)
                                                break
                                        #print(auxx_index)
                                        mesa.append(aux1[auxx_index])
                                        auxcp1=aux1[auxx_index]
                                        #print(mesa)
                                        #print(auxcp2)
                                        aux_indexv=auxx_index
                                        #print('1',mesa)
                                else:
                                    None
                                    #Deja que tire randomicamente
                                #print('Mano player 2',aux2)
                                #print('----------------------------------------------------')
                            # ------------------------------------------------------------------
                            if comparalen==len(mesa):
                                # Si no hay frecuencias ni nada tiro random (Tirar randomicamente)
                                #print("TIRO CUALQUIERA")
                                #print('----------------------------------------------------')
                                # Mira si las frecuencias de las cartas en mi
                                # mano son las mismas
                                aux_dic_cont=Counter(aux1)
                                #print(aux_dic_cont)
                                veri=list(aux_dic_cont.values())
                                veri_count=Counter(veri)
                                #print(veri_count)
                                condi=0
                                # Si es 1 que escoga randomicamente
                                if len(veri_count)==1:
                                    condi=1
                                #print(condi)
                                aux_mayo=0
                                aux_comp=0
                                for i in aux_dic_cont:
                                    if condi!=1:
                                        if aux_mayo<aux_dic_cont[i]:
                                            aux_mayo=aux_dic_cont[i]
                                            aux_comp=i
                                            #print(i)
                                #print('aaa',aux_comp)
                                # Si las frecuencias son diferentes
                                if aux_comp!=0:
                                    for iii in range(len(aux1)):
                                        if aux_comp==aux1[iii]:
                                            mesa.append(aux1[iii])
                                            auxcp1=aux1[iii]
                                            aux_indexv=iii
                                            #print('Deb imprimir solo una vez mesa',mesa)
                                            break
                                # Si son las mismas escoge un random
                                else:
                                    tirar_random=random.randint(0,len(aux1)-1)
                                    mesa.append(aux1[tirar_random])
                                    auxcp1=aux1[tirar_random]
                                    #aux2.pop(tirar_random)
                                    aux_indexv=tirar_random
                                #print('Mano player 2',aux2)
                                #print('----------------------------------------------------')
                        index1=aux_indexv
                        # AAA
                        # Agregar al diccionario contar
                        if aux1[index1] in cuenta:
                            cuenta[mesa[len(mesa)-1]]+=1
                        else:
                            cuenta[mesa[len(mesa)-1]]=1
                        # Aux para comparar caida y limpia
                        #auxcp1=aux1[index1]
                        aux1.pop(index1)
                        #print('Cuenta',cuenta)
                        mesa,cartonp1,scorep1=buscamain(mesa,cartonp1,scorep1,auxcp1,auxcp2)
                        #print("Carton player 1: ",cartonp1,"Carton player 2: ",cartonp2)
                        #print("Score:   ",scorep1,"Score:   ",scorep2)
                        #print("\n")
                        comparalen=len(mesa)
                        # =====================================================================
                        #print("Player 2")
                        #print("MESA:", mesa)
                        #print("Que juegas?")
                        #print(aux2)
                        # -----------------------------------------------------------------------------------------------
                        aux_indexv=-1
                        # ------------------------------------------------------------------
                        # Agente experto
                        # ------------------------------------------------------------------
                        #print('----------------------------------------------------')
                        # Verifica si puedo caerle, pero ene este caso la ultima carta de la mesa no necesariamente
                        # es la carta tirada en el turno anterior. Entonces la prioridad no seria de "si se puede caer"
                        # seria la suma de cartas, si siguiente, al menos me llevo una
                        #print('SI SE PUEDE CAER')
                        #print('----------------------------------------------------')
                        
                        if len(mesa)>0:
                            for i in aux2:
                                aux_indexv+=1
                                #print('CAERLE',i,mesa[len(mesa)-1])
                                if i==mesa[len(mesa)-1] and auxcp1==i:
                                    #print('ENTRA')
                                    mesa.append(i)
                                    auxcp2=i
                                    #aux2.pop(aux_indexv)
                                    break
                                else:
                                    None
                            #print('Mano player 2',aux2)
                            #print('----------------------------------------------------')
                        
                        # ------------------------------------------------------------------*
                        
                        if comparalen==len(mesa):
                            aux_indexv=0
                            # Verifica si alguna suma
                            #print('SI ALGUNA SUMA')
                            #print('----------------------------------------------------')
                            for i in aux2:
                                svalor=sumarcartas(mesa,i,aux_sumar,aux_suman)
                                
                                #print("Si alguna suma, cuantos suma",svalor)
                                # if svalor> algo: tire esa carta y llevese las cartas
                                # elimine la carta tirada de aux2.pop(aux_indexv)
                            #print('Mano player 2',aux2)
                            #print('----------------------------------------------------')
                        
                        # ------------------------------------------------------------------
                        
                        if comparalen==len(mesa):
                            aux_indexv=-1
                            # Verificar si me puedo llevar Una-Siguiente
                            #print('SI ALMENOS ME LLEVO UNA')
                            #print('----------------------------------------------------')
                            # Ordenar las cartas de la mano
                            # Cartas a Numeros
                            for i in range(len(aux2)):
                                if aux2[i]=='A':
                                    aux2[i]=1
                                elif aux2[i]=='J':
                                    aux2[i]=8
                                elif aux2[i]=='Q':
                                    aux2[i]=9
                                elif aux2[i]=='K':
                                    aux2[i]=10
                                else:
                                    aux2[i]=int(aux2[i])
                            #print('Sin ordenar',aux2)
                            aux2.sort()
                            #print('Ordenado',aux2)
                            # Numeros a cartas
                            for i in range(len(aux2)):
                                if aux2[i]==1:
                                    aux2[i]='A'
                                elif aux2[i]==8:
                                    aux2[i]='J'
                                elif aux2[i]==9:
                                    aux2[i]='Q'
                                elif aux2[i]==10:
                                    aux2[i]='K'
                                else:
                                    aux2[i]=str(aux2[i])
                            #print('Vuelta',aux2)
                            
                            for i in aux2:
                                aux_indexv+=1
                                if i in mesa:
                                    mesa.append(i)
                                    auxcp2=i
                                    #aux2.pop(aux_indexv)
                                    break
                            # Programar llevarme la que tenga mas o menos frecuencias
                            #print('Mano player 2',aux2)
                            #print('index ',aux_indexv)
                            #print('----------------------------------------------------')
                        
                        # ------------------------------------------------------------------*
                        
                        if comparalen==len(mesa):
                            aux_indexv=-1
                            # Si no hay carta similar, tirar la carta con mas frecuencias
                            #print('TIRAR BASADO EN FRECUENCIAS')
                            #print('----------------------------------------------------')
                            aux_dic={}
                            aux_mayor=0
                            aux_mayor_n=0
                            for i in aux2:
                                if i in cuenta:
                                    # Obtener carta con mas frecuencia
                                    if cuenta[i]>aux_mayor_n:
                                        aux_mayor_n=cuenta[i]
                                        aux_mayor=i
                                    # Meter valores a aux_dic
                                    aux_dic[i]=cuenta[i]
                            #print(aux_dic)
                            #obtener la carta con mas frecuencia
                            #print(aux_mayor)
                            #print(aux_mayor_n)
                            # Buscar cartas que tienen la misma frecuencia
                            aux_dic2={}
                            for i in aux_dic:
                                if aux_dic[i]==aux_mayor_n:
                                    aux_dic2[i]=aux_mayor_n
                            #print('Lista frecuencias mayores encontradas que esten en mi mano',aux_dic2)
                            # Elegir randomicamente que carta votar
                            if len(aux_dic2)>0:
                                # Mira si las frecuencias de las cartas en mi
                                # mano son las mismas
                                aux_dic_cont=Counter(aux2)
                                #print(aux_dic_cont)
                                veri=list(aux_dic_cont.values())
                                veri_count=Counter(veri)
                                #print(veri_count)
                                condi=0
                                # Si es 1 que escoga randomicamente
                                if len(veri_count)==1:
                                    condi=1
                                #print(condi)
                                aux_mayo=0
                                aux_comp=0
                                for i in aux_dic_cont:
                                    if condi!=1:
                                        if aux_mayo<aux_dic_cont[i]:
                                            aux_mayo=aux_dic_cont[i]
                                            aux_comp=i
                                            #print(i)
                                #print('aaa',aux_comp)
                                #print(aux_dic2)
                                
                                if aux_comp!=0:
                                    #print('ENTRA')
                                    # Si son las mismas y es K, Q o J tirar la que no suma
                                    if 'K' in aux_dic2:
                                        for it in range(len(aux2)):
                                            if aux2[it]=='K':
                                                mesa.append(aux2[it])
                                                auxcp2=aux2[it]
                                                aux_indexv=it
                                                #print('2-1 K',mesa, it)
                                                break
                                    elif 'Q' in aux_dic2:
                                        for it in range(len(aux2)):
                                            if aux2[it]=='Q':
                                                mesa.append(aux2[it])
                                                auxcp2=aux2[it]
                                                aux_indexv=it
                                                #print('2-1 Q',mesa, it)
                                                break
                                    elif 'J' in aux_dic2:
                                        for it in range(len(aux2)):
                                            if aux2[it]=='J':
                                                mesa.append(aux2[it])
                                                auxcp2=aux2[it]
                                                aux_indexv=it
                                                #print('2-1 J',mesa, it)
                                                break
                                    else:
                                        # Si son las mismas escoge un random
                                        tirar_random=random.randint(0,len(aux_dic2)-1)
                                        valor_tirar=list(aux_dic2.keys())
                                        #print('Lista',valor_tirar,'Carta a tirar', valor_tirar[tirar_random])
                                        auxx_index=-1
                                        for i in aux2:
                                            auxx_index+=1
                                            if i==valor_tirar[tirar_random]:
                                                #print(auxx_index)
                                                break
                                        #print(auxx_index)
                                        mesa.append(aux2[auxx_index])
                                        auxcp2=aux2[auxx_index]
                                        #print(mesa)
                                        #print(auxcp2)
                                        aux_indexv=auxx_index
                                        #print('2-2',mesa)
                                else:
                                    #print('ENTRA 2')
                                    # Si son las mismas escoge un random
                                    tirar_random=random.randint(0,len(aux_dic2)-1)
                                    valor_tirar=list(aux_dic2.keys())
                                    #print('Lista',valor_tirar,'Carta a tirar', valor_tirar[tirar_random])
                                    auxx_index=-1
                                    for i in aux2:
                                        auxx_index+=1
                                        if i==valor_tirar[tirar_random]:
                                            #print(auxx_index)
                                            break
                                    #print(auxx_index)
                                    mesa.append(aux2[auxx_index])
                                    auxcp2=aux2[auxx_index]
                                    #print(mesa)
                                    #print(auxcp2)
                                    aux_indexv=auxx_index
                                    #print('1',mesa)
                                
                            else:
                                None
                                #Deja que tire randomicamente
                            #print('Mano player 2',aux2)
                            #print('----------------------------------------------------')
                        
                        # ------------------------------------------------------------------
                        if comparalen==len(mesa):
                            # Si no hay frecuencias ni nada tiro random (Tirar randomicamente)
                            #print("TIRO CUALQUIERA")
                            #print('----------------------------------------------------')
                            # Mira si las frecuencias de las cartas en mi
                            # mano son las mismas
                            aux_dic_cont=Counter(aux2)
                            #print(aux_dic_cont)
                            veri=list(aux_dic_cont.values())
                            veri_count=Counter(veri)
                            #print(veri_count)
                            condi=0
                            # Si es 1 que escoga randomicamente
                            if len(veri_count)==1:
                                condi=1
                            #print(condi)
                            aux_mayo=0
                            aux_comp=0
                            for i in aux_dic_cont:
                                if condi!=1:
                                    if aux_mayo<aux_dic_cont[i]:
                                        aux_mayo=aux_dic_cont[i]
                                        aux_comp=i
                                        #print(i)
                            #print('aaa',aux_comp)
                            # Si las frecuencias son diferentes
                            if aux_comp!=0:
                                for iii in range(len(aux2)):
                                    if aux_comp==aux2[iii]:
                                        mesa.append(aux2[iii])
                                        auxcp2=aux2[iii]
                                        aux_indexv=iii
                                        #print('Deb imprimir solo una vez mesa',mesa)
                                        break
                            # Si son las mismas escoge un random
                            else:
                                tirar_random=random.randint(0,len(aux2)-1)
                                mesa.append(aux2[tirar_random])
                                auxcp2=aux2[tirar_random]
                                #aux2.pop(tirar_random)
                                aux_indexv=tirar_random
                            #print('Mano player 2',aux2)
                            #print('----------------------------------------------------')
                        
                        index2=aux_indexv
                        #print('index',index2)
                        # -----------------------------------------------------------------------------------------------
                        # Agregar al diccionario contar
                        if aux2[index2] in cuenta:
                            cuenta[mesa[len(mesa)-1]]+=1
                        else:
                            cuenta[mesa[len(mesa)-1]]=1
                        # Aux para comparar caida y limpia
                        #auxcp2=aux2[index2]
                        aux2.pop(index2)
                        #print('Mano player 2',aux2)
                        #print('Cuentap2',cuenta)
                        # A sumado igual
                        #print('Cuenta',cuenta)
                        mesa,cartonp2,scorep2=buscamain(mesa,cartonp2,scorep2,auxcp1,auxcp2)
                        #print("Carton player 1: ",cartonp1,"Carton player 2: ",cartonp2)
                        #print("Score:   ",scorep1,"Score:   ",scorep2)
                        #print("\n")
                    else:
                        comparalen=len(mesa)
                        #print("Player 2")
                        #print("MESA:", mesa)
                        #print("Que juegas?")
                        #print(aux2)
                        if len(cuenta)==0:
                            # Mira si las frecuencias de las cartas en mi
                            # mano son las mismas
                            aux_dic_cont=Counter(aux2)
                            #print(aux_dic_cont)
                            veri=list(aux_dic_cont.values())
                            #print(veri)
                            veri_count=Counter(veri)
                            #print(veri_count)
                            condi=0
                            # Si es 1 que escoga randomicamente
                            if len(veri_count)==1:
                                condi=1
                            #print(condi)
                            aux_mayo=0
                            aux_comp=0
                            for i in aux_dic_cont:
                                if condi!=1:
                                    # Hay mas de 1 carta igual en mi mano
                                    if aux_mayo<aux_dic_cont[i]:
                                        aux_mayo=aux_dic_cont[i]
                                        aux_comp=i
                                        #print(i)
                            #print('aaa',aux_comp)
                            # Si las frecuencias son diferentes
                            if aux_comp!=0:
                                for iii in range(len(aux2)):
                                    if aux_comp==aux2[iii]:
                                        mesa.append(aux2[iii])
                                        auxcp2=aux2[iii]
                                        aux_indexv=iii
                                        #print('Deb imprimir solo una vez mesa',mesa)
                                        break
                            # Si son las mismas escoge un random
                            else:
                                tirar_random=random.randint(0,len(aux_dic2)-1)
                                valor_tirar=list(aux_dic2.keys())
                                #print('Lista',valor_tirar,'Carta a tirar', valor_tirar[tirar_random])
                                auxx_index=-1
                                for i in aux2:
                                    auxx_index+=1
                                    if i==valor_tirar[tirar_random]:
                                        #print(auxx_index)
                                        break
                                #print(auxx_index)
                                mesa.append(aux2[auxx_index])
                                auxcp2=aux2[auxx_index]
                                #print(mesa)
                                #print(auxcp2)
                                aux_indexv=auxx_index
                        else:
                            # -----------------------------------------------------------------------------------------------
                            aux_indexv=-1
                            # ------------------------------------------------------------------
                            # Agente experto
                            # ------------------------------------------------------------------
                            #print('----------------------------------------------------')
                            # Verifica si puedo caerle, pero ene este caso la ultima carta de la mesa no necesariamente
                            # es la carta tirada en el turno anterior. Entonces la prioridad no seria de "si se puede caer"
                            # seria la suma de cartas, si siguiente, al menos me llevo una
                            #print('SI SE PUEDE CAER')
                            #print('----------------------------------------------------')
                            
                            if len(mesa)>0:
                                for i in aux2:
                                    aux_indexv+=1
                                    #print('CAERLE',i,mesa[len(mesa)-1],auxcp1)
                                    if i==mesa[len(mesa)-1] and auxcp1==i:
                                        #print('ENTRA')
                                        mesa.append(i)
                                        auxcp2=i
                                        #aux2.pop(aux_indexv)
                                        break
                                    else:
                                        None
                                #print('Mano player 2',aux2)
                                #print('----------------------------------------------------')
                            
                            # ------------------------------------------------------------------*
                            
                            # Sin esto funciona
                            if comparalen==len(mesa):
                                aux_indexv=0
                                # Verifica si alguna suma
                                #print('SI ALGUNA SUMA')
                                #print('----------------------------------------------------')
                                for i in aux2:
                                    svalor=sumarcartas(mesa,i,aux_sumar,aux_suman)
                                    
                                    #print("Si alguna suma, cuantos suma",svalor)
                                    # if svalor> algo: tire esa carta y llevese las cartas
                                    # elimine la carta tirada de aux2.pop(aux_indexv)
                                #print('Mano player 2',aux2)
                                #print('----------------------------------------------------')
                            
                            # ------------------------------------------------------------------
                            
                            if comparalen==len(mesa):
                                aux_indexv=-1
                                # Verificar si me puedo llevar Una-Siguiente
                                #print('SI ALMENOS ME LLEVO UNA')
                                #print('----------------------------------------------------')
                                # Ordenar las cartas de la mano
                                # Cartas a Numeros
                                for i in range(len(aux2)):
                                    if aux2[i]=='A':
                                        aux2[i]=1
                                    elif aux2[i]=='J':
                                        aux2[i]=8
                                    elif aux2[i]=='Q':
                                        aux2[i]=9
                                    elif aux2[i]=='K':
                                        aux2[i]=10
                                    else:
                                        aux2[i]=int(aux2[i])
                                #print('Sin ordenar',aux2)
                                aux2.sort()
                                #print('Ordenado',aux2)
                                # Numeros a cartas
                                for i in range(len(aux2)):
                                    if aux2[i]==1:
                                        aux2[i]='A'
                                    elif aux2[i]==8:
                                        aux2[i]='J'
                                    elif aux2[i]==9:
                                        aux2[i]='Q'
                                    elif aux2[i]==10:
                                        aux2[i]='K'
                                    else:
                                        aux2[i]=str(aux2[i])
                                #print('Vuelta',aux2)
                                
                                for i in aux2:
                                    aux_indexv+=1
                                    if i in mesa:
                                        mesa.append(i)
                                        auxcp2=i
                                        #aux2.pop(aux_indexv)
                                        break
                                # Programar llevarme la que tenga mas o menos frecuencias
                                #print('Mano player 2',aux2)
                                #print('index ',aux_indexv)
                                #print('----------------------------------------------------')
                            
                            # ------------------------------------------------------------------*
                            
                            if comparalen==len(mesa):
                                aux_indexv=-1
                                # Si no hay carta similar, tirar la carta con mas frecuencias
                                #print('TIRAR BASADO EN FRECUENCIAS')
                                #print('----------------------------------------------------')
                                aux_dic={}
                                aux_mayor=0
                                aux_mayor_n=0
                                for i in aux2:
                                    if i in cuenta:
                                        # Obtener carta con mas frecuencia
                                        if cuenta[i]>aux_mayor_n:
                                            aux_mayor_n=cuenta[i]
                                            aux_mayor=i
                                        # Meter valores a aux_dic
                                        aux_dic[i]=cuenta[i]
                                #print(aux_dic)
                                #obtener la carta con mas frecuencia
                                #print(aux_mayor)
                                #print(aux_mayor_n)
                                # Buscar cartas que tienen la misma frecuencia
                                aux_dic2={}
                                for i in aux_dic:
                                    if aux_dic[i]==aux_mayor_n:
                                        aux_dic2[i]=aux_mayor_n
                                #print('Lista frecuencias mayores encontradas que esten en mi mano',aux_dic2)
                                # Elegir randomicamente que carta votar
                                if len(aux_dic2)>0:
                                    # Mira si las frecuencias de las cartas en mi
                                    # mano son las mismas
                                    aux_dic_cont=Counter(aux2)
                                    #print(aux_dic_cont)
                                    veri=list(aux_dic_cont.values())
                                    veri_count=Counter(veri)
                                    #print(veri_count)
                                    condi=0
                                    # Si es 1 que escoga randomicamente
                                    if len(veri_count)==1:
                                        condi=1
                                    #print(condi)
                                    aux_mayo=0
                                    aux_comp=0
                                    for i in aux_dic_cont:
                                        if condi!=1:
                                            if aux_mayo<aux_dic_cont[i]:
                                                aux_mayo=aux_dic_cont[i]
                                                aux_comp=i
                                                #print(i)
                                    #print('aaa',aux_comp)
                                    #print(aux_dic2)
                                    
                                    if aux_comp!=0:
                                        #print('ENTRA')
                                        # Si son las mismas y es K, Q o J tirar la que no suma
                                        if 'K' in aux_dic2:
                                            for it in range(len(aux2)):
                                                if aux2[it]=='K':
                                                    mesa.append(aux2[it])
                                                    auxcp2=aux2[it]
                                                    aux_indexv=it
                                                    #print('2-1 K',mesa, it)
                                                    break
                                        elif 'Q' in aux_dic2:
                                            for it in range(len(aux2)):
                                                if aux2[it]=='Q':
                                                    mesa.append(aux2[it])
                                                    auxcp2=aux2[it]
                                                    aux_indexv=it
                                                    #print('2-1 Q',mesa, it)
                                                    break
                                        elif 'J' in aux_dic2:
                                            for it in range(len(aux2)):
                                                if aux2[it]=='J':
                                                    mesa.append(aux2[it])
                                                    auxcp2=aux2[it]
                                                    aux_indexv=it
                                                    #print('2-1 J',mesa, it)
                                                    break
                                        else:
                                            # Si son las mismas escoge un random
                                            tirar_random=random.randint(0,len(aux_dic2)-1)
                                            valor_tirar=list(aux_dic2.keys())
                                            #print('Lista',valor_tirar,'Carta a tirar', valor_tirar[tirar_random])
                                            auxx_index=-1
                                            for i in aux2:
                                                auxx_index+=1
                                                if i==valor_tirar[tirar_random]:
                                                    #print(auxx_index)
                                                    break
                                            #print(auxx_index)
                                            mesa.append(aux2[auxx_index])
                                            auxcp2=aux2[auxx_index]
                                            #print(mesa)
                                            #print(auxcp2)
                                            aux_indexv=auxx_index
                                            #print('2-2',mesa)
                                    else:
                                        #print('ENTRA 2')
                                        # Si son las mismas pero son numeros escoge un random
                                        tirar_random=random.randint(0,len(aux_dic2)-1)
                                        valor_tirar=list(aux_dic2.keys())
                                        #print('Lista',valor_tirar,'Carta a tirar', valor_tirar[tirar_random])
                                        auxx_index=-1
                                        for i in aux2:
                                            auxx_index+=1
                                            if i==valor_tirar[tirar_random]:
                                                #print(auxx_index)
                                                break
                                        #print(auxx_index)
                                        mesa.append(aux2[auxx_index])
                                        auxcp2=aux1[auxx_index]
                                        #print(mesa)
                                        #print(auxcp2)
                                        aux_indexv=auxx_index
                                        #print('1',mesa)
                                    
                                else:
                                    None
                                    #Deja que tire randomicamente
                                #print('Mano player 2',aux2)
                                #print('----------------------------------------------------')
                            
                            # ------------------------------------------------------------------
                            if comparalen==len(mesa):
                                # Si no hay frecuencias ni nada tiro random (Tirar randomicamente)
                                #print("TIRO CUALQUIERA")
                                #print('----------------------------------------------------')
                                # Mira si las frecuencias de las cartas en mi
                                # mano son las mismas
                                aux_dic_cont=Counter(aux2)
                                #print(aux_dic_cont)
                                veri=list(aux_dic_cont.values())
                                veri_count=Counter(veri)
                                #print(veri_count)
                                condi=0
                                # Si es 1 que escoga randomicamente
                                if len(veri_count)==1:
                                    condi=1
                                #print(condi)
                                aux_mayo=0
                                aux_comp=0
                                for i in aux_dic_cont:
                                    if condi!=1:
                                        if aux_mayo<aux_dic_cont[i]:
                                            aux_mayo=aux_dic_cont[i]
                                            aux_comp=i
                                            #print(i)
                                #print('aaa',aux_comp)
                                # Si las frecuencias son diferentes
                                if aux_comp!=0:
                                    for iii in range(len(aux2)):
                                        if aux_comp==aux2[iii]:
                                            mesa.append(aux2[iii])
                                            auxcp2=aux2[iii]
                                            aux_indexv=iii
                                            #print('Deb imprimir solo una vez mesa',mesa)
                                            break
                                # Si son las mismas escoge un random
                                else:
                                    tirar_random=random.randint(0,len(aux2)-1)
                                    mesa.append(aux2[tirar_random])
                                    auxcp2=aux2[tirar_random]
                                    #aux2.pop(tirar_random)
                                    aux_indexv=tirar_random
                                #print('Mano player 2',aux2)
                                #print('----------------------------------------------------')
                        index2=aux_indexv
                        # Agregar al diccionario contar
                        if aux2[index2] in cuenta:
                            cuenta[mesa[len(mesa)-1]]+=1
                        else:
                            cuenta[mesa[len(mesa)-1]]=1
                        # Aux para comparar caida y limpia
                        auxcp2=aux2[index2]
                        aux2.pop(index2)
                        #print('Mano player 2',aux2)
                        #print('Cuentap2',cuenta)
                        # A sumado igual
                        #print('Cuenta',cuenta)
                        mesa,cartonp2,scorep2=buscamain(mesa,cartonp2,scorep2,auxcp1,auxcp2)
                        #print("Carton player 1: ",cartonp1,"Carton player 2: ",cartonp2)
                        #print("Score:   ",scorep1,"Score:   ",scorep2)
                        #print("\n")
                        # =====================================================================
                        comparalen=len(mesa)
                        #print("Player 1")
                        #print("MESA:", mesa)
                        #print("Que juegas?")
                        #print(aux1)
                        # AAA
                        # -----------------------------------------------------------------------------------------------
                        aux_indexv=-1
                        # ------------------------------------------------------------------
                        # Agente experto
                        # ------------------------------------------------------------------
                        #print('----------------------------------------------------')
                        # Verifica si puedo caerle, pero ene este caso la ultima carta de la mesa no necesariamente
                        # es la carta tirada en el turno anterior. Entonces la prioridad no seria de "si se puede caer"
                        # seria la suma de cartas, si siguiente, al menos me llevo una
                        #print('SI SE PUEDE CAER')
                        #print('----------------------------------------------------')
                        if len(mesa)>0:
                            for i in aux1:
                                aux_indexv+=1
                                #print('CAERLE',i,mesa[len(mesa)-1])
                                if i==mesa[len(mesa)-1] and auxcp2==i:
                                    #print('ENTRA')
                                    mesa.append(i)
                                    auxcp1=i
                                    #aux2.pop(aux_indexv)
                                    break
                                else:
                                    None
                            #print('Mano player 2',aux2)
                            #print('----------------------------------------------------')
                        # ------------------------------------------------------------------*
                        if comparalen==len(mesa):
                            aux_indexv=0
                            # Verifica si alguna suma
                            #print('SI ALGUNA SUMA')
                            #print('----------------------------------------------------')
                            for i in aux1:
                                svalor=sumarcartas(mesa,i,aux_sumar,aux_suman)
                                #print("Si alguna suma, cuantos suma",svalor)
                                # if svalor> algo: tire esa carta y llevese las cartas
                                # elimine la carta tirada de aux2.pop(aux_indexv)
                            #print('Mano player 2',aux2)
                            #print('----------------------------------------------------')
                        # ------------------------------------------------------------------
                        if comparalen==len(mesa):
                            aux_indexv=-1
                            # Verificar si me puedo llevar Una-Siguiente
                            #print('SI ALMENOS ME LLEVO UNA')
                            #print('----------------------------------------------------')
                            # Ordenar las cartas de la mano
                            # Cartas a Numeros
                            for i in range(len(aux1)):
                                if aux1[i]=='A':
                                    aux1[i]=1
                                elif aux1[i]=='J':
                                    aux1[i]=8
                                elif aux1[i]=='Q':
                                    aux1[i]=9
                                elif aux1[i]=='K':
                                    aux1[i]=10
                                else:
                                    aux1[i]=int(aux1[i])
                            #print('Sin ordenar',aux2)
                            aux1.sort()
                            #print('Ordenado',aux2)
                            # Numeros a cartas
                            for i in range(len(aux1)):
                                if aux1[i]==1:
                                    aux1[i]='A'
                                elif aux1[i]==8:
                                    aux1[i]='J'
                                elif aux1[i]==9:
                                    aux1[i]='Q'
                                elif aux1[i]==10:
                                    aux1[i]='K'
                                else:
                                    aux1[i]=str(aux1[i])
                            #print('Vuelta',aux2)
                            
                            for i in aux1:
                                aux_indexv+=1
                                if i in mesa:
                                    mesa.append(i)
                                    auxcp1=i
                                    #aux2.pop(aux_indexv)
                                    break
                            # Programar llevarme la que tenga mas o menos frecuencias
                            #print('Mano player 2',aux2)
                            #print('index ',aux_indexv)
                            #print('----------------------------------------------------')
                        # ------------------------------------------------------------------*
                        if comparalen==len(mesa):
                            aux_indexv=-1
                            # Si no hay carta similar, tirar la carta con mas frecuencias
                            #print('TIRAR BASADO EN FRECUENCIAS')
                            #print('----------------------------------------------------')
                            aux_dic={}
                            aux_mayor=0
                            aux_mayor_n=0
                            for i in aux1:
                                if i in cuenta:
                                    # Obtener carta con mas frecuencia
                                    if cuenta[i]>aux_mayor_n:
                                        aux_mayor_n=cuenta[i]
                                        aux_mayor=i
                                    # Meter valores a aux_dic
                                    aux_dic[i]=cuenta[i]
                            #print(aux_dic)
                            #obtener la carta con mas frecuencia
                            #print(aux_mayor)
                            #print(aux_mayor_n)
                            # Buscar cartas que tienen la misma frecuencia
                            aux_dic2={}
                            for i in aux_dic:
                                if aux_dic[i]==aux_mayor_n:
                                    aux_dic2[i]=aux_mayor_n
                            #print('Lista frecuencias mayores encontradas que esten en mi mano',aux_dic2)
                            # Elegir randomicamente que carta votar
                            if len(aux_dic2)>0:
                                # Mira si las frecuencias de las cartas en mi
                                # mano son las mismas
                                aux_dic_cont=Counter(aux1)
                                #print(aux_dic_cont)
                                veri=list(aux_dic_cont.values())
                                veri_count=Counter(veri)
                                #print(veri_count)
                                condi=0
                                # Si es 1 que escoga randomicamente
                                if len(veri_count)==1:
                                    condi=1
                                #print(condi)
                                aux_mayo=0
                                aux_comp=0
                                for i in aux_dic_cont:
                                    if condi!=1:
                                        if aux_mayo<aux_dic_cont[i]:
                                            aux_mayo=aux_dic_cont[i]
                                            aux_comp=i
                                            #print(i)
                                #print('aaa',aux_comp)
                                #print(aux_dic2)
                                # YAYA
                                # YAYA
                                if aux_comp!=0:
                                    #print('ENTRA')
                                    # Si son las mismas y es K, Q o J tirar la que no suma
                                    if 'K' in aux_dic2:
                                        for it in range(len(aux1)):
                                            if aux1[it]=='K':
                                                mesa.append(aux1[it])
                                                auxcp1=aux1[it]
                                                aux_indexv=it
                                                #print('2-1 K',mesa, it)
                                                break
                                    elif 'Q' in aux_dic2:
                                        for it in range(len(aux1)):
                                            if aux1[it]=='Q':
                                                mesa.append(aux1[it])
                                                auxcp1=aux1[it]
                                                aux_indexv=it
                                                #print('2-1 Q',mesa, it)
                                                break
                                    elif 'J' in aux_dic2:
                                        for it in range(len(aux1)):
                                            if aux1[it]=='J':
                                                mesa.append(aux1[it])
                                                auxcp1=aux1[it]
                                                aux_indexv=it
                                                #print('2-1 J',mesa, it)
                                                break
                                        
                                    else:
                                        # Si son las mismas escoge un random
                                        tirar_random=random.randint(0,len(aux_dic2)-1)
                                        valor_tirar=list(aux_dic2.keys())
                                        #print('Lista',valor_tirar,'Carta a tirar', valor_tirar[tirar_random])
                                        auxx_index=-1
                                        for i in aux1:
                                            auxx_index+=1
                                            if i==valor_tirar[tirar_random]:
                                                #print(auxx_index)
                                                break
                                        #print(auxx_index)
                                        mesa.append(aux1[auxx_index])
                                        auxcp1=aux1[auxx_index]
                                        #print(mesa)
                                        #print(auxcp2)
                                        aux_indexv=auxx_index
                                        #print('2-2',mesa)
                                else:
                                    #print('Entra 2')
                                    # Si son las mismas escoge un random
                                    tirar_random=random.randint(0,len(aux_dic2)-1)
                                    valor_tirar=list(aux_dic2.keys())
                                    #print('Lista',valor_tirar,'Carta a tirar', valor_tirar[tirar_random])
                                    auxx_index=-1
                                    for i in aux1:
                                        auxx_index+=1
                                        if i==valor_tirar[tirar_random]:
                                            #print(auxx_index)
                                            break
                                    #print(auxx_index)
                                    mesa.append(aux1[auxx_index])
                                    auxcp1=aux1[auxx_index]
                                    #print(mesa)
                                    #print(auxcp2)
                                    aux_indexv=auxx_index
                                    #print('1',mesa)
                            else:
                                None
                                #Deja que tire randomicamente
                            #print('Mano player 2',aux2)
                            #print('----------------------------------------------------')
                        # ------------------------------------------------------------------
                        if comparalen==len(mesa):
                            # Si no hay frecuencias ni nada tiro random (Tirar randomicamente)
                            #print("TIRO CUALQUIERA")
                            #print('----------------------------------------------------')
                            # Mira si las frecuencias de las cartas en mi
                            # mano son las mismas
                            aux_dic_cont=Counter(aux1)
                            #print(aux_dic_cont)
                            veri=list(aux_dic_cont.values())
                            veri_count=Counter(veri)
                            #print(veri_count)
                            condi=0
                            # Si es 1 que escoga randomicamente
                            if len(veri_count)==1:
                                condi=1
                            #print(condi)
                            aux_mayo=0
                            aux_comp=0
                            for i in aux_dic_cont:
                                if condi!=1:
                                    if aux_mayo<aux_dic_cont[i]:
                                        aux_mayo=aux_dic_cont[i]
                                        aux_comp=i
                                        #print(i)
                            #print('aaa',aux_comp)
                            # Si las frecuencias son diferentes
                            if aux_comp!=0:
                                for iii in range(len(aux1)):
                                    if aux_comp==aux1[iii]:
                                        mesa.append(aux1[iii])
                                        auxcp1=aux1[iii]
                                        aux_indexv=iii
                                        #print('Deb imprimir solo una vez mesa',mesa)
                                        break
                            # Si son las mismas escoge un random
                            else:
                                tirar_random=random.randint(0,len(aux1)-1)
                                mesa.append(aux1[tirar_random])
                                auxcp1=aux1[tirar_random]
                                #aux2.pop(tirar_random)
                                aux_indexv=tirar_random
                            #print('----------------------------------------------------')
                        index1=aux_indexv
                        # AAA
                        # Agregar al diccionario contar
                        if aux1[index1] in cuenta:
                            cuenta[mesa[len(mesa)-1]]+=1
                        else:
                            cuenta[mesa[len(mesa)-1]]=1
                        #print('Cuentap1',cuenta)
                        # Aux para comparar caida y limpia
                        auxcp1=aux1[index1]
                        aux1.pop(index1)
                        #print('Cuenta',cuenta)
                        mesa,cartonp1,scorep1=buscamain(mesa,cartonp1,scorep1,auxcp1,auxcp2)
                        #print("Carton player 1: ",cartonp1,"Carton player 2: ",cartonp2)
                        #print("Score:   ",scorep1,"Score:   ",scorep2)
                        #print("\n")
            aux_turno+=1
            #print("---------- SCORE Antes ----------")
            #print("Score player 1   ",scorep1,"Score player 2   ",scorep2)
            #print("\n\n\n")
            if scorep1<30:
                if cartonp1>19:
                    mod=cartonp1%19
                    if mod%2==0:
                        scorep1+=mod+6
                    else:
                        scorep1+=mod+5
            if scorep2<30:
                if cartonp2>19:
                    mod=cartonp2%19
                    if mod%2==0:
                        scorep2+=mod+6
                    else:
                        scorep2+=mod+5
            #print("---------- SCORE Ahora ----------")
            #print("Score player 1:   ",scorep1,"Score player 2:   ",scorep2)
            #print("\n\n\n")
        if scorep1>=40:
            #print("Gano Player 1")
            winplayer1+=1
        else:
            #print("Gano Player 2")
            winplayer2+=1
        auxt=winplayer1+winplayer2
        if auxt==100:
            winplayer1list.append(winplayer1)
            winplayer2list.append(winplayer2)
        elif auxt==200:
            winplayer1list.append(winplayer1)
            winplayer2list.append(winplayer2)
        elif auxt==300:
            winplayer1list.append(winplayer1)
            winplayer2list.append(winplayer2)
        elif auxt==400:
            winplayer1list.append(winplayer1)
            winplayer2list.append(winplayer2)
        elif auxt==500:
            winplayer1list.append(winplayer1)
            winplayer2list.append(winplayer2)
        elif auxt==600:
            winplayer1list.append(winplayer1)
            winplayer2list.append(winplayer2)
        elif auxt==700:
            winplayer1list.append(winplayer1)
            winplayer2list.append(winplayer2)
        elif auxt==800:
            winplayer1list.append(winplayer1)
            winplayer2list.append(winplayer2)
        elif auxt==900:
            winplayer1list.append(winplayer1)
            winplayer2list.append(winplayer2)
        elif auxt==1000:
            winplayer1list.append(winplayer1)
            winplayer2list.append(winplayer2)
    print('Resultado ',xy+1)
    for i in range(10):
        print('Agent 1:',winplayer1list[i],'Agent 2: ',winplayer2list[i])
    print('\n\n')
input()
