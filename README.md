# DHAPI
DHAPI is a Daggerheart a Botscirpt for Discord that allows you to get information about Daggerheart and even create new Character Sheets. 

# Current Features
- Display currently available offical cards (void cards to be added in the future (Dread and Blood Domain not available))
- Learn more about the different Daggerheart Domain cards
- Access all currently availabnle Void Content in PDF from Directly from Discord
- Create a new Character sheet within Discord and Download it. 

# Future Features
- Adverseries Statblocks
- Encouter Planner
- NPC Generator

# How to use this Project:
When the Bot Starts it fetches current available information form different sources such as https://www.daggerheart.com/srd/, [orthling](https://www.reddit.com/user/orthling/)'s [google-sheet](https://docs.google.com/spreadsheets/d/1cIoBHAvvuScHrAUnwjGvd-2AxfgsLamWCtx-5x7YYGo/edit?gid=1820067966#gid=1820067966), https://cardcreator.daggerheart.com and, https://www.daggerheart.com/thevoid/

When everything is downloaded the bot has the following functions:

- !card CARDNAME  &rarr; Dispalys an available card     
- !domain None | DOMAINNAME | DOMAINCARDNAME &rarr; Provides information on the avialbale Domains, the available Cards per Domain or displays a domaincard in the chat 
- !newchar NAME | CLASS | SUBCLASS | COMMUNITY | ANCESTRY &rarr; Creates a new charactersheet with all information filled in based on given inputs
- !void None &rarr; Provides Downloadable PDFs to the content available on "The Void"

# How this project was created
I realized that there is no API available for Daggerheart content, which is why I thoght it might help me and other friends of the game. Plus i wanted an excuse to combine two of my hobbies DH and Programming. 

# License
This product includes materials from the Daggerheart System Reference Document 1.0, © Critical Role, LLC. under the terms of the Darrington Press Community Gaming (DPCGL) License. More information can be found at  https://www.daggerheart.com. There are no previous modifications by others. 