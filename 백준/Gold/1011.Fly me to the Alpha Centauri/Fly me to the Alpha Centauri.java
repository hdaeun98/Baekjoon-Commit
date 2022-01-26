import java.util.Scanner;

public class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n=sc.nextInt();
		for (int i=0;i<n;i++) {
			int x=sc.nextInt();
			int y=sc.nextInt();
			
			int d=y-x;
			int m=(int)Math.round(Math.sqrt(d));
			
			if(d>Math.pow(m, 2)) {
				System.out.println((int)m*2);
			}
			else {
				System.out.println((int)m*2-1);
			}
		}
	}
}