    Esse algoritmo usa como base o A* porém não com todas as funcionalidades
    pois não temos o valor de G.
    
    O valor que usamos é a soma da distância do node vizinho com o player até o final do labirinto.
    e.g:

    F = DISTANCIA_ATÉ_FINAL + NODE_DISTANCIA_ATÉ_FINAL

    O código então, escolhe o node com menor F pois a distância até o final teoricamente iria levar até o final do labirinto pela menor distância possível.
    
    Algumas regras extras foram adicionadas para melhorar como o algoritmo funciona:
            
            °- Paredes ou borda do mapa ou qualquer coisa que não seja "." setam o F = 99999999 assim o código considera esse NODE um obstáculo.

            °- O caminho passado pelo player, no caso o rastro "0", é considerado 9999999 assim evitando que o algoritmo considere um lugar que ele já passou
            
            °- Se o Player ficar preso, o código retorna o "NÃO ACHEI" como direção, o que irá reiniciar o código e colocar um X na posição que ele travou, de modo que ele vai lentamente desconsiderar locais sem saída.

               e.g:
                    Mapa:
                        ['0' 'X' 'X' '█' 'X' 'X']
                        ['0' '0' 'X' 'X' 'X' 'X']
                        ['█' '0' '█' '█' '█' 'X']
                        ['X' '0' '█' '@' '█' 'X']
                        ['█' '0' '█' '1' '█' 'X']
                        ['.' '0' '0' '0' '█' 'X']

            °- Como não podemos andar na diagonal, temos que verificar se o Node PAI é atravessavel, assim podemos ir para o Node FILHO
                
                MAPA DE NODES:
                    FILHO    PAI   FILHO
                    [NODE1][NODE2][NODE3]
                PAI [NODE4][     ][NODE5]PAI
                    [NODE6][NODE7][NODE8]
                    FILHO    PAI   FILHO
