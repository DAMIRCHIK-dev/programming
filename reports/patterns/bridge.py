# reports/patterns/bridge.py
from abc import ABC, abstractmethod
from reports.query import current_inventory

class DataProvider(ABC):
    @abstractmethod
    def fetch(self):
        ...

class InventoryProvider(DataProvider):
    def fetch(self):
        return current_inventory()

class Report(ABC):
    def __init__(self, provider: DataProvider):
        self.provider = provider
    @abstractmethod
    def render(self):
        ...

class TableReport(Report):
    def render(self):
        data = self.provider.fetch()
        return {"type": "table", "rows": data}

class ChartReport(Report):
    def render(self):
        data = self.provider.fetch()
        return {"type": "chart", "points": data}
