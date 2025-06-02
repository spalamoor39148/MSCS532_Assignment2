# MSCS532_Assignment2 
Implemented the quick sort and merge sort algorithms and compared the implimentation by running them on various data

Summary of Results
Quick Sort was faster than Merge Sort on most inputs, especially for large and random data.

Merge Sort was more stable in performance regardless of input order.

Quick Sort used more memory due to creating new sublists in each recursive call.

Merge Sort used moderate, predictable memory because of its merging process.

Why Quick Sort Often Wins in Practice
Faster execution: Fewer data copies and better use of CPU cache.

Good pivot choice (middle element) helped avoid worst-case O(n²).

Quick Sort’s constant factors are lower than Merge Sort, making it faster despite the same Θ(n log n) time complexity.

Memory Usage
Our implementation of Quick Sort created new lists at each step — this increased memory usage.

Merge Sort needed only one extra list per recursion level — more efficient memory use.

Conclusion
Use Quick Sort for speed when input is random or unknown.

Use Merge Sort when stability or predictable performance is important.

For low memory environments, avoid Quick Sort with sublist creation — use the in-place version.