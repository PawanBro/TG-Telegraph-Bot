import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1969753435:AAHO0CMs7-vcyT7HKQ6O4jwz6ygqIdTK0LI")

    APP_ID = int(os.environ.get("APP_ID", 3550946))

    API_HASH = os.environ.get("API_HASH", "6235d84de3799a511c4e609d1a0bddb5")
