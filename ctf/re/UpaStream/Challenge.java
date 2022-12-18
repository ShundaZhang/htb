import java.util.Arrays;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;

public class Challenge {
  public static void main(String[] paramArrayOfString) {
    String str = "FLAG";
    Objects.requireNonNull(System.out);
    dunkTheFlag(str).stream().forEach(System.out::println);
  }
  
  private static List<String> dunkTheFlag(String paramString) {
    return Arrays.asList(new String[] { ((String)((List)((String)((List)((String)((List)paramString.chars().mapToObj(paramInt -> Character.valueOf((char)paramInt)).collect(Collectors.toList())).stream().peek(paramCharacter -> hydrate(paramCharacter)).map(paramCharacter -> paramCharacter.toString()).reduce("", (paramString1, paramString2) -> paramString2 + paramString2)).chars().mapToObj(paramInt -> Character.valueOf((char)paramInt)).collect(Collectors.toList())).stream().map(paramCharacter -> paramCharacter.toString()).reduce(String::concat).get()).chars().mapToObj(paramInt -> Integer.valueOf(paramInt)).collect(Collectors.toList())).stream().map(paramInteger -> moisten(paramInteger.intValue())).map(paramInteger -> Integer.valueOf(paramInteger.intValue())).map(Challenge::drench).peek(Challenge::waterlog).map(Challenge::dilute).map(Integer::toHexString).reduce("", (paramString1, paramString2) -> paramString1 + paramString1 + "O")).repeat(5) });
  }
  
  private static Integer hydrate(Character paramCharacter) {
    return Integer.valueOf(paramCharacter.charValue() - 1);
  }
  
  private static Integer moisten(int paramInt) {
    return Integer.valueOf((int)((paramInt % 2 == 0) ? paramInt : Math.pow(paramInt, 2.0D)));
  }
  
  private static Integer drench(Integer paramInteger) {
    return Integer.valueOf(paramInteger.intValue() << 1);
  }
  
  private static Integer dilute(Integer paramInteger) {
    return Integer.valueOf(paramInteger.intValue() / 2 + paramInteger.intValue());
  }
  
  private static byte waterlog(Integer paramInteger) {
    paramInteger = Integer.valueOf((((paramInteger.intValue() + 2) * 4 % 87 ^ 0x3) == 17362) ? (paramInteger.intValue() * 2) : (paramInteger.intValue() / 2));
    return paramInteger.byteValue();
  }
}

