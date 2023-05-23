#Keyword:
#JAVA
#Java
#java

#LD_LIBRARY_PATH=/usr/lib/jvm/java-18-openjdk-amd64/lib/server/ ./coffee_invocation
#binwalk --run-as=root -D='.*' ./coffee_invocation

#http://www.javadecompilers.com/

'''
//
// Decompiled by Procyon v0.5.36
//

public class Verify1
{
    private static boolean compareByte(final Byte b, final Short n) {
        return b == (short)n;
    }

    public static void main(final String[] array) {
        if (array == null || array.length != 2) {
            System.out.println("Verifying requires source and target");
            System.exit(1);
            return;
        }
        final String s = array[0];
        final String s2 = array[1];
        if (s == null || s2 == null) {
            System.out.println("Source and Target may not be null");
            System.exit(2);
            return;
        }
        if (s.length() != s2.length()) {
            System.out.println("Source and Target don't have the same length");
            System.exit(2);
            return;
        }
        System.out.println("Verifying user is of terrestrial origin...");
        for (int i = 0; i < s.length(); ++i) {
            if (!compareByte((byte)s.charAt(i), (short)(byte)s2.charAt(i))) {
                System.out.println("=> User might be an alien!!!");
                System.exit(3);
                return;
            }
        }
    }
}

import java.util.stream.Collector;
import java.util.stream.Collectors;
import java.util.function.Function;
import java.util.Arrays;

// 
// Decompiled by Procyon v0.5.36
// 

public class Verify2
{
    private static boolean compareByte(final Byte b, final Short n) {
        System.out.println(invokedynamic(makeConcatWithConstants:(II)Ljava/lang/String;, (byte)b, (short)n));
        return b == (short)n;
    }
    
    private static String complexSort(final String s, final Boolean b) {
        final Object[] array = s.chars().mapToObj(n -> Character.valueOf((char)n)).toArray();
        if (b) {
            Arrays.sort(array);
        }
        return Arrays.stream(array).map((Function<? super Object, ?>)Object::toString).collect((Collector<? super Object, ?, String>)Collectors.joining());
    }
    
    private static Boolean verifyPassword(final String s, final String anObject) {
        return s.equals(anObject);
    }
    
    public static void main(final String[] array) {
        if (array == null || array.length != 1) {
            System.out.println("Verifying requires source");
            System.exit(1);
            return;
        }
        final String s = array[0];
        if (s == null) {
            System.out.println("Source may not be null");
            System.exit(1);
            return;
        }
        if (s.length() % 2 != 0) {
            System.out.println("Length must be even");
            System.exit(1);
            return;
        }
        System.out.println("Verifying user has authorization...");
        for (int i = 0; i < s.length() / 2; ++i) {
            if (complexSort(s.substring(i * 2, i * 2 + 2), true).equals(complexSort("Cr1KD5mk0_uUzQYifaGVqlN2B3wvpgPtSx6Odo{8hjJLHy9IXb4RnWZ}TAFEsMce7", false).substring(i * 2, i * 2 + 2))) {
                System.exit(i + 3);
            }
        }
        if (!verifyPassword(s, "Tinfoil")) {
            System.out.println("Please enter the correct password");
            System.exit(2);
        }
    }
}
'''


#HTB{th3_s3cr3t3_r3c1p3_1s_23_h0ur5_str41ght_0f_r34d1ng_J4v4_d0cs}
