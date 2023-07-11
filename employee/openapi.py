from typing import Any, TypeAlias

from fastapi import status
from pydantic import BaseModel

OpenAPIResponseType: TypeAlias = dict[int | str, dict[str, Any]]


class ErrorModel(BaseModel):
    detail: str


EMPLOYEE_NOT_FOUND: OpenAPIResponseType = {
    status.HTTP_404_NOT_FOUND: {
        "model": ErrorModel,
        "content": {
            "application/json": {
                "examples": {
                    status.HTTP_404_NOT_FOUND: {
                        "summary": "Employee not found",
                        "value": {
                            "detail": "No employee found with the provided ID:"
                            " '7c926000-613b-468e-a17d-a3fa1e3ef0e8'."
                        },
                    },
                },
            },
        },
    },
}
