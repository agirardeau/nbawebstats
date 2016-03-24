.. highlight:: python

=====
Usage
=====

Get players in a given season::

    players = request_stats('all-players', {'Season': 2015})

Get career stats for a given player::

    career_stats = request_stats('player-career-stats', {'PlayerID': 3415843})

Get game logs for a given player and season::

    game_logs = request_stats('player-game-logs', {'PlayerID': 3415843, 'Season': 2015})

Get info about teams in the league::

    team_info = request_stats('league-franchise-history')

Get game logs for a given team::

    game_logs = request_stats('team-game-logs', {'TeamID': 259, 'Season': 2015})

Get information about a particular game::

    game_logs = request_stats('game-boxscore-advanced', {'GameID': 74256945})
