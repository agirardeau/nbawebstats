====================
Request Reference
====================

********
Requests
********

.. _request-all-players:

all-players
-------------------------------


:Required Parameters: :ref:`Season <param-season>`

:Optional Parameters: :ref:`IsOnlyCurrentSeason <param-isonlycurrentseason>`, :ref:`LeagueID <param-leagueid>`

:Return Fields: ``'list'``
    

.. _request-draft-agility:

draft-agility
-------------------------------


:Required Parameters: :ref:`SeasonYear <param-seasonyear>`

:Optional Parameters: :ref:`LeagueID <param-leagueid>`

:Return Fields: ``'data'``
    

.. _request-draft-anthro:

draft-anthro
-------------------------------


:Required Parameters: :ref:`SeasonYear <param-seasonyear>`

:Optional Parameters: :ref:`LeagueID <param-leagueid>`

:Return Fields: ``'data'``
    

.. _request-draft-combine-all-stats:

draft-combine-all-stats
-------------------------------


:Required Parameters: :ref:`SeasonYear <param-seasonyear>`

:Optional Parameters: :ref:`LeagueID <param-leagueid>`

:Return Fields: ``'data'``
    

.. _request-draft-non-stationary-shooting:

draft-non-stationary-shooting
-------------------------------


:Required Parameters: :ref:`SeasonYear <param-seasonyear>`

:Optional Parameters: :ref:`LeagueID <param-leagueid>`

:Return Fields: ``'data'``
    

.. _request-draft-spot-shooting:

draft-spot-shooting
-------------------------------


:Required Parameters: :ref:`SeasonYear <param-seasonyear>`

:Optional Parameters: :ref:`LeagueID <param-leagueid>`

:Return Fields: ``'data'``
    

.. _request-game-boxscore-advanced:

game-boxscore-advanced
-------------------------------


:Required Parameters: :ref:`GameID <param-gameid>`

:Optional Parameters: :ref:`EndPeriod <param-endperiod>`, :ref:`EndRange <param-endrange>`, :ref:`RangeType <param-rangetype>`, :ref:`StartPeriod <param-startperiod>`, :ref:`StartRange <param-startrange>`

:Return Fields: ``'player-stats'``, ``'team-stats'``
    

.. _request-game-boxscore-fourfactors:

game-boxscore-fourfactors
-------------------------------


:Required Parameters: :ref:`GameID <param-gameid>`

:Optional Parameters: :ref:`EndPeriod <param-endperiod>`, :ref:`EndRange <param-endrange>`, :ref:`RangeType <param-rangetype>`, :ref:`StartPeriod <param-startperiod>`, :ref:`StartRange <param-startrange>`

:Return Fields: ``'player-stats'``, ``'team-stats'``
    

.. _request-game-boxscore-misc:

game-boxscore-misc
-------------------------------


:Required Parameters: :ref:`GameID <param-gameid>`

:Optional Parameters: :ref:`EndPeriod <param-endperiod>`, :ref:`EndRange <param-endrange>`, :ref:`RangeType <param-rangetype>`, :ref:`StartPeriod <param-startperiod>`, :ref:`StartRange <param-startrange>`

:Return Fields: ``'player-stats'``, ``'team-stats'``
    

.. _request-game-boxscore-scoring:

game-boxscore-scoring
-------------------------------


:Required Parameters: :ref:`GameID <param-gameid>`

:Optional Parameters: :ref:`EndPeriod <param-endperiod>`, :ref:`EndRange <param-endrange>`, :ref:`RangeType <param-rangetype>`, :ref:`StartPeriod <param-startperiod>`, :ref:`StartRange <param-startrange>`

:Return Fields: ``'player-stats'``, ``'team-stats'``
    

.. _request-game-boxscore-summary:

game-boxscore-summary
-------------------------------


:Required Parameters: :ref:`GameID <param-gameid>`

:Optional Parameters: 

:Return Fields: ``'game-summary'``, ``'other-stats'``, ``'officials'``, ``'inactive-players'``, ``'game-info'``, ``'line-score'``, ``'last-meeting'``, ``'season-series'``, ``'-available-video'``
    

.. _request-game-boxscore-tracking:

game-boxscore-tracking
-------------------------------


:Required Parameters: :ref:`GameID <param-gameid>`

:Optional Parameters: 

:Return Fields: ``'player-stats'``, ``'team-stats'``
    

.. _request-game-boxscore-traditional:

game-boxscore-traditional
-------------------------------


:Required Parameters: :ref:`GameID <param-gameid>`

:Optional Parameters: :ref:`EndPeriod <param-endperiod>`, :ref:`EndRange <param-endrange>`, :ref:`RangeType <param-rangetype>`, :ref:`StartPeriod <param-startperiod>`, :ref:`StartRange <param-startrange>`

:Return Fields: ``'player-stats'``, ``'team-stats'``
    

.. _request-game-boxscore-usage:

game-boxscore-usage
-------------------------------


:Required Parameters: :ref:`GameID <param-gameid>`

:Optional Parameters: :ref:`EndPeriod <param-endperiod>`, :ref:`EndRange <param-endrange>`, :ref:`RangeType <param-rangetype>`, :ref:`StartPeriod <param-startperiod>`, :ref:`StartRange <param-startrange>`

:Return Fields: ``'player-stats'``, ``'team-stats'``
    

.. _request-game-play-by-play:

game-play-by-play
-------------------------------


:Required Parameters: :ref:`GameID <param-gameid>`

:Optional Parameters: :ref:`EndPeriod <param-endperiod>`, :ref:`StartPeriod <param-startperiod>`

:Return Fields: ``'plays'``, ``'-available-video'``
    

.. _request-league-classic-stats:

league-classic-stats
-------------------------------


:Required Parameters: :ref:`Season <param-season>`

:Optional Parameters: :ref:`DateFrom <param-datefrom>`, :ref:`DateTo <param-dateto>`, :ref:`GameScope <param-gamescope>`, :ref:`GameSegment <param-gamesegment>`, :ref:`LastNGames <param-lastngames>`, :ref:`LeagueID <param-leagueid>`, :ref:`Location <param-location>`, :ref:`MeasureType <param-measuretype>`, :ref:`Month <param-month>`, :ref:`OpponentTeamID <param-opponentteamid>`, :ref:`Outcome <param-outcome>`, :ref:`PaceAdjust <param-paceadjust>`, :ref:`Period <param-period>`, :ref:`PerMode <param-permode>`, :ref:`PlayerExperience <param-playerexperience>`, :ref:`PlayerPosition <param-playerposition>`, :ref:`PlusMinus <param-plusminus>`, :ref:`Rank <param-rank>`, :ref:`SeasonSegment <param-seasonsegment>`, :ref:`SeasonType <param-seasontype>`, :ref:`StarterBench <param-starterbench>`, :ref:`VsConference <param-vsconference>`, :ref:`VsDivision <param-vsdivision>`

:Return Fields: ``'stats'``
    

.. _request-league-clutch-stats:

league-clutch-stats
-------------------------------


:Required Parameters: :ref:`Season <param-season>`

:Optional Parameters: :ref:`AheadBehind <param-aheadbehind>`, :ref:`ClutchTime <param-clutchtime>`, :ref:`DateFrom <param-datefrom>`, :ref:`DateTo <param-dateto>`, :ref:`GameScope <param-gamescope>`, :ref:`GameSegment <param-gamesegment>`, :ref:`LastNGames <param-lastngames>`, :ref:`LeagueID <param-leagueid>`, :ref:`Location <param-location>`, :ref:`MeasureType <param-measuretype>`, :ref:`Month <param-month>`, :ref:`OpponentTeamID <param-opponentteamid>`, :ref:`Outcome <param-outcome>`, :ref:`PaceAdjust <param-paceadjust>`, :ref:`Period <param-period>`, :ref:`PerMode <param-permode>`, :ref:`PlayerExperience <param-playerexperience>`, :ref:`PlayerPosition <param-playerposition>`, :ref:`PlusMinus <param-plusminus>`, :ref:`PointDiff <param-pointdiff>`, :ref:`Rank <param-rank>`, :ref:`SeasonSegment <param-seasonsegment>`, :ref:`SeasonType <param-seasontype>`, :ref:`StarterBench <param-starterbench>`, :ref:`VsConference <param-vsconference>`, :ref:`VsDivision <param-vsdivision>`

:Return Fields: ``'clutch'``
    

.. _request-league-daily-scoreboard:

league-daily-scoreboard
-------------------------------


:Required Parameters: 

:Optional Parameters: 

:Return Fields: ``'game-header'``, ``'linescore'``, ``'series-standings'``, ``'last-meeting'``, ``'eastern-conference-standings'``, ``'western-conference-standings'``, ``'available'``, ``'team-leaders'``, ``'ticket-links'``, ``'win-probability'``
    

.. _request-league-franchise-history:

league-franchise-history
-------------------------------


:Required Parameters: 

:Optional Parameters: :ref:`LeagueID <param-leagueid>`

:Return Fields: ``'current-teams'``, ``'defunct-teams'``
    

.. _request-league-leaders:

league-leaders
-------------------------------


:Required Parameters: :ref:`Season <param-season>`, :ref:`StatCategory <param-statcategory>`

:Optional Parameters: :ref:`LeagueID <param-leagueid>`, :ref:`PerMode <param-permode>`, :ref:`Scope <param-scope>`, :ref:`SeasonType <param-seasontype>`

:Return Fields: ``'leaders'``
    

.. _request-league-lineups:

league-lineups
-------------------------------


:Required Parameters: :ref:`GameID <param-gameid>`, :ref:`Season <param-season>`

:Optional Parameters: :ref:`DateFrom <param-datefrom>`, :ref:`DateTo <param-dateto>`, :ref:`GameSegment <param-gamesegment>`, :ref:`GroupQuantity <param-groupquantity>`, :ref:`LastNGames <param-lastngames>`, :ref:`LeagueID <param-leagueid>`, :ref:`Location <param-location>`, :ref:`MeasureType <param-measuretype>`, :ref:`Month <param-month>`, :ref:`OpponentTeamID <param-opponentteamid>`, :ref:`Outcome <param-outcome>`, :ref:`PaceAdjust <param-paceadjust>`, :ref:`Period <param-period>`, :ref:`PerMode <param-permode>`, :ref:`PlusMinus <param-plusminus>`, :ref:`Rank <param-rank>`, :ref:`SeasonSegment <param-seasonsegment>`, :ref:`SeasonType <param-seasontype>`, :ref:`VsConference <param-vsconference>`, :ref:`VsDivision <param-vsdivision>`

:Return Fields: ``'lineups'``
    

.. _request-league-playoff-picture:

league-playoff-picture
-------------------------------


:Required Parameters: :ref:`SeasonID <param-seasonid>`

:Optional Parameters: :ref:`LeagueID <param-leagueid>`

:Return Fields: ``'eastern-conf-playoff-picture'``, ``'western-confe-playoff-picture'``, ``'eastern-conf-standing'``, ``'western-conf-standing'``, ``'eastern-conf-remaining-games'``, ``'western-conf-remaining-games'``
    

.. _request-league-team-shot-locations:

league-team-shot-locations
-------------------------------


:Required Parameters: :ref:`Season <param-season>`

:Optional Parameters: :ref:`DateFrom <param-datefrom>`, :ref:`DateTo <param-dateto>`, :ref:`DistanceRange <param-distancerange>`, :ref:`GameScope <param-gamescope>`, :ref:`GameSegment <param-gamesegment>`, :ref:`LastNGames <param-lastngames>`, :ref:`LeagueID <param-leagueid>`, :ref:`Location <param-location>`, :ref:`MeasureType <param-measuretype>`, :ref:`Month <param-month>`, :ref:`OpponentTeamID <param-opponentteamid>`, :ref:`Outcome <param-outcome>`, :ref:`PaceAdjust <param-paceadjust>`, :ref:`Period <param-period>`, :ref:`PerMode <param-permode>`, :ref:`PlayerExperience <param-playerexperience>`, :ref:`PlayerPosition <param-playerposition>`, :ref:`PlusMinus <param-plusminus>`, :ref:`Rank <param-rank>`, :ref:`SeasonSegment <param-seasonsegment>`, :ref:`SeasonType <param-seasontype>`, :ref:`StarterBench <param-starterbench>`, :ref:`VsConference <param-vsconference>`, :ref:`VsDivision <param-vsdivision>`

    

.. _request-league-transactions:

league-transactions
-------------------------------


:Required Parameters: 

:Optional Parameters: 

    

.. _request-player-career-stats:

player-career-stats
-------------------------------


:Required Parameters: :ref:`PlayerID <param-playerid>`

:Optional Parameters: :ref:`LeagueID <param-leagueid>`, :ref:`PerMode <param-permode>`

:Return Fields: ``'season-totals-regular'``, ``'career-totals-regular'``, ``'season-totals-post'``, ``'career-totals-post'``, ``'season-totals-allstar'``, ``'career-totals-allstar'``, ``'season-totals-college'``, ``'career-totals-college'``, ``'season-rankings-regular'``, ``'season-rankings-post'``, ``'season-high'``, ``'career-high'``, ``'next-game'``
    

.. _request-player-defense-dashboard:

player-defense-dashboard
-------------------------------


:Required Parameters: :ref:`PlayerID <param-playerid>`, :ref:`Season <param-season>`, :ref:`TeamID <param-teamid>`

:Optional Parameters: :ref:`DateFrom <param-datefrom>`, :ref:`DateTo <param-dateto>`, :ref:`GameSegment <param-gamesegment>`, :ref:`LastNGames <param-lastngames>`, :ref:`LeagueID <param-leagueid>`, :ref:`Location <param-location>`, :ref:`Month <param-month>`, :ref:`OpponentTeamID <param-opponentteamid>`, :ref:`Outcome <param-outcome>`, :ref:`Period <param-period>`, :ref:`PerMode <param-permode>`, :ref:`SeasonSegment <param-seasonsegment>`, :ref:`SeasonType <param-seasontype>`, :ref:`VsConference <param-vsconference>`, :ref:`VsDivision <param-vsdivision>`

:Return Fields: ``'defending-shot'``
    

.. _request-player-demographics:

player-demographics
-------------------------------


:Required Parameters: :ref:`PlayerID <param-playerid>`

:Optional Parameters: 

:Return Fields: ``'player-info'``, ``'headline-stats'``
    

.. _request-player-game-logs:

player-game-logs
-------------------------------


:Required Parameters: :ref:`PlayerID <param-playerid>`, :ref:`Season <param-season>`

:Optional Parameters: :ref:`SeasonType <param-seasontype>`

:Return Fields: ``'logs'``
    

.. _request-player-general-splits:

player-general-splits
-------------------------------
.. warning:: This data may no longer be offered by nba.com.

:Required Parameters: :ref:`PlayerID <param-playerid>`, :ref:`Season <param-season>`

:Optional Parameters: :ref:`DateFrom <param-datefrom>`, :ref:`DateTo <param-dateto>`, :ref:`GameSegment <param-gamesegment>`, :ref:`LastNGames <param-lastngames>`, :ref:`LeagueID <param-leagueid>`, :ref:`Location <param-location>`, :ref:`MeasureType <param-measuretype>`, :ref:`Month <param-month>`, :ref:`OpponentTeamID <param-opponentteamid>`, :ref:`Outcome <param-outcome>`, :ref:`PaceAdjust <param-paceadjust>`, :ref:`Period <param-period>`, :ref:`PerMode <param-permode>`, :ref:`PlusMinus <param-plusminus>`, :ref:`Rank <param-rank>`, :ref:`SeasonSegment <param-seasonsegment>`, :ref:`SeasonType <param-seasontype>`, :ref:`VsConference <param-vsconference>`, :ref:`VsDivision <param-vsdivision>`

:Return Fields: ``'overall'``, ``'location'``, ``'wins-losses'``, ``'month'``, ``'pre-post-allstar'``, ``'starting-position'``, ``'days-rest'``
    

.. _request-player-passing-dashboard:

player-passing-dashboard
-------------------------------


:Required Parameters: :ref:`PlayerID <param-playerid>`, :ref:`Season <param-season>`, :ref:`TeamID <param-teamid>`

:Optional Parameters: :ref:`DateFrom <param-datefrom>`, :ref:`DateTo <param-dateto>`, :ref:`GameSegment <param-gamesegment>`, :ref:`LastNGames <param-lastngames>`, :ref:`LeagueID <param-leagueid>`, :ref:`Location <param-location>`, :ref:`Month <param-month>`, :ref:`OpponentTeamID <param-opponentteamid>`, :ref:`Outcome <param-outcome>`, :ref:`Period <param-period>`, :ref:`PerMode <param-permode>`, :ref:`SeasonSegment <param-seasonsegment>`, :ref:`SeasonType <param-seasontype>`, :ref:`VsConference <param-vsconference>`, :ref:`VsDivision <param-vsdivision>`

:Return Fields: ``'passes-made'``, ``'passes-received'``
    

.. _request-player-rebound-dashboard:

player-rebound-dashboard
-------------------------------


:Required Parameters: :ref:`PlayerID <param-playerid>`, :ref:`Season <param-season>`, :ref:`TeamID <param-teamid>`

:Optional Parameters: :ref:`DateFrom <param-datefrom>`, :ref:`DateTo <param-dateto>`, :ref:`GameSegment <param-gamesegment>`, :ref:`LastNGames <param-lastngames>`, :ref:`LeagueID <param-leagueid>`, :ref:`Location <param-location>`, :ref:`Month <param-month>`, :ref:`OpponentTeamID <param-opponentteamid>`, :ref:`Outcome <param-outcome>`, :ref:`Period <param-period>`, :ref:`PerMode <param-permode>`, :ref:`SeasonSegment <param-seasonsegment>`, :ref:`SeasonType <param-seasontype>`, :ref:`VsConference <param-vsconference>`, :ref:`VsDivision <param-vsdivision>`

:Return Fields: ``'overall'``, ``'shot-type'``, ``'contesting-rebounders'``, ``'shot-distance'``, ``'rebound-distance'``
    

.. _request-player-rebound-log:

player-rebound-log
-------------------------------
.. warning:: This data may no longer be offered by nba.com.

:Required Parameters: :ref:`PlayerID <param-playerid>`, :ref:`Season <param-season>`, :ref:`TeamID <param-teamid>`

:Optional Parameters: :ref:`DateFrom <param-datefrom>`, :ref:`DateTo <param-dateto>`, :ref:`GameSegment <param-gamesegment>`, :ref:`LastNGames <param-lastngames>`, :ref:`LeagueID <param-leagueid>`, :ref:`Location <param-location>`, :ref:`Month <param-month>`, :ref:`OpponentTeamID <param-opponentteamid>`, :ref:`Outcome <param-outcome>`, :ref:`Period <param-period>`, :ref:`SeasonSegment <param-seasonsegment>`, :ref:`SeasonType <param-seasontype>`, :ref:`VsConference <param-vsconference>`, :ref:`VsDivision <param-vsdivision>`

:Return Fields: ``'log'``
    

.. _request-player-shot-chart:

player-shot-chart
-------------------------------


:Required Parameters: :ref:`GameID <param-gameid>`, :ref:`PlayerID <param-playerid>`, :ref:`Season <param-season>`, :ref:`TeamID <param-teamid>`

:Optional Parameters: :ref:`AheadBehind <param-aheadbehind>`, :ref:`ClutchTime <param-clutchtime>`, :ref:`ContextFilter <param-contextfilter>`, :ref:`ContextMeasure <param-contextmeasure>`, :ref:`DateFrom <param-datefrom>`, :ref:`DateTo <param-dateto>`, :ref:`EndPeriod <param-endperiod>`, :ref:`EndRange <param-endrange>`, :ref:`GameSegment <param-gamesegment>`, :ref:`LastNGames <param-lastngames>`, :ref:`LeagueID <param-leagueid>`, :ref:`Location <param-location>`, :ref:`Month <param-month>`, :ref:`OpponentTeamID <param-opponentteamid>`, :ref:`Outcome <param-outcome>`, :ref:`Period <param-period>`, :ref:`Position <param-position>`, :ref:`RangeType <param-rangetype>`, :ref:`RookieYear <param-rookieyear>`, :ref:`SeasonSegment <param-seasonsegment>`, :ref:`SeasonType <param-seasontype>`, :ref:`StartPeriod <param-startperiod>`, :ref:`StartRange <param-startrange>`, :ref:`VsConference <param-vsconference>`, :ref:`VsDivision <param-vsdivision>`

:Return Fields: ``'chart'``, ``'leagueaverage'``
    

.. _request-player-shot-dashboard:

player-shot-dashboard
-------------------------------


:Required Parameters: :ref:`PlayerID <param-playerid>`, :ref:`Season <param-season>`, :ref:`TeamID <param-teamid>`

:Optional Parameters: :ref:`DateFrom <param-datefrom>`, :ref:`DateTo <param-dateto>`, :ref:`GameSegment <param-gamesegment>`, :ref:`LastNGames <param-lastngames>`, :ref:`LeagueID <param-leagueid>`, :ref:`Location <param-location>`, :ref:`Month <param-month>`, :ref:`OpponentTeamID <param-opponentteamid>`, :ref:`Outcome <param-outcome>`, :ref:`Period <param-period>`, :ref:`PerMode <param-permode>`, :ref:`SeasonSegment <param-seasonsegment>`, :ref:`SeasonType <param-seasontype>`, :ref:`VsConference <param-vsconference>`, :ref:`VsDivision <param-vsdivision>`

:Return Fields: ``'overall'``, ``'general'``, ``'shot-clock'``, ``'dribble'``, ``'closest-defender'``, ``'closest-defender-10ft'``, ``'touch-time'``
    

.. _request-player-shot-log:

player-shot-log
-------------------------------
.. warning:: This data may no longer be offered by nba.com.

:Required Parameters: :ref:`PlayerID <param-playerid>`, :ref:`Season <param-season>`, :ref:`TeamID <param-teamid>`

:Optional Parameters: :ref:`DateFrom <param-datefrom>`, :ref:`DateTo <param-dateto>`, :ref:`GameSegment <param-gamesegment>`, :ref:`LastNGames <param-lastngames>`, :ref:`LeagueID <param-leagueid>`, :ref:`Location <param-location>`, :ref:`Month <param-month>`, :ref:`OpponentTeamID <param-opponentteamid>`, :ref:`Outcome <param-outcome>`, :ref:`Period <param-period>`, :ref:`SeasonSegment <param-seasonsegment>`, :ref:`SeasonType <param-seasontype>`, :ref:`VsConference <param-vsconference>`, :ref:`VsDivision <param-vsdivision>`

:Return Fields: ``'log'``
    

.. _request-playtype-player-cut:

playtype-player-cut
-------------------------------


:Required Parameters: 

:Optional Parameters: 

:Return Fields: ``'offensive'``, ``'defensive'``, ``'season'``
    

.. _request-playtype-player-handoff:

playtype-player-handoff
-------------------------------


:Required Parameters: 

:Optional Parameters: 

:Return Fields: ``'offensive'``, ``'defensive'``, ``'season'``
    

.. _request-playtype-player-isolation:

playtype-player-isolation
-------------------------------


:Required Parameters: 

:Optional Parameters: 

:Return Fields: ``'offensive'``, ``'defensive'``, ``'season'``
    

.. _request-playtype-player-misc:

playtype-player-misc
-------------------------------


:Required Parameters: 

:Optional Parameters: 

:Return Fields: ``'offensive'``, ``'defensive'``, ``'season'``
    

.. _request-playtype-player-offrebound:

playtype-player-offrebound
-------------------------------


:Required Parameters: 

:Optional Parameters: 

:Return Fields: ``'offensive'``, ``'defensive'``, ``'season'``
    

.. _request-playtype-player-offscreen:

playtype-player-offscreen
-------------------------------


:Required Parameters: 

:Optional Parameters: 

:Return Fields: ``'offensive'``, ``'defensive'``, ``'season'``
    

.. _request-playtype-player-postup:

playtype-player-postup
-------------------------------


:Required Parameters: 

:Optional Parameters: 

:Return Fields: ``'offensive'``, ``'defensive'``, ``'season'``
    

.. _request-playtype-player-pr-ball-handler:

playtype-player-pr-ball-handler
-------------------------------


:Required Parameters: 

:Optional Parameters: 

:Return Fields: ``'offensive'``, ``'defensive'``, ``'season'``
    

.. _request-playtype-player-pr-roll-man:

playtype-player-pr-roll-man
-------------------------------


:Required Parameters: 

:Optional Parameters: 

:Return Fields: ``'offensive'``, ``'defensive'``, ``'season'``
    

.. _request-playtype-player-spotup:

playtype-player-spotup
-------------------------------


:Required Parameters: 

:Optional Parameters: 

:Return Fields: ``'offensive'``, ``'defensive'``, ``'season'``
    

.. _request-playtype-player-transition:

playtype-player-transition
-------------------------------


:Required Parameters: 

:Optional Parameters: 

:Return Fields: ``'offensive'``, ``'defensive'``, ``'season'``
    

.. _request-playtype-team-cut:

playtype-team-cut
-------------------------------


:Required Parameters: 

:Optional Parameters: 

:Return Fields: ``'offensive'``, ``'defensive'``, ``'season'``
    

.. _request-playtype-team-handoff:

playtype-team-handoff
-------------------------------


:Required Parameters: 

:Optional Parameters: 

:Return Fields: ``'offensive'``, ``'defensive'``, ``'season'``
    

.. _request-playtype-team-isolation:

playtype-team-isolation
-------------------------------


:Required Parameters: 

:Optional Parameters: 

:Return Fields: ``'offensive'``, ``'defensive'``, ``'season'``
    

.. _request-playtype-team-misc:

playtype-team-misc
-------------------------------


:Required Parameters: 

:Optional Parameters: 

:Return Fields: ``'offensive'``, ``'defensive'``, ``'season'``
    

.. _request-playtype-team-offrebound:

playtype-team-offrebound
-------------------------------


:Required Parameters: 

:Optional Parameters: 

:Return Fields: ``'offensive'``, ``'defensive'``, ``'season'``
    

.. _request-playtype-team-offscreen:

playtype-team-offscreen
-------------------------------


:Required Parameters: 

:Optional Parameters: 

:Return Fields: ``'offensive'``, ``'defensive'``, ``'season'``
    

.. _request-playtype-team-postup:

playtype-team-postup
-------------------------------


:Required Parameters: 

:Optional Parameters: 

:Return Fields: ``'offensive'``, ``'defensive'``, ``'season'``
    

.. _request-playtype-team-pr-ball-handler:

playtype-team-pr-ball-handler
-------------------------------


:Required Parameters: 

:Optional Parameters: 

:Return Fields: ``'offensive'``, ``'defensive'``, ``'season'``
    

.. _request-playtype-team-pr-roll-man:

playtype-team-pr-roll-man
-------------------------------


:Required Parameters: 

:Optional Parameters: 

:Return Fields: ``'offensive'``, ``'defensive'``, ``'season'``
    

.. _request-playtype-team-spotup:

playtype-team-spotup
-------------------------------


:Required Parameters: 

:Optional Parameters: 

:Return Fields: ``'offensive'``, ``'defensive'``, ``'season'``
    

.. _request-playtype-team-transition:

playtype-team-transition
-------------------------------


:Required Parameters: 

:Optional Parameters: 

:Return Fields: ``'offensive'``, ``'defensive'``, ``'season'``
    

.. _request-sportvu-catch-and-shoot:

sportvu-catch-and-shoot
-------------------------------


:Required Parameters: :ref:`Year <param-year>`

:Optional Parameters: 

:Return Fields: ``'data'``
    

.. _request-sportvu-defense:

sportvu-defense
-------------------------------


:Required Parameters: :ref:`Year <param-year>`

:Optional Parameters: 

:Return Fields: ``'data'``
    

.. _request-sportvu-drives:

sportvu-drives
-------------------------------


:Required Parameters: :ref:`Year <param-year>`

:Optional Parameters: 

:Return Fields: ``'data'``
    

.. _request-sportvu-passing:

sportvu-passing
-------------------------------


:Required Parameters: :ref:`Year <param-year>`

:Optional Parameters: 

:Return Fields: ``'data'``
    

.. _request-sportvu-pull-up-shooting:

sportvu-pull-up-shooting
-------------------------------


:Required Parameters: :ref:`Year <param-year>`

:Optional Parameters: 

:Return Fields: ``'data'``
    

.. _request-sportvu-rebounding:

sportvu-rebounding
-------------------------------


:Required Parameters: :ref:`Year <param-year>`

:Optional Parameters: 

:Return Fields: ``'data'``
    

.. _request-sportvu-shooting:

sportvu-shooting
-------------------------------


:Required Parameters: :ref:`Year <param-year>`

:Optional Parameters: 

:Return Fields: ``'data'``
    

.. _request-sportvu-speed:

sportvu-speed
-------------------------------


:Required Parameters: :ref:`Year <param-year>`

:Optional Parameters: 

:Return Fields: ``'data'``
    

.. _request-sportvu-team-catch-and-shoot:

sportvu-team-catch-and-shoot
-------------------------------


:Required Parameters: :ref:`Year <param-year>`

:Optional Parameters: 

:Return Fields: ``'data'``
    

.. _request-sportvu-team-defense:

sportvu-team-defense
-------------------------------


:Required Parameters: :ref:`Year <param-year>`

:Optional Parameters: 

:Return Fields: ``'data'``
    

.. _request-sportvu-team-drives:

sportvu-team-drives
-------------------------------


:Required Parameters: :ref:`Year <param-year>`

:Optional Parameters: 

:Return Fields: ``'data'``
    

.. _request-sportvu-team-passing:

sportvu-team-passing
-------------------------------


:Required Parameters: :ref:`Year <param-year>`

:Optional Parameters: 

:Return Fields: ``'data'``
    

.. _request-sportvu-team-pull-up-shooting:

sportvu-team-pull-up-shooting
-------------------------------


:Required Parameters: :ref:`Year <param-year>`

:Optional Parameters: 

:Return Fields: ``'data'``
    

.. _request-sportvu-team-rebounding:

sportvu-team-rebounding
-------------------------------


:Required Parameters: :ref:`Year <param-year>`

:Optional Parameters: 

:Return Fields: ``'data'``
    

.. _request-sportvu-team-shooting:

sportvu-team-shooting
-------------------------------


:Required Parameters: :ref:`Year <param-year>`

:Optional Parameters: 

:Return Fields: ``'data'``
    

.. _request-sportvu-team-speed:

sportvu-team-speed
-------------------------------


:Required Parameters: :ref:`Year <param-year>`

:Optional Parameters: 

:Return Fields: ``'data'``
    

.. _request-sportvu-team-touches:

sportvu-team-touches
-------------------------------


:Required Parameters: :ref:`Year <param-year>`

:Optional Parameters: 

:Return Fields: ``'data'``
    

.. _request-sportvu-touches:

sportvu-touches
-------------------------------


:Required Parameters: :ref:`Year <param-year>`

:Optional Parameters: 

:Return Fields: ``'data'``
    

.. _request-team-game-logs:

team-game-logs
-------------------------------


:Required Parameters: :ref:`Season <param-season>`, :ref:`TeamID <param-teamid>`

:Optional Parameters: :ref:`SeasonType <param-seasontype>`

:Return Fields: ``'logs'``
    

.. _request-team-history:

team-history
-------------------------------


:Required Parameters: :ref:`TeamID <param-teamid>`

:Optional Parameters: 

    

.. _request-team-info:

team-info
-------------------------------


:Required Parameters: :ref:`Season <param-season>`, :ref:`TeamID <param-teamid>`

:Optional Parameters: :ref:`LeagueID <param-leagueid>`, :ref:`SeasonType <param-seasontype>`

:Return Fields: ``'info'``, ``'season-ranks'``
    

.. _request-team-lineups:

team-lineups
-------------------------------


:Required Parameters: :ref:`Season <param-season>`, :ref:`TeamID <param-teamid>`

:Optional Parameters: :ref:`DateFrom <param-datefrom>`, :ref:`DateTo <param-dateto>`, :ref:`GameSegment <param-gamesegment>`, :ref:`LastNGames <param-lastngames>`, :ref:`LeagueID <param-leagueid>`, :ref:`Location <param-location>`, :ref:`MeasureType <param-measuretype>`, :ref:`Month <param-month>`, :ref:`OpponentTeamID <param-opponentteamid>`, :ref:`Outcome <param-outcome>`, :ref:`PaceAdjust <param-paceadjust>`, :ref:`Period <param-period>`, :ref:`PerMode <param-permode>`, :ref:`PlusMinus <param-plusminus>`, :ref:`Rank <param-rank>`, :ref:`SeasonSegment <param-seasonsegment>`, :ref:`SeasonType <param-seasontype>`, :ref:`VsConference <param-vsconference>`, :ref:`VsDivision <param-vsdivision>`

:Return Fields: ``'overall'``, ``'lineups'``
    

.. _request-team-on-off-court:

team-on-off-court
-------------------------------


:Required Parameters: :ref:`Season <param-season>`, :ref:`TeamID <param-teamid>`

:Optional Parameters: :ref:`DateFrom <param-datefrom>`, :ref:`DateTo <param-dateto>`, :ref:`GameSegment <param-gamesegment>`, :ref:`LastNGames <param-lastngames>`, :ref:`LeagueID <param-leagueid>`, :ref:`Location <param-location>`, :ref:`MeasureType <param-measuretype>`, :ref:`Month <param-month>`, :ref:`OpponentTeamID <param-opponentteamid>`, :ref:`Outcome <param-outcome>`, :ref:`PaceAdjust <param-paceadjust>`, :ref:`Period <param-period>`, :ref:`PerMode <param-permode>`, :ref:`PlusMinus <param-plusminus>`, :ref:`Rank <param-rank>`, :ref:`SeasonSegment <param-seasonsegment>`, :ref:`SeasonType <param-seasontype>`, :ref:`VsConference <param-vsconference>`, :ref:`VsDivision <param-vsdivision>`

:Return Fields: ``'overall'``, ``'on-court'``, ``'off-court'``, ``'overall-summary'``, ``'on-court-summary'``, ``'off-court-summary'``
    

.. _request-team-rebounding:

team-rebounding
-------------------------------


:Required Parameters: :ref:`Season <param-season>`, :ref:`TeamID <param-teamid>`

:Optional Parameters: :ref:`DateFrom <param-datefrom>`, :ref:`DateTo <param-dateto>`, :ref:`GameSegment <param-gamesegment>`, :ref:`LastNGames <param-lastngames>`, :ref:`LeagueID <param-leagueid>`, :ref:`Location <param-location>`, :ref:`Month <param-month>`, :ref:`OpponentTeamID <param-opponentteamid>`, :ref:`Outcome <param-outcome>`, :ref:`Period <param-period>`, :ref:`PerMode <param-permode>`, :ref:`SeasonSegment <param-seasonsegment>`, :ref:`SeasonType <param-seasontype>`, :ref:`VsConference <param-vsconference>`, :ref:`VsDivision <param-vsdivision>`

:Return Fields: ``'overall'``, ``'shot-type'``, ``'contesting-rebounders'``, ``'shot-distance'``, ``'rebound-distance'``
    

.. _request-team-roster:

team-roster
-------------------------------


:Required Parameters: :ref:`Season <param-season>`, :ref:`TeamID <param-teamid>`

:Optional Parameters: :ref:`LeagueID <param-leagueid>`

:Return Fields: ``'players'``, ``'coaches'``
    

.. _request-team-season-stats:

team-season-stats
-------------------------------


:Required Parameters: :ref:`Season <param-season>`, :ref:`TeamID <param-teamid>`

:Optional Parameters: :ref:`DateFrom <param-datefrom>`, :ref:`DateTo <param-dateto>`, :ref:`GameSegment <param-gamesegment>`, :ref:`LastNGames <param-lastngames>`, :ref:`LeagueID <param-leagueid>`, :ref:`Location <param-location>`, :ref:`MeasureType <param-measuretype>`, :ref:`Month <param-month>`, :ref:`OpponentTeamID <param-opponentteamid>`, :ref:`Outcome <param-outcome>`, :ref:`PaceAdjust <param-paceadjust>`, :ref:`Period <param-period>`, :ref:`PerMode <param-permode>`, :ref:`PlusMinus <param-plusminus>`, :ref:`Rank <param-rank>`, :ref:`SeasonSegment <param-seasonsegment>`, :ref:`SeasonType <param-seasontype>`, :ref:`VsConference <param-vsconference>`, :ref:`VsDivision <param-vsdivision>`

:Return Fields: ``'overall'``, ``'player-totals'``
    

.. _request-team-shooting:

team-shooting
-------------------------------


:Required Parameters: :ref:`Season <param-season>`, :ref:`TeamID <param-teamid>`

:Optional Parameters: :ref:`DateFrom <param-datefrom>`, :ref:`DateTo <param-dateto>`, :ref:`GameSegment <param-gamesegment>`, :ref:`LastNGames <param-lastngames>`, :ref:`LeagueID <param-leagueid>`, :ref:`Location <param-location>`, :ref:`Month <param-month>`, :ref:`OpponentTeamID <param-opponentteamid>`, :ref:`Outcome <param-outcome>`, :ref:`Period <param-period>`, :ref:`PerMode <param-permode>`, :ref:`SeasonSegment <param-seasonsegment>`, :ref:`SeasonType <param-seasontype>`, :ref:`VsConference <param-vsconference>`, :ref:`VsDivision <param-vsdivision>`

:Return Fields: ``'general'``, ``'shot-clock'``, ``'dribble'``, ``'closest-defender'``, ``'closest-defender-10ft'``, ``'touch-time'``
    

.. _request-team-shooting-splits:

team-shooting-splits
-------------------------------


:Required Parameters: :ref:`Season <param-season>`, :ref:`TeamID <param-teamid>`

:Optional Parameters: :ref:`DateFrom <param-datefrom>`, :ref:`DateTo <param-dateto>`, :ref:`GameSegment <param-gamesegment>`, :ref:`LastNGames <param-lastngames>`, :ref:`LeagueID <param-leagueid>`, :ref:`Location <param-location>`, :ref:`MeasureType <param-measuretype>`, :ref:`Month <param-month>`, :ref:`OpponentTeamID <param-opponentteamid>`, :ref:`Outcome <param-outcome>`, :ref:`PaceAdjust <param-paceadjust>`, :ref:`Period <param-period>`, :ref:`PerMode <param-permode>`, :ref:`PlusMinus <param-plusminus>`, :ref:`Rank <param-rank>`, :ref:`SeasonSegment <param-seasonsegment>`, :ref:`SeasonType <param-seasontype>`, :ref:`VsConference <param-vsconference>`, :ref:`VsDivision <param-vsdivision>`

:Return Fields: ``'overall'``, ``'shot-5ft'``, ``'shot-8ft'``, ``'shot-area'``, ``'assisted-shot'``, ``'shot-type'``, ``'assisted-by'``
    

.. _request-team-splits:

team-splits
-------------------------------


:Required Parameters: :ref:`Season <param-season>`, :ref:`TeamID <param-teamid>`

:Optional Parameters: :ref:`DateFrom <param-datefrom>`, :ref:`DateTo <param-dateto>`, :ref:`GameSegment <param-gamesegment>`, :ref:`LastNGames <param-lastngames>`, :ref:`LeagueID <param-leagueid>`, :ref:`Location <param-location>`, :ref:`MeasureType <param-measuretype>`, :ref:`Month <param-month>`, :ref:`OpponentTeamID <param-opponentteamid>`, :ref:`Outcome <param-outcome>`, :ref:`PaceAdjust <param-paceadjust>`, :ref:`Period <param-period>`, :ref:`PlusMinus <param-plusminus>`, :ref:`Rank <param-rank>`, :ref:`SeasonSegment <param-seasonsegment>`, :ref:`SeasonType <param-seasontype>`, :ref:`VsConference <param-vsconference>`, :ref:`VsDivision <param-vsdivision>`

:Return Fields: ``'overall'``, ``'location'``, ``'wins-losses'``, ``'month'``, ``'pre-post-allstar'``, ``'days-rest'``
    

**********
Parameters
**********

.. _param-aheadbehind:

AheadBehind
---------------------


:Type: :ref:`Enumerated <type-enumerated>`

:Options: ``'Ahead or Behind'``, ``'Behind or Tied'``, ``'Ahead or Tied'``

:Default: ``"Ahead or Behind"``

.. _param-clutchtime:

ClutchTime
---------------------


:Type: :ref:`Enumerated <type-enumerated>`

:Options: ``''``, ``'Last 5 Minutes'``, ``'Last 4 Minutes'``, ``'Last 3 Minutes'``, ``'Last 2 Minutes'``, ``'Last 1 Minute'``, ``'Last 30 Seconds'``, ``'Last 10 Seconds'``

:Default: ``""``

.. _param-contextfilter:

ContextFilter
---------------------
Honestly don't know what the format of this argument should be, but there's a request that requires it so it defaults to always empty.

:Type: :ref:`Enumerated <type-enumerated>`

:Options: ``''``

:Default: ``""``

.. _param-contextmeasure:

ContextMeasure
---------------------


:Type: :ref:`Enumerated <type-enumerated>`

:Options: ``'FGM'``, ``'FGA'``, ``'PG_PCT'``, ``'FG3M'``, ``'FG3A'``, ``'FG3_PCT'``, ``'PF'``, ``'EFG_PCT'``, ``'TS_PCT'``, ``'PTS_FB'``, ``'PTS_OFF_TOV'``, ``'PTS_2ND_CHANCE'``, ``'PF'``

:Default: ``"FGM"``

.. _param-datefrom:

DateFrom
---------------------


:Type: :ref:`Date <type-date>`

:Default: ``""``

.. _param-dateto:

DateTo
---------------------


:Type: :ref:`Date <type-date>`

:Default: ``""``

.. _param-distancerange:

DistanceRange
---------------------


:Type: :ref:`Enumerated <type-enumerated>`

:Options: ``''``, ``'5ft Range'``, ``'8ft Range'``, ``'By Zone'``

:Default: ``""``

.. _param-endperiod:

EndPeriod
---------------------


:Type: :ref:`Integer <type-integer>`

:Default: ``"10"``

.. _param-endrange:

EndRange
---------------------


:Type: :ref:`Integer <type-integer>`

:Default: ``"28800"``

.. _param-gameid:

GameID
---------------------


:Type: :ref:`Integer <type-integer>`


.. _param-gamescope:

GameScope
---------------------


:Type: :ref:`Enumerated <type-enumerated>`

:Options: ``''``, ``'Yesterday'``, ``'Last 10'``

:Default: ``""``

.. _param-gamesegment:

GameSegment
---------------------


:Type: :ref:`Enumerated <type-enumerated>`

:Options: ``''``, ``'First Half'``, ``'Second Half'``, ``'Overtime'``

:Default: ``""``

.. _param-groupquantity:

GroupQuantity
---------------------


:Type: :ref:`Integer <type-integer>`

:Default: ``"5"``

.. _param-isonlycurrentseason:

IsOnlyCurrentSeason
---------------------


:Type: :ref:`Boolean <type-boolean>`

:Default: ``"False"``

.. _param-lastngames:

LastNGames
---------------------


:Type: :ref:`Integer <type-integer>`

:Default: ``"0"``

.. _param-leagueid:

LeagueID
---------------------


:Type: :ref:`Enumerated <type-enumerated>`

:Options: ``'NBA'``, ``'NBADL'``, ``'WNBA'``

:Default: ``"NBA"``

.. _param-location:

Location
---------------------


:Type: :ref:`Enumerated <type-enumerated>`

:Options: ``''``, ``'Home'``, ``'Road'``

:Default: ``""``

.. _param-measuretype:

MeasureType
---------------------


:Type: :ref:`Enumerated <type-enumerated>`

:Options: ``'Base'``, ``'Advanced'``, ``'Misc'``, ``'Four Factors'``, ``'Scoring'``, ``'Opponent'``, ``'Usage'``

:Default: ``"Base"``

.. _param-month:

Month
---------------------


:Type: :ref:`Integer <type-integer>`

:Default: ``"0"``

.. _param-opponentteamid:

OpponentTeamID
---------------------


:Type: :ref:`Integer <type-integer>`

:Default: ``"0"``

.. _param-outcome:

Outcome
---------------------


:Type: :ref:`Enumerated <type-enumerated>`

:Options: ``''``, ``'W'``, ``'L'``

:Default: ``""``

.. _param-paceadjust:

PaceAdjust
---------------------


:Type: :ref:`Boolean <type-boolean>`

:Default: ``"False"``

.. _param-permode:

PerMode
---------------------
Whether returned stats should be given as totals, per game, per 36 minutes, etc. Some requests may not accept all values of this argument, however "Totals" and "PerGame" are always permitted.

:Type: :ref:`Enumerated <type-enumerated>`

:Options: ``'Totals'``, ``'PerGame'``, ``'MinutesPer'``, ``'Per48'``, ``'Per40'``, ``'Per36'``, ``'PerMinute'``, ``'PerPossession'``, ``'PerPlay'``, ``'Per100Possessions'``, ``'Per100Plays'``

:Default: ``"Totals"``

.. _param-period:

Period
---------------------


:Type: :ref:`Integer <type-integer>`

:Default: ``"0"``

.. _param-playerexperience:

PlayerExperience
---------------------


:Type: :ref:`Enumerated <type-enumerated>`

:Options: ``''``, ``'Rookie'``, ``'Sophomore'``, ``'Veteran'``

:Default: ``""``

.. _param-playerid:

PlayerID
---------------------


:Type: :ref:`Integer <type-integer>`


.. _param-playerposition:

PlayerPosition
---------------------


:Type: :ref:`Enumerated <type-enumerated>`

:Options: ``''``, ``'F'``, ``'C'``, ``'G'``, ``'C-F'``, ``'F-C'``, ``'F-G'``, ``'G-F'``

:Default: ``""``

.. _param-plusminus:

PlusMinus
---------------------


:Type: :ref:`Boolean <type-boolean>`

:Default: ``"False"``

.. _param-pointdiff:

PointDiff
---------------------


:Type: :ref:`Integer <type-integer>`

:Default: ``""``

.. _param-position:

Position
---------------------


:Type: :ref:`Enumerated <type-enumerated>`

:Options: ``''``, ``'Guard'``, ``'Center'``, ``'Forward'``

:Default: ``""``

.. _param-rangetype:

RangeType
---------------------


:Type: :ref:`Integer <type-integer>`

:Default: ``"2"``

.. _param-rank:

Rank
---------------------


:Type: :ref:`Boolean <type-boolean>`

:Default: ``"False"``

.. _param-rookieyear:

RookieYear
---------------------
(Guess) Include only players with the given rookie year?

:Type: :ref:`Season <type-season>`

:Default: ``""``

.. _param-scope:

Scope
---------------------


:Type: :ref:`Enumerated <type-enumerated>`

:Options: ``''``, ``'RS'``, ``'S'``, ``'Rookies'``

:Default: ``""``

.. _param-season:

Season
---------------------


:Type: :ref:`Season <type-season>`


.. _param-seasonid:

SeasonID
---------------------
From the perspective of the user this is the same as :ref:`Season <param-season>`, though it is handled differently internally.

:Type: :ref:`Season <type-season>`


.. _param-seasonsegment:

SeasonSegment
---------------------


:Type: :ref:`Enumerated <type-enumerated>`

:Options: ``''``, ``'Post All-Star'``, ``'Pre All-Star'``

:Default: ``""``

.. _param-seasontype:

SeasonType
---------------------
Some requests may not support pre-season.

:Type: :ref:`Enumerated <type-enumerated>`

:Options: ``'Regular Season'``, ``'Playoffs'``, ``'All Star'``, ``'Pre Season'``

:Default: ``"Regular Season"``

.. _param-seasonyear:

SeasonYear
---------------------
Same as :ref:`Season <param-season>`.

:Type: :ref:`Season <type-season>`


.. _param-startperiod:

StartPeriod
---------------------


:Type: :ref:`Integer <type-integer>`

:Default: ``"1"``

.. _param-startrange:

StartRange
---------------------


:Type: :ref:`Integer <type-integer>`

:Default: ``"0"``

.. _param-starterbench:

StarterBench
---------------------


:Type: :ref:`Enumerated <type-enumerated>`

:Options: ``''``, ``'Starters'``, ``'Bench'``

:Default: ``""``

.. _param-statcategory:

StatCategory
---------------------


:Type: :ref:`Enumerated <type-enumerated>`

:Options: ``'MIN'``, ``'FGM'``, ``'FGA'``, ``'FG_PCT'``, ``'FG3M'``, ``'FG3A'``, ``'FF3_PCT'``, ``'FTM'``, ``'FTA'``, ``'FT_PCT'``, ``'OREB'``, ``'DREB'``, ``'REB'``, ``'AST'``, ``'STL'``, ``'BLK'``, ``'TOV'``, ``'PTS'``, ``'EFF'``


.. _param-teamid:

TeamID
---------------------


:Type: :ref:`Integer <type-integer>`


.. _param-vsconference:

VsConference
---------------------


:Type: :ref:`Enumerated <type-enumerated>`

:Options: ``''``, ``'East'``, ``'West'``

:Default: ``""``

.. _param-vsdivision:

VsDivision
---------------------


:Type: :ref:`Enumerated <type-enumerated>`

:Options: ``''``, ``'Atlantic'``, ``'Central'``, ``'Northwest'``, ``'Pacific'``, ``'SouthEast'``, ``'SouthWest'``, ``'East'``, ``'West'``

:Default: ``""``

.. _param-year:

Year
---------------------


:Type: :ref:`Integer <type-integer>`


***************
Parameter Types
***************

.. _type-integer:

Integer
-------

Parameters of type Integer accept standard Python integers.

.. _type-boolean:

Boolean
-------

Parameters of type Enumerated accept standard Python boolean values ``True`` and
``False``.

.. _type-enumerated:

Enumerated
----------

Parameters of type Enumerated accept Python strings. Each parameter has a set
of string values that it allows as options, see documentation for the
particular parameter to see what those values are. Some enumerated parameters
allow empty strings; semantically this indicates that the parameter is left
unspecified.

.. _type-date:

Date
----

Parameters of type Date accept Python ``datetime.date`` objects.

.. _type-season:

Season
------

Parameters of type Season accept four digit integers (i.e., integers between
1000 and 9999). Values should correspond to the year that a season begins; for
example, the value 2008 indicates the 2008-2009 NBA season.
