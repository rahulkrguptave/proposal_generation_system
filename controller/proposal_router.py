from fastapi import APIRouter, Form, UploadFile, Body

from proposal_generation_service.services import generate_proposal_content_with_ai

router = APIRouter(prefix="/api")


@router.get("/test")
def test_repositories():
    return {"message": "Welcome to the world of Virtual Employee"}


@router.post("/generate-document")
def get_proposal_document(user_requirement: str = Form(...)):
    response = generate_proposal_content_with_ai(user_requirement)
    return response
