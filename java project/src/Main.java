public class Main {

    public static void main(String[] args) {


        System.out.println("Hello World!");
    }

    public void printMsg() {

        add(3, 5);
        add(4, 8);
        String newString = reduceString("world is very beautifal", "or");
        System.out.println("this is my first idea");
        System.out.println(newString);
    }


    private int add(int a, int b) {
        return a + b;
    }

    //字符串拼接
    private String addString(String a, String b) {
        return a + b;
    }

    private String reduceString(String a, String b) {
        return a.replace(b, "");
    }
}
