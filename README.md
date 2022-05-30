# Mudae Bot
A bot for Discord Mudae bot, lol. Useful to get specific characters

### How to use:
1. Get your request's authorization header. it's in any request to Discord's site, check devtools;
1. Get the channel's id. it's in the url, after /channel/[id];
1. Get the emoji you want to react (url encoded);
1. Go to preferences.json;
1. Change:
    - "your-username" to your username in server
    - "mudae-username" to mudae's username in server
    - "auth" to the authorization
    - "channel" to the channel's id
    - "command-to-make" to the command of your preference. it needs to return a claimable character
    - "emoji-reaction" to the url encoded emoji
    - "wishlist": add any character you want
    - "wishlist-series": add any anime/game series you want, the number is the minimum of kakera (server need to have $togglekakera on)
1. Be sure your PC's clock is up to date

# Still in development!

#### TODOS:
- [ ] sending messages
- [ ] implement timer (timer, offset)
- [ ] auto-claim if more than X kakera