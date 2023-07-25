from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 10940339
    API_HASH = "4cdbbcc7a57756127b1f3df13a7ee175"
    # the name to display in your alive message
    ALIVE_NAME = "Radha"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://xhagcmjv:RcihLUmDeUm5X8oZwsr5iaesaVrBxxXi@mahmud.db.elephantsql.com/xhagcmjv"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1AZWarzwBu0czf1XlIK_SChgdqieKFM3tc6L5bmQWJLNeTmaM68rBV7-yzVLHF15ftSmwjBEkKrQL5XrtJjUWEHYRH7ITNTAxKW_zmmmrXUh44OEw-G-HKd4Pmdst0UK2po7TUgO5nNGuusBc0lJJsZIuR574NxIWEw522QszeZOBanI8FtJ0mRunak3PM02Fq8Ul6PnpNGNYYfqzp7IiTCPLLJUO8y9nrhoM6gRL36johWqKrmCPHOPEoqcrtQ3I_jtzFNMQG5SxzMLjRq2VqLiRQVB1uOeBJvqqAHRyeL4BC4SWTb6tz_Jo9s5MLkLrUKS0hUD9oBXuCZSqi4Pjh2c3bYMVX0Y="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6035983646:AAF98AENKvE4w0Zx69Fgze91WwDa1iOo7Xo"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001628448230
    # command 
    COMMAND_HAND_LER = ">"
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = ">"
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"