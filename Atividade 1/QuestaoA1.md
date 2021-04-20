Estados válidos:

for(int x=0; x < torre.tamanho - 1; x++){
	if(torre[x] > torre[x+1]){
		estado_valido = true
	}else if(torre[x+1] == 0){
		estado_valido = true
	}else{
		estado_valido = false
		break
	}
}

return 

O fim de cada sub-lista é o topo da torre e lógicamente o inicio de cada pilha é a base da torre.
O valor 0 representa falta/vazio, ou seja, representa um espaço vazio que aceita um disco.
Um valor menor jamais pode estar a frente de um valor maior, salvo o valor 0 que indica espaço vazio.