gunicorn -b 0.0.0.0:7000 -w 4 -k uvicorn.workers.UvicornWorker server:app --reload
