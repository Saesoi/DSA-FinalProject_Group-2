async function selectionSort(arr, visualize) {
    let n = arr.length;
    async function sort() {
        for (let i = 0; i < n - 1; i++) {
            if (stopRequested) return;
            let minIndex = i;
            for (let j = i + 1; j < n; j++) {
                if (stopRequested) return;
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }
            if (minIndex !== i) {
                [arr[i], arr[minIndex]] = [arr[minIndex], arr[i]];
                visualize(arr, [i, minIndex]);
                await new Promise(resolve => setTimeout(resolve, 200)); // Delay for visualization
            }
        }
    }
    await sort();
    return arr;
}