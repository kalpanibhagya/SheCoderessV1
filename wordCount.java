import java.util.*;
 
 
class TestClass {
    public static void main(String args[] )  {
       Scanner s=new Scanner(System.in);
       String w =s.nextLine();
       String[] h1 =w.split("[^\\w']+");
       System.out.println(h1.length);
    }
}