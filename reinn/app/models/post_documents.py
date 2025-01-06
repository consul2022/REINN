from sqlalchemy import Column, Integer, String, ForeignKey, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from ..database import Base



class PostDocument(Base):
    __tablename__ = "post_document"  # название таблицы в БД
    id = Column(Integer, primary_key=True, index=True)
    documents = Column(String, nullable=True, unique=False)
    post_id = Column(Integer, ForeignKey("post_user.id"), nullable=False, unique=False)

    post_user = relationship("PostUser", back_populates="post_documents")


