.. highlight:: python

=====
Usage
=====

Import and construct the :class:`WebInterface` class from ``nbawebstats``::

    from nbawebstats.inferface import WebInterface
    w = WebInterface()

Get players in a given season::

    players = w.request('all-players', {'Season': 2015})

Get career stats for a given player::

    career_stats = w.request('player-career-stats', {'PlayerID': 3415843})

Get game logs for a given player and season::

    game_logs = w.request('player-game-logs', {'PlayerID': 3415843, 'Season': 2015})

Get info about teams in the league::

    team_info = w.request('league-franchise-history')

Get game logs for a given team::

    game_logs = w.request('team-game-logs', {'TeamID': 259, 'Season': 2015})

Get information about a particular game::

    game_logs = w.request('game-boxscore-advanced', {'GameID': 74256945})
