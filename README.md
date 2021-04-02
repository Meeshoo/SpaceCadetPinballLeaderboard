# SpaceCadetPinballLeaderboard
A Django thing that displays 3D Space Cadet Pinball scores on a leaderboard, with python based client.

Client files are in the Client folder, there is one that posts your scores onces and exits and one that posts them every 30 seconds (ideal to be put in a startup folder).

Currently runs on port 5050, but can be changed when running the server. Note if you do that you will have the change the port the client posts to in the client scripts.


## Get going

1. Edit SpaceCadetPinballLeaderboard/settings.py and change the SECRET_KEY to something long and random, currently ALLOWED_HOSTS only has 127.0.0.1, but change this also if needed
2. Run the server with `python manage.py runserver 127.0.0.1:5050`, then kill it with CTRL + C. This is so it makes the SQLite file.
3. Run `python manage.py makemigrations`
4. Run `python manage.py migrate`
5. Run server again with `python manage.py runserver 127.0.0.1:5050`

Your server should be up and running!

## Notes

- The game only stores your highscores once you close the game, so if you set a new highscore you will have to close the game for it to be posted to the server.
- Currently the server only displays results if there are 10 scores in the database (TOFIX).
