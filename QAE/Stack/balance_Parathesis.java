
import java.util.*;

class balance_Parathesis{
    
    public static void main(String[] args) throws Exception {
        String[] inpArr = { "({[]})", "()[]{}", "([)]", "", null, "(){", "()[{}]"};

        for(String inp : inpArr)
            System.out.println(isValid_Paranthesis(inp));
        
    }
    
    /*
     * approach:
     * use a stack to store all the open braces 
     * when you see a close brace pop the stack and compare if its a matching brace or not 
     * if not return false else continue 
     * wend 
     * if stack is empty then return true else false
     */   

     public static boolean isValid_Paranthesis (String str){
        // O(n) || O(n)
        if (str == null || str.length() == 0) return false;

        Map<Character,Character> map = new HashMap<>();
        map.put('(',')');
        map.put('{','}');
        map.put('[',']');

        Stack<Character> s = new Stack<>();

        for( char c : str.toCharArray()){

        if (map.containsKey(c)) s.push(c);

        else if (s.isEmpty() || c != map.get(s.pop())) return false;

        }

        return s.isEmpty();
    }

}


