/*
Use Java Reflection to dynamically invoke private class methods, after unzipping Challenge.class from the given stream.jar

Compile as follows: javac -Xlint:unchecked -cp "." Main.java && java Main

The flag is matched by group delimited by O, (1-1 mapping) corresponding to a single ASCII char, working right-to-left from d8 … b71b

The output.txt string is repeated five times, so can just take one of those five sequences
*/

import java.util.*;
 
import java.lang.reflect.*;
 
 
 
public class Main {
 
  @SuppressWarnings("unchecked")
 
  public static void main(String[] args) {
 
    try {
 
      Class<?> clazz = Class.forName("Challenge");
 
      Method method = clazz.getDeclaredMethod("dunkTheFlag",String.class);
 
      method.setAccessible(true);
 
 
      //match the longest string
      String base = "HTB{";
      //String base = "HTB{Ja";
      //String base = "HTB{JaV@";
      //String base = "HTB{JaV@_S";
      //String base = "HTB{JaV@_STr";
      //String base = "HTB{JaV@_STr3@";
      //String base = "HTB{JaV@_STr3@m$";
      //String base = "HTB{JaV@_STr3@m$_A";
      //String base = "HTB{JaV@_STr3@m$_Ar3";
      //String base = "HTB{JaV@_STr3@m$_Ar3_R";
      //String base = "HTB{JaV@_STr3@m$_Ar3_REa";
      //......
      //String base = "HTB{JaV@_STr3@m$_Ar3_REaLlY_Hard}";
 
      for (int i=0x20; i<0x7f; i++) {
 
        for (int j=0x20; j<0x7f; j++) {
 
          String c0 = Character.toString(i);
 
          String c1 = Character.toString(j);
 
          System.out.print(c0+c1+" : ");
 
          List<String> ss = (List<String>) method.invoke(null,base+c0+c1);
 
          ss.stream().forEach(System.out::println);
 
        }
 
      }
 
      // _:69c3
 
      // b71b 12c 156 6e43 d8 _ 5cd3 144 e4 6e43 37cb f6 _ 1e7b 156 3183 _ 6c 8b3b c0 1e7b 156 fc 50bb _ c0 102 6e43 de b14b c6 fc d8
 
    }
 
    catch (ClassNotFoundException ex) {ex.printStackTrace();}
 
    catch (IllegalAccessException ex) {ex.printStackTrace();}
 
    catch (NoSuchMethodException ex) {ex.printStackTrace();}
 
    catch (InvocationTargetException ex) {ex.printStackTrace();}
 
  }
 
}
