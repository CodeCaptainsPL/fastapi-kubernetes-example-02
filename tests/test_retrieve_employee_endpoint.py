import uuid

from fastapi.testclient import TestClient

from employee import schemas


def test_employee_and_200_http_status_should_be_returned_when_employee_have_been_created(
    test_client: TestClient,
    correct_employee_payload: schemas.EmployeeCreatePayload,
) -> None:
    response = test_client.post(
        url="/employees",
        json=correct_employee_payload.dict(),
    )
    created_employee = response.json()
    retrieve_response = test_client.get(url=f"/employees/{created_employee['id']}")
    assert retrieve_response.status_code == 200
    assert retrieve_response.json() == created_employee


def test_http_404_exception_should_be_thrown_when_employee_does_not_exist(
    test_client: TestClient,
) -> None:
    incorrect_uuid4 = uuid.uuid4()
    response = test_client.get(url=f"/employees/{incorrect_uuid4}")
    assert response.status_code == 404
    assert response.json() == {
        "detail": f"No employee found with the provided ID: '{incorrect_uuid4}'."
    }
