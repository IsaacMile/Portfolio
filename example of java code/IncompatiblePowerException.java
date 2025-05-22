package tcg;

/**
 * if a card is given with a ability power type different to one of its abilities, causing an error in the game
 */
public class IncompatiblePowerException extends Exception{
    String power1;
    String power2; 

    public IncompatiblePowerException(String n_msg, String n_pow1, String n_pow2) {
        super(n_msg);
        power1 = n_pow1;
        power2 = n_pow2;
    }

    @Override
    public String toString() {
        return (getMessage() + "," + power1 + "," + power2);
    }
}
