async function countingSortForRadix(arr, exp, visualize) {
    const output = new Array(arr.length);
    const count = new Array(10).fill(0);

    for (let i = 0; i < arr.length; i++) {
        if (stopRequested) return;
        count[Math.floor((arr[i] / exp) % 10)]++;
    }

    for (let i = 1; i < 10; i++) {
        if (stopRequested) return;
        count[i] += count[i - 1];
    }

    for (let i = arr.length - 1; i >= 0; i--) {
        if (stopRequested) return;
        output[count[Math.floor((arr[i] / exp) % 10)] - 1] = arr[i];
        count[Math.floor((arr[i] / exp) % 10)]--;
        visualize(output, [i]);
        await new Promise(resolve => setTimeout(resolve, 200)); // Delay for visualization
    }

    for (let i = 0; i < arr.length; i++) {
        if (stopRequested) return;
        arr[i] = output[i];
    }
}

async function radixSort(arr, visualize) {
    const max = Math.max(...arr);

    for (let exp = 1; Math.floor(max / exp) > 0; exp *= 10) {
        await countingSortForRadix(arr, exp, visualize);
    }
    return arr;
}