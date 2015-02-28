# Skybot Plugins

Plugins for your [Skybot](http://github.com/rmmh/skybot)!

## twitch.py
Unfurls Twitch URLs with title, game, status and viewers.

### Usage
```
<bcoia> twitch.tv/twitchplayspokemon
<skybot> TwitchPlaysPokemon is LIVE playing Pokémon Battle Revolution | Twitch Plays Pokemon (Enter moves via chat!!!) | 557 viewers
```

Also adds `.twitch [username]` command to search a username manually. Output includes the channel's URL.
```
<bcoia> .twitch saltybet
<skybot> SaltyBet is LIVE playing M.U.G.E.N | Salty's Dream Cast Casino! Place your bets at www.saltybet.com | 351 viewers | http://www.twitch.tv/saltybet
```

### Installation
1. Place `twitch.py` in your Skybot's `/plugins/` directory. That's it!

## hearthstone.py
Queries local Hearthstone JSON database (provided by hearthstonejson.com) for a given card name and returns information. Returns closest match for partial names.

### Usage
```
<bcoia> .hs argent
<skybot> (6) Argent Commander | Rare Neutral Minion, Expert set | 4/2, Charge, Divine Shield
```

### Installation
1. Place `AllSets.json` from hearthstonejson.com in your Skybot's root directory.
2. Place `hearthstone.py` into your Skybot's `/plugins/` directory.

## vox.py
Allows quick tweeting to a public account.

### Usage

Using "undo" will delete the last tweet made, with a time limit of 1 hour.
Using a URL to another tweet will retweet it.
Any other text will tweet it to the account.
```
<bcoia> .vox This is a tweet.
<skybot> Tweeted: This is a tweet.
<bcoia> .vox undo
<skybot> Removed Tweet: This is a tweet.
<bcoia> .vox https://twitter.com/twitter/status/145344012
<skybot> Retweeted: working on iphones via 'hahlo' and 'pocket tweets' - fun!
```
### Installation
1. Place 'twitter.py' in your Skybot's '/plugins/' directory.
2. Go to [the Twitter App Manager](https://apps.twitter.com) while logged into the twitter account you wish to use. Create a new app. Generate and remember the consumer, consumer secret, access, and access secret API keys.
3. Open the Skybot config. In the API keys list, add the following entry:
```
"vox":
{
	"consumer": "<consumer API key>",
	"consumer_secret": "<consumer secret API key>",
	"access": "<access API key>",
	"access_secret": "<access secret API key>",
	"my_name": "<name of account being used>"
},
```
