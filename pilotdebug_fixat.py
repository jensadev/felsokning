print('En enklare konverterare \nProgrammet skall ersätta alla siffror skrivna med text till siffror.')
dict = {"ett":1,
        "två":2,
        "tre":3,
        "fyra":4,
        "fem":5,
        "sex":6,
        "sju":7,
        "åtta":8,
        "nio":9,
        "tio":10}
text = "" # fixa tom sträng
while ("q" not in text): # så länge inte q
    text = input("Mata in en mening med små bokstäver (Avsluta med q).")
    for ersätt in dict:
        if ersätt in text:
            text = text.replace(ersätt, str(dict[ersätt])) # kasta om till sträng
    print("Den konverterade texten blev som följer:\n")
    print(text)
