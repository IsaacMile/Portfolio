package tcg;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Stack;
import java.util.List;

/**
 * deck of abstract cards, can be any number of types of cards within restrictions of constants
 */
public class CardDeck implements ICardDeck{
    final int MAX_DECK_SIZE = 18;
    final int MIN_CHARACTER_CARDS = 1;
    final int MAX_EPIC_CARDS = 3;
    final int MAX_CARD_COPIES = 3;

    Stack<AbstractCard> cards;

    /**
     * instantiates a card deck with 3 lists of power, character and effect cards
     * @param powerCards to be added to the deck
     * @param characterCards to be added to the deck
     * @param effectCards to be added to the deck
     * @throws IllegalArgumentException if the resulting deck violates any rules of the game 
     */
    public CardDeck(PowerCard[] powerCards, CharacterCard[] characterCards, 
                    EffectCard[] effectCards) throws IllegalArgumentException{
        int num_cards = powerCards.length + characterCards.length + effectCards.length;
        if (num_cards > MAX_DECK_SIZE) {
            throw new IllegalArgumentException();
        }
        if (characterCards.length < MIN_CHARACTER_CARDS) {
            throw new IllegalArgumentException();
        }

        ArrayList<AbstractCard> card_list = new ArrayList<AbstractCard>(num_cards);
        int epic_cards = 0;
        HashMap<String, Integer> repeated = new HashMap<String, Integer>();
        for (PowerCard card : powerCards) {
            if (card.getCardRarity() == Rarity.EPIC) {
                epic_cards++;
            }
            if (repeated.get(card.getCardName()) != null) {
                repeated.put(card.getCardName(), repeated.get(card.getCardName()) + 1);
                if (repeated.get(card.getCardName()) > MAX_CARD_COPIES) {
                    throw new IllegalArgumentException();
                }
            }
            else {
                repeated.put(card.getCardName(), 1);
            }
            
            card_list.add(card);
        }
        repeated.clear();
        for (EffectCard card : effectCards) {
            if (card.getCardRarity() == Rarity.EPIC) {
                epic_cards++;
            }  
            if (repeated.get(card.getCardName()) != null) {
                repeated.put(card.getCardName(), repeated.get(card.getCardName()) + 1);
                if (repeated.get(card.getCardName()) > MAX_CARD_COPIES) {
                    throw new IllegalArgumentException();
                }
            }
            else {
                repeated.put(card.getCardName(), 1);
            }
            card_list.add(card);
        }
        repeated.clear();
        for (CharacterCard card : characterCards) {
            if (card.getCardRarity() == Rarity.EPIC) {
                epic_cards++;
            }            
            if (repeated.get(card.getCardName()) != null) {
                repeated.put(card.getCardName(), repeated.get(card.getCardName()) + 1);
                if (repeated.get(card.getCardName()) > MAX_CARD_COPIES) {
                    throw new IllegalArgumentException();
                }
            }
            else {
                repeated.put(card.getCardName(), 1);
            }
            card_list.add(card);
        }
        if (epic_cards > MAX_EPIC_CARDS) {
            throw new IllegalArgumentException();
        }

        cards = new Stack<AbstractCard>();
        for (int count = 0; count < num_cards; count++) {
            int random_card = (int) (Math.random() * card_list.size());
            cards.push(card_list.get(random_card));
            card_list.remove(random_card);
        }
    }

    @Override
    public void insertCard(AbstractCard card) {
        cards.add((int) (Math.random() * cards.size()), card);
    }
    
    @Override
    public AbstractCard drawCard() {
        if (isEmpty()) {
            return null;
        }
        return cards.pop();
    }

    @Override
    public List<AbstractCard> drawThree() {
        AbstractCard[] ret_lst = {cards.pop(), cards.pop(), cards.pop()};
        return Arrays.asList(ret_lst);
    }

    @Override
    public int getDeckSize() {
        return cards.size();
    }

    @Override 
    public boolean isEmpty() {
        return (cards.size() == 0);
    }
}
