from _calendar import GoogleCalendarTools
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def main(private_key, public_key):
    private_key = 'c04003ead0b0adae584dde596f3496ea'
    public_key = '33bb8e7fee31a8263ba0be122b8adc87'
    calendar = GoogleCalendarTools(private_key=private_key, public_key=public_key)
    events = calendar.get_events(period=60)
    return events

@app.get("/test")
def test():
    return {"Hello": "World"}
