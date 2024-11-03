import java.io.*;
import java.util.*;

public class SecureFind {

    private static boolean hacker_filter(String input) {
        String[] ban_chars = {"&",";","|","#","`","$","\""};
        for(int i=0;i<ban_chars.length;i++) {
            if (input.contains(ban_chars[i]) ) {System.out.println("No hackers here !");return false;}
        }
        return true;
    }

     private static void runCmd(String regex) throws IOException, InterruptedException  {
        if (!hacker_filter(regex)) return;

        ProcessBuilder pb = new ProcessBuilder(new String[] { "bash", "-i"});
        pb.redirectErrorStream(true);

        // Launch and wait:
        Process p = pb.start();

        // Send + close STDIN stream
        try(OutputStream os = p.getOutputStream()) {
            if (regex != null) os.write((" find . -type f -regex \"" + regex + "\"").getBytes());
        }
        // Print STDOUT+ERR stream
        try(var stdo = p.getInputStream()) {
            stdo.transferTo(System.out);
        }
    }


    public static void main(String[] args) throws IOException, InterruptedException {
        if (args.length == 0) {System.out.println("[*] Usage : /bin/java -jar /tmp/SecureFind.jar 'REGEX'");return;}
        runCmd(args[0]);
    }
}