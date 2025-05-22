package tcg;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;

/**
 * class defines a table of non-symetrical weaknesses and strengths of various PowerTypes 
 */
public class PowerAdjustment {
    protected HashMap<PowerType, ArrayList<HashSet<PowerType>>> adjustment;
    public final int BUFF = 20;
    public final int NERF = -20;

    public PowerAdjustment() {
        adjustment = new HashMap<PowerType, ArrayList<HashSet<PowerType>>>();
    }

    public boolean addType(PowerType type1, PowerType type2, boolean isStrong) {
        if (adjustment.get(type1) == null) {
            ArrayList<HashSet<PowerType>> n_list = new ArrayList<HashSet<PowerType>>(2);
            n_list.add(new HashSet<PowerType>());
            n_list.add(new HashSet<PowerType>());
            adjustment.put(type1, n_list);
        } 
        boolean ret_bool;           
        ArrayList<HashSet<PowerType>> add_lst = adjustment.get(type1);
        if (isStrong) {
            ret_bool = add_lst.get(0).add(type2);
            adjustment.put(type1, add_lst);
        }
        else {
            ret_bool = add_lst.get(1).add(type2);
            adjustment.put(type1, add_lst);
        }
        return ret_bool;
    }

    public Set<PowerType> strongAgainst(PowerType type) {
        if (adjustment.get(type) == null) {
            return null;
        }
        return adjustment.get(type).get(0);
    }

    public Set<PowerType> weakAgainst(PowerType type) {
        if (adjustment.get(type) == null) {
            return null;
        }
        return adjustment.get(type).get(1);
    }

    public int getAdjustment (PowerType type1, PowerType type2) {
        if (adjustment.get(type1) == null) {
            return 0;
        }
        if (adjustment.get(type1).get(0) != null && adjustment.get(type1).get(0).contains(type2)) {
            return BUFF;
        }
        if (adjustment.get(type1).get(1) != null && adjustment.get(type1).get(1).contains(type2)) {
            return NERF;
        }
        return 0;
    }
}
