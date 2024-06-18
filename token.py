def tokenRecognizer(word: str):
    word = word.lower()
    try:
        if isSubjek(word): return 'S'
        elif isPredikat(word): return 'P'
        elif isObjek(word): return 'O'
        elif isKeterangan(word): return 'K'
        else: raise Exception("TokenUnrecognizedError")
    except Exception as e: 
        print(f"ERROR: {e}")
        print(f"Word \"{word}\" tidak masuk ke kategori token manapun\n")
        return '?'
        
def isSubjek(word: str) -> bool:
    # Subjek = {'aku', 'ayah', 'ibu', 'kamu', 'kakak'}
    currState = 0
    for letter in word:
        match currState:
            case -1: break
            case 0:
                if letter == 'a': currState = 1
                elif letter == 'k': currState = 2
                else: currState = -1
            case 1:
                if letter == 'k': currState = 3
                elif letter == 'y': currState = 4
                elif letter == 'i': currState = 5
                else: currState = -1
            case 2: currState = 6 if letter == 'a' else -1
            case 3: currState = 7 if letter == 'u' else -1 # final state
            case 7: currState = 7 if letter == ' ' else -1 # final state
            case 4: currState = 8 if letter == 'a' else -1
            case 8: currState = 9 if letter == 'h' else -1
            case 9: currState = 10 if letter == ' ' else -1 # final state
            case 5: currState = 10 if letter == 'b' else -1
            case 6: currState = 11 if letter == 'm' else -1
            case 11: currState = 12 if letter == 'u' else -1 # final state
            case 12: currState = 12 if letter == ' ' else -1 # final state
    return currState == 7 or currState == 10 or currState == 12

def isPredikat(word: str) -> bool:
    # Predikat = {'membaca', 'membeli', 'menaruh', 'mengambil', 'melihat'}
    currState = 0
    for letter in word:
        match currState:
            case -1: break
            case 0:
                if letter == 'm': currState = 1
                else: currState = -1
            case 1: currState = 2 if letter == 'e' else -1
            case 2:
                if letter == 'm': currState = 3
                elif letter == 'n': currState = 4
                else: currState = -1
            case 3:
                if letter == 'b': currState = 5
                elif letter == 'a': currState = 6
                else: currState = -1
            case 4: currState = 7 if letter == 'a' else -1
            case 5: currState = 8 if letter == 'a' else -1
            case 6: currState = 9 if letter == 'c' else -1
            case 7:
                if letter == 'r': currState = 10
                elif letter == 't': currState = 11
                elif letter == 'g': currState = 12
                else: currState = -1
            case 8: currState = 13 if letter == 'c' else -1
            case 9: currState = 14 if letter == 'a' else -1 # final state
            case 10: currState = 15 if letter == 'u' else -1
            case 11: currState = 16 if letter == 'a' else -1
            case 12: currState = 17 if letter == 'a' else -1
            case 13: currState = 14 if letter == 'a' else -1 # final state
            case 14: currState = 14 if letter == ' ' else -1 # final state
            case 15: currState = 18 if letter == 'h' else -1 # final state
            case 16: currState = 19 if letter == 'm' else -1
            case 17: currState = 20 if letter == 'i' else -1
            case 18: currState = 18 if letter == ' ' else -1 # final state
            case 19: currState = 21 if letter == 'b' else -1 # final state
            case 20: currState = 22 if letter == 'l' else -1
            case 21: currState = 21 if letter == ' ' else -1 # final state
            case 22: currState = 14 if letter == 'i' else -1 # final state
    return currState == 14 or currState == 18 or currState == 21 or currState == 22


def isObjek(word: str) -> bool:
    # Objek = {'buku', 'kamus', 'koran', 'komik', 'majalah'}
    currState = 0
    for letter in word:
        match currState:
            case -1: break
            case 0:
                if letter == 'b': currState = 1
                elif letter == 'k': currState = 2
                elif letter == 'm': currState = 3
                else: currState = -1
            case 1: currState = 4 if letter == 'u' else -1
            case 4: currState = 5 if letter == 'k' else -1
            case 5: currState = 6 if letter == 'u' else -1 # final state
            case 6: currState = 6 if letter == ' ' else -1 # final state
            case 2:
                if letter == 'a': currState = 7
                elif letter == 'o': currState = 8
                else: currState = -1
            case 7: currState = 9 if letter == 'm' else -1
            case 9: currState = 10 if letter == 'u' else -1
            case 10: currState = 11 if letter == 's' else -1 # final state
            case 11: currState = 11 if letter == ' ' else -1 # final state
            case 8: currState = 12 if letter == 'r' else -1
            case 12: currState = 13 if letter == 'a' else -1
            case 13: currState = 14 if letter == 'n' else -1 # final state
            case 14: currState = 14 if letter == ' ' else -1 # final state
            case 3: currState = 15 if letter == 'a' else -1
            case 15: currState = 16 if letter == 'j' else -1
            case 16: currState = 17 if letter == 'a' else -1
            case 17: currState = 18 if letter == 'l' else -1
            case 18: currState = 19 if letter == 'a' else -1
            case 19: currState = 20 if letter == 'h' else -1 # final state
            case 20: currState = 20 if letter == ' ' else -1 # final state
    return currState == 6 or currState == 11 or currState == 14 or currState == 20


def isKeterangan(word: str) -> bool:
    # Ket = {'sekarang', 'pagi ini', 'di toko', 'di meja'}
    currState = 0
    for letter in word:
        match currState:
            case -1: break
            case 0:
                if letter == 's': currState = 1
                elif letter == 'p': currState = 2
                elif letter == 'd': currState = 3
                else: currState = -1
            case 1: currState = 4 if letter == 'e' else -1
            case 4: currState = 5 if letter == 'k' else -1
            case 5: currState = 6 if letter == 'a' else -1
            case 6: currState = 7 if letter == 'r' else -1
            case 7: currState = 8 if letter == 'a' else -1
            case 8: currState = 9 if letter == 'n' else -1
            case 9: currState = 10 if letter == 'g' else -1 # final state
            case 10: currState = 10 if letter == ' ' else -1 # final state
            case 2: currState = 11 if letter == 'a' else -1
            case 11: currState = 12 if letter == 'g' else -1
            case 12: currState = 13 if letter == 'i' else -1
            case 13: currState = 14 if letter == ' ' else -1
            case 14: currState = 15 if letter == 'i' else -1
            case 15: currState = 16 if letter == 'n' else -1
            case 16: currState = 17 if letter == 'i' else -1 # final state
            case 17: currState = 17 if letter == ' ' else -1 # final state
            case 3:
                if letter == 'i': currState = 18
                else: currState = -1
            case 18:
                if letter == ' ': currState = 19
                else: currState = -1
            case 19:
                if letter == 't': currState = 20
                elif letter == 'm': currState = 21
                else: currState = -1
            case 20: currState = 22 if letter == 'o' else -1
            case 22: currState = 23 if letter == 'k' else -1
            case 23: currState = 24 if letter == 'o' else -1 # final state
            case 24: currState = 24 if letter == ' ' else -1 # final state
            case 21: currState = 25 if letter == 'e' else -1
            case 25: currState = 26 if letter == 'j' else -1
            case 26: currState = 27 if letter == 'a' else -1 # final state
            case 27: currState = 27 if letter == ' ' else -1 # final state
    return currState == 10 or currState == 17 or currState == 24 or currState == 27

def parser(sentence):
    # Definisikan jenis kesalahan yang akan digunakan untuk menandai kesalahan parsing
    ERR = Exception('ParsingError')
    
    # Memecah kalimat menjadi kata-kata individu dan menambahkan string kosong di akhir
    words = sentence.split()
    words.append('')
    
    # List untuk menyimpan hasil parsing
    res = []
    
    # Stack untuk menyimpan status parsing
    stack = []
    
    # State awal
    state = 0
    print("Stack:")
    print(stack)
    
    # Mulai dengan '#' sebagai penanda akhir stack
    stack.append('#')
    state = 1
    print(stack)
    
    # Tambahkan 'X' ke stack untuk mulai parsing dari non-terminal 'X'
    stack.append('X')
    state = 2
    
    # Indeks untuk iterasi melalui kata-kata
    i = 0
    
    try:
        # Lakukan parsing sampai stack hanya berisi '#'
        while stack[-1] != '#':
            print(stack)
            
            # Ambil kata saat ini
            word = words[i]
            
            # Dapatkan token dari kata saat ini jika kata tidak kosong
            if word != '': 
                token = tokenRecognizer(word)
            
            # Tentukan tindakan berdasarkan elemen teratas dari stack
            match stack[-1]:
                case 'X':
                    if token == 'S':
                        stack.pop()
                        stack.append('Y')
                        stack.append('P')
                        stack.append('S')
                    else: 
                        raise ERR
                case 'Y':
                    if word == '':
                        stack.pop()
                    else:
                        if token == 'O':
                            stack.pop()
                            stack.append('Z')
                            stack.append('O')
                        elif token == 'K':
                            stack.pop()
                            stack.append('Z')
                        else: 
                            raise ERR
                case 'Z':
                    if word == '':
                        stack.pop()
                    elif token == 'K':
                        stack.pop()
                        stack.append('K')
                    else: 
                        raise ERR
                case 'S':
                    if token == 'S':
                        res.append(stack.pop())
                        stack.append(word)
                    else: 
                        raise ERR
                case 'P':
                    if token == 'P':
                        res.append(stack.pop())
                        stack.append(word)
                    else: 
                        raise ERR
                case 'O':
                    if token == 'O':
                        res.append(stack.pop())
                        stack.append(word)
                    else: 
                        raise ERR
                case 'K':
                    if token == 'K':
                        res.append(stack.pop())
                        stack.append(word)
                    else: 
                        raise ERR
                case _:
                    if token != '?':
                        stack.pop()
                        i += 1
                    else: 
                        raise ERR
        
        print(stack)
        stack.pop()
        print(stack)

        print("Struktur: ", end='')
        for i in res[:-1]:
            print(f"{i} - ", end='')
        print(res[-1], "\n")

        return True 
    except Exception as e:
        print(f"ERROR: {e}")
        print(f"Kalimat \"{sentence}\" struktur tidak sesuai\n")
        return False


if __name__ == '__main__':  
    sentence = input("Kalimat: ")
    print()
    print(f"String: {sentence}\nStatus: Diterima\n") if parser(sentence) else print(f"String: {sentence}\nStatus: Ditolak \n") # type: ignore