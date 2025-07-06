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
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# create uvicorn app
app = FastAPI(title=Config.settings.PROJECT_NAME)

# configure cors
app = configureCors(app)

# define routes
app.include_router(api_fetcher_router,prefix=Config.settings.API_V1_STR)

try:
      dist_path = os.path.join(BASE_DIR, "..", "frontend", "product-listing", "product-listing", "dist")
      # Serve frontend from /frontend/dist
      app.mount("/", StaticFiles(directory=dist_path, html=True), name="static")
except Exception as e:
      print("Mounting the frontend directory failed: " + str(e))

if __name__ == "__main__":
      uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

#localhost:8000/docs for swagger