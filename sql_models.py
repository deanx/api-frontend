from pydantic import BaseModel

class Perguntas1Create(BaseModel):
    id: int
    email: str
    idade: int
    genero: str
    escolaridade: str
    renda_familiar: str
    naturalidade: str
    class Config:
        orm_mode = True

class Perguntas2Create(BaseModel):
    id: int
    frequencia: str
    quais_redes: str
    redes_mais: str
    tipo_conteudo_consome: str
    tipo_conteudo_compartilha: str
    marcas: str
    como_decide: str
    tipo_evita: str
    mais_gosta: str
    email: str
    class Config:
        orm_mode = True


class PerguntasFinaisCreate(BaseModel):
    id: int
    email: str
    perg1: str
    perg2: str
    perg3: str
    perg4: str
    perg5: str
    perg6: str
    perg7: str
    perg8: str
    perg9: str
    perg10: str
    class Config:
        orm_mode = True

class FileUploadContent(BaseModel):
    email_addr: int
    bytes: str