# JCromp

## preface
Have you heard this puzzle? Chomp
If you have not heard about it.
I recommend you to visit the link in Chromp section and understand its rule before reading this article.

## Chomp
https://en.wikipedia.org/wiki/Chomp

# info:
## about inventor:
Invented by myself.
English name: Huang Jay
GitHub name: 40843245 (same as this author)

# intro
This named was invented by myself.
This game is a variant of Chomp, a funny puzzle.
Why did I call it JChomp?
The reason was very simple. 
My English name is Huang Jay.
I combined the first letter of my english name and the word "Chomp".
The rule is very simple.

# Rule
## intro to Chomp:
The Chomp is a puzzle with 2 player.
Given n1 * n2 blocks of chocolate (To make it brief, I will call one block of chocolate as one block).
The top-left most block is poisoned. If one eats the block, one will die and lose this game.
One must select a block. Eat the selected block together with those that are below it and its right)
It is impossible to draw in Chomp.

## intro to JChromp:
1. With pl players.
2. Given n1 * n2 blocks of chocolate (To make it brief, I will call one block of chocolate as one block).
where there are P poison blocks P={(x1,y1),...,(xp,yp)}

3. One must select a block.If possible, we call it is a valid selection,
eat the selected block together with those who are below it within e1 rows and right it within e2 columns.
If NOT possible, then we call it is invalid selection,
reselect a block (the selected block together with those will NOT be eaten).

4. One who eat one or many poison blocks will lose the game.

5. If there are NO any valid selections, the game ties.

## NOTE
NOTE that

1. For existence of the block,
We call the block DOES exist iff the block is NOT out of bound of the board and it has NOT been eaten.

2. For the term eaten size,
it refers the size one must eat after a valid selection.
For example,
If the eaten size is (2,3), one must eat consecutive 2 rows with 3 columns blocks once one select with validity.

3. For definition of a valid selection, 
a valid selection for the block at point (x,y) refers the continuous blocks those are below within e1 rows 
and are right e2 columns are BOTH exist (See the NOTE 1st point).
For more details, see my examples in my note (.docx file)

4. Pay a lot of attetntion of directions and coordinations.
From up to down, the row and x-axis value are changed. When x-axis value increase 1 unit, the next row are increased by 1.
From left to right, the col and y-axis value are changed. When y-axis value increase 1 unit, the next column are increased by 1.
It is applied here and in my code.

5. In my code, 
out of range are checked first, then blocks had been eaten, then poisoned blocks are eaten.

out of range > blocks had been eaten > poisoned blocks are eaten

For more details, see my figures in my note (.docx file)

## code
The Python will be place in GitHub.

## Restriction to the code:
1. There are at least 2 players and at most 4 players.
2. The row of board size can be an integer from 4 to 15, and so is the column of board size.
3. The row of eaten size can be an integer from 1 to  3, and so is the column of eaten size.
4. The number of poisoned block must be between 1 and "min(4, the row of board size * the column of board size)".
5. The position of poisoned block must NOT be out of bound of the board.

# News
## Release NOTE
v2 : Chomp_Variant_v2(optimized) are put in GitHub in 2023/01/17 20:58 p.m.
