#Import a função a função responsavel por criar a conexão com o banco de dados
from sqlalchemy import create_engine

#importar tipos de dados e estruturas das colunas
from sqlalchemy import Column, Integer, String, Float, Boolean

#importar a classe base para criar os modelos orm
from sqlalchemy.orm import declarative_base

# Importar a ferramenta para criar sessões de banco
from sqlalchemy.orm import sessionmaker

# Criar classe base do ORM
Base = declarative_base()

# Classe = tabela
# Objeto = linha da tabela
# Atributo = coluna da tabela

# Classe Produto representa a tabela no banco de dados
class Produto(Base):
    #nome da tabela no banco
    __tablename__ = "produtos"

    # Coluna id
    # Integer = Número inteiro
    # primary_key = True
    id = Column(Integer, primary_key=True)
    
    # Nome do produto
    # String > texto
    nome = Column(String(100))

    # Preço do produto
    # Float = número decimal
    preco = Column(Float)

    # Quantidade em estoque
    estoque = Column(Integer)

    # Produto ativo ou inativo
    ativo = Column(Boolean, default=True)

    # Método construtor
    def __init__(self, nome, preco, estoque, ativo):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.ativo = ativo
    
    #Representação do objeto para imprimir
    def __repr__(self):
        return f"Produto(id={self.id}, nome={self.nome}, preco={self.preco}, estoque={self.estoque}, ativo={self.ativo})"

# Criar a conexão com sqlite
# echo=True = log do sql
engine = create_engine("sqlite:///estoque.db", echo=True)

# Criar as tabelas no banco se não existirem
Base.metadata.create_all(engine)

# Cria uma fabrica de sessões conectada ao banco
Session = sessionmaker(bind=engine)

# Sessão ativa - pense nela como um carinho de compras
Session = Session()

# Criar
# Criar objetos produto
produto1 = Produto("Notebook", 2499.99, 100, True)
produto2 = Produto("Calça Jeans", 79.99, 50, True)
produto3 = Produto("Tênis", 149.99, 30, True)

# Adicionar os produtos na sessão (carrinho)
Session.add(produto1)
Session.add(produto2)
Session.add(produto3)

# Confirmar a inserção no banco
# Salvar no banco de dados
Session.commit()

# Listar
# Buscar todos os produtos do banco
produtos = Session.query(Produto).all()
for produto in produtos:
    print(f"id: {produto.id}, nome: {produto.nome}, preço: {produto.preco}, estoque: {produto.estoque}, ativo: {produto.ativo}")