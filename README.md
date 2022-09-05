# SpaceCadetPinballLeaderboard
A Django thing that displays 3D Space Cadet Pinball scores on a leaderboard, with python based client, and DynamoDB database.

Client files are in the Client folder, there is one that posts your scores onces and exits and one that posts them every 30 seconds (ideal to be put in a startup folder).

## NOTE: If you want an easy local setup use the sqlite-local branch, setup instructions are in the README

### Notes

- The game only stores your highscores once you close the game, so if you set a new highscore you will have to close the game for it to be posted to the server.
