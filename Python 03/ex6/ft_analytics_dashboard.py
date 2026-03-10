#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_analytics_dashboard.py                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mahendri <mahendri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/06 11:36:14 by mahendri            #+#    #+#            #
#   Updated: 2026/03/06 11:36:14 by mahendri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


class Player:
    def __init__(
        self,
        name: str = "",
        level: int = 0,
        sessions_played: list[dict] = [{}],
        favorite_mode: str = "",
        achievements_count: int = 0,
        region: str = ""
    ) -> None:
        self.__name: str = name
        self.__level: int = level
        self.__sessions_played: list[dict] = sessions_played
        if (sessions_played and sessions_played[0]):
            self.__sessions_played = self.set_session(sessions_played)
        self.__favorite_mode: str = favorite_mode
        self.__achievements_count: int = achievements_count
        self.__total_score: int = 0
        if self.get_total_score():
            self.__total_score = self.get_total_score()
        self.__region: str = region
        self.__is_logged: bool = True

    def login(self) -> None:
        self.__is_logged = True

    def logout(self) -> None:
        self.__is_logged = False

    def get_self(self) -> dict:
        player = {
            'name': self.__name,
            'level': self.__level,
            'sessions_played': self.__sessions_played,
            'favorite_mode': self.__favorite_mode,
            'achievements_count': self.__achievements_count,
            'total_score': self.__total_score,
            'region': self.__region,
            'is_logged': self.__is_logged
        }
        return player

    def set_session(self, sessions: list[dict]) -> list[dict]:
        player_sessions_count: int = sum(session['player'] == self.__name
                                         for session in sessions)
        player_sessions: list[dict] = [{}] * player_sessions_count
        index: int = 0
        for session in sessions:
            if session['player'] == self.__name:
                session_copy = session.copy()
                del session_copy['player']
                player_sessions[index] = session_copy
                index += 1
        return player_sessions

    def get_sessions(self) -> list[dict]:
        return self.__sessions_played

    def get_total_score(self) -> int:
        if not (self.__sessions_played and self.__sessions_played[0]):
            return 0
        total_score: int = 0
        for session in self.__sessions_played:
            total_score += session['score']
        return total_score

    def display(self) -> None:
        print(f"name:{self.__name} <level:{self.__level}>\n"
              f"total score: {self.__total_score}\n"
              f"sessions_played:{self.__sessions_played}\t"
              f"favorite_mode:{self.__favorite_mode}\t"
              f"achievements_count:{self.__achievements_count}\n")


def get_all_sessions(data: dict) -> list[dict]:
    return (data)['sessions']


def get_players(data: dict, sessions_data: list[dict]) -> list[Player]:
    players_datas: dict = data['players']
    players: list[Player] = [Player()] * len(players_datas)
    index: int = 0
    for [key, data] in players_datas.items():
        players[index] = Player(
            key,
            data['level'],
            sessions_data,
            data['favorite_mode'],
            data['achievements_count'],
            data['region']
        )
        index += 1
    return players


class GameAnalytics:
    def __init__(self, data: dict, players: list[Player]) -> None:
        self.__data: dict = data
        self.__players: list[Player] = players

    @staticmethod
    def get_unique_achievements() -> set[str]:
        unique_achievements: set[str] = set()
        datas: list[str] = [
            'boss_slayer', 'collector', 'first_kill', 'level_10',
            'perfectionist', 'speed_demon', 'treasure_hunter'
        ]
        for data in datas:
            unique_achievements.add(data)
        return unique_achievements

    def get_data(self) -> dict:
        return self.__data

    def get_game_modes(self) -> set[str]:
        modes: set[str] = set()
        data_modes: dict = (self.__data)['game_modes']
        for mode in data_modes:
            modes.add(mode)
        return (modes)

    def list_comprehension(self) -> None:
        players: list[Player] = self.__players

        print("=== List Comprehension Examples ===")

        high_scored_players_count: int = (
            sum(player.get_self()['total_score'] > 2000
                for player in players)
        )
        high_scored_players: list[str] = [""] * high_scored_players_count
        index: int = 0
        for player in players:
            player_data: dict = player.get_self()
            if (player_data['total_score'] > 2000):
                high_scored_players[index] = player_data['name']
                index += 1
        print(f"High scorers (>2000): {high_scored_players}")

        score_doubled: list[int] = [0] * len(players)
        index = 0
        for player in players:
            player_data = player.get_self()
            score_doubled[index] = player_data['total_score'] * 2
            index += 1
        print(f"Scores doubled: {score_doubled}")

        active_players_count: int = (
            sum(player.get_self()['is_logged']
                for player in players)
        )
        active_players: list[Player] = [Player()] * active_players_count
        index = 0
        for player in players:
            player_data = player.get_self()
            if (player_data['is_logged']):
                active_players[index] = player_data['name']
                index += 1
        print(f"Active players: {active_players}")

    def dict_comprehension(self) -> None:
        players: list[Player] = self.__players

        print("=== Dict Comprehension Examples ===")

        players_scores: dict[str, int] = {}
        for player in players:
            player_data: dict = player.get_self()
            players_scores[player_data['name']] = player_data['total_score']
        print(f"Player scores: {players_scores}")

        score_categories: dict[str, int] = {}
        score_categories['high'] = 3
        score_categories['medium'] = 2
        score_categories['low'] = 1
        print(f"Score categories: {score_categories}")

        players_achievements_count: dict[str, int] = {}
        for player in players:
            player_data = player.get_self()
            players_achievements_count[player_data['name']] = (
                player_data['achievements_count']
            )
        print(f"Achievement counts: {players_achievements_count}")

    def set_comprehension(self) -> None:
        players: list[Player] = self.__players

        print("=== Dict Comprehension Examples ===")

        unique_players: set[str] = set()
        for player in players:
            player_data: dict = player.get_self()
            unique_players.add(player_data['name'])
        print(f"Unique players: {unique_players}")

        achievements: set[str] = self.get_unique_achievements()
        unique_achievements: set[str] = set()
        for achievement in achievements:
            unique_achievements.add(achievement)
        print(f"Unique achievements: {unique_achievements}")

        regions: list[str] = [player.get_self()['region']
                              for player in players]
        active_regions: set[str] = set()
        for region in regions:
            active_regions.add(region)
        print(f"Active regions: {active_regions}")

    def rank_players(self) -> list[dict[str, str | int]]:
        players: list[Player] = self.__players

        players_datas: list[dict[str, str | int]] = [{}] * len(players)
        index: int = 0
        for player in players:
            players_datas[index] = player.get_self()
            index += 1

        rank_players: list[dict[str, str | int]] = sorted(
            players_datas,
            key=lambda player: player['total_score'], reverse=True
        )
        rank_players = sorted(
            players_datas,
            key=lambda player: player['total_score'], reverse=True
        )
        return rank_players

    def combined_analysis(self) -> None:
        players: list[Player] = self.__players
        unique_achievements: set[str] = self.get_unique_achievements()

        print(f"Total players: {len(players)}")
        print(f"Total unique achievements: {len(unique_achievements)}")

        score_list: list[int] = [0] * len(players)
        index: int = 0
        for player in players:
            player_data: dict = player.get_self()
            score_list[index] = player_data['total_score']
            index += 1
        print(f"Average score: {(sum(score_list) / len(score_list)):.1f}")

        ranked_players: list[dict[str, str | int]] = self.rank_players()
        top_player: dict[str, str | int] = ranked_players[0]
        print(f"Top performer: {top_player['name']} "
              f"({top_player['total_score']} points, "
              f"{top_player['achievements_count']} achievements)")

    def run(self) -> None:
        print()
        print("=== Game Analytics Dashboard ===")

        print()
        self.list_comprehension()

        print()
        self.dict_comprehension()

        print()
        self.set_comprehension()

        print()
        self.combined_analysis()


if __name__ == "__main__":
    data: dict = {
        "players": {
            "alice": {
                "level": 41,
                "total_score": 2824,
                "sessions_played": 13,
                "favorite_mode": "ranked",
                "achievements_count": 5,
                "region": "central"
            },
            "bob": {
                "level": 16,
                "total_score": 4657,
                "sessions_played": 27,
                "favorite_mode": "ranked",
                "achievements_count": 2,
                "region": "central"
            },
            "charlie": {
                "level": 44,
                "total_score": 9935,
                "sessions_played": 21,
                "favorite_mode": "ranked",
                "achievements_count": 7,
                "region": "south"
            },
            "diana": {
                "level": 3,
                "total_score": 1488,
                "sessions_played": 21,
                "favorite_mode": "casual",
                "achievements_count": 4,
                "region": "east"
            },
            "eve": {
                "level": 33,
                "total_score": 1434,
                "sessions_played": 81,
                "favorite_mode": "casual",
                "achievements_count": 7,
                "region": "north"
            },
            "frank": {
                "level": 15,
                "total_score": 8359,
                "sessions_played": 85,
                "favorite_mode": "competitive",
                "achievements_count": 1,
                "region": "north"
            },
        },
        "sessions": [
            {
                "player": "bob",
                "duration_minutes": 94,
                "score": 1831,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "bob",
                "duration_minutes": 32,
                "score": 1478,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "diana",
                "duration_minutes": 17,
                "score": 1570,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "alice",
                "duration_minutes": 98,
                "score": 1981,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "diana",
                "duration_minutes": 15,
                "score": 2361,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "eve",
                "duration_minutes": 29,
                "score": 2985,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "frank",
                "duration_minutes": 34,
                "score": 1285,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "alice",
                "duration_minutes": 53,
                "score": 1238,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "bob",
                "duration_minutes": 52,
                "score": 1555,
                "mode": "casual",
                "completed": False,
            },
            {
                "player": "frank",
                "duration_minutes": 92,
                "score": 2754,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "eve",
                "duration_minutes": 98,
                "score": 1102,
                "mode": "casual",
                "completed": False,
            },
            {
                "player": "diana",
                "duration_minutes": 39,
                "score": 2721,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "frank",
                "duration_minutes": 46,
                "score": 329,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "charlie",
                "duration_minutes": 56,
                "score": 1196,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "eve",
                "duration_minutes": 117,
                "score": 1388,
                "mode": "casual",
                "completed": False,
            },
            {
                "player": "diana",
                "duration_minutes": 118,
                "score": 2733,
                "mode": "competitive",
                "completed": True,
            },
            {
                "player": "charlie",
                "duration_minutes": 22,
                "score": 1110,
                "mode": "ranked",
                "completed": False,
            },
            {
                "player": "frank",
                "duration_minutes": 79,
                "score": 1854,
                "mode": "ranked",
                "completed": False,
            },
            {
                "player": "charlie",
                "duration_minutes": 33,
                "score": 666,
                "mode": "ranked",
                "completed": False,
            },
            {
                "player": "alice",
                "duration_minutes": 101,
                "score": 292,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "frank",
                "duration_minutes": 25,
                "score": 2887,
                "mode": "competitive",
                "completed": True,
            },
            {
                "player": "diana",
                "duration_minutes": 53,
                "score": 2540,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "eve",
                "duration_minutes": 115,
                "score": 147,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "frank",
                "duration_minutes": 118,
                "score": 2299,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "alice",
                "duration_minutes": 42,
                "score": 1880,
                "mode": "casual",
                "completed": False,
            },
            {
                "player": "alice",
                "duration_minutes": 97,
                "score": 1178,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "eve",
                "duration_minutes": 18,
                "score": 2661,
                "mode": "competitive",
                "completed": True,
            },
            {
                "player": "bob",
                "duration_minutes": 52,
                "score": 761,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "eve",
                "duration_minutes": 46,
                "score": 2101,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "charlie",
                "duration_minutes": 117,
                "score": 1359,
                "mode": "casual",
                "completed": True,
            },
        ],
        "game_modes": ["casual", "competitive", "ranked"],
        "achievements": [
            "first_blood",
            "level_master",
            "speed_runner",
            "treasure_seeker",
            "boss_hunter",
            "pixel_perfect",
            "combo_king",
            "explorer",
        ],
    }

    all_sessions: list[dict] = get_all_sessions(data)
    players: list[Player] = get_players(data, all_sessions)

    game_analytics = GameAnalytics(data, players)
    game_analytics.run()
