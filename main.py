import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from controller import proposal_router


apps = FastAPI()

apps.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

apps.include_router(proposal_router.router)




if __name__ == "__main__":
    uvicorn.run("main:apps", host="localhost", port=1801)