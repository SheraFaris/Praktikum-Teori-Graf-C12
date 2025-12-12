class TreeNode:
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.children = []
        self.sequence = [value]
    
    def add_child(self, child):
        self.children.append(child)

def build_tree(arr, index, parent_sequence):
    node = TreeNode(arr[index], index)
    node.sequence = parent_sequence + [arr[index]]
    
    
    for i in range(index + 1, len(arr)):
        if arr[i] > arr[index]:
            child = build_tree(arr, i, node.sequence)
            node.add_child(child)
    
    return node

def find_lmis(arr):
    
    
    if not arr:
        return []
    
    
    roots = []
    for i in range(len(arr)):
        root = build_tree(arr, i, [])
        roots.append(root)
    
    
    longest = []
    
    def dfs(node):
        nonlocal longest
        
        if len(node.sequence) > len(longest):
            longest = node.sequence.copy()
        
        for child in node.children:
            dfs(child)
    
    
    for root in roots:
        dfs(root)
    
    return longest

def print_tree(node, prefix="", is_last=True):
    print(prefix + ("└── " if is_last else "├── ") + str(node.value))
    
    for i, child in enumerate(node.children):
        extension = "    " if is_last else "│   "
        print_tree(child, prefix + extension, i == len(node.children) - 1)

def main():
    print("=" * 60)
    print("LARGEST MONOTONICALLY INCREASING SUBSEQUENCE (LMIS) by C12")
    print("=" * 60)
    print()
    
    
    print("Masukkan array (pisahkan dengan koma):")
    print("Contoh: 4, 1, 13, 7, 0, 2, 8, 11, 3")
    user_input = input("Input: ")
    
    try:
        
        arr = [int(x.strip()) for x in user_input.split(',')]
        
        print("\n" + "=" * 60)
        print(f"Array original: {arr}")
        print("=" * 60)
        
        
        result = find_lmis(arr)
        
        print("\n" + "=" * 60)
        print("HASIL:")
        print("=" * 60)
        print(f"LMIS: {result}")
        print(f"Panjang: {len(result)}")
        print("=" * 60)
        
        
        print("\nIngin melihat visualisasi tree? (y/n): ", end="")
        show_tree = input().lower()
        
        if show_tree == 'y':
            print("\n" + "=" * 60)
            print("VISUALISASI TREE (5 root pertama):")
            print("=" * 60)
            
            roots = []
            for i in range(min(5, len(arr))):
                root = build_tree(arr, i, [])
                roots.append(root)
            
            for i, root in enumerate(roots):
                print(f"\nRoot {i+1} (value={root.value}):")
                print_tree(root)
        
    except ValueError:
        print("\nError: Input tidak valid! Pastikan format benar.")
    except Exception as e:
        print(f"\nError: {e}")


def find_lmis_dp(arr):
    if not arr:
        return []
    
    n = len(arr)
    
    dp = [[arr[i]] for i in range(n)]
    
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and len(dp[j]) + 1 > len(dp[i]):
                dp[i] = dp[j] + [arr[i]]
    
    
    return max(dp, key=len)


def test_examples():
    print("=" * 60)
    print("TESTING DENGAN CONTOH-CONTOH")
    print("=" * 60)
    
    test_cases = [
        [4, 1, 13, 7, 0, 2, 8, 11, 3],
        [10, 9, 2, 5, 3, 7, 101, 18],
        [0, 1, 0, 3, 2, 3],
        [7, 7, 7, 7],
        [1, 2, 3, 4, 5]
    ]
    
    for i, arr in enumerate(test_cases, 1):
        result = find_lmis(arr)
        print(f"\nTest {i}:")
        print(f"  Input:  {arr}")
        print(f"  LMIS:   {result}")
        print(f"  Length: {len(result)}")

if __name__ == "__main__":
    
    main()  
    