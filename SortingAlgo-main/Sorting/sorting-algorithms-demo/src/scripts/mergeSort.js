async function mergeSort(arr, visualize) {
    if (arr.length <= 1) {
        return arr;
    }

    const mid = Math.floor(arr.length / 2);
    const left = await mergeSort(arr.slice(0, mid), visualize);
    const right = await mergeSort(arr.slice(mid), visualize);

    return await merge(left, right, visualize);
}

async function merge(left, right, visualize) {
    let result = [];
    let leftIndex = 0;
    let rightIndex = 0;

    while (leftIndex < left.length && rightIndex < right.length) {
        if (stopRequested) return;
        if (left[leftIndex] < right[rightIndex]) {
            result.push(left[leftIndex]);
            leftIndex++;
        } else {
            result.push(right[rightIndex]);
            rightIndex++;
        }
        visualize(result.concat(left.slice(leftIndex)).concat(right.slice(rightIndex)), [leftIndex, rightIndex]);
        await new Promise(resolve => setTimeout(resolve, 200)); // Delay for visualization
    }

    return result.concat(left.slice(leftIndex)).concat(right.slice(rightIndex));
}