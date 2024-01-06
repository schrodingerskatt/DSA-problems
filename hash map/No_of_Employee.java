import java.util.*;
public class No_of_Employee {

public static void findCEO(HashMap<String, String>mp){
    String ceo = "";
    HashSet<String>employees = new HashSet<>(mp.keySet());

    for(String emp: employees){

        String manager = mp.get(emp);

        if(manager.equals(emp)){
            ceo = emp;
        }else{
            if(mp.containsKey(manager)){
                HashSet<String>manager_employees = mp.get(manager);
            }
        }
    }



}






public static void main(String args[]){
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();

    HashMap<String,String>map = new HashMap<>();
    for(int i = 0; i < n; i++){
        map.put(sc.next(),sc.next());
    }
    findCount(map);
}
    
}
