import java.io.*;
import java.util.*;

public class Solution {
    private final String ALPHABET = "abcdefghijklmnopqrstuvwxyz";
    private final String alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

public String encrypt(int n,String plainText,int shiftKey)
     {

 
           //plainText = plainText.toLowerCase();
           String cipherText="";
           for(int i=0;i<n;i++)
           {   
		if(plainText.charAt(i)>=97&&plainText.charAt(i)<=122){
		if(plainText.charAt(i)!=' ')
			{
                int charPosition = ALPHABET.indexOf(plainText.charAt(i));
                int keyVal = (shiftKey+charPosition)%26;
                char replaceVal = this.ALPHABET.charAt(keyVal);
                cipherText += replaceVal;
			}
		else
		 cipherText = cipherText + " ";
				
		}
               else if(plainText.charAt(i)>=65&&plainText.charAt(i)<=90)
                   {
                   int charPosition = alpha.indexOf(plainText.charAt(i));
                int keyVal = (shiftKey+charPosition)%26;
                char replaceVal = this.alpha.charAt(keyVal);
                cipherText += replaceVal;
               }
		else
		 cipherText+=plainText.charAt(i);
			
           }
           return cipherText;
     }

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        int n,k;
        String str;
        Scanner get = new Scanner(System.in);
        n=get.nextInt();
        str=get.next();
        k=get.nextInt();
        Solution cc = new Solution();
        String cipher = cc.encrypt(n,str,k);
        System.out.println(cipher);
    }
}
