# JSDChomp
## intro
It's a two-player perfect game.
You must think the strategy to win this game. Without any fortunate.
Additionally, it is impossible to draw.

## inventer info:
Invented by myself.
English name: Huang Jay
GitHub name: 40843245 (same as the author's GitHub name)

## Why I name it as JSDChomp?
I name it with acronym.
JSDChomp = Jay + Single Direction + Chomp

## Rule:
1. With 2 player.
2. Select board size first.
3. One who eat poisoned block will die and lose this game.
4. In each turn, one must select a block and determine the direction.  
    
   If it is a valid selection, then eat the block. 
   Then according to the direction, pick the next block and eat it until there are NO block one can pick with the specified direction.
   
   If it is NOT a valid selection, reselect it.
5. Extra eat rule:
   To compensate the advantage of first player. 
   2's player can determine to execute the Extra eat rule only after 2's player first valid selection at first round and before second round.

## NOTE to Extra eat rule:

2's player can NOT determine to execute the Extra eat rule then select a block for 2's player turn.
2's player must select a valid block and direction, eat it. Then to determine to execute it.
2's player can NOT regret the decision. 
(For example, it is NOT allowed that 2's player DON'T execute the Extra eat rule and during selection in second round in 2's player, he or she said that he or she want to execute the rule.)

## NOTE:
1. Here, a valid selection refers the block has NOT been eaten yet and it's NOT out of bound of the board (according to board size).
2. It is impossible to draw.

## Code
I will place Python code in GitHub.

## NOTE about code:
1. The index is start at 0.
2. The coordinate is same as the game JChomp which was also published in GitHub.

## Restriction to code:
1. The row of board size must be an integer between 8 and 30, and so is the column of board size.
2. The number of poisoned block must be an integer bewteen 1 and 3.

## Release NOTE:
I plan to place first version in GitHub at 2023/01/18 15:20p.m.
