// Linear Searching Algorithm

/*class DSA{
    public static void main(String[] args){
        int arr[] = {10, 20, 30, 40, 50};
        int searchElement = 20;
        boolean flag = false;
        for(int i = 0; i < arr.length; i++){
            if(searchElement == arr[i]){
                System.out.println("Element found at Position : "+i);
                flag = true;
                break;
            }
        }
        if(!flag){
            System.out.println("Element not found !!!");
        }
    }
}*/


// Binary Searching Algorithm

/*class DSA{
    public static void main(String[] args){
        int[] arr = {10, 20, 30, 40, 50, 60, 70};
        int left = 0; int data = 70;
        int right = arr.length - 1;
        while(left <= right){
            int mid = (left + right) / 2;
                if(data == arr[mid]){
                    System.out.println("Element found at : "+mid);
                    return;
                } else if (data < arr[mid]){
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
        }
         System.out.println("Element not found.");
    }
}*/

// Bubble Sort Algorithm

/*class DSA{
    public static void main(String[] args){
        int arr[] = {10, 32, 12, 32, 43, 2};
        int n = arr.length;
        for(int i = 0; i <= n - 1; i++){
            boolean flag = false;
            for(int j = 0; j <= n - 1; j++){
                if(arr[j] > arr[j + 1]){
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    flag = true;
                }
            }
            if(!flag){
                break;
            }
        }
        for(int i = 0; i < n; i++){
            System.out.println(" "+arr[i]+" ");
        }
    }
}*/

// Insertion sort Algorithm

/*class DSA{
    public static void main(String[] args){
        int arr[] = {10,2, 54, 23, 12};
        int n = arr.length;
        for(int i = 1; i < n; i++){
            int temp = arr[i];
            int j = i + 1;
            while(j >= 0 && arr[j]>temp){
                arr[j+1] = arr[j];
                j--;
            }
            arr[j+1] = temp;
        }
        for(int element:arr){
            System.out.println(element);
        }
    }
}
*/

// Queue

