# battleship
partial implementation of the battleship board game

I decided to go with three classes: Board, Ship, and BattleShip.

Board implements the behavior of the board, focusing specifically on the fact
that you need to add marks on a grid of a certain size (specified on creation).
This class also takes care of the very troublesome translation between
gameboard positions (A1, F3, ...) to (x, y) coordinates (e.g. (0, 0)...).

Ship enables you to create ships according to various classes. Information
about the ship is retained. Technically, you could do without all of this and
could put that information in the board, but that would make for very poor
OOP design, in my opinion.

BattleShip basically implements the game itself (except that a Player class
has not yet been created ... it should be!). This class enables you to do
such things as adding a ship onto the board, or firing a missile.
