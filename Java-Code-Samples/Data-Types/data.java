
class Data_Types
{
    public static void main(String[] args)
    {
        byte by = 127; // Stores whole numbers from -128 to 127
        int num1 = 9; // Stores whole numbers from -2,147,483,648 to 2,147,483,647
        short sh = 558; // Stores whole numbers from -32,768 to 32,767
        long l = 55849l; // Stores whole numbers from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
        float f = 5.8f; // Stores fractional numbers. Sufficient for storing 6 to 7 decimal digits
        double d = 5.8; // Stores fractional numbers. Sufficient for storing 15 decimal digits
        char c = 'k'; // Stores a single character/letter or ASCII values
        boolean b = false; // Stores true or false values
        

        System.out.printf("Integer: %s\nByte: %s",num1, by);
        System.out.printf("\nShort: %s\nLong: %s",sh, l);
        System.out.printf("\nFloat: %s\nDouble: %,.2f",f, d); // Variable "d" is set two decimal digits and displayed as float not matter the decimal point
        // -- https://docs.oracle.com/javase/tutorial/java/data/numberformat.html
        // ----^^Website for printf
        System.out.printf("\nCharacter: %s\nBoolean: %s",c, b);

    }
}