async function insertionSort(arr, visualize) {
    let n = arr.length;
    async function sort() {
        for (let i = 1; i < n; i++) {
            if (stopRequested) return;
            let key = arr[i];
            let j = i - 1;
            while (j >= 0 && arr[j] > key) {
                if (stopRequested) return;
                arr[j + 1] = arr[j];
                j = j - 1;
                visualize(arr);
                await new Promise(resolve => setTimeout(resolve, 200)); // Delay for visualization
            }
            arr[j + 1] = key;
            visualize(arr);
            await new Promise(resolve => setTimeout(resolve, 200)); // Delay for visualization
        }
    }
    await sort();
    return arr;
}