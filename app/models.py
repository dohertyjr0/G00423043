from sqlalchemy  import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class EquipmentDB(Base):
    __tablename__ = "equipment"
    id: Mapped[int] = mapped_column(primary_key = True, index = True)
    equipment_id: Mapped[int] = mapped_column(unique = True, index = True, nullable = False)
    student_id: Mapped[str] = mapped_column(String(6), unique = True, nullable = True)
    description: Mapped[str] = mapped_column(String(100), nullable = False)
    priority: Mapped[int] = mapped_column(Integer, nullable = False, index = True)

