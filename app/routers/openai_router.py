from fastapi import APIRouter, HTTPException, Request

from app.external_services.openai_service import get_chat_response

router = APIRouter(
    prefix='/openai'
)

@router.post("/chat")
async def health(request: Request):
    try:
        body = await request.json()
        message = body.get("message")
        response = await get_chat_response(message)
        return {"response": response}
    except Exception as e:
        print(f"Error: {e}")
        return {"error": str(e)}