function countSwaps(a) {
    // Initialize our swap counter and set the length of the array to a variable.
    let numSwaps = 0;
    const n = a.length;

    // This algorithm was provided by the question
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n - 1; j++) {
            // Swap adjacent elements if they are in decreasing order
            if (a[j] > a[j + 1]) {

                // use ES6 syntax to make the swap instead of defining another function
                [a[j], a[j + 1]] = [a[j + 1], a[j]];

                //Increment our swap counter.
                numSwaps++;
            }
        }
    }

    // Console log the desired output.
    console.log(`Array is sorted in ${numSwaps} swaps.`);
    console.log(`First Element: ${a[0]}`);
    console.log(`Last Element: ${a[n - 1]}`);
}