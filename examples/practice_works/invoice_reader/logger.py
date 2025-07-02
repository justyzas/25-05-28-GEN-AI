import datetime as dt


def log(text: str):
    with open("log.txt", 'a') as f:
        f.write(f"[{dt.datetime.now()}]: {text}\n")
