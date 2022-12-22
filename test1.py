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

#seqs = dict(sorted(seqs.items(), key=lambda item: item[1], reverse=True)) Ennek majd kevert hosszúságú karakterláncoknál lesz értelme


print(f"Original character count: {len(file)}")
tmp = file
idx = 0
for key, value in seqs.items():
    tmp = tmp.replace(key, str(idx))
    idx += 1
print(f"After replacements: {len(tmp)}")
print(f"Character seqence 1x has to be saved, takes: {len(seqs)*seq_len}")
print(f"Character count after: {(len(seqs)*seq_len)+len(tmp)}")


# TODO:
# Leplacelem a karakterláncokat a számmal a szövegben - gond hogy kell a szám elé és mögé karakter hogy tudjam az egy index szám.
# Emellé kell egy lista ami a szavak előfordulási indexeit tárolja

# TODO:
# Egyéb ötlet hogy mihez kezdjek ezzel a továbbiakban


# TODO IMPROVEMENT
# Az index karakteres hosszának megjelelő leggyakoribb karakterláncokat mentsek
# PL amígy az index < 1000 addig nézhetek max 3 hosszú karakterláncot. Egyenes arányossagban növekedjek a lánc hossz az index hosszával