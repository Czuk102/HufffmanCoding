


class Node:
    def __init__(self, czestosc, symbol, lewy_dzieciak=None, prawy_dzieciak=None):
        # probability of symbol
        self.czestosc = czestosc

        self.symbol = symbol

        self.lewy_dzieciak = lewy_dzieciak

        self.prawy_dzieciak = prawy_dzieciak

        #  (0/1)
        self.kod = ''



codes = {}


def Calculate_Codes(node, val=''):
    # huffman code for current node
    newVal = val + str(node.kod)

    if (node.lewy_dzieciak):
        Calculate_Codes(node.lewy_dzieciak, newVal)
    if (node.prawy_dzieciak):
        Calculate_Codes(node.prawy_dzieciak, newVal)

    if (not node.lewy_dzieciak and not node.prawy_dzieciak):
        codes[node.symbol] = newVal

    return codes


def stworz_slownik(data):
    symbols = dict()
    for element in data:
        if element in symbols:
            symbols[element] += 1
        else:
            symbols[element] = 1
    return symbols


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2


    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r


    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        heapify(arr, n, largest)



def Output_Encoded(data, coding):
    encoding_output = []
    for c in data:
        encoding_output.append(coding[c])

    string = ''.join([str(item) for item in encoding_output])
    return string


def Huffman_Encoding(data):
    slownik = stworz_slownik(data)
    litery = slownik.keys()

    wezly = []

    # tworzy drzewo huffmana
    for symbol in slownik:
        wezly.append(Node(slownik.get(symbol), symbol))

    i = len(wezly)+1
    while len(wezly) > 1:

        # heapify(wezly, len(wezly), i)
        wezly = sorted(wezly, key=lambda x: x.czestosc)
        # for node in nodes:
        #      print(node.symbol, node.prob)

        lewy = wezly[0]
        prawy = wezly[1]

        lewy.kod = 1
        prawy.kod = 0

        # tworzy nowy wezel z dwóch najmniejszych
        nowyWezel = Node(lewy.czestosc + prawy.czestosc, lewy.symbol + prawy.symbol, lewy, prawy)

        #heappop()
        wezly.remove(lewy)
        # i = i - 1

        wezly.remove(prawy)

        #heappush()
        wezly.append(nowyWezel)

    huffman_encoding = Calculate_Codes(wezly[0])
    return huffman_encoding

    # encoded_output = Output_Encoded(data, huffman_encoding)
    # return encoded_output


def encode_input(data, coding):
    return Output_Encoded(data,coding)

def binaryToDecimal(n):
    num = n

    dec_value = 0

    base = 1

    le = len(num)
    for i in range(le - 1, -1, -1):

        # dla 1szego bitu
        if (num[i] == '1'):
            dec_value += base
        base = base * 2


    return dec_value


def setStringtoASCII(string):

    N = int(len(string))

    if (N % 8 != 0):
        return "Not Possible!"

    res = ""

    # bierze 8em znaków i zamienia na dziesietne
    for i in range(0, N, 8):
        decimal_value = binaryToDecimal(string[i: i + 8])

        # dodaje zamienione na utf-8 do stringa
        res += chr(decimal_value)

    return res


input_file = open("input.txt", "r", encoding="utf8")
text = input_file.read()
input_file.close()

data = text
slownik = Huffman_Encoding(data)
output_file = open("output.txt", "w", encoding="utf8")
output_file.write(str(slownik))
output_file.write("\n")
output_file.close()
output_file = open("output.txt", "a", encoding="utf8")
zakodowany_string = encode_input(data, slownik)
binary_str = zakodowany_string

# dopełnienie zerami do 8bitow
reszta = len(binary_str ) % 8
newstr = binary_str.ljust(len(binary_str) + 8 - reszta, "0")


a = setStringtoASCII(newstr)
output_file.write(a)

output_file.close()



