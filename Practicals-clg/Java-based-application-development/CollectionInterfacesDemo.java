import java.util.*;
public class CollectionInterfacesDemo {
    public static void main(String[] args) {
        
        List<String> list = new ArrayList<>();
        list.add("Apple");
        list.add("Banana");
        list.add("Cherry");
        list.add(1, "Mango");
        System.out.println("\nList elements: " + list);
        System.out.println("Element at index 2: " + list.get(2));
        list.set(2, "Orange");
        System.out.println("List after modification: " + list);
        list.remove("Mango");
        System.out.println("List after removing 'Mango': " + list);
        System.out.println("Is 'Apple' in the list? " +
        list.contains("Apple"));
        System.out.println("Size of the list: " + list.size());

        Set<String> set = new HashSet<>();
        set.add("Dog");
        set.add("Cat");
        set.add("Bird");
        set.add("Cat");
        System.out.println("\nSet elements: " + set);
        set.remove("Bird");
        System.out.println("Set after removing 'Bird': " + set);
        System.out.println("Is 'Cat' in the set? " + set.contains("Cat"));
        System.out.println("Size of the set: " + set.size());
        
        Map<Integer, String> map = new HashMap<>();
        map.put(1, "John");
        map.put(2, "Jane");
        map.put(3, "Doe");
        System.out.println("\nMap elements: " + map);
        System.out.println("Value for key 2: " + map.get(2));
        map.put(2, "Mary");
        System.out.println("Map after updating key 2:" + map);
        map.remove(3);
        System.out.println("Map after removing key 3: " + map);
        System.out.println("Is key 1 present in the map? " + map.containsKey(1));
        System.out.println("Is value 'Jane' present in the map? " +map.containsValue("Jane"));
        System.out.println("Size of the map: " + map.size());        
    }
}
