class heuristica:


    @staticmethod
    def getHeurisitica(torres):
        #h (x)= (the total number of disks of left and middle poles)
        #  + 
        # 2*（number of disks that in the right pole and smaller than any disk that in left or middle poles）
        for _ in range(3):
            torres[_] = list(filter((0).__ne__, torres[_]))
        
        return (len(torres[0]) + len(torres[1])) + 2*(heuristica.getRegra3Pilha(torres))
        


    @staticmethod
    def getRegra3Pilha(torresg):
        torresg[0].extend(torresg[1])
        contador = 0

        for _ in torresg[2]:
            for _2 in torresg[0]:
                if _ < _2:
                    contador += 1
                    break
        
        return(contador)
            



#hr = heuristica.getHeurisitica([[0, 0, 0, 0], [0, 0, 0, 0], [4, 3, 2, 1]])

