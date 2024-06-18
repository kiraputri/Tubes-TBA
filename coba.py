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
    subjek_set = {'aku', 'ayah', 'ibu', 'kamu', 'kakak'}
    return word in subjek_set

def isPredikat(word: str) -> bool:
    # Predikat = {'membaca', 'membeli', 'menaruh', 'mengambil', 'melihat'}
    predikat_set = {'membaca', 'membeli', 'menaruh', 'mengambil', 'melihat'}
    return word in predikat_set

def isObjek(word: str) -> bool:
    # Objek = {'buku', 'kamus', 'koran', 'komik', 'majalah'}
    objek_set = {'buku', 'kamus', 'koran', 'komik', 'majalah'}
    return word in objek_set

def isKeterangan(word: str) -> bool:
    # Ket = {'sekarang', 'besok', 'ditoko', 'dimeja', 'kemarin'}
    keterangan_set = {'sekarang', 'besok', 'ditoko', 'dimeja', 'kemarin'}
    return word in keterangan_set

def parser(sentence):
    ERR = Exception('ParsingError')

    words = sentence.lower().split()
    words.append('')

    res = []
    stack = []
    state = 0
    print("Stack:")
    print(stack)

    stack.append('#')
    state = 1
    print(stack)

    stack.append('X')
    state = 2

    i = 0

    try:
        while stack[-1] != '#':
            print(stack)
            word = words[i]
            if word != '':
                token = tokenRecognizer(word)

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
    print(f"String: {sentence}\nStatus: Diterima\n") if parser(sentence) else print(f"String: {sentence}\nStatus: Ditolak \n")
