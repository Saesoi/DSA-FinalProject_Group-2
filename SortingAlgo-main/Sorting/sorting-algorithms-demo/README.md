# Sorting Algorithms Demo

This project demonstrates various sorting algorithms through a web application. Each algorithm is visualized with animations to help understand how they work. The project includes both JavaScript implementations for web visualization and Python implementations for backend processing.

## Project Structure

```
sorting-algorithms-demo
├── src
│   ├── index.html          # Main HTML document
│   ├── styles
│   │   └── styles.css      # CSS styles for the web page
│   ├── scripts
│   │   ├── bubbleSort.js   # Bubble sort algorithm
│   │   ├── selectionSort.js # Selection sort algorithm
│   │   ├── insertionSort.js # Insertion sort algorithm
│   │   ├── mergeSort.js     # Merge sort algorithm
│   │   ├── quickSort.js     # Quick sort algorithm
│   │   ├── randomQuickSort.js # Random quick sort algorithm
│   │   ├── countingSort.js  # Counting sort algorithm
│   │   └── radixSort.js     # Radix sort algorithm
│   └── python
│       ├── bubble_sort.py   # Python implementation of bubble sort
│       ├── selection_sort.py # Python implementation of selection sort
│       ├── insertion_sort.py # Python implementation of insertion sort
│       ├── merge_sort.py     # Python implementation of merge sort
│       ├── quick_sort.py     # Python implementation of quick sort
│       ├── random_quick_sort.py # Python implementation of random quick sort
│       ├── counting_sort.py  # Python implementation of counting sort
│       └── radix_sort.py     # Python implementation of radix sort
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies
```

## Getting Started

To run the web application:

1. Open `src/index.html` in a web browser.
2. Use the buttons to select and visualize different sorting algorithms.

### Python Scripts

To run the Python scripts:

1. Ensure you have Python installed on your machine.
2. Install the required dependencies listed in `requirements.txt` using the command:
   ```
   pip install -r requirements.txt
   ```
3. Run the desired Python script from the `src/python` directory using:
   ```
   python script_name.py
   ```

## Contributing

Feel free to contribute by adding more algorithms or improving the visualizations. 

## License

This project is open-source and available under the MIT License.