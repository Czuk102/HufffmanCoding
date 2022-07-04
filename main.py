

from collections import OrderedDict

class Node:
    def __init__(self, frequency, symbol, left_kid=None, right_kid=None):

        self.frequency = frequency

        self.symbol = symbol

        self.left_kid = left_kid

        self.right_kid = right_kid

        #  (0/1)
        self.code = ''


codes = {}

def Calculate_Codes(node, val=''):
    # huffman code for current node
    newVal = val + str(node.code)

    if (node.left_kid):
        Calculate_Codes(node.left_kid, newVal)
    if (node.right_kid):
        Calculate_Codes(node.right_kid, newVal)

    if (not node.left_kid and not node.right_kid):
        codes[node.symbol] = newVal

    return codes


def count_ocurrences(data):
    symbols = OrderedDict()
    for element in data:
        if element in symbols:
            symbols[element] += 1
        else:
            symbols[element] = 1
    return symbols


def min_heapify(A, k):
    l = left(k)
    r = right(k)
    if l < len(A) and A[l].frequency < A[k].frequency:
        smallest = l
    else:
        smallest = k
    if r < len(A) and A[r].frequency < A[smallest].frequency:
        smallest = r
    if smallest != k:
        A[k], A[smallest] = A[smallest], A[k]
        min_heapify(A, smallest)


def build_min_heap(A):
    n = int((len(A)//2)-1)
    for k in range(n, -1, -1):
        min_heapify(A, k)


def Output_Encoded(data, coding):
    encoding_output = []
    for c in data:
        encoding_output.append(coding[c])

    string = ''.join([str(item) for item in encoding_output])
    return string





def left(k):
    return 2 * k + 1


def right(k):
    return 2 * k + 2


def Huffman_Encoding(data):
    occurrences = count_ocurrences(data)
    nodes = []

    # tworzy drzewo huffmana
    for symbol in occurrences:
        nodes.append(Node(occurrences.get(symbol), symbol))

    while len(nodes) > 1:

        build_min_heap(nodes)

        left = nodes[0]
        nodes.pop(0)

        right = nodes[0]
        nodes.pop(0)

        left.code = 0
        right.code = 1

        # tworzy nowy wezel z dwóch najmniejszych
        newNode = Node(left.frequency + right.frequency, left.symbol + right.symbol, left, right)
        nodes.append(newNode)

    huffman_encoding = Calculate_Codes(nodes[0])
    return huffman_encoding


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

# odczyt inputu
input_file = open("input.txt", "r", encoding="utf8")
text = input_file.read()
input_file.close()

data = text
print(count_ocurrences(text))

#tworzenie kodowania
dictionary = Huffman_Encoding(data)
output_file = open("output.txt", "w", encoding="utf8")
output_file.write(str(dictionary))
output_file.write("\n")
output_file.close()

output_file = open("output.txt", "a", encoding="utf8")
coded_string = Output_Encoded(data, dictionary)
binary_str = coded_string

# dopełnienie zerami do 8bitow
reminder = len(binary_str ) % 8
newstr = binary_str.ljust(len(binary_str) + 8 - reminder, "0")
final_output = setStringtoASCII(newstr)
output_file.write(final_output)

output_file.close()



