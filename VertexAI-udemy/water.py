"""
Container With Most Water Problem

You are given an integer array height of length n. There are n vertical lines 
drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the 
container contains the most water.

Return the maximum amount of water a container can store.

Example:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
    In this case, the max area of water (blue section) the container can contain is 49.

Algorithm: Two Pointer Approach
- Start with two pointers at the beginning and end of the array
- Calculate the area between these two lines
- Move the pointer with the smaller height inward
- Keep track of the maximum area found
"""

def max_area(height):
    """
    Find the maximum amount of water that can be contained.
    
    Args:
        height (List[int]): Array representing the height of vertical lines
    
    Returns:
        int: Maximum amount of water that can be stored
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not height or len(height) < 2:
        return 0
    
    left = 0  # Left pointer
    right = len(height) - 1  # Right pointer
    max_water = 0
    
    while left < right:
        # Calculate the width between the two lines
        width = right - left
        
        # Calculate the height (limited by the shorter line)
        current_height = min(height[left], height[right])
        
        # Calculate the area (water that can be stored)
        current_area = width * current_height
        
        # Update maximum area if current area is larger
        max_water = max(max_water, current_area)
        
        # Move the pointer with the smaller height inward
        # This is the key insight: moving the taller line won't help
        # because the area is limited by the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water


def max_area_brute_force(height):
    """
    Brute force solution for comparison (O(n²) time complexity).
    
    Args:
        height (List[int]): Array representing the height of vertical lines
    
    Returns:
        int: Maximum amount of water that can be stored
    """
    if not height or len(height) < 2:
        return 0
    
    max_water = 0
    n = len(height)
    
    for i in range(n):
        for j in range(i + 1, n):
            width = j - i
            current_height = min(height[i], height[j])
            current_area = width * current_height
            max_water = max(max_water, current_area)
    
    return max_water


def visualize_container(height, left_idx, right_idx):
    """
    Visualize the container formed by two lines.
    
    Args:
        height (List[int]): Array representing the height of vertical lines
        left_idx (int): Index of left line
        right_idx (int): Index of right line
    """
    print(f"\nContainer between index {left_idx} and {right_idx}:")
    print(f"Left line height: {height[left_idx]}")
    print(f"Right line height: {height[right_idx]}")
    print(f"Width: {right_idx - left_idx}")
    print(f"Water height: {min(height[left_idx], height[right_idx])}")
    print(f"Water area: {(right_idx - left_idx) * min(height[left_idx], height[right_idx])}")


# Test cases
def test_max_area():
    """Test the max_area function with various test cases."""
    
    test_cases = [
        {
            "height": [1, 8, 6, 2, 5, 4, 8, 3, 7],
            "expected": 49,
            "description": "Example case"
        },
        {
            "height": [1, 1],
            "expected": 1,
            "description": "Two equal lines"
        },
        {
            "height": [4, 3, 2, 1, 4],
            "expected": 16,
            "description": "Symmetric case"
        },
        {
            "height": [1, 2, 1],
            "expected": 2,
            "description": "Three lines"
        },
        {
            "height": [1, 2, 4, 3],
            "expected": 4,
            "description": "Four lines"
        },
        {
            "height": [],
            "expected": 0,
            "description": "Empty array"
        },
        {
            "height": [5],
            "expected": 0,
            "description": "Single line"
        }
    ]
    
    print("Testing Container With Most Water Algorithm")
    print("=" * 50)
    
    for i, test in enumerate(test_cases, 1):
        height = test["height"]
        expected = test["expected"]
        description = test["description"]
        
        # Test optimized solution
        result_optimized = max_area(height)
        
        # Test brute force solution (only for small arrays to avoid timeout)
        if len(height) <= 10:
            result_brute_force = max_area_brute_force(height)
            match_brute_force = result_brute_force == expected
        else:
            result_brute_force = "Skipped (too large)"
            match_brute_force = True
        
        match_optimized = result_optimized == expected
        
        print(f"\nTest {i}: {description}")
        print(f"Input: {height}")
        print(f"Expected: {expected}")
        print(f"Optimized result: {result_optimized} {'✓' if match_optimized else '✗'}")
        print(f"Brute force result: {result_brute_force} {'✓' if match_brute_force else '✗'}")
        
        if not match_optimized:
            print(f"❌ TEST FAILED!")
        else:
            print(f"✅ Test passed!")


def find_optimal_container(height):
    """
    Find and display the optimal container configuration.
    
    Args:
        height (List[int]): Array representing the height of vertical lines
    """
    if not height or len(height) < 2:
        print("Need at least 2 lines to form a container!")
        return
    
    left = 0
    right = len(height) - 1
    max_water = 0
    best_left = 0
    best_right = 0
    
    print(f"\nFinding optimal container for: {height}")
    print("Step-by-step process:")
    print("-" * 40)
    
    step = 1
    while left < right:
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height
        
        print(f"Step {step}: left={left}(h={height[left]}), right={right}(h={height[right]})")
        print(f"         width={width}, height={current_height}, area={current_area}")
        
        if current_area > max_water:
            max_water = current_area
            best_left = left
            best_right = right
            print(f"         *** NEW MAXIMUM! ***")
        
        if height[left] < height[right]:
            left += 1
            print(f"         Moving left pointer → {left}")
        else:
            right -= 1
            print(f"         Moving right pointer → {right}")
        
        step += 1
        print()
    
    print(f"OPTIMAL SOLUTION:")
    print(f"Best container: lines at index {best_left} and {best_right}")
    print(f"Heights: {height[best_left]} and {height[best_right]}")
    print(f"Maximum water: {max_water}")
    
    return max_water, best_left, best_right


if __name__ == "__main__":
    # Run tests
    test_max_area()
    
    # Interactive example
    print("\n" + "=" * 60)
    print("INTERACTIVE EXAMPLE")
    print("=" * 60)
    
    # Example from the problem
    example_height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    max_water, left_idx, right_idx = find_optimal_container(example_height)
    
    # Visualize the optimal solution
    print("\n" + "=" * 40)
    print("VISUALIZATION OF OPTIMAL SOLUTION")
    print("=" * 40)
    visualize_container(example_height, left_idx, right_idx)
    
    print("\n" + "=" * 60)
    print("Try with your own input!")
    print("Example: python water.py")
    print("Then modify the example_height array in the code")
