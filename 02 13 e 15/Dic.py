pessoa =  {"Nome": 'Joaõ', "Ultimo Nome": 'Oliveira',"Idade": '20', "Curso": 'Matematica',"Endereço": 'CE'}
print (pessoa)
print (pessoa["Nome"])
print (pessoa["Ultimo Nome"])
print (pessoa["Idade"])
print (pessoa["Curso"])
print (pessoa["Endereço"])
del(pessoa["Curso"])
pessoa ["Ultimo Nome"] = 'Lopes' 
print (pessoa)
print (pessoa["Endereço"])
pessoa2 = pessoa.copy()
pessoa2["Nome"] = 'Carlos'
pessoa2["Idade"] = '30'
print (pessoa2)


