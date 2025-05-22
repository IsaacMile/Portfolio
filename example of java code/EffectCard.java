package tcg;

/**
 * effects cards are used to have an effect on rules of cards during play for a specific number of turns, played onto a character card
 */
public class EffectCard extends AbstractCard{
    String cardInstructions;
    int cardTurnCount;
    boolean cardCoinToss;

    public EffectCard(String n_card_name, String n_card_instr, int n_card_trn_cnt, 
                      boolean n_card_coin_tss) throws IllegalArgumentException {
        if (n_card_trn_cnt < 0 || n_card_trn_cnt > 3) {
            throw new IllegalArgumentException();
        }
        setCardName(n_card_name);
        cardInstructions = n_card_instr;
        cardTurnCount = n_card_trn_cnt;
        cardCoinToss = n_card_coin_tss;
        cardType = CardType.EFFECT;
        calculateRarity();
        AbstractCard.cardCount++;
    }

    @Override
    protected void calculateRarity() {
        if (cardTurnCount == 1) {
            cardRarity = Rarity.COMMON;
        }
        else if (cardTurnCount == 2 || (cardTurnCount == 3 && cardCoinToss)) {
            cardRarity = Rarity.UNCOMMON;
        }
        else if (cardTurnCount == 3) { //and !cardCoinToss implied by else
            cardRarity = Rarity.RARE;
        }
        else { //cardTurnCount == 0
            cardRarity = Rarity.EPIC;
        }
    }

    public String getCardInstructions() {
        return cardInstructions;
    }

    public int getCardTurnCount() {
        return cardTurnCount;
    }

    public boolean getCardCoinToss() {
        return cardCoinToss;
    }

    @Override
    public String toString() {
        return (super.toString() + "," + getCardInstructions() + "," + getCardTurnCount() + "," + 
                getCardCoinToss());
    }
}
