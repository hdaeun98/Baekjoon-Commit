import java.util.Scanner;

public class Main{
	public static void main(String[] args) {
		Scanner input1 = new Scanner(System.in);
		int n=input1.nextInt();
		int s=1;
		for (int i=n;i>0;i--) {
			s*=i;
		}
		System.out.print(s);
	}
}