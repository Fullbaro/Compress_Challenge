file = open("test.txt", "r").read()

# Megkeresni az optimális leggyakoribb, leghosszabb karakterláncokat,
# amiket egyedien elmentek, és indexeket, hogy hol fordulnak elő.
# Ha a karakterlánc hosszabb  mint az indexe, akkor máris spóroltam

seq_len = 0 # Karakterlánc hossz számláló
while True: # Addig keresem az ideális karakterlánc hosszt, amíg meg nem találom
    seqs = {} # kulcs a karakterlánc, érték az előfordulások száma a szövegben
    for i in range(len(file)-seq_len): # Minden karakteren végigmegyek
        sequence = "" # Ez lesz az aktuális karakterlánc
        for j in range(seq_len): # Aktulális karakter és az éppen soron lévő karakterlánc hossz mennyiésű karaktert fűzök hozzá
            sequence += file[i+j]
        if sequence not in seqs: # Ha még nem láttam ilyet, letárolom
            count = file.count(sequence) # Hányszor fordul elő a szövegben
            if count > 1: # Ha minimum 2x, akkor megéri lecserélni majd indexre
                seqs[sequence] = count # Az egyedi karakterláncokat tartlmazza, előfordulási mennyiséggel értéknek                                

        # TALÁN BUG: HA EGY LÁNCOT LEMENTETTEM, A KÖVI KERESÉSE A MENTETT UTÁN KEZDŐDJÖN, NE PETID A MENTETT LÁNC 2. KARAKTERÉNÉL

        print(f"Sequnce length: {seq_len}, Process: {round(i/(len(file)-seq_len)*100)}%")#, Appearence count: {sum(seqs.values())*seq_len}")
        
        # A karakterláncok leendő indexe több karakter-e mint maga a lánc. -> több karakter-e leírni számmal mint eredetileg volt
        if len(str(len(seqs))) >= seq_len:        
            break
    
    if len(str(len(seqs))) >= seq_len:
        seq_len += 1    # Próbálkozzunk hosszabb karakterláncokkal
    else:
        print("Best sequnce length found:", seq_len)
        break

idxl = 0 # Ha leírod az indexeket egyesével egymás után, hány karaktert fognak kitenni összesen
for i in range(len(seqs)):
    idxl += len(str(i))
a = sum(seqs.values()) * seq_len # A karakterláncok előfordulásai összesen * milyen hosszúak
b = len(seqs) # Hány karakterlánc van
c = a - b # Hány karaktert spórolok meg a karakterláncok indexekre való cseréjével
d = c - idxl # Az indexeket is el kell mentenem valahova
e = d - len(seqs)*seq_len # A karakterláncokat is el kell menetem 1x, hogy tudjam mi lett indexre cserélve

print(e, len(file))
print(f"Characters saved: {e} = {round((e / len(file)) * 100)}%")


# for key, value in seqs.items():
#     print(key, value)

# TODO:
# Leplacelem a karakterláncokat a számmal a szövegben - gond hogy kell a szám elé és mögé karakter hogy tudjam az egy index szám.
# Emellé kell egy lista ami a szavak előfordulási indexeit tárolja

# TODO:
# Egyéb ötlet hogy mihez kezdjek ezzel a továbbiakban


# TODO IMPROVEMENT
# Az index karakteres hosszának megjelelő leggyakoribb karakterláncokat mentsek
# PL amígy az index < 1000 addig nézhetek max 3 hosszú karakterláncot. Egyenes arányossagban növekedjek a lánc hossz az index hosszával