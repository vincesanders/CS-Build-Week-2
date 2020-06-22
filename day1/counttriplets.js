function countTriplets(arr, r) {
    let solution = 0;
    const possibleTrips = {};
    const triplets = {};

    arr.forEach(num => { //O(n) - time
        //if a triplets for this value have been found add them to the solution.
        solution += (triplets[num] || 0);

        //Set nextNum to the next value in the geometric progression.
        const nextNum = num * r;

        //Add found triplets for nextNum to possible triplets that were found for num
        triplets[nextNum] = ((triplets[nextNum] || 0) + (possibleTrips[num] || 0));

        //Since nextNum was calculated from a num in the array,
        //it's added to the possible triplets dictionary.
        possibleTrips[nextNum] = (possibleTrips[nextNum] || 0) + 1
    })
    return solution;
}