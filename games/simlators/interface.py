

# シミュレータのインターフェース
class SimulatorInterface():
    def __init__(self, name, playercap):
        self.name = name
        self.playercap = playercap

    # プレイヤー追加
    def add_player(self, name):
        pass

    # ゲームスタート
    def start_game(self):
        pass

    # 次のターン
    def next_turn(self):
        pass

    # 行動の種類を返す
    def get_action_types(self):
        pass

    # 行動
    def action(self, action, pname):
        pass

    # ゲーム情報を返す
    def get_info(self):
        pass

