class linear_search {
    static int search(int arr[], int key) {
        int len = arr.length;

        for(int i = 0; i < len; i++){
            if(arr[i] == key){
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args){
            int arr[] = {1, 2, 3, 4, 5, 6};
            int key = 3;
            int position = search(arr, key) + 1;
            System.out.println(position);
    }
}