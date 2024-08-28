import json
import requests

from datetime import datetime, timedelta, timezone
from icalendar import Calendar

class GoogleCalendarTools:

    def __init__(self, private_key, public_key):
        # プライベートカレンダーを取得
        self.private_ical = 'https://calendar.google.com/calendar/ical/haradakaito.shizuoka%40gmail.com/private-' + private_key + '/basic.ics'
        self.private_ical = requests.get(self.private_ical)
        self.private_ical.raise_for_status()
        self.private_ical = Calendar.from_ical(self.private_ical.text)
        # パブリックカレンダーを取得
        self.public_ical = 'https://calendar.google.com/calendar/ical/minelab.jp_8ssb6bcklf9il488gdf8diknb0%40group.calendar.google.com/private-' + public_key + '/basic.ics'
        self.public_ical = requests.get(self.public_ical)
        self.public_ical.raise_for_status()
        self.public_ical = Calendar.from_ical(self.public_ical.text)

    def get_events(self, period:int):
        private_events = self._get_private_events()
        public_events = self._get_public_events()
        events = private_events + public_events
        events = self._ical_parse(src=events, period=period)
        return events

    # プライベートイベントを取得
    def _get_private_events(self):
        private_events = [tmp for tmp in self.private_ical.walk('VEVENT')]
        return private_events

    # パブリックイベントを取得
    def _get_public_events(self):
        public_events = [tmp for tmp in self.public_ical.walk('VEVENT')]
        public_events = [tmp for tmp in public_events if '原田' in tmp.get('SUMMARY') or 'WR' in tmp.get('SUMMARY')]
        return public_events

    def _ical_parse(self, src, period):
        today = datetime.now().replace(tzinfo=timezone.utc).date()
        end   = datetime.now().replace(tzinfo=timezone.utc).date() + timedelta(days=period)
        events = [tmp for tmp in src if today <= self._datetime_to_date(tmp.get('DTSTART').dt) <= end]
        events = sorted(events, key=lambda x: self._datetime_to_date(x.get('DTSTART').dt))
        event_list = []
        for e in events:
            event_time = self._change_timezone(e.get('DTSTART').dt).strftime('%Y/%m/%d %H:%M')
            event_name = str(e.get('SUMMARY'))
            event_list.append((event_time, event_name))
        return event_list

    def _change_timezone(self, src):
        if isinstance(src, datetime):
            return src.astimezone(timezone(timedelta(hours=9)))
        else:
            return src

    def _datetime_to_date(self, src):
        if isinstance(src, datetime):
            return src.date()
        else:
            return src