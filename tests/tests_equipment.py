import pytest

def equipment_payload(equipment_id = "2", student_id = "3", description = "The Biggest Digger Ever", priority = "3"):
    return {"equipment_id": equipment_id, "student_id": student_id, "description": description, "priority": priority}

def test_equipment_created_retrieved_returns_201_200(client):
    response_post = client.post("/requests/equipment", json = equipment_payload)
    response_get = client.get("/request/equipment/")
    assert response_post.status_code == 201
    assert response_get.status_code == 200

@pytest.mark.parametrize("bad_student_id", 
                         ["FT-34556", "TT-T1356", "ST-444443"])
def test_bad_student_id_returns_422(client, bad_student_id):
    response = client.post("/requests/equipment", json = equipment_payload(student_id = bad_student_id))
    assert response.status_code == 422

@pytest.mark.parametrize("bad_priority",
                        ["1", "6"])
def test_priority_filtering_returns_correct_values(client, bad_priority):
    created = client.post("/request/equipment/priority}", json = equipment_payload(priority = bad_priority))
    response = client.get(f"/request/equipment/{created["priority"]}")
    assert response.status_code == 200
    assert response.json()["priority"] == []


