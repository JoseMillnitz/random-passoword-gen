
import cmath
import random

#input de palavra chave
az = input("digite uma palavra chave: ")
cachurros = 76
#calculos para ter numeros superior a 0...
#para obter quantidade de numeros equivalentes a quantidade de letras
#usadas, remova o if e use apenas a opreacao de else
#se quiser usar somente o maior, use somente o de if
if len(az) < cachurros:
   ay = len(az)*100**len(az)*100**len(az)*100
#if é usado automaticamente se o numero de caracteres for superior a 
#76 caracteres, isso ocorre por conta de um bug que wess descobriu
#tem mais um bug q eu pensei depois da criatividade dele mas ainda nao
#corrigi
else:
   ay = len(az)**len(az)*10
#usa a seed para gerar numeros aleatorios baseado na propria palavra
random.seed(ay)
#aqui a magica acontece, uso um numero "aleatorio" (seedado) vezes ele
#mesmo, pois por alguma porra de motivo que desconheço, o seed gera
#abaixo de 0 sempre, então quando uso ele vezes alguma coisa superior
#a 9 (10 ou mais) ele sempre vai conseguir sair do 0
#para ter mesma quantidade de numeros em relacao a caractere da palavra
#dada voce eleva a quantidade de letras pela quantidade de letras vezes
#o numero 10
aw = int(random.random()*ay)
#print do resultado
print(f'{aw}+{aw}={az}^2')
#aqui testes em relacao ao codigo binario que meu amigo wess ofereceu
#01101010 01101111 01110011 11101001 00100000 01110000 01100101 01101100 01110101 01100100 01101111
teste = 11778525301413298992029758157648931734330868323474129207110593030530512598327437941701204738327392698620060581698027449539414884820727641762050964773226212608385022154123023258874146769171719913472
#01101010 01101111 01110011 11101001 00100000 01110000 01100101 01101100 0111
teste2 = 803313199914781355295215478882827410279434629284265577295453189663055873458841224832566330787719843444394455014328360536108825474719927580491776
#print dos dois testes com as quantidades de caracteres
if aw == teste:
   print("ta ok 1")
if aw == teste2:
  print("ta ok 2")
