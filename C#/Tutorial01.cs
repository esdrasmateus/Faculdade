using System;

namespace C_
{
    class Tutorial01
    {
        static void Main(string[] args)
        {

            //--------------------------GREATER THAN/EQUAL TO------------------

            // Console.WriteLine("Welcome! Tickets are 5$. Please insert cash.");

            // int cash = Convert.ToInt32(Console.ReadLine());

            // if (cash < 5)
            // {
            //     Console.WriteLine("That's not enough money!");
            // }
            // else if (cash == 5)
            // {
            //     Console.WriteLine("Here is your ticket.");
            // }
            // else
            // {
            //     int change = cash - 5;
            //     Console.WriteLine("Here is your ticket and " + change + " dollars in change");
            // }

            //--------------------------CONVERT--------------------------------

            // int age, height;

            // Console.Write("Please input your age: ");
            // age = Convert.ToInt32(Console.ReadLine());

            // Console.Write("Please input your height (cm): ");
            // height = Convert.ToInt32(Console.ReadLine());

            // if (age >= 18 && height >= 160)
            // {
            //     Console.WriteLine("You can enter!");
            // }
            // else
            // {
            //     Console.WriteLine("You don't meet the requirements!");
            // }

            //--------------------------FOR LOOP-------------------------------

            // Console.Write("How many cool numbers do you want? ");

            // int count = Convert.ToInt32(Console.ReadLine());

            // for (int i = 1; i <= count; i++)
            // {
            //     double result = Math.Pow(2, i);
            //     Console.WriteLine(result);
            // }

            //--------------------------WHILE LOOP-----------------------------

            Random numberGen = new Random();

            int roll = 0, attempts = 0;

            Console.WriteLine("Press enter to roll the die.");

            while(roll != 6)
            {
                Console.ReadKey();

                roll = numberGen.Next(1, 7);
                Console.WriteLine("You rolled: " + roll);
                attempts++;
            }

            Console.WriteLine("You took " + attempts + " attempts to roll a six!");

            // Wait before closing
            Console.ReadKey();
        }
    }
}
