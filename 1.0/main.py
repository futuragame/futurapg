# -*- coding: utf-8 -*-
#GPL 2.0
import hashlib
##WERSJA 1.0 [DEV]
import re
import random
import time
import sys
debugmode = True


def rot13(s):
    result = ""

    # Loop over characters.
    for v in s:
        # Convert to number with ord.
        c = ord(v)

        # Shift number back or forward.
        if c >= ord('a') and c <= ord('z'):
            if c > ord('m'):
                c -= 13
            else:
                c += 13
        elif c >= ord('A') and c <= ord('Z'):
            if c > ord('M'):
                c -= 13
            else:
                c += 13

        # Append to result.
        result += chr(c)

    # Return transformation.
    return result

def gensave():
    data = 'eq:' + str(eq)
    savehash = hashlib.md5(data)
    print data
    print savehash.hexdigest()
def readsave():
    eq = 
def levelup(): #levelupuj gracza
    global player
    global maxplayer
    player['level'] += 1
    maxplayer['life'] += player['level'] * 10+(10 * player['level']) / 3

    sepme()
    print 'Awans na ' + str(player['level']) + ' level!' #AWANS????!?!?!11111
    print 'Max. Życie: ' + str(maxplayer['life']) #maksymalne życie
    print 'Dośw. do następnego lvl: ' + str(player['level'] * 1.5) #maksymalny lvl
    sepme()
    raw_input('Kontynuuj...')
def ust_seed(): #ustaw losowy seed
    random.seed(int(round(time.time() * 1000)))
region = 'city' #region; pozycja gracza
maxplayer = {'life': 100} #maxymalne statystyki gracza
player = {'prim_attack': 10, 'life': 100, 'money': 100, 'level': 1, 'xp': 0} #stat gracza
#enemies
e_bug = {'displayname': 'Buggy', 'prim_attack': 5, 'life': 20, 'rewardmoney': 10, 'rewardxp': 4} 
e_vampir = {'displayname': 'Vampir', 'prim_attack': 6, 'life': 22, 'rewardmoney': 11, 'rewardxp': 6}
eq_prim_attack = {'displayname': 'Zwykły drewniany miecz', 'attackdamage': 10} #super atak
eq_sec_attack = {} #słaby atak
#########ITEMY
item_sword_wood_regular = {'displayname': 'Zwykły drewniany miecz', 'attackdamage': 10}
item_food_flesh_mini = {'type': 'food', 'displayname': 'Mięso /15 hp', 'healhp': 15}
#########ITEMY
eq_chest = {} #zbroja :napierśnik
eq = [{'displayname': 'batman'}, {'displayname': 'jb'}, {'displayname': 'lolcatz'}] #ekwipunek
print 'CODE RPG 1.0'
#debug msg
def dbug(text): #msg debugowania
    if debugmode == True:
        print 'DEBUG: ' + str(text)
def chk_lvl():
    if int(player['xp']) >= player['level'] * 1.5: #sprawdz level
        global player
        global maxplayer
        levelup()
        player['xp'] = 0
#show menu
def s_menu():
    chk_lvl()
    global player
    global maxplayer
    sepme()
    print 'Lvl: ' + str(player['level'])
    print 'Życie: ' + str(player['life'])
    print 'Kasa: ' + str(player['money'])
    sepme()
    print '1)Eq'
    print '2)Las'
    print '3)Sklep'
    sepme()
    #opcje w menu
    menu_opt = raw_input('>')
    if menu_opt == '1': #eq
        s_eq()
    elif menu_opt == '2': #bitwa
        s_fight()
    elif menu_opt == '3': #sklep
        s_shop()
    elif menu_opt == '2370': #kod na lvl up
        levelup()
        s_menu()
    elif menu_opt == '888':
        gensave()
    else:
        #błąd w menu
        print 'Błąd: Nieprawidłowa opcja w menu'
        print menu_opt
        s_menu()

def s_shop(): #sklep
    global item_food_flesh_mini
    global eq
    global player
    print '1) Mięso 15 hp: 10$'
    shop_opcja = raw_input('>')
    if shop_opcja == '1':
        player['money'] -= 10
        eq.append(item_food_flesh_mini.copy())
    s_menu()
#show eq
def s_eq():
    global eq
    global player
    global eq_prim_attack
    global eq_sec_attack
    global eq_chest
    
    sepme() ####
    print 'EQ:'
    print 'Kasa:' + str(player['money']) #hajs
    print 'Życie:' + str(player['life']) #life
    eq_cursor = 1
    for item in eq: #dropnij liste itemów
        print '(' + str(eq_cursor) + ')>' + str(item['displayname'])
        eq_cursor = eq_cursor + 1
    if eq_prim_attack != {}:
        print 'Pierwszy' + '>' + str(eq_prim_attack['displayname']) #eq noszone
    if eq_sec_attack != {}:
        print 'Drugi' + '>' + str(eq_sec_attack['displayname'])
    if eq_chest != {}:
        print 'Napierśnik' + '>' + str(eq_chest['displayname'])
    sepme() ####
    print '1) Przenieś item'
    print '2) Przenieś item do zbroi'
    print '3) Przenieś item do ekwipunku'
    print '4) Użyj'
    print '0) Wyjdź'
    eq_opcja = raw_input('>')
    
    if eq_opcja == '1': #przenoszenie z A do B
        print 'Podaj item "a"'
        a = raw_input('>>>')
        print 'Podaj item "b"'
        b = raw_input('>>>')
        a, b = int(a)-1, int(b)-1 #rzeźbienie o -1 i int()
        eq[a], eq[b] = eq[b], eq[a] #przestawianie
        s_eq() #powrót do eq
        
    elif eq_opcja == '2': #przenoszenie do zbroi
        print 'Podaj item "a"'
        a = raw_input('>>>')
        print 'Podaj miejsce:'
        print '1>Ręka dominująca'
        print '2>Ręka druga'
        print '3>Napierśnik'
        b = raw_input('>>>')
        a, b = int(a)-1, int(b)
        tempa = ''
        if b == 1:
            temp_eq = eq[a] #kopia
            temp_b = temp_eq.copy() #funkcja kopii słownika
            eq_prim_attack = temp_b #ustawianie zmiennej
            eq.pop(a) #usuwanie pozostałości
        if b == 2:
            temp_eq = eq[a]
            temp_b = temp_eq.copy()
            eq_sec_attack = temp_b
            eq.pop(a)
        if b == 3:
            temp_eq = eq[a]
            temp_b = temp_eq.copy()
            eq_chest = temp_b
            eq.pop(a)
            
    elif eq_opcja == '3':
        print 'Podaj miejsce "a":'
        print '1>Ręka dominująca'
        print '2>Ręka druga'
        print '3>Napierśnik'
        a = int(raw_input('>'))
        if a == 1:
            temp_eq = eq_prim_attack.copy() #kopiowanie słownika
            eq.append(temp_eq) #dodawanie słownika do eq
            eq_prim_attack = {} #reset pozostałości
            
    elif eq_opcja == '4':
        print 'Podaj id itemu'
        a = raw_input('>')
        b = eq[int(a)-1].copy() #kopiowanie
        eq.pop(int(a)-1) #usuwanie pozostałości
        if b['type'] == 'food':
            player['life'] += b['healhp'] #dodaj życie
            
            if player['life'] > maxplayer['life']: #jeśli przekroczono limit życia
                player['life'] = maxplayer['life'] #to ustaw życie na max. życie
        print 'Uleczono: ' + str(player['life'])
        
    elif eq_opcja == 0:
        print 'Wychodzenie z eq'
    s_menu()
#fight
def s_fight():
    global life
    global money
    global prim_attack
    global e_vampir
    global e_bug
    dbug('Menu walki')
    #battle data
    #sprawdz życie gracza
    if player['life'] >= 1:
        enemy_data = {} #czyszczenie temp
        randenemy = random.choice(['e_bug', 'e_vampir']) #losowanie przeciwnika
        dbug(randenemy)
        time.sleep(0.3)
        if randenemy == 'e_bug': #sprawdzanie co wylosowano
            enemy_data = e_bug.copy()
        if randenemy == 'e_vampir':
            enemy_data = e_vampir.copy()
        time.sleep(0.2)
        print 'Rozpoczynasz walkę z: ' + str(enemy_data['displayname']) #nazwa przeciwnika
        #walka
        while True:
            #atak gracza
            time.sleep(0.8)
            #===exec
            if enemy_data['life'] <= 0:
                print 'Gracz wygrał'
                p_win = True
                break
            elif player['life'] <= 0:
                print 'Gracz przegrał'
                p_win = False
                break
            #===exec
            
            print '>>>Ruch gracza; atak: ' + str(player['prim_attack'] + eq_prim_attack['attackdamage']) #info o ataku
            enemy_data['life'] = enemy_data['life'] - (player['prim_attack'] + eq_prim_attack['attackdamage']) #atak gracza w przeciwnika
            print 'Życie przeciwnika: ' + str(enemy_data['life'])
            
            #===exec
            if enemy_data['life'] <= 0:
                print 'Gracz wygrał'
                p_win = True
                break
            elif player['life'] <= 0:
                print 'Gracz przegrał'
                p_win = False
                break
            #===exec
            
            #atak przeciwnika
            print '<<<Ruch przeciwnika; atak: ' + str(enemy_data['prim_attack'])
            player['life'] = player['life'] - enemy_data['prim_attack'] #atak przeciwnika w gracza
            print 'Życie gracza:' + str(player['life'])
            
            #===exec
            if enemy_data['life'] <= 0:
                print 'Gracz wygrał'
                p_win = True
                break
            elif player['life'] <= 0:
                print 'Gracz przegrał'
                p_win = False
                break
            #===exec
            
        dbug('koniec walki')
        if p_win == True: #nagroda za walkę
            print 'Zdobywasz: ' + str(enemy_data['rewardmoney']) + ' Xp: ' + str(enemy_data['rewardxp'])
            player['money'] = player['money'] + enemy_data['rewardmoney']
            player['xp'] += (enemy_data['rewardxp'])
            
        if player['life'] <= 0: #Jestem duchem?
            print 'Jesteś duchem!'
            print 'Wrócisz do siebie za 5 sekund'
            time.sleep(5) #TAK! jesteś! lol
        raw_input('Kontynuuj...')
        s_menu() #powrót do menu
    else:
        print 'Za mało życia'
        raw_input('Kontynuuj...')
        s_menu()
#podziałka
def sepme():
    print '=' * 10
ust_seed() #ustaw seed z godziny
s_menu() #idź do menu
#kopie:
'''
if enemy_data['life'] <= 0:
    print 'Gracz wygrał'
    break
elif player['life'] <= 0:
    print 'Gracz przegrał'
'''
