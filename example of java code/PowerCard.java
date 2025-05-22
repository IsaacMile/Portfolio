package tcg;

/**
 * defines a card that is attached to character card to allow the use of abilities
 */
public class PowerCard extends AbstractCard{
    int cardPowerStrength;

    public PowerCard(String n_card_name, int n_card_pow_str) throws IllegalArgumentException{
        if (n_card_pow_str < 1 || n_card_pow_str > 5) {
            throw new IllegalArgumentException();
        }
        setCardName(n_card_name);
        cardPowerStrength = n_card_pow_str;
        cardType = CardType.POWER;
        calculateRarity();
        AbstractCard.cardCount++;
    }

    @Override
    protected void calculateRarity() {
        if (cardPowerStrength == 1) {
            cardRarity = Rarity.COMMON;
        }
        else if (cardPowerStrength == 4) {
            cardRarity = Rarity.RARE;
        }
        else if (cardPowerStrength == 5) {
            cardRarity = Rarity.EPIC;
        }
        else { //if cardPowerStrength == 2 or 3
            cardRarity = Rarity.UNCOMMON;
        }
    }

    public int getCardPowerStrength() {
        return cardPowerStrength;
    }

    @Override
    public String toString() {
        return (super.toString() + "," + getCardPowerStrength());
    }

    public static void main(String[] args) {
        
    }
}
