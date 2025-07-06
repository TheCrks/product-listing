#3rd party
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from api.FetcherApi import api_fetcher_router
from core import Config
# api routers

# api configs & initialiser
from initialiser import configureCors

# uvicorn
import uvicorn

# create uvicorn app
app = FastAPI(title=Config.settings.PROJECT_NAME)

# configure cors
app = configureCors(app)

# define routes
app.include_router(api_fetcher_router,prefix=Config.settings.API_V1_STR)

# Serve frontend from /frontend/dist
app.mount("/", StaticFiles(directory="frontend/dist", html=True), name="static")

if __name__ == "__main__":
      uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

#localhost:8000/docs for swagger