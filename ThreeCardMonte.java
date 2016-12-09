/* Jon Ham
 * CECS 174
 * Assign 12
 */
import java.util.Random;
import java.util.Scanner;


public class ThreeCardMonte{
    public static int randInt(int min, int max){
        Random rand = new Random();
        int randomNum = rand.nextInt((max - min) + 1) + min;
        return randomNum;
    }

    public static void main(String[] args){
        boolean invalid = true;
        int money = 100;
        int win = 0;
        int lose = 0;
        int percent = 0;
        int played = 0;

        while(invalid){
            Scanner in = new Scanner(System.in);

            System.out.println("Three Card Monte: ");
            System.out.println("1. Play");
            System.out.println("2. Quit");
            boolean invalid_option = true;
            while(invalid_option) {
                System.out.println("Enter option: ");
                int input;
                if (in.hasNextInt()) {
                    input = in.nextInt();
                    if (input < 1 || input > 2) {
                        System.out.println("Invalid entry. Enter 1 or 2.");
                    } else {
                        if (money <= 0) {
                            System.out.println("You have $" + money);
                            System.out.println("You have lost all your money.");
                            System.out.println("Thanks for playing.");
                            System.out.println("");
                            System.out.println("Statistics - ");
                            System.out.println("Games Played: " + played);
                            System.out.println("Games Won: " + win);
                            System.out.println("Games Lost: " + lose);
                            double percentage = (win / played) * 100;
                            System.out.println("You won " + percentage + "% of the games.");
                            invalid_option = false;
                            invalid = false;
                        }else{
                            if(input == 1){
                                played++;
                                boolean invalid_bet = true;
                                while(invalid_bet){
                                    System.out.println("You have $" + money);
                                    System.out.println("How much you wanna bet? ");
                                    int input_bet;
                                    if(in.hasNextInt()){
                                        input_bet = in.nextInt();
                                        if(input_bet > money){
                                            System.out.println("You cannot bet more than you have.");
                                        }else{
                                            boolean invalid_guess = true;
                                            while(invalid_guess){
                                                System.out.println("-------   -------   -------");
                                                System.out.println("|     |   |     |   |     |");
                                                System.out.println("|  X  |   |  X  |   |  X  |");
                                                System.out.println("|     |   |     |   |     |");
                                                System.out.println("-------   -------   -------");
                                                System.out.println("Guess where the queen's at: ");
                                                int input_guess;
                                                if(in.hasNextInt()){
                                                    input_guess = in.nextInt();
                                                    if(input_guess < 1 || input_guess > 3){
                                                        System.out.println("Invalid entry. Must be between 1 and 3.");
                                                    }else{
                                                        int random = randInt(1, 3);
                                                        switch (random){
                                                            case 1:
                                                                System.out.println("-------   -------   -------");
                                                                System.out.println("|     |   |     |   |     |");
                                                                System.out.println("|  K  |   |  K  |   |  Q  |");
                                                                System.out.println("|     |   |     |   |     |");
                                                                System.out.println("-------   -------   -------");
                                                                break;
                                                            case 2:
                                                                System.out.println("-------   -------   -------");
                                                                System.out.println("|     |   |     |   |     |");
                                                                System.out.println("|  K  |   |  Q  |   |  K  |");
                                                                System.out.println("|     |   |     |   |     |");
                                                                System.out.println("-------   -------   -------");
                                                                break;
                                                            case 3:
                                                                System.out.println("-------   -------   -------");
                                                                System.out.println("|     |   |     |   |     |");
                                                                System.out.println("|  Q  |   |  K  |   |  K  |");
                                                                System.out.println("|     |   |     |   |     |");
                                                                System.out.println("-------   -------   -------");
                                                                break;
                                                        }
                                                        if (input_guess == random){
                                                            System.out.println("You got lucky this time.");
                                                            money += input_bet;
                                                            win++;
                                                            invalid_guess = false;
                                                            invalid_bet = false;
                                                            invalid_option = false;
                                                        }else{
                                                            System.out.println("Sorry, it was card number "+random);
                                                            System.out.println("You lose $"+input_bet);
                                                            money -= input_bet;
                                                            lose++;
                                                            invalid_guess = false;
                                                            invalid_bet = false;
                                                            invalid_option = false;
                                                        }
                                                    }
                                                }

                                            }
                                        }
                                    }
                                }
                            }else if(input == 2){
                                System.out.println("Thanks for playing.");
                                System.out.println("");
                                System.out.println("Statistics - ");
                                System.out.println("Games Played: " + played);
                                System.out.println("Games Won: " + win);
                                System.out.println("Games Lost: " + lose);
                                double percentage;
                                System.out.println("You won 0.0% of the games.");
                                invalid_option = false;
                                invalid = false;
                            }

                        }
                    }
                }
            }
        }
    }
}