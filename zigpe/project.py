# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy import (Column, Integer, Unicode, ForeignKey, DateTime,
                        UnicodeText)
from sqlalchemy.orm import relationship
from sqlalchemy.orm.collections import attribute_mapped_collection

from .db import Base

__all__ = 'User', 'Credential', 'PasswordCredential',

class Project(Base):

    id = Column(Integer, primary_key=True)

	title = Colum(Unicode, nullable=False, unique=True)

	content = Column(Unicode, nullable=False, unique=True)

	category = Column(Unicode, nullable=False)

	file = Column(Blob)

	__tablename__ = 'projects'
