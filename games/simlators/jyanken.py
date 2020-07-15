from .interface import SimulatorInterface


class Jyanken(SimulatorInterface):
    def __init__(self):
        self.playercap = 2
        super().__init__("janken", self.playercap)
        self.players = list()

    # override
    def add_player(self, user):
        pass

    # override
    def start_game(self):
        pass

    # override
    def next_turn(self):
        pass

    # override
    def get_action_types(self):
        return ["gu", "tyoki", "pa"]

    # override
    def action(self, action, pname):
        pass

    # override
    def get_info(self):
        pass

