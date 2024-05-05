from sqlalchemy.orm import Session

import models, sql_models

def save_perguntas1(db: Session, perguntas1: sql_models.Perguntas1Create):
    db_perguntas1 = models.Perguntas1(**perguntas1.dict())
    db.add(db_perguntas1)
    print(db_perguntas1)
    db.commit()
    db.refresh(db_perguntas1)
    return db_perguntas1

def save_perguntas2(db: Session, perguntas2: sql_models.Perguntas2Create):
    db_perguntas2 = models.Perguntas2(**perguntas2.dict())
    db.add(db_perguntas2)
    print(db_perguntas2)
    db.commit()
    db.refresh(db_perguntas2)
    return db_perguntas2

def save_perguntas_finais(db: Session, perguntas_finais: sql_models.PerguntasFinaisCreate):
    db_perguntas_finais = models.PerguntasFinais(**perguntas_finais.dict())
    db.add(db_perguntas_finais)

    db.commit()
    db.refresh(db_perguntas_finais)
    return db_perguntas_finais