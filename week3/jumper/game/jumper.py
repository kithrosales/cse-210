class Jumper:

    def __init__(self) -> None:
        self.parachute = None

    def cut_line(self):
        """ Remove the first line """
        self.parachute = self.parachute[1:]

    def init_parachute(self):
        """ Initialize the parachute """
        self.parachute = [
            "   ___",
            "  /___\\",
            "  \   /",
            "   \ /",
            "    0",
            "   /|\\",
            "   / \\"
        ]
    
    def draw_parachute(self):
        """ Draw a parachute """
        for parachute in self.parachute:
            print(parachute)