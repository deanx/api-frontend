from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database import Base

class Perguntas1(Base):
    __tablename__ = "perguntas1"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    idade = Column(Integer)
    genero = Column(String)
    escolaridade = Column(String)
    renda_familiar = Column(String)
    naturalidade = Column(String)

class Perguntas2(Base):
    __tablename__ = "perguntas2"
    
    id = Column(Integer, primary_key=True, index=True)
    frequencia = Column(String)
    quais_redes = Column(String)
    redes_mais = Column(String)
    tipo_conteudo_consome = Column(String)
    tipo_conteudo_compartilha = Column(String)
    marcas = Column(String)
    como_decide = Column(String)
    tipo_evita = Column(String)
    mais_gosta = Column(String)
    email = Column(String)
    
class PerguntasFinais(Base):
    __tablename__ = "perguntasfinais"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    perg1 = Column(String)
    perg2 = Column(String)
    perg3 = Column(String)
    perg4 = Column(String)
    perg5 = Column(String)
    perg6 = Column(String)
    perg7 = Column(String)
    perg8 = Column(String)
    perg9 = Column(String)
    perg10 = Column(String)