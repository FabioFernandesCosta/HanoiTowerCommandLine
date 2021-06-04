A torre de hanoi possui 3 torres
cada torre tem a seguinte fórmula para mover todas os seus discos para uma outra torre

2 ^ N - 1

onde N é o número de discos da torre

Para melhor exemplificar, imagine a seguinte situação

(1) ( ) ( )
(2) ( ) ( )
(3) ( ) ( )
___________
 1   2   3  

Para a torre 1 conseguir mover todos os seus discos para outra torre, com o menor numero de jogadas possíveis
ela movera ((2 ^ 3) - 1), que é o mesmo que 7
já a torre 2 e 3 tem -1 movimento para vencer, pois não existem discos ali, por isso é importante só aplicar a função nas torres que tem disco
Essa função será nossa heurística, ou seja, nos guiaremos baseados na quantidade de movimentos restantes para a melhor vitória possivel.
Já a HeuristicaAStar se baseia em duas contas, a primeira é o numero de discos que estão presentes na primeira e segunda torre, a segunda conta, é equivalente ao numero de discos presentes na terceira torre que são menores que qualquer um dos discos presentes nas outras duas torres multiplicado por 2.
