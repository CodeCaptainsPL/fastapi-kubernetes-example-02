from typing import Any

import pytest
from fastapi.testclient import TestClient
from freezegun import freeze_time

from employee import schemas


@freeze_time(time_to_freeze="2012-01-14 12:00:01")
def test_employee_should_be_created_and_201_http_status_returned_when_payload_is_correct(
    test_client: TestClient,
    correct_employee_payload: schemas.EmployeeCreatePayload,
) -> None:
    response = test_client.post(
        url="/employees",
        json=correct_employee_payload.dict(),
    )
    assert response.status_code == 201
    employee = response.json()
    assert employee["name"] == correct_employee_payload.name
    assert employee["position"] == correct_employee_payload.position
    assert employee["salary"] == correct_employee_payload.salary
    assert employee["created_at"] == "2012-01-14T12:00:01+00:00"
    test_client.delete(url="/employees")


@pytest.mark.parametrize(
    ("field_name", "field_value"),
    [
        ("position", None),
        ("name", None),
        ("salary", None),
        ("salary", 0),
        ("salary", -1),
    ],
)
def test_http_422_exception_should_be_thrown_when_invalid_payload_schema_is_provided(
    test_client: TestClient,
    correct_employee_payload: schemas.EmployeeCreatePayload,
    field_name: str,
    field_value: Any,
) -> None:
    payload_as_dict = correct_employee_payload.dict()
    payload_as_dict[field_name] = field_value
    response = test_client.post(url="/employees", json=payload_as_dict)
    assert response.status_code == 422
