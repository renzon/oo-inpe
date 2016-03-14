# Exercício 1.

O que alterei da arquitetura de sala de aula foi criar a Classe GeradorDecorator.
Se não fizesse isso, todo gerador deveria receber instância de Despachador.
Além disso, deveria sempre "lembrar" de chamar o métodod respectivo despachar com evento.
Com o uso do padrão isso ficou desnecessário e isolado no código de apenas uma classe.

# Para executar

pasta rodar python main.py do pacote ex1.


##Exemplo de execução:
    /usr/local/Cellar/python3/3.4.3/Frameworks/Python.framework/Versions/3.4/bin/python3.4 /Users/renzo/PycharmProjects/oo-inpe/ex1/main.py
    ###### Tempo: 1 #########
    --------Evento gerador msgs:
    --------- Termino de msgs
    ###### Tempo: 2 #########
    --------Evento gerador msgs:
    --------- Termino de msgs
    ###### Tempo: 3 #########
    MSG
    Contador: 0
    --------Evento gerador msgs:
    MSG
    --------- Termino de msgs
    ###### Tempo: 4 #########
    --------Evento gerador msgs:
    MSG
    --------- Termino de msgs
    ###### Tempo: 5 #########
    MSG
    Contador: 1
    MSG
    Contador: 2
    --------Evento gerador msgs:
    MSG
    MSG
    MSG
    --------- Termino de msgs
    ###### Tempo: 6 #########
    --------Evento gerador msgs:
    MSG
    MSG
    MSG
    --------- Termino de msgs
    ###### Tempo: 7 #########
    --------Evento gerador msgs:
    MSG
    MSG
    MSG
    --------- Termino de msgs
    ###### Tempo: 8 #########
    --------Evento gerador msgs:
    MSG
    MSG
    MSG
    --------- Termino de msgs
    ###### Tempo: 9 #########
    MSG. Tempo=9
    Contador: 3
    --------Evento gerador msgs:
    MSG
    MSG
    MSG
    MSG. Tempo=9
    --------- Termino de msgs
    ###### Tempo: 10 #########
    MSG
    Contador: 4
    --------Evento gerador msgs:
    MSG
    MSG
    MSG
    MSG. Tempo=9
    MSG
    --------- Termino de msgs
    ###### Tempo: 11 #########
    --------Evento gerador msgs:
    MSG
    MSG
    MSG
    MSG. Tempo=9
    MSG
    --------- Termino de msgs
    ###### Tempo: 12 #########
    --------Evento gerador msgs:
    MSG
    MSG
    MSG
    MSG. Tempo=9
    MSG
    --------- Termino de msgs
    ###### Tempo: 13 #########
    --------Evento gerador msgs:
    MSG
    MSG
    MSG
    MSG. Tempo=9
    MSG
    --------- Termino de msgs
    ###### Tempo: 14 #########
    MSG
    Contador: 5
    --------Evento gerador msgs:
    MSG
    MSG
    MSG
    MSG. Tempo=9
    MSG
    MSG
    --------- Termino de msgs
    ###### Tempo: 15 #########
    MSG
    Contador: 6
    --------Evento gerador msgs:
    MSG
    MSG
    MSG
    MSG. Tempo=9
    MSG
    MSG
    MSG
    --------- Termino de msgs
    ###### Tempo: 16 #########
    --------Evento gerador msgs:
    MSG
    MSG
    MSG
    MSG. Tempo=9
    MSG
    MSG
    MSG
    --------- Termino de msgs
    ###### Tempo: 17 #########
    --------Evento gerador msgs:
    MSG
    MSG
    MSG
    MSG. Tempo=9
    MSG
    MSG
    MSG
    --------- Termino de msgs
    ###### Tempo: 18 #########
    --------Evento gerador msgs:
    MSG
    MSG
    MSG
    MSG. Tempo=9
    MSG
    MSG
    MSG
    --------- Termino de msgs
    ###### Tempo: 19 #########
    MSG. Tempo=19
    Contador: 7
    --------Evento gerador msgs:
    MSG
    MSG
    MSG
    MSG. Tempo=9
    MSG
    MSG
    MSG
    MSG. Tempo=19
    --------- Termino de msgs
    
    Process finished with exit code 0
