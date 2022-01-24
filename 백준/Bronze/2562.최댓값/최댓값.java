import java.util.Scanner;

public class Main{
	public static void main(String[] args) {
		int[] a = new int[9];
		Scanner sc = new Scanner(System.in);
		for (int i=0;i<9;i++) {
			a[i]=sc.nextInt();
		}
		sc.close();
		int max=0;
		int index=0;
		for (int i=0;i<9;i++) {
			if (max<a[i]) {
				max=a[i];
				index=i;
			}
		}
		System.out.print(max+"\n"+(index+1));
	}
}