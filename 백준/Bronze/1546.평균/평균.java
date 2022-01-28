import java.util.Scanner;
import java.util.Arrays;
public class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n=sc.nextInt();
		double a[]=new double[n];
		int max=0;
		for (int i=0;i<n;i++) {
			a[i]=sc.nextDouble();
		}
		sc.close();
		Arrays.sort(a);;
		double s=0;
		for (int j=0;j<n-1;j++) {
			s+=(a[j]/a[n-1]*100);
		}
		s=((s+100)/n);
		System.out.println(s);
	}
}