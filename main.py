from _calendar import GoogleCalendarTools
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def main(private_key, public_key, period):
    try:
        calendar = GoogleCalendarTools(private_key=private_key, public_key=public_key)
        events = calendar.get_events(period=int(period))
        return events
    except Exception as e:
        return {"error": str(e)}

@app.get("/test")
def test():
    return {"Hello": "World"}
