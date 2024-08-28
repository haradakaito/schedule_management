from _calendar import GoogleCalendarTools
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def main():
    calendar = GoogleCalendarTools()
    events = calendar.get_events(period=60)
    return events

@app.get("/test")
def test():
    return {"Hello": "World"}
