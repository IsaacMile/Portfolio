package tcg;
import java.util.List;

/**
 * interface for a deck of cards 
 */
public interface ICardDeck {

    /**
     * adds a card into the deck
     * @param card to be added
     */
    public void insertCard(AbstractCard card);

    /**
     * draws a card from the deck
     * @return card drawn
     */
    public AbstractCard drawCard();

    public List<AbstractCard> drawThree();

    public int getDeckSize();

    public boolean isEmpty();
}
