<p align="center">Pyrogram and Telethon String Session Bot


<p align="center"><a href="https://www.github.com/anunicn47/StringSessionBot"><img src="https://graph.org/file/ff8305e937ef8e29e1ab1.jpg" width="1000"></a></p>

Telegram bot to generate pyrogram and telethon string session.

### Script to get your telegram Session in telethon and pyrogram.

<a href="https://replit.com/@anunicn47/GenerateStringSession?v=1"><img src="https://graph.org/file/f45cf901be8648213590f.jpg" alt="generate_string" /></a>



### Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/anunicn47/StringSessionBot)

1. Tap on above button and fill `API_ID`, `API_HASH`, `BOT_TOKEN` (and `MUST_JOIN`).
2. Then tap "Deploy App" below it. Wait till deploying is complete (will take atmost 2 minutes).
3. After deploying is complete, tap on "Manage App"
4. Check the logs to see if your bot is ready!

### Local Deploying

1. Clone the repo
   ```markdown
   git clone https://github.com/anunicn47/StringSessionBot
   ```
2. Get a `DATABASE_URL`. If you don't know how, deploy using Heroku Button only or delete database things as it's not a compulsion.
   
3. Rename `.env.sample` to `.env` and fill the needed variables

4. Enter the directory
   ```markdown
   cd StringSessionBot
   ```

5. Install all the dependencies
   ```markdown
   pip install -r requirements.txt
   ```

6. Run the file
   ```markdown
   python3 bot.py
   ```

## Environment Variables

#### Mandatory Vars

- `API_ID` - Get this from [my.telegram.org](https://my.telegram.org/auth)
- `API_HASH` - Get this from [my.telegram.org](https://my.telegram.org/auth)
- `BOT_TOKEN` - Get this from [@BotFather](https://t.me/BotFather)
- `DATABASE_URL` - Will be automatically added by Heroku.
- `MUST_JOIN` - Username/ID of your telegram channel/group.

## Functions

- Generate Pyrogram user string session
- Generate Pyrogram bot string session
- Generate Pyrogram (Major) Version 1 and 2 string sessions
- Generate Telethon string session


