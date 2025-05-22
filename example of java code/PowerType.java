package tcg;

/**
 * stores all types that can be strong or weak against each other
 */
public enum PowerType {
    BALANCED("Balanced", 0),
    BUILDER("Builder", 1),
    EXPLORER("Explorer", 2),
    FARMER("Farmer", 3),
    PVP("PvP", 4),
    REDSTONE("Redstone", 5);

    public final String label;
    public final int value;

    private PowerType(String n_label, int n_val) {
        label = n_label;
        value = n_val;
    }

    public String getLabel() {
        return label;
    }

    public int getValue() {
        return value;
    }


}
