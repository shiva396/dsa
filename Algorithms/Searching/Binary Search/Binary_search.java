class Binary_search {
    static int search(int arr[], int key){
        int first = 0;
        int last = arr.length - 1;

        while(first <= last){
            int mid = (first + last) / 2;
            if (arr[mid] == key) {
                return mid;
            }
            else if (arr[mid] > key) {
                last = mid - 1;
            }else{
                first = mid + 1;
            }
        }
        return -1;
    }

    //Driver code
    public static void main(String[] args) {
        int arr[] = {1, 2, 3, 4, 5, 6, 7};
        int key = 4;
        int ind = search(arr, key);
        System.out.println(ind);
    }
}