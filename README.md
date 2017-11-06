# battleship
partial implementation of the battleship board game

I decided to go with three classes: Board, Ship, and BattleShip.

Board implements the behavior of the board, focusing specifically on the fact
that you need to add marks on a grid of a certain size (specified on creation).
This class also takes care of the very troublesome translation between
gameboard positions (A1, F3, ...) to (x, y) coordinates (e.g. (0, 0)...).
Board also lets you print out two different versions of the gameboard: one 
where the ships are hidden (as when you are guessing where your opponents are), 
and one where the ships are viewable (as when you have your own ships
in front of you and the opponent is calling missile shots).

Ship enables you to create ships according to various classes. Information
about the ship is retained. Technically, you could do without all of this and
could put that information in the board, but that would make for very poor
OOP design, in my opinion.

BattleShip basically implements the game itself (except that a Player class
has not yet been created ... it should be!). This class enables you to do
such things as adding a ship onto the board, or firing a missile.

There is also a suite of test modules based on the unittest paradigm.
Each test module corresponds to one of the above three classes.
