from _calendar import GoogleCalendarTools

def main():
    calendar = GoogleCalendarTools()
    events = calendar.get_events(period=60)
    return events

if __name__ == '__main__':
    main()
