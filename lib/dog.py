# from models import Dog

# def create_table(base):
#     pass

# def save(session, dog):
#     pass

# def get_all(session):
#     pass

# def find_by_name(session, name):
#     pass

# def find_by_id(session, id):
#     pass

# def find_by_name_and_breed(session, name, breed):
#     pass

# def update_breed(session, dog, breed):
#     pass

#!/usr/bin/env python3

from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    breed = Column(String)

def create_table(base, engine):
    base.metadata.create_all(engine)


def save(session, dog):
    """Saves a dog instance to the database."""
    session.add(dog)
    session.commit()

def get_all(session):
    """Retrieves all dogs from the database."""
    return session.query(Dog).all()

def find_by_name(session, name):
    """Finds a dog by name."""
    return session.query(Dog).filter(Dog.name == name).first()

def find_by_id(session, id):
    """Finds a dog by ID."""
    return session.query(Dog).get(id)

def find_by_name_and_breed(session, name, breed):
    """Finds a dog by both name and breed."""
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()

def update_breed(session, dog, breed):
    """Updates a dog's breed."""
    dog.breed = breed
    session.commit()

if __name__ == "__main__":
    engine = create_engine('sqlite:///dogs.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    create_table(engine)

    # Example usage
    new_dog = Dog(name="Buddy", breed="Golden Retriever")
    save(session, new_dog)

    all_dogs = get_all(session)
    print([f"{dog.id}: {dog.name} ({dog.breed})" for dog in all_dogs])
