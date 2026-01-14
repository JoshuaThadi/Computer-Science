// Practical No.4
/* FCFS scheduling algorithm */
// https://ctxt.io/2/AAB4GskIEQ


import java.util.Scanner;

class Fcfs {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n, at[], bt[], wt[], tat[], st[], ft[];
        float awt = 0, avgTat = 0;

        System.out.println("Enter No. of processes : ");
        n = sc.nextInt();

        // Initializing arrays for n processes
        bt = new int[n];
        ft = new int[n];
        st = new int[n];
        wt = new int[n];
        tat = new int[n];
        at = new int[n];

        System.out.println("**********");
        // Input Burst Time for each process
        for (int i = 0; i < n; i++) {
            System.out.println("Enter Burst time for process " + (i + 1) + ":");
            bt[i] = sc.nextInt();
        }

        System.out.println("**********");
        // Input Arrival Time for each process
        for (int i = 0; i < n; i++) {
            System.out.println("Enter Arrival time for process " + (i + 1) + ":");
            at[i] = sc.nextInt();
        }

        // Initialize start time for the first process
        st[0] = at[0];
        wt[0] = 0;  // Waiting time for the first process is 0

        // Calculating start time and waiting time for the rest of the processes
        for (int i = 1; i < n; i++) {
            st[i] = st[i - 1] + bt[i - 1];  // Start time = finish time of the previous process
            wt[i] = st[i] - at[i];  // Waiting time = start time - arrival time

            if (wt[i] < 0) {  // If waiting time is negative, set it to 0
                wt[i] = 0;
            }
        }

        // Calculating finish time, turnaround time, and accumulating totals
        for (int i = 0; i < n; i++) {
            ft[i] = st[i] + bt[i];  // Finish time = start time + burst time
            tat[i] = ft[i] - at[i];  // Turnaround time = finish time - arrival time

            awt += wt[i];  // Accumulate total waiting time
            avgTat += tat[i];  // Accumulate total turnaround time
        }

        // Output the process details
        System.out.println("***********");
        System.out.println("PR  BT  ST  FT  WT  TAT");
        for (int i = 0; i < n; i++) {
            System.out.println((i + 1) + "   " + bt[i] + "   " + st[i] + "   " + ft[i] + "   " + wt[i] + "   " + tat[i]);
        }

        // Calculate and display averages
        awt = awt / n;
        avgTat = avgTat / n;

        System.out.println("**********\n Avg. Waiting Time : " + awt + "\n************");
        System.out.println("**********\n Avg. Turnaround Time: " + avgTat + "\n************");
    }
}
