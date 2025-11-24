#User
#id, email, username, password_hash

# Note
#id, title, content, user_id, tags

# Tag
#id, value
from sqlmodel import SQLModel, Field, Relationship, Session
from datetime import datetime
from app.database import engine

class User(SQLModel, table=True):
    __tablename__ = 'users' #type: ignore
    
    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(unique=True, max_length=255, index=True)
    username: str = Field(max_length=50)
    hash_password: str = Field(max_length=255)
    created_at: datetime = Field(default=datetime.now())
    
    notes: list['Note'] = Relationship(back_populates='user')
    
class Note(SQLModel, table=True):
    
    __tablename__ = 'notes' #type: ignore
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(max_length=50)
    content: str
    user_id: int = Field(foreign_key='users.id', index=True)
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now())

    user: User = Relationship(back_populates='notes')
    

def create_tables():
    SQLModel.metadata.create_all(engine)
    
if __name__ == '__main__':
    # create_tables()

    with Session(engine) as session:
        user = User(
            email='admin@example.com',
            username='admin user',
            hash_password='initialpassword',
            
        )
        session.add(user)
        session.commit()
        
        print(f'created user {user.id} {user.username}')
        if user.id:
            note = Note(
                title="first note",
                content="Learn Python",
                user_id=user.id
            )
            session.add(note)
            session.commit()
            print(f'session added {note.id}')
    



