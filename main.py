from _calendar import GoogleCalendarTools
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def main(private_key, public_key):
    calendar = GoogleCalendarTools(private_key=private_key, public_key=public_key)
    events = calendar.get_events(period=60)
    return events

@app.get("/test")
def test():
    return {"Hello": "World"}
