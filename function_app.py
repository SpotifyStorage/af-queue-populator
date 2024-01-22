import logging
import azure.functions as func
import requests

app = func.FunctionApp()

@app.schedule(schedule="0 0 * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False, ) 
def playcount_trigger(myTimer: func.TimerRequest) -> None:
    # if myTimer.past_due:
    #     logging.info('The timer is past due!')

    response = requests.get('https://spotify-playcount.livelyocean-7de1f403.canadacentral.azurecontainerapps.io/album_queue/populate')

    logging.info('The album queue populator endpoint has been called')