package tcg;

/**
 * the ability that a given character card can have with a cost, power type and damage 
 */
public class Ability {
    protected String abilityName;
    protected String abilityPowerType;
    protected int abilityPowerStrength;
    protected int abilityDamage;

    /**
     * instatiates ability as a wildcard with 2 strength and 100 damage
     */
    public Ability() {
        abilityName = "WildCard";
        abilityPowerType = "ANY";
        abilityPowerStrength = 2;
        abilityDamage = 100;
    }

    /**
     * instantiates ability with specific specificiations
     * @param n_abil_name of the ability
     * @param n_abil_pow_typ that the ability requires 
     * @param n_abil_pow_str that the ability requires to be used
     * @param n_abil_dmg of the ability 
     * @throws IllegalArgumentException if the damage or power strength are invalid numbers
     */
    public Ability(String n_abil_name, String n_abil_pow_typ, int n_abil_pow_str, int n_abil_dmg) 
      throws IllegalArgumentException {
        if (n_abil_dmg <= 0 || n_abil_dmg > 200 || n_abil_dmg % 10 != 0 || 
            n_abil_pow_str <= 0 || n_abil_pow_str > 5) {
                throw new IllegalArgumentException();
        }
        abilityName = n_abil_name;
        abilityPowerType = n_abil_pow_typ;
        abilityPowerStrength = n_abil_pow_str;
        abilityDamage = n_abil_dmg;
    }

    public String getAbilityName() {
        return abilityName;
    }

    public String getAbilityPowerType() {
        return abilityPowerType;
    }

    public int getAbilityPowerStrength() {
        return abilityPowerStrength;
    }

    public int getAbilityDamage() {
        return abilityDamage;
    }
    
    /**
     * nerfs an ability by reducing its damage by 10, accounting for power strength required when damage goes less than 70
     * @return true if change was successful
     */
    public boolean nerf() {
        if (abilityDamage == 10) {
            return false;
        }
        else if (abilityDamage == 70) {
            if (abilityPowerStrength == 1) {
                return false;
            }
            else {
                abilityPowerStrength -= 1;
            }
        }
        abilityDamage -= 10;
        return true;
    }

    /**
     * buffs an ability by inreasing its damage by 10, accounting for power strength required when damage goes greater than 130
     * @return true if change was successful
     */
    public boolean buff() {
        if (abilityDamage == 200) {
            return false;
        }
        else if (abilityDamage == 130) {
            if (abilityPowerStrength == 5) {
                return false;
            }
            else {
                abilityPowerStrength += 1;
            }
        }
        abilityDamage += 10;
        return true;
    }

    /**
     * outputs relevant attributes as comma seperated list
     */
    @Override
    public String toString() {
        return (abilityName + "," + abilityPowerType + "," + abilityPowerStrength + "," + abilityDamage);
    }
} 
