async function randomQuickSort(arr, left = 0, right = arr.length - 1, visualize) {
    if (left < right) {
        const pivotIndex = await partition(arr, left, right, visualize);
        await randomQuickSort(arr, left, pivotIndex - 1, visualize);
        await randomQuickSort(arr, pivotIndex + 1, right, visualize);
    }
    return arr;
}

async function partition(arr, left, right, visualize) {
    const pivotIndex = Math.floor(Math.random() * (right - left + 1)) + left;
    const pivotValue = arr[pivotIndex];
    [arr[pivotIndex], arr[right]] = [arr[right], arr[pivotIndex]];
    let storeIndex = left;

    for (let i = left; i < right; i++) {
        if (stopRequested) return;
        if (arr[i] < pivotValue) {
            [arr[i], arr[storeIndex]] = [arr[storeIndex], arr[i]];
            storeIndex++;
            visualize(arr, [i, storeIndex]);
            await new Promise(resolve => setTimeout(resolve, 200)); // Delay for visualization
        }
    }
    [arr[storeIndex], arr[right]] = [arr[right], arr[storeIndex]];
    visualize(arr, [storeIndex, right]);
    await new Promise(resolve => setTimeout(resolve, 200)); // Delay for visualization
    return storeIndex;
}