// Practical No.5
/* WAP to implement with no premption SJF scheduling Agorithm */

import java.util.Scanner;

class SJF {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n, AT[], BT[], WT[], TAT[], ST[], FT[];
        float AWT = 0, AVGTAT = 0;

        System.out.println("Enter No. of Processes: ");
        n = sc.nextInt();

        // Initializing arrays
        BT = new int[n];
        FT = new int[n];
        ST = new int[n];
        WT = new int[n];
        TAT = new int[n];
        AT = new int[n];

        // Input Burst Time for each process
        System.out.println("**********");
        for (int i = 0; i < n; i++) {
            System.out.println("Enter Burst Time for process " + (i + 1) + ":");
            BT[i] = sc.nextInt();
        }

        // Assuming all Arrival Times (AT) are 0
        // If you want to input arrival times, uncomment this section
        /*
        for (int i = 0; i < n; i++) {
            System.out.println("Enter Arrival Time for process " + (i + 1) + ":");
            AT[i] = sc.nextInt();
        }
        */

        // Sort processes by Burst Time (SJF)
        int temp;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (BT[j] > BT[j + 1]) {
                    // Swap burst times
                    temp = BT[j];
                    BT[j] = BT[j + 1];
                    BT[j + 1] = temp;

                    // Swap arrival times for consistency
                    temp = AT[j];
                    AT[j] = AT[j + 1];
                    AT[j + 1] = temp;
                }
            }
        }

        // Initialize start time for the first process
        ST[0] = 0;
        WT[0] = 0;  // Waiting time for the first process is 0

        // Calculate Start Time and Waiting Time for each process
        for (int i = 1; i < n; i++) {
            ST[i] = ST[i - 1] + BT[i - 1];  // Start time = finish time of the previous process
            WT[i] = ST[i] - AT[i];  // Waiting time = start time - arrival time

            if (WT[i] < 0) {  // If waiting time is negative, set it to 0
                WT[i] = 0;
            }
        }

        // Calculate Finish Time, Turnaround Time, and accumulate totals
        for (int i = 0; i < n; i++) {
            FT[i] = ST[i] + BT[i];  // Finish time = start time + burst time
            TAT[i] = FT[i] - AT[i];  // Turnaround time = finish time - arrival time

            AWT += WT[i];  // Accumulate total waiting time
            AVGTAT += TAT[i];  // Accumulate total turnaround time
        }

        // Output the process details
        System.out.println("**********");
        System.out.println(" BT  ST  FT  WT  TAT ");
        for (int i = 0; i < n; i++) {
            System.out.println(" " + BT[i] + "   " + ST[i] + "   " + FT[i] + "   " + WT[i] + "   " + TAT[i]);
        }

        // Calculate and display averages
        AWT /= n;
        AVGTAT /= n;

        System.out.println("**********\nAVG WT: " + AWT + "\n**********");
        System.out.println("AVG TAT: " + AVGTAT);
    }
}
