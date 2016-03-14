# Exercício 1.

O que alterei da arquitetura de sala de aula foi criar a Classe GeradorDecorator.
Se não fizesse isso, todo gerador deveria receber instância de Despachador.
Além disso, deveria sempre "lembrar" de chamar o métodod respectivo despachar com evento.
Com o uso do padrão isso ficou desnecessário e isolado no código de apenas uma classe.

# Para executar

pasta rodar python main.py do pacote ex1.


##Exemplo de execução:
    Renzos-MacBook-Pro:oo-inpe renzo$ cd ex1/
    Renzos-MacBook-Pro:ex1 renzo$ python3 main.py 
    ###### Tempo: 1 #########
    --------Evento gerador msgs:
    --------- Termino de msgs
    ###### Tempo: 2 #########
    --------Evento gerador msgs:
    --------- Termino de msgs
    ###### Tempo: 3 #########
    --------Evento gerador msgs:
    --------- Termino de msgs
    ###### Tempo: 4 #########
    --------Evento gerador msgs:
    --------- Termino de msgs
    ###### Tempo: 5 #########
    MSG
    Contador: 0
    --------Evento gerador msgs:
    MSG
    --------- Termino de msgs
    ###### Tempo: 6 #########
    --------Evento gerador msgs:
    MSG
    --------- Termino de msgs
    ###### Tempo: 7 #########
    --------Evento gerador msgs:
    MSG
    --------- Termino de msgs
    ###### Tempo: 8 #########
    MSG. Tempo=8
    Contador: 1
    --------Evento gerador msgs:
    MSG
    MSG. Tempo=8
    --------- Termino de msgs
    ###### Tempo: 9 #########
    --------Evento gerador msgs:
    MSG
    MSG. Tempo=8
    --------- Termino de msgs
    ###### Tempo: 10 #########
    MSG
    Contador: 2
    --------Evento gerador msgs:
    MSG
    MSG. Tempo=8
    MSG
    --------- Termino de msgs
    ###### Tempo: 11 #########
    --------Evento gerador msgs:
    MSG
    MSG. Tempo=8
    MSG
    --------- Termino de msgs
    ###### Tempo: 12 #########
    --------Evento gerador msgs:
    MSG
    MSG. Tempo=8
    MSG
    --------- Termino de msgs
    ###### Tempo: 13 #########
    --------Evento gerador msgs:
    MSG
    MSG. Tempo=8
    MSG
    --------- Termino de msgs
    ###### Tempo: 14 #########
    --------Evento gerador msgs:
    MSG
    MSG. Tempo=8
    MSG
    --------- Termino de msgs
    ###### Tempo: 15 #########
    MSG
    Contador: 3
    --------Evento gerador msgs:
    MSG
    MSG. Tempo=8
    MSG
    MSG
    --------- Termino de msgs
    ###### Tempo: 16 #########
    --------Evento gerador msgs:
    MSG
    MSG. Tempo=8
    MSG
    MSG
    --------- Termino de msgs
    ###### Tempo: 17 #########
    MSG. Tempo=17
    Contador: 4
    --------Evento gerador msgs:
    MSG
    MSG. Tempo=8
    MSG
    MSG
    MSG. Tempo=17
    --------- Termino de msgs
    ###### Tempo: 18 #########
    --------Evento gerador msgs:
    MSG
    MSG. Tempo=8
    MSG
    MSG
    MSG. Tempo=17
    --------- Termino de msgs
    ###### Tempo: 19 #########
    --------Evento gerador msgs:
    MSG
    MSG. Tempo=8
    MSG
    MSG
    MSG. Tempo=17
    --------- Termino de msgs

