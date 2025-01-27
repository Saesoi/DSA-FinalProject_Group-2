async function quickSort(arr, left = 0, right = arr.length - 1, visualize) {
    if (left < right) {
        const pivotIndex = await partition(arr, left, right, visualize);
        await quickSort(arr, left, pivotIndex - 1, visualize);
        await quickSort(arr, pivotIndex + 1, right, visualize);
    }
    return arr;
}

async function partition(arr, left, right, visualize) {
    const pivot = arr[right];
    let i = left - 1;

    for (let j = left; j < right; j++) {
        if (stopRequested) return;
        if (arr[j] < pivot) {
            i++;
            [arr[i], arr[j]] = [arr[j], arr[i]];
            visualize(arr, [i, j]);
            await new Promise(resolve => setTimeout(resolve, 200)); // Delay for visualization
        }
    }
    [arr[i + 1], arr[right]] = [arr[right], arr[i + 1]];
    visualize(arr, [i + 1, right]);
    await new Promise(resolve => setTimeout(resolve, 200)); // Delay for visualization
    return i + 1;
}