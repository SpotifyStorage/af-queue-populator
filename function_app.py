from datetime import datetime
import logging
import azure.functions as func
import requests

app = func.FunctionApp()

@app.schedule(schedule="0 0 * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def playcount_trigger(myTimer: func.TimerRequest) -> None:

    response = requests.get('https://spotify-playcount.livelyocean-7de1f403.canadacentral.azurecontainerapps.io/album_queue/populate')

    logging.info(f'The album queue populator endpoint has been called at {datetime.now()} (Montreal time)')

@app.schedule(schedule="0 22 * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def discovery_trigger(myTimer: func.TimerRequest) -> None:

    response = requests.get('https://discover-new-releases.livelyocean-7de1f403.canadacentral.azurecontainerapps.io/discover/populate')

    logging.info(f'The artist queue populator endpoint has been called at {datetime.now()} (Montreal time)')

    