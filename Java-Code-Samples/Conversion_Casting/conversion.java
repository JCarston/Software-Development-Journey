class Conversion_Casting
{
    public static void main(String[] args)
    {
        // Convert data type
        byte b = 127;
        int a = b;
        System.out.println(a);

        // This Creates a type conversion error
        // int something = 12;
        // byte k = something;
        // System.out.println(k);


        // Use the following to cast type
        int data_point = 12;
        Byte k = (byte)data_point; //Switches variable into a byte
        System.out.println(k);
        System.out.println(k.getClass().getName()); // displays the data type of the variable


        byte c = 10;
        byte d = 30;
        int result = c*d; // Promotes bytes into an integer because the value exceeds 127
        System.out.println(result);
    }
}