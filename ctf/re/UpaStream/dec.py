'''
jadx

package defpackage;

import java.io.PrintStream;
import java.util.Arrays;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/* renamed from: Challenge  reason: default package */
/* loaded from: stream.jar:Challenge.class */
public class Challenge {
    public static void main(String[] strArr) {
        Stream<String> stream = dunkTheFlag("FLAG").stream();
        PrintStream printStream = System.out;
        Objects.requireNonNull(printStream);
        stream.forEach(this::println);
    }

    private static List<String> dunkTheFlag(String str) {
        return Arrays.asList(((String) ((List) ((String) ((List) ((String) ((List) str.chars().mapToObj(i -> {
            return Character.valueOf((char) i);
        }).collect(Collectors.toList())).stream().peek(ch -> {
            hydrate(ch);
        }).map(ch2 -> {
            return ch2.toString();
        }).reduce("", str2, str3 -> {
            return str3 + str2;
        })).chars().mapToObj(i2 -> {
            return Character.valueOf((char) i2);
        }).collect(Collectors.toList())).stream().map(ch3 -> {
            return ch3.toString();
        }).reduce((v0, v1) -> {
            return v0.concat(v1);
        }).get()).chars().mapToObj(i3 -> {
            return Integer.valueOf(i3);
        }).collect(Collectors.toList())).stream().map(num -> {
            return moisten(num.intValue());
        }).map(num2 -> {
            return Integer.valueOf(num2.intValue());
        }).map(Challenge::drench).peek(Challenge::waterlog).map(Challenge::dilute).map((v0) -> {
            return Integer.toHexString(v0);
        }).reduce("", str4, str5 -> {
            return str4 + str5 + "O";
        })).repeat(5));
    }

    /* JADX INFO: Access modifiers changed from: private */
    public static Integer hydrate(Character ch) {
        return Integer.valueOf(ch.charValue() - 1);
    }

    /* JADX INFO: Access modifiers changed from: private */
    public static Integer moisten(int i) {
        return Integer.valueOf((int) (i % 2 == 0 ? i : Math.pow(i, 2.0d)));
    }

    private static Integer drench(Integer num) {
        return Integer.valueOf(num.intValue() << 1);
    }

    private static Integer dilute(Integer num) {
        return Integer.valueOf((num.intValue() / 2) + num.intValue());
    }

    private static byte waterlog(Integer num) {
        return Integer.valueOf(((((num.intValue() + 2) * 4) % 87) ^ 3) == 17362 ? num.intValue() * 2 : num.intValue() / 2).byteValue();
    }
}
'''


