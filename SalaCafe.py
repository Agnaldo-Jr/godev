from Sala import Sala

class SalaCafe(Sala):
    
    def __init__(self, nome, lotacao_limite):
        super().__init__(nome, lotacao_limite)