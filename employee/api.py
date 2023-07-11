from fastapi import APIRouter, HTTPException, status
from pydantic import UUID4

from employee import schemas
from employee.openapi import EMPLOYEE_NOT_FOUND

router = APIRouter(prefix="/employees", tags=["employees"])

EMPLOYEES = {}


@router.post(path="", status_code=status.HTTP_201_CREATED)
def create_employee_endpoint(
    payload: schemas.EmployeeCreatePayload,
) -> schemas.EmployeeCreated:
    new_employee = schemas.EmployeeCreated(
        name=payload.name,
        position=payload.position,
        salary=payload.salary,
    )
    EMPLOYEES[new_employee.id] = new_employee
    return new_employee


@router.get(path="")
def list_employees_endpoint() -> list[schemas.EmployeeCreated]:
    return list(EMPLOYEES.values())


@router.delete(path="", status_code=status.HTTP_204_NO_CONTENT)
def clear_all_employees_endpoint() -> None:
    EMPLOYEES.clear()


@router.get(path="/{employee_id}", responses=EMPLOYEE_NOT_FOUND)
def retrieve_employee_endpoint(employee_id: UUID4) -> schemas.EmployeeCreated:
    try:
        return EMPLOYEES[employee_id]
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No employee found with the provided ID: '{employee_id}'.",
        )
