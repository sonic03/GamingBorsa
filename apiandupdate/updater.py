from datetime import datetime
import os

from apscheduler.schedulers.background import BackgroundScheduler
from . import apivegüncelleme


def start():
        scheduler = BackgroundScheduler()
        scheduler.add_job(apivegüncelleme.lol, 'interval', minutes=2)
        scheduler.add_job(apivegüncelleme.oav, 'interval', minutes=2)
        scheduler.add_job(apivegüncelleme.updateall, 'interval', minutes=3)
        print("güncelleme çalıştı")
        s=datetime.now()
        print(s)
        
        
        scheduler.start()