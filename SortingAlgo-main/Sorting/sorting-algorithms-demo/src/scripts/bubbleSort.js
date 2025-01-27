async function bubbleSort(arr, visualize) {
    let n = arr.length;
    let swapped;

    async function sort() {
        for (let i = 0; i < n - 1; i++) {
            if (stopRequested) return;
            swapped = false;
            for (let j = 0; j < n - i - 1; j++) {
                if (stopRequested) return;
                if (arr[j] > arr[j + 1]) {
                    [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
                    swapped = true;
                    visualize(arr, [j, j + 1]);
                    await new Promise(resolve => setTimeout(resolve, 200)); // Delay for visualization
                }
            }
            if (!swapped) break;
        }
    }

    await sort();
    return arr;
}