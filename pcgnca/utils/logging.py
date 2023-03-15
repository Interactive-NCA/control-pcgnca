"""
Make output in the terminal more readable.
"""

from rich.console import Console
from rich.table import Table
from rich import box

import datetime

from ._rich_themes import SCRIPT_INFO

class ScriptInformation:

    def __init__(self):
        self.theme = SCRIPT_INFO
        self.c = Console(theme=self.theme, record=True)
        self.time_format = "%B %d %Y %H:%M:%S"

    def section_start(self, text):
        self.c.rule(text, style="section")

    def show_table(self, title, columns, rows):
        table = Table(title=title, expand=True, box=box.SIMPLE)
        for column in columns:
            table.add_column(column, style="rose")
        
        for row in rows:
            table.add_row(*row)
        
        self.c.print(table)

    def working_on(self, text):
        self.c.print(":snake: " + text, style="working")

    def script_time(self):
        text = datetime.datetime.now().strftime(self.time_format)
        self.c.print(":calendar: " + text, style="time")

    def important_metric(self, desc, metric):
        text = f":traffic_light: [imp_desc]{desc}[/]: [imp_metr]{metric}[/]"
        self.c.print(text)

    def author(self, firstn, lastn):
        text = f":panda_face: [subtle]Created by[/] [foam]{firstn} {lastn}[/]"
        self.c.print(text)

    def save(self, path):
        self.c.save_html(path)