class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        self.markGridTwo(grid)
        
        color = 2
        while True:
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == color:
                        if (self.expand(grid, i + 1, j, color) or
                            self.expand(grid, i - 1, j, color) or
                            self.expand(grid, i, j + 1, color) or
                            self.expand(grid, i, j - 1, color)):
                            return color - 2
            color += 1
    
    def markGridTwo(self, grid: List[List[int]]) -> None:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.markGridTwoHelper(grid, i, j)
                    return
    
    def markGridTwoHelper(self, grid: List[List[int]], i: int, j: int) -> None:
        if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]):
            return
        if grid[i][j] != 1:
            return
        grid[i][j] = 2
        self.markGridTwoHelper(grid, i + 1, j)
        self.markGridTwoHelper(grid, i - 1, j)
        self.markGridTwoHelper(grid, i, j + 1)
        self.markGridTwoHelper(grid, i, j - 1)
    
    def expand(self, grid: List[List[int]], i: int, j: int, color: int) -> bool:
        if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]):
            return False
        if grid[i][j] == 0:
            grid[i][j] = color + 1
        return grid[i][j] == 1
