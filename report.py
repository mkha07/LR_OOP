from typing import Dict
from openpyxl import Workbook


def write_overdue_report(result: Dict[str, int], output_path: str) -> str:
    wb = Workbook()
    ws = wb.active
    ws.title = "Просроченные"
    ws.append(["Вид мебели", "Количество просроченных единиц"])
    for furniture_type, qty in sorted(result.items(), key=lambda x: x[1], reverse=True):
        ws.append([furniture_type, qty])
    wb.save(output_path)
    return output_path
