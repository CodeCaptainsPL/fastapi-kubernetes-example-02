from fastapi.testclient import TestClient
from freezegun import freeze_time

from employee import schemas


def test_empty_list_and_200_http_status_should_be_returned_when_no_employees_have_been_created(
    test_client: TestClient,
) -> None:
    response = test_client.get(url="/employees")
    assert response.status_code == 200
    assert response.json() == []


@freeze_time(time_to_freeze="2012-01-14 12:00:01")
def test_employees_and_200_http_status_should_be_returned_when_employees_have_been_created(
    test_client: TestClient,
    correct_employee_payload: schemas.EmployeeCreatePayload,
) -> None:
    create_response = test_client.post(
        url="/employees", json=correct_employee_payload.dict()
    )
    assert create_response.status_code == 201
    response = test_client.get(url="/employees")
    created_employees = response.json()
    assert response.status_code == 200
    assert created_employees == [create_response.json()]
    test_client.delete(url="/employees")
