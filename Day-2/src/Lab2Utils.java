public class Lab2Utils {


    public static String welcomeMessage(String name) {
        return "Hi " + name + ", welcome to the world of Java!";
    }


    public static int largest(int a, int b, int c) {
        return Math.max(a, Math.max(b, c));
    }


    public static void printDigitsInWords(int number) {
        String[] digitWords = {"Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
        String numStr = Integer.toString(number);
        for (char digit : numStr.toCharArray()) {
            System.out.print(digitWords[digit - '0'] + " ");
        }
        System.out.println();
    }
}