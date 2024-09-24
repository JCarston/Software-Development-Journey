class operation
{
    public static void main(String[] args)
    {
        int num1 = 7;
        int num2 = 5;

        int result = num1 + num2;
        int result1 = num1 / num2; // Normal Division
        int result2 = num1 % num2; // Long division 5 goes into 7 one full time with a remainder of 2 // Bigger number is written first

        System.out.println(result);
        System.out.println(result1);
        System.out.println(result2);
        
        
        int data1 = num1++; // post - increment
        //^^ This is 7 because the ++ comes after operation

        int data = ++num1; // pre - increment
        //^^ this is 9 because after line 17 the value is 8 ( ++ operation is completed) and then the pre - increment is applied

        System.out.printf("data: %s,\ndata1: %s", data, data1);

    }
}