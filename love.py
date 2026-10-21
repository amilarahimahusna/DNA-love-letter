# go inside the folder called love
cd love 

# open notepad
notepad love.py

#drop all this code to the notepad 
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz .,!?'-"

CODE = {'00': 'A', '01': 'C', '10': 'G', '11': 'T'}
BACK = {'A': '00', 'C': '01', 'G': '10', 'T': '11'}
PAIR = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

def encode(message):
    dna = ''
    for letter in message:
        number = ALPHABET.index(letter)      # position in our list
        bits = format(number, '06b')         # 6 digits, not 8
        for i in range(0, 6, 2):             # 0, 2, 4
            dna += CODE[bits[i:i+2]]
    return 'ATG' + dna + 'TAA'

def decode(dna):
    dna = dna[3:-3]
    message = ''
    for i in range(0, len(dna), 3):          # 3 DNA letters at a time
        bits = ''
        for base in dna[i:i+3]:
            bits += BACK[base]
        message += ALPHABET[int(bits, 2)]    # number -> letter
    return message

def complement(dna):
    return ''.join(PAIR[base] for base in dna)

# Change this message to your own love letter!
message = "You are my favorite experiment"

dna = encode(message)
print("DNA:       ", dna)
print("Partner:   ", complement(dna))
print("Decoded:   ", decode(dna))

#save the file 
#run the code 
python love.py

