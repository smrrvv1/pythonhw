from fastapi import Depends, FastAPI, Body
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal, Person 

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def main():
    return FileResponse("public/index.html")

@app.get("/api/users")
def get_people(db: Session = Depends(get_db)):
    return db.query(Person).all()

@app.get("/api/users/{id}")
def get_person(id: int, db: Session = Depends(get_db)):
    person = db.query(Person).filter(Person.id == id).first()
    if person == None:  
        return JSONResponse(status_code=404, content={ "message": "Пользователь не найден"})
    return person

@app.post("/api/users")
def create_person(data = Body(), db: Session = Depends(get_db)):
    person = Person(name=data["name"], age=data["age"])
    db.add(person)
    db.commit()
    db.refresh(person)
    return person

@app.put("/api/users")
def edit_person(data = Body(), db: Session = Depends(get_db)):
    person = db.query(Person).filter(Person.id == data["id"]).first()
    if person == None: 
        return JSONResponse(status_code=404, content={ "message": "Пользователь не найден"})
    person.age = data["age"]
    person.name = data["name"]
    db.commit() 
    db.refresh(person)
    return person

@app.delete("/api/users/{id}")
def delete_person(id: int, db: Session = Depends(get_db)):
    person = db.query(Person).filter(Person.id == id).first()
    if person == None:
        return JSONResponse(status_code=404, content={ "message": "Пользователь не найден"})
    db.delete(person)  
    db.commit()    
    return person