public class test {


    public static void main(String[] args) {

        var a = "discuss.leetcode.com";


//        Arrays.stream(a.split("\\.")).forEach(System.out::println);
        for (int i = 0; i < a.split("\\.").length; i++) {

            System.out.println(a.split("\\.", 1)[0]);
            System.out.println(a.split("\\.", 2)[1]);
            System.out.println(a.split("\\.", 3)[2]);

            break;
        }
    }
}