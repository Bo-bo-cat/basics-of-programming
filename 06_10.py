## Завдання 10: Календар подій
from datetime import datetime

class Event:
    def init(self, name, date, time, desc=""): self.name, self.date, self.time, self.desc = name, date, time, desc
    def repr(self): return f"{self.date} {self.time} — {self.name}"
    def dt(self): return datetime.strptime(f"{self.date} {self.time}", "%Y-%m-%d %H:%M")

class Calendar:
    def init(self): self.events = []
    def add_event(self, e): self.events.append(e) if not self.has_conflict(e) else print(f"⚠️ Конфлікт: '{e.name}' не додано.")
    def get_events_by_date(self, d): return [e for e in self.events if e.date == d]
    def get_upcoming_events(self): return sorted(self.events, key=lambda e: e.dt())
    def remove_event(self, n): self.events = [e for e in self.events if e.name != n]
    def has_conflict(self, e): return any(x.date == e.date and x.time == e.time for x in self.events)


if name == "main":
    cal = Calendar()
    cal.add_event(Event("Meeting", "2024-01-15", "10:00", "Team sync"))
    cal.add_event(Event("Lunch", "2024-01-15", "13:00"))
    cal.add_event(Event("Meeting", "2024-01-15", "10:00"))  
    print("\n Події 2024-01-15:", cal.get_events_by_date("2024-01-15"))
    print("\n Усі події:", cal.get_upcoming_events())
    cal.remove_event("Lunch")
    print("\n Після видалення:", cal.get_upcoming_events())