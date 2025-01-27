async function countingSort(arr, visualize) {
    const max = Math.max(...arr);
    const count = new Array(max + 1).fill(0);
    const output = new Array(arr.length);

    for (let i = 0; i < arr.length; i++) {
        if (stopRequested) return;
        count[arr[i]]++;
    }

    for (let i = 1; i <= max; i++) {
        if (stopRequested) return;
        count[i] += count[i - 1];
    }

    for (let i = arr.length - 1; i >= 0; i--) {
        if (stopRequested) return;
        output[count[arr[i]] - 1] = arr[i];
        count[arr[i]]--;
        visualize(output, [i]);
        await new Promise(resolve => setTimeout(resolve, 200)); // Delay for visualization
    }

    for (let i = 0; i < arr.length; i++) {
        if (stopRequested) return;
        arr[i] = output[i];
    }
    return arr;
}