class Lanchonete:
    def __init__(self):
        self.cardapio = {
            "100": 1.20,
            "101": 1.30,
            "102": 1.50,
            "103": 1.20,
            "104": 1.30,
            "105": 1.00
        }
        self.total_geral = 0

    def total_item(self, codigo, qtd):
        if codigo not in self.cardapio:
            print("Produto não cadastrado")
            return
        preco_item = self.cardapio[codigo]
        total_item = qtd * preco_item
        print(f"Total do lanche {codigo} é: R$ {total_item:.2f}")
        self.total_geral += total_item

    def finalizar(self):
        print(f"\nTotal geral do pedido: R$ {self.total_geral:.2f}")


lanchonete = Lanchonete()

while True:
    cod = input("Código do lanche desejado (ou 'fim' para encerrar): ")
    if cod.lower() == "fim":
        break
    qtd = int(input("Quantas unidades?: "))
    lanchonete.total_item(cod, qtd)

lanchonete.finalizar()
