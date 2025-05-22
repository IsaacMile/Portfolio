package tcg;
import java.util.Arrays;
import java.util.List; 

/**
 * central cards of the game, other cards add onto character cards to increase or allow abilities to defeat opponents 
 * character cards
 */
public class CharacterCard extends AbstractCard{
    int cardHealth;
    String cardPowerType;
    List<Ability> cardAbilities;

    public CharacterCard(String n_card_name, String n_card_pow_typ, int n_card_health, 
                         Ability[] n_card_abils) 
                         throws IllegalArgumentException, IncompatiblePowerException {
        if (n_card_health < 120 || n_card_health > 400 || n_card_health % 10 != 0 || 
            n_card_abils.length != 2) {
                throw new IllegalArgumentException();
        }

        for (Ability abil : n_card_abils) {
            if (abil.getAbilityPowerType() != n_card_pow_typ && 
                abil.getAbilityPowerType() != "ANY") {
                    throw new IncompatiblePowerException(
                        ("CharacterCard: Ability " 
                        + abil.getAbilityName() + 
                        " does not match power type"), 
                        abil.getAbilityPowerType(), n_card_pow_typ);
            }
        }
        setCardName(n_card_name);
        cardType = CardType.CHARACTER;
        cardHealth = n_card_health;
        cardPowerType = n_card_pow_typ;
        cardAbilities = Arrays.asList(n_card_abils);
        calculateRarity();
        AbstractCard.cardCount++;
    }

    @Override
    protected void calculateRarity() {
        int cmbin_dmg = 0;
        boolean any_abil = false;
        for (Ability abil : cardAbilities) {
            cmbin_dmg += abil.getAbilityDamage();
            if (abil.getAbilityPowerType() == "ANY") {
                any_abil = true;
            }
        }
        if (cardHealth <= 200 && cmbin_dmg <= 100 && !any_abil) {
            cardRarity = Rarity.COMMON;
        }
        else if (cardHealth <= 200 && cmbin_dmg <= 200 && !any_abil) {
            cardRarity = Rarity.UNCOMMON;
        }
        else if (cmbin_dmg <= 300) {
            cardRarity = Rarity.RARE;
        }
        else if (cardHealth >= 220) {
            cardRarity = Rarity.EPIC;
        }
        else {
            cardRarity = Rarity.COMMON;
        }
    }

    public String getCardPowerType() {
        return cardPowerType;
    }

    public int getCardHealth() {
        return cardHealth;
    }

    public int getAbilityDamage(int position) throws IllegalArgumentException{
        if (position < 0 || position > 1) {
            throw new IllegalArgumentException();
        }
        return cardAbilities.get(position).abilityDamage;
    }

    public int getAbilityPowerStrength(int position) throws IllegalArgumentException{
        if (position < 0 || position > 1) {
            throw new IllegalArgumentException();
        }
        return cardAbilities.get(position).abilityPowerStrength;
    }

    @Override
    public String toString() {
        return (super.toString() + "," + cardHealth + "," + cardPowerType + "," + 
                cardAbilities.get(0) + "," + cardAbilities.get(1));
    }
}
