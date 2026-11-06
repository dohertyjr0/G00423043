from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StringConstraints

EquipmentID = Annotated[int, Field(gt = 0)]
StudentID = Annotated[str, StringConstraints(pattern = r"^ST-[A-Z][A-Z]\d{4}$")]
Description = Annotated[str, StringConstraints(min_length = 5, max_length = 100)]
Priority = Annotated[int, Field(gt = 0, lt = 6)]

class EquipmentCreate(BaseModel):
    equipment_id: EquipmentID
    student_id: StudentID
    description: Description
    priority: Priority
    
class EquipmentRead(BaseModel):
    model_config = ConfigDict(from_attributes = True)
    id: int
    equipment_id: EquipmentID
    student_id: StudentID
    description: Description
    priority: Priority