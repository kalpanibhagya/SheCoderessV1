import java.util.*;
 
public class Main{
 
    public static void main(String params[]){
        Scanner scanner = new Scanner(System.in);
 
        int n=scanner.nextInt();
        int k=scanner.nextInt();
 
        int towerStatus[]=new int[n];
        for (int i=0;i<n;i++)
            towerStatus[i]=scanner.nextInt();
 
        System.out.print(getElectricity(towerStatus,k));
 
    }
 
    private static int getElectricity(int[] towerStatus,int k) {
        int result=0,temp=0;
        int i=0,j;
        while (i<towerStatus.length){
            result=temp;
             j=i+k-1;
            if (i+k-1>=towerStatus.length)
                j=towerStatus.length-1;
            
            while (j>=i-k+1&&j>=0){
                if (towerStatus[j]==1){
                    temp+=1;
                    i=j+k;
                    break;
                }
                j-=1;
            }
            if (result==temp)
                return -1;
            result=temp;
        }
        return result;
    }
}