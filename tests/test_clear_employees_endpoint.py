from fastapi.testclient import TestClient

from employee import schemas


def test_all_employees_should_be_removed_and_204_http_status_returned_when_employees_exist(
    test_client: TestClient,
    correct_employee_payload: schemas.EmployeeCreatePayload,
) -> None:
    test_client.post(
        url="/employees",
        json=correct_employee_payload.dict(),
    )
    response = test_client.get(url="/employees")
    assert len(response.json()) == 1
    clear_response = test_client.delete(url="/employees")
    assert clear_response.status_code == 204
    response = test_client.get(url="/employees")
    assert len(response.json()) == 0
