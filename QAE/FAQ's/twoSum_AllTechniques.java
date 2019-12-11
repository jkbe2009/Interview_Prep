
import java.util.*;

class twoSum_AllTechniques{
    
    public static void main(String[] args) {
        int[] a = { 1, 9, 12, 3, 7, 5 };
        int[] b = { 1, 3, 5, 7, 10 };

        //int[] result = twoSumBF(a,4);
        //int[] result = twoSumBS(a,4);
        //int[] result = twoSumTwoPointer(b,10);
        int[] result = twoSumHM(b, 12);

        System.out.println(Arrays.toString(result));
    }

    public static int[] twoSumBF(int[] a, int sum) {
        // O(n2) | O(1)
        if (a == null || a.length == 0)
            return new int[] { -1, -1 };

        for (int i = 0; i < a.length - 1; i++) {
            for (int j = i + 1; j < a.length; j++) {
                if (a[i] + a[j] == sum)
                    return new int[] { i, j };
            }
        }

        return new int[] { -1, -1 };
    }

    public static int[] twoSumBS(int[] a, int sum) {
        // O(nlogn) | O(1)
        if (a == null || a.length == 0)
            return new int[] { -1, -1 };

        Arrays.sort(a);

        for (int i = 0; i < a.length; i++) {
            int diff = sum - a[i];
            if (bSearch(a, diff) != -1)
                return new int[] { i, bSearch(a, diff) };
        }

        return new int[] { -1, -1 };
    }

    public static int bSearch(int[] inp, int key) {
        // O(logn)
        int low = 0, high = inp.length - 1;

        while (low <= high) {
            int mid = (int) Math.floor((low + high) / 2);
            if (inp[mid] == key)
                return mid;
            else if (key < inp[mid])
                high = mid - 1;
            else
                low = mid + 1;
        }

        return -1;
    }

    public static int[] twoSumTwoPointer(int[] a, int target) {
        // O(nlogn) | O(1)
        if (a == null || a.length == 0)
            return new int[] { -1, -1 };

        int l = 0, r = a.length - 1;

        while (l < r) {
            int sum = a[l] + a[r];

            if (sum == target)
                return new int[] { l, r };
            else if (sum < target)
                l++;
            else
                r--;
        }

        return new int[] { -1, -1 };
    }

    public static int[] twoSumHM(int[] a, int target) {
        // O(n) | O(n)
        if (a == null || a.length == 0)
            return new int[] { -1, -1 };

        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < a.length; i++) {
            int diff = target - a[i];

            if (map.containsKey(diff))
                return new int[] { map.get(diff), i };
            else
                map.put(a[i], i);
        }

        return new int[] { -1, -1 };
    }

}


