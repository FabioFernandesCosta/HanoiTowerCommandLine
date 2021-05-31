class heuristica:

    def __init__(self) -> None:
        pass

    def getHeur(self, torres):
        torreUm = len(torres[0])
        torreDois = len(torres[1])
        a, b = self.calc(torreUm), self.calc(torreDois)

        if (a != -1) and (b != -1):
            return a + b
        elif (a != -1):
            return a
        elif (b != -1):
            return b
        else:
            return 0        
    
    def calc(self, valor):
        return ((2 ** valor) - 1)


