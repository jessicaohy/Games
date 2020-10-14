-- Jessica Oh Hui Yu 29886465
-- FIT2102 Assignment 2

-- FILE-LEVEL DOC
{-|
    Firstly, if the player has Club Two in his/her cards, the player will be the one who starts the game and play Club Two. 
    Since it is the first card of the game and not a Heart, it will save False in the memory, which tells whether Heart cards have been played.

    Secondly, if the trick is empty, it means that the player is the first player for the round.
    If the player does not have any cards that are not Heart in his/her cards, it means he/she has no other choice but to start the round with a Heart card,
    then a list of all his/her cards will be returned.
    If not, if the memory stored is True, it means a Heart card has been played before and the player can start with any of his/her cards,
    then a list of all his/her cards will also be returned.
    Else, it means that nobody played a Heart card yet and the player has to play a card that is not Heart. 
    A list of cards containing no Heart card will be returned. 

    Thirdly, if the trick is not empty, it means that the player is not the first player for the round.
    Get the last trick and check what is the suit that the first player played.
    If the player has cards of the same suit as the suit the first player played, then the player has to play the same suit as the first player.
    
    The first heuristic is to throw Spade Queen card when someone played a Spade King or Ace so that half of the points will be given to the other player.
    If the first player played a Spade, if the non-first player have a Spade Queen card, check the trick for Spade Ace or Spade King.
    If the trick has a Spade Ace or Spade King, it means someone played a card that is higher than Spade Queen card. 
    This means that if the player throws the Spade Queen card, he/she does not have to be the one getting the points.
    A list containing Queen Spade card will be returned.

    If not, a list containing cards of the same suit as the first player will be returned.

    The second heuristic is to check is to throw the highest point card when the player does not have card of the same suit as the first player.
    Throwing the highest point card will increase his/her chance of not getting points if he/she has to play point cards in the future rounds.
    Get the last trick and if the first player played Club Two card, it means that it is the first round of the game.
    If the player does not have any cards that have no points, then he/she has no choice but to play a point card.
    Since the player does not have the same suit as the first person, regardless of the card he/she plays, he/she will not have to take any points.
    This is a good opportunity to throw the point cards.
    The player's cards will be sorted using quick sort and the card at the end of the list will be the highest point card.
    A list containing the highest point card will be returned.

    If not, a list containing cards that have no points will be returned.

    If it is not the first round, the player can play point cards and a list containing the highest Heart card will also be returned.

    Else, a list containing all the player's cards will be returned.

    Lastly, all these lists that are returned are valid cards that can be played. The first card of the list will be played.
    The memory will be updated.
    If the memory is True, it means that Heart cards have been played and the memory stays as True.
    Else, it will check through the history, the part containing what all the players played for the round and check whether Heart card has been played.
    If Heart card has been played, memory will be updated to True, else it will stay as False.

    A tuple containing the card the player play and the updated memory will be returned.

-}


-- | Write a report describing your design and strategy here.
module Player (
    playCard,
    makeBid
)
where

-- You can add more imports as you need them.
import Hearts.Types

import Cards

-- CHECK HAND IF THRE IS CLUB OF 2  
has_two_clubs :: [Card] -> Bool
has_two_clubs cards = elem (Card Club Two) cards                                    -- checks if cards has Card Club Two. if yes, return True, else False
----------------------------------------------------
-- NOT FIRST PLAYER

-- get first player suit
getFirstPlayerSuit :: [(Card, PlayerId)] -> Suit
getFirstPlayerSuit trick = getSuit firstPlayerTrick
    where 
        firstPlayerTrick = last trick                                               -- last trick contains what first player played
        getSuit ((Card suit _), _) = suit                                           -- return suit

-- check if suit of the cards is the same as the target suit
checkSuit :: Suit -> Card -> Bool
checkSuit targetSuit (Card suit _) = if suit == targetSuit then True else False     -- if suit is the same as target suit then True else False

-- get first player card
getFirstPlayerCard :: [(Card, PlayerId)] -> Card
getFirstPlayerCard trick = getCard firstPlayerTrick
    where 
        firstPlayerTrick = last trick                                               -- last trick contains what first player played
        getCard (card, _) = card                                                    -- return card

-- check if card is the same as the target suit
checkCard :: Card -> Card -> Bool
checkCard targetCard card = if card == targetCard then True else False              -- if card is the same as target card then True else False

-- FIRST PLAYER

-- get memory out to check if Hearts have been played
getWhetherPlayedPoints :: Maybe ([(Card, PlayerId)], String) -> String
getWhetherPlayedPoints Nothing = "False"
getWhetherPlayedPoints (Just (_, memory)) = memory                                  -- return memory containing "True" or "False" whether Heart cards have been played

-- check that card has NO point
checkNoPoints :: Card -> Bool
checkNoPoints (Card suit num) = if suit == Heart || (suit == Spade && num == Queen) then False else True    -- if is NOT point cards return True else False

-- check that card has point
hasPoints :: Card -> Bool
hasPoints (Card suit num) = if suit == Heart || (suit == Spade && num == Queen) then True else False        -- if is point card, return True else False

-- check that card is not a Heart
checkNoHearts :: Card -> Bool
checkNoHearts (Card suit _) = if suit == Heart then False else True                                         -- if suit of card is not Heart then True else False


-- if player is the FIRST PLAYER IN THE ROUND
isFirstPlayer :: [Card] -> [(Card, PlayerId)] -> Maybe ([(Card, PlayerId)], String) -> [Card]
isFirstPlayer cards _ history
    |filter checkNoHearts cards == [] = cards                                       -- hands are all hearts, return all cards
    |getWhetherPlayedPoints history == "True" = cards                               -- if hearts played, return all cards
    |otherwise = filter checkNoHearts cards                                         -- if hearts not played, return cards that are not Heart

-- if player is NOT THE FIRST PLAYER IN THE ROUND
isNotFirstPlayer :: [Card] -> [(Card, PlayerId)] -> Maybe ([(Card, PlayerId)], String) -> [Card]
isNotFirstPlayer cards trick _
    |filter (checkSuit (getFirstPlayerSuit trick)) cards /= [] = 
        if ((getFirstPlayerSuit trick) == Spade) && ((filter (checkCard (Card Spade Queen)) cards) /= []) && (trickHasKingAceSpade trick == True) then [(Card Spade Queen)]
        else filter (checkSuit (getFirstPlayerSuit trick)) cards                                                    -- check if can follow first player
    |checkCard (getFirstPlayerCard trick) (Card Club Two) == True =                                                 -- if is first round
        if filter checkNoPoints cards == [] then [highestPointCard cards] else filter checkNoPoints cards           -- check if hands are all points anot
    |filter hasPoints cards /= [] = [highestPointCard (filter hasPoints cards)]                                     -- not first round
    |otherwise = cards                                                                                              -- dont have first player card and not first round, can throw anything

------------------------------------------------------
-- UPDATE MEMORY (stores whether Heart cards have been played)

updateMemory :: Maybe ([(Card, PlayerId)], String) -> String
updateMemory Nothing = "False"
updateMemory (Just (prevRound, memory))
    |memory == "True" = "True"                                  -- if hearts cards have been played, dont have to check again
    |otherwise = checkPrevRound prevRound                       -- hearts cards have not been played, check most recent round
    where
        checkPrevRound [] = "False"                                                                         -- base
        checkPrevRound (((Card suit _), _):xs) = if suit == Heart then "True" else checkPrevRound xs        -- recursion

--------------------------------------------------
-- HEURISTIC APPROACH

-- Heuristic:
-- if someone played a card and i dont have the suit, play the highest point card
-- return highest point card out of all point cards
-- hearts or spade
highestPointCard :: [Card] -> Card
highestPointCard pointCardsList
    |hasSpadeQueen pointCardsList == True = (Card Spade Queen)          -- highest = spade queen
    |otherwise = highestHeartCard pointCardsList                        -- find highest Heart card
    -- highest heart card

-- check if there is Spade Queen card in the cards
hasSpadeQueen :: [Card] -> Bool
hasSpadeQueen [] = False                                                -- base. checked thru everything no queen spade
hasSpadeQueen ((Card suit num):xs)
    |suit == Spade && num == Queen = True                               -- has spade queen
    |otherwise = hasSpadeQueen xs                                       -- recursion

-- get the highest Heart card
highestHeartCard :: [Card] -> Card
highestHeartCard heartCardsList = last (sort heartCardsList)            -- last card of the sorted list is the highest card

-- Sort list using Quick Sort (Lecture 6)
sort :: Ord a => [a] -> [a]
sort [] = []                                                            -- base
sort (pivot:rest) = lesser ++ [pivot] ++ greater
  where
    lesser = sort (filter (<pivot) rest)                                -- recursion
    greater = sort (filter (>=pivot) rest)                              -- recursion

-- Heuristic:
-- if someone throw king or ace spade, throw queen of spade

-- first player start with spade
-- check trick if anyone threw king or ace of spades
-- if have then player throw queen of spade
trickHasKingAceSpade :: [(Card, PlayerId)] -> Bool
trickHasKingAceSpade [] = False                                         -- base. check thru the list, no king or ace spade
trickHasKingAceSpade (((Card suit num),_):xs)
    |suit == Spade && (num == King || num == Ace) = True                -- has king or ace spade
    |otherwise = trickHasKingAceSpade xs                                -- recursion


-- =================================================== --
-- returns a tuple (card player throws, updated memory)
-- memory stores True or False whether Heart card has been played
playCard :: PlayFunc
playCard _ cards trick history
    |has_two_clubs cards == True = ((Card Club Two), "False")                           -- clubs of 2 has to play it first
    |trick == [] = ((isFirstPlayer cards trick history)!!0, updateMemory history)       -- first player of the round
    |otherwise = ((isNotFirstPlayer cards trick history)!!0, updateMemory history)      -- not the first player of the round


    -- error "You need to implement the playCard function."



-- | Not used, do not remove.
makeBid :: BidFunc
makeBid = undefined
