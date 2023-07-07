# See the Sunset

You are given an array of positive non-zero integers representing the heights of buildings. Additionally, you are given a string indicating the direction in which all the buildings are facing, either "EAST" or "WEST". Your task is to write a function that returns an array containing the indices of the buildings from which you can see the sunset.

A building is said to see the sunset if its height is greater than all the buildings behind it in the given direction. In other words, if a building with index i is taller than all the buildings with indices j where j < i (if facing west) or j > i (if facing east), then it can see the sunset.

The function should take the array of building heights and the direction as input and return an array containing the indices of the buildings that can see the sunset. The indices in the output array should be sorted in ascending order.

To summarize, the function should identify the buildings that have an unobstructed view of the sunset based on their height and the specified direction. It should return an array of the indices of such buildings, sorted in ascending order.

Sample Input #1
buildings = [3, 5, 4, 4, 3, 1, 3, 2]
direction = "EAST"

Sample Output #1
[1, 3, 6, 7]

    // Below is a visual representation of the sample input.
    //    _
    //   | |_ _
    //  _| | | |_   _
    // | | | | | | | |_
    // | | | | | |_| | |
    // |_|_|_|_|_|_|_|_|

Sample Input #2
buildings = [3, 5, 4, 4, 3, 1, 3, 2]
direction = "WEST"

Sample Output #2
[0, 1]

    // The buildings are the same as in the first sample
    // input, but their direction is reversed.
