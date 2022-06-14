from datetime import datetime

def logger(viesti):
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " " + viesti)