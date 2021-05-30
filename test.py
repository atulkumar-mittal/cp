heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]


def findConnectivity(heights, i, j, p, q, bag):
    if (i < 0 or j < 0 or i >= len(heights) or j >= len(heights[0]) or heights[i][j - 1] > heights[i][j] or
            heights[i - 1][j] > heights[i][j] or heights[i][j + 1] > heights[i][j] or heights[i + 1][j] > heights[i][
                j]):
        return false;

    if i == 0 or j == 0 or i == len(heights) - 1 or j == len(heights[0])

    # if any cell is reached to the other side add it into the bag

    if (findConnectivity(heights, i - 1, j, bag) and findConnectivity(heights, i, j - 1, bag)) and (
            findConnectivity(heights, i, j + 1, bag) and findConnectivity(heights, i + 1, j, bag))

        bag.append([i, j])


for i in range(len(heights)):
    for j in range(len(heights[0]):
        bag = []
    p = False
    a = False
    findConnectivity(heights, i, j, p, q, bag);

    print(bag)

    # 1 1 1 5
    # 5 5 3 5
    # 5 4 5 5
    # 5 5 5 5
    # 5 5 5 5

    #
    # Your previous Java content is preserved below:
    #
    # /*
    #  * Click `Run` to execute the snippet below!
    #  */
    #
    # import java.io.*;
    # import java.util.*;
    #
    # /*
    #  * To execute Java, please define "static void main" on a class
    #  * named Solution.
    #  *
    #  * If you need more classes, simply define them inline.
    #  */
    #
    # class Solution {
    #   public static void main(String[] args) {
    #     ArrayList<String> strings = new ArrayList<String>();
    #     strings.add("Hello, World!");
    #     strings.add("Welcome to CoderPad.");
    #     strings.add("This pad is running Java " + Runtime.version().feature());
    #
    #     for (String string : strings) {
    #       System.out.println(string);
    #     }
    #   }
    # }
    #
    #
    # /*
    # Your previous Plain Text content is preserved below:
    #
    # This is just a simple shared plaintext pad, with no execution capabilities.
    #
    # When you know what language you'd like to use for your interview,
    # simply choose it from the dropdown in the top bar.
    #
    # You can also change the default language your pads are created with
    # in your account settings: https://app.coderpad.io/settings
    #
    # Enjoy your interview!
    #
    # ====================
    #
    # Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    # Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    #
    # You are given an m x n integer matrix heights representing the height of each unit cell in a continent. The Pacific ocean touches the continent's left and top edges, and the Atlantic ocean touches the continent's right and bottom edges.
    #
    # Water can only flow in four directions: up, down, left, and right. Water flows from a cell to an adjacent one with an equal or lower height.
    #
    # Return a list of grid coordinates where water can flow to both the Pacific and Atlantic oceans.
    #
    #

    # p p p p p p
    # p 1 2 9 3 5 a
    # p 3 6 3 4 4 a
    # p 2 8 5 3 1 a
    # p 6 7 1 4 5 a
    # p 1 1 1 2 4 a
    #   a a a a a

    #
    #
    # for each cell in my 2d array:
    #
    #
    #
    # example 2:
    # Input: heights = [[2,1],[1,2]]
    # Output: [[0,0],[0,1],[1,0],[1,1]]
    #  */
