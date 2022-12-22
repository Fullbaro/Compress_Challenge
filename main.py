

class Compressor:

    def __init__(self):
        self.path: str
        self.file: str
        self.char_seqs: dict
        self.unique_char: chr        
        self.keys = ""

    def read_file(self, path):
        self.path = path
        self.file = open(path, "r").read()

    def find_unique_char(self):
        idx = 32
        while True:
            c = chr(idx)
            if c not in self.file:
                self.unique_char = c
                break
            idx += 1        
            

    def find_char_sequences(self):
        temp_file = self.file
        seq_len = 0 
        while True: 
            self.char_seqs = {}
            idx = 0
            while idx <= len(self.file)-seq_len:
                sequence = "" 
                for j in range(seq_len):
                    sequence += self.file[idx+j+1]
                if sequence not in self.char_seqs:
                    idx += seq_len
                    count = temp_file.count(sequence)
                    if count > 1:
                        self.char_seqs[sequence] = count
                        temp_file = temp_file.replace(sequence, self.unique_char)                        
                
                print(f"Sequnce length: {seq_len}, Process: {round(idx/(len(self.file)-seq_len)*100)}%")
                                
                if len(str(len(self.char_seqs))) >= seq_len:
                    break

                idx += 1
            
            if len(str(len(self.char_seqs))) >= seq_len:
                seq_len += 1
                temp_file = self.file
            else:
                print("Best sequnce length found:", seq_len)
                break
    
    def sort_char_sequences(self):
        self.char_seqs = dict(sorted(self.char_seqs.items(), key=lambda item: item[1], reverse=True))

    def create_keys(self):
        idx = 32
        for key, _ in self.char_seqs.items():
            while True:
                character = chr(idx)
                if character not in self.file and character is not self.unique_char:
                    self.file = self.file.replace(key, character)                                                    
                    self.keys += character+key+self.unique_char
                    break        
                idx += 1        

    def save_compressed_file(self):
        file = open("compressed.dni", "w")
        file.write(self.keys+self.file)
        file.close()

    def test_compress_size(self):        
        old = open(self.path, "r")
        old.seek(0, 2)
        old_size = old.tell()
        new = open("compressed.dni", "r")
        new.seek(0, 2)
        new_size = new.tell()
        print(f"A tömörítés mértéke {round(((old_size - new_size) / old_size) * 100, 2)} %")    

    def restore_file(self):
        self.read_file("compressed.dni")
        
        idx = self.file.rindex(self.unique_char)+1
        file_o = self.file[idx:]


        keys = self.file.split(self.unique_char)
        for chr in keys[:-1]:
            u_chr = chr[0]
            seq_chr = chr[1:]
            file_o = file_o.replace(u_chr, seq_chr)

        file = open("restored.txt", "w")
        file.write(file_o)
        file.close()
        



C = Compressor()
C.read_file("original_file.txt")
C.find_unique_char()

C.find_char_sequences()
#C.sort_char_sequences() # Ez valamiért elbassza WTF
C.create_keys()
C.save_compressed_file()
C.test_compress_size()

C.restore_file()