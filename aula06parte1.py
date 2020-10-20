num = 0

numext=("zero","um","dois","tres","quatro","cinco","seis","sete","oito","nove")

num = int(input("Digite o numero de um a nove(ou digite 10 para fechar o programa): "))
if num == 10:
    exit
else:
    print(numext[num])


