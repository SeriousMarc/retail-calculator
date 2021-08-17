"""
Run Application Logic
"""
from contextlib import suppress

import uvicorn

from fastapi import FastAPI
from sqlalchemy.exc import SQLAlchemyError

from retail_calculator.api.routes import router
from retail_calculator.db.utils import db_heartbeat, init_models, prepare_db


app = FastAPI()
app.include_router(router)


@app.on_event('startup')
async def startup_event():
    await init_models()
    await db_heartbeat()

    # quick solution to fill up db with tax and discount data
    with suppress(SQLAlchemyError):
        await prepare_db()


if __name__ == '__main__':
    uvicorn.run('retail_calculator.app:app', port=8000, host='0.0.0.0', access_log=True)
