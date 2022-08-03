## Startup on your own server

1. Create telegram bot using [@BotFather](t.me/BotFather) and get token;
2. Create telegram public channel, add a bot to it and give him admin rights (At least, `Post messages` permission);
3. Replace constant `BOT_TOKEN` value with a string containing your telegram bot token;
4. Replace constant `TELEGRAM_CHANNEL_NAME` value with a string containing inner telegram link to your public channel (for example, `@eth_price_info`);
5. Start script in the background: `python3 main.py &`