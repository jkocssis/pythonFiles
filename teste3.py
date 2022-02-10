from dataclasses import dataclass

@dataclass
class Item:
    nome: str
    preco_unitario: float 
    quantidade: int = 0  

    def custo_total(self) -> float:
        return self.preco_unitario * self.quantidade 

item = Item('machado', 1000,10)
print(repr(item))

print("R$",item.custo_total())