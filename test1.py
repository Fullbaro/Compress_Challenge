file = open("original_file.txt", "r").read()
temp_file = file
unique_char = "😀"
# Megkeresni az optimális leggyakoribb, leghosszabb karakterláncokat,
# amiket egyedien elmentek, és indexeket, hogy hol fordulnak elő.
# Ha a karakterlánc hosszabb  mint az indexe, akkor máris spóroltam

seq_len = 0 # Karakterlánc hossz számláló
while True: # Addig keresem az ideális karakterlánc hosszt, amíg meg nem találom
    seqs = {} # kulcs a karakterlánc, érték az előfordulások száma a szövegben
    ii = 0
    while ii <= len(file)-seq_len: # Minden karakteren végigmegyek
        sequence = "" # Ez lesz az aktuális karakterlánc
        for j in range(seq_len): # Aktulális karakter és az éppen soron lévő karakterlánc hossz mennyiésű karaktert fűzök hozzá           
            sequence += file[ii+j]
        if sequence not in seqs: # Ha még nem láttam ilyet, letárolom            
            ii += seq_len # HA EGY LÁNCOT LEMENTETTEM, A KÖVI KERESÉSE A MENTETT UTÁN KEZDŐDJÖN, NE PETID A MENTETT LÁNC 2. KARAKTERÉNÉL
            count = temp_file.count(sequence) # Hányszor fordul elő a szövegben            
            if count > 1: # Ha minimum 2x, akkor megéri lecserélni majd indexre
                seqs[sequence] = count # Az egyedi karakterláncokat tartlmazza, előfordulási mennyiséggel értéknek                                
                temp_file = temp_file.replace(sequence, unique_char) # Ha ezt a láncot mentettem, többet ne forduljon elő
        

        print(f"Sequnce length: {seq_len}, Process: {round(ii/(len(file)-seq_len)*100)}%")#, Appearence count: {sum(seqs.values())*seq_len}")
        
        # A karakterláncok leendő indexe több karakter-e mint maga a lánc. -> több karakter-e leírni számmal mint eredetileg volt
        if len(str(len(seqs))) >= seq_len:        
            break

        ii += 1
    
    if len(str(len(seqs))) >= seq_len:
        seq_len += 1    # Próbálkozzunk hosszabb karakterláncokkal
        temp_file = file # Visszaállítom a temp fiájlt az új láncok kereséséhez
    else:
        print("Best sequnce length found:", seq_len)
        break






seqs = dict(sorted(seqs.items(), key=lambda item: item[1], reverse=False)) #Ennek majd kevert hosszúságú karakterláncoknál lesz értelme

print("Original: ", len(file))

idx = 0
key_dict = ""
for key, value in seqs.items():
    while True:
        character = chr(idx)
        if character not in file:
            file = file.replace(key, character)            
            key_dict += key+unique_char+character
            break

        idx += 1

print("After", len(file))
print("Kulcsok mentése foglal:", len(key_dict))

f = open("compressed.txt", "w")
f.write(key_dict+file)
f.close()


# Test result
old = open('original_file.txt', 'r')
old.seek(0, 2)
old_size = old.tell()
new = open('compressed.txt', 'r')
new.seek(0, 2)
new_size = new.tell()
print(f"A tömörítés mértéke {round(((old_size - new_size) / old_size) * 100, 2)} %")