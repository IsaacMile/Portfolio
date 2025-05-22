package tcg;

/**
 * abstract class that defines basic card without specifying type of card
 */
public abstract class AbstractCard {
    String cardName;
    CardType cardType;
    Rarity cardRarity;
    static int cardCount;

    public String getCardName() {
        return cardName;
    }

    public CardType getCardType() {
        return cardType;
    }

    public Rarity getCardRarity() {
        return cardRarity;
    }

    public int getCardCount() {
        return cardCount;
    }

    public void setCardName(String n_card_name) {
        cardName = n_card_name;
    }

    /**
     * uses the values of the card to calculate what rarity it should be, 
     * calculation changes based on type of card
     */
    protected abstract void calculateRarity();

    @Override
    public String toString() {
        return (getCardType() + "," + getCardName() + "," + getCardRarity());
    }

    /**
     * tests if card equals another card by just checking name
     * @param card2 being tested against
     * @return true if they are equal
     */
    public boolean equals(AbstractCard card2) {
        return this.getCardName() == card2.getCardName();
    }
}
