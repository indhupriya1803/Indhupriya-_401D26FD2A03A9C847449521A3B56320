class Player:
  def play(self):
    print("the player is playing cricket ")
class Batsman(Player):
  def play(self):
    print("Batsman  is bating")
class Bowler(Player):
  def play(self):
    print("The Bowler is bowling")
batsman=Batsman()
bowler=Bowler()
batsman.play()
bowler.play()