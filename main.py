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

    # Método construtor
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    #Representação do objeto para imprimir
    def __repr__(self):
        return f"Produto(id={self.id}, nome='{self.nome}', preco={self.preco})"
    
# Criar a conexão com sqlite
# echo=True = log do sql
engine = create_engine("sqlite:///estoque.db", echo=True)

# Criar as tabelas no banco se não existirem
Base.metadata.create_all(engine)

