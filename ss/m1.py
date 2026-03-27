cidade = [
    [1, 0, 2, 0, 1],  
    [0, 9, 2, 1, 3],  
    [1, 0, 1, 9, 2],  
    [9, 3, 0, 2, 1],  
    [0, 1, 2, 0, 9] 
]

casa = 0
grl = 0
hosp = 0
ad = 0
rsn = 0

for i in list (range(len(cidade))):
    for n in cidade[i]:
        if n ==1:
            casa += 1
        if n == 2:
            hosp += 1
        if n == 3: 
            grl += 1
        if n == 9:
            ad +=1
        if n == 0:
            rsn += 1
            
print(f"casas {casa} | hospital {hosp} | gerador {grl} | areas destruidas {ad} | ruas vazias {rsn}")
