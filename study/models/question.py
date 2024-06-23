from sqlalchemy import Column, Integer, String, DateTime
from study.database import Base
from datetime import datetime

class Question(Base):
    __tablename__ = 'question'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    mail = Column(String(255))
    content = Column(String(1024))
    create_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    def __init__(self, name=None, mail=None, content=None):
        self.name = name
        self.mail = mail
        self.content = content

    def __repr__(self):
        return f'<User {self.name!r}>'
