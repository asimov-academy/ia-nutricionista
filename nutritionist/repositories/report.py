import json
from typing import List, Optional
from datetime import datetime
from tinydb import Query
from nutritionist.models import Report
from nutritionist.repositories.base_repository import BaseRepository


class ReportRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.report_table = self.get_table('reports')

    def create_report(self, user_id: int, content: str) -> Report:
        report = Report(
            user_id=user_id,
            content=content,
        )
        self.report_table.insert(json.loads(report.model_dump_json()))
        return report

    def get_reports_by_user_and_date(self, user_id: int, date: datetime) -> List[Report]:
        ReportQuery = Query()
        results = self.report_table.search(
            (ReportQuery.user_id == user_id) & 
            (ReportQuery.date.test(lambda d: datetime.fromisoformat(d).date() == date.date()))
        )
        return [Report(**report) for report in results]

    def delete_report(self, report_id: int) -> None:
        ReportQuery = Query()
        self.report_table.remove(ReportQuery.id == report_id)

    def get_report_by_id(self, report_id: int) -> Optional[Report]:
        ReportQuery = Query()
        result = self.report_table.get(ReportQuery.id == report_id)
        return Report(**result) if result else None

    def get_all_reports(self) -> List[Report]:
        all_reports = self.report_table.all()
        return [Report(**report) for report in all_reports]
