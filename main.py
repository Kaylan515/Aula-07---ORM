#Import a função a função responsavel por criar a conexão com o banco de dados
from sqlalchemy import create_engine

#importar tipos de dados e estruturas das colunas
from sqlalchemy import Column, Integer, String, Float, Boolean

#importar a classe base para criar os modelos orm
from sqlalchemy.orm import declarative_base

# Importar a ferramenta para criar sessões de banco
from sqlalchemy.orm import sessionmaker