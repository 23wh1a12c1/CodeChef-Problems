#  C



import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner s = new Scanner(System.in);
		int t = s.nextInt();
		while(t-->0){
		    int b1 = s.nextInt();
		    int b2 = s.nextInt();
		    int b3 = s.nextInt();
		    if((b1==0 && b2==0 && b3==0) || (b1==1 && (b2==0 && b3==0)) || (b2==1 && (b1==0 && b3==0)) || (b3==1 && (b2==0 && b1==0))){
		        System.out.println("Water filling time");
		    }else{
		        System.out.println("Not now");
		    }
		}
	}
}





# PYTHON3




t = int(input())
for _ in range(t):
    b1, b2, b3 = map(int, input().split())
    if (b1 == 0 and b2 == 0 and b3 == 0) or \
       (b1 == 1 and b2 == 0 and b3 == 0) or \
       (b2 == 1 and b1 == 0 and b3 == 0) or \
       (b3 == 1 and b1 == 0 and b2 == 0):
        print("Water filling time")
    else:
        print("Not now")

















