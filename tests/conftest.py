import pytest
from fastapi.testclient import TestClient

from employee import schemas
from employee.main import app


@pytest.fixture()
def test_client() -> TestClient:
    return TestClient(app=app)


@pytest.fixture()
def correct_employee_payload() -> schemas.EmployeeCreatePayload:
    return schemas.EmployeeCreatePayload(
        name="John Doe",
        position="Software Engineer",
        salary=1000.0,
    )
