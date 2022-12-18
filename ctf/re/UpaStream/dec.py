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
from functools import reduce

target = 'b71bO12cO156O6e43Od8O69c3O5cd3O144Oe4O6e43O37cbOf6O69c3O1e7bO156O3183O69c3O6cO8b3bOc0O1e7bO156OfcO50bbO69c3Oc0O102O6e43OdeOb14bOc6OfcOd8O'

def enc(flag):
	list1 = map(lambda x: str(ord(x)-1), flag)
	#list1 = flag
	for i in range(0,len(list1),2):
		try:
			list1[i],list1[i+1] = list1[i+1],list1[i]
		except:
			continue
	list1 = ''.join(list1)
	#print list1

	'''
	list10 = []
	for i in range(0,len(list1),2):
		try:
			list10.append(list1[i]+list1[i+1])
		except:
			continue
	print list10
	'''

	list2 = map(lambda x: ord(x) if ord(x)%2 == 0 else ord(x)**2, list1)
	#print list2

	list3 = map(lambda x: x << 1, list2)
	#print list3

	list4 = map(lambda x: (x/2, x*2)[((((x + 2) * 4) % 87) ^ 3) == 17362], list3)
	#list4 = list3
	#print list4

	list5 = map(lambda x: x/2+x, list4)
	#print list5

	list6 = map(lambda x: hex(x)[2:], list5)
	#print list6

	list7 = []
	for i in range(0, len(list6), 2):
		try:
			list7.append(list6[i])
			list7.append(list6[i+1])
			list7.append('O')
		except:
			continue
	list7 = ''.join(list7)
	#print list7
	return list7

#print enc('HTB{7357_f419!}')

for i in range(32,127,1):
	for j in range(32,127,1):
		flag = chr(i)+chr(j)
		s = enc(flag)
		#if s == target[:len(s)]:
		if s in target:
			#print s
			print flag
