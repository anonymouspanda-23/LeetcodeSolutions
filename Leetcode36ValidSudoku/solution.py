from typing import List


class Solution:
    # The question can be viewed at https://leetcode.com/problems/valid-sudoku/description/

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Set all flags to true by default.
        rows_valid = True
        cols_valid = True
        grids_valid = True

        # Loop through all the rows in the board and validate them.
        for row in range(len(board)):
            rows_valid &= self.validate_row(board, row)

        # If not all rows are valid, the remaining checks need not be performed. Immediately return false.
        if not rows_valid:
            return False

        # Loop through all the columns in the board and validate them.
        for col in range(len(board[0])):
            cols_valid &= self.validate_column(board, col)

        # If not all columns are valid, the remaining checks need not be performed. Immediately return false.
        if not cols_valid:
            return False

        # Loop through all 3x3 grids in the board and validate them.
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                grids_valid &= self.validate_grid(board, row, col)

        # Return the value of the last check.
        return grids_valid

    def validate_row(self, board: List[List[str]], row: int) -> bool:
        """
        This function returns true if the entire row is valid and false otherwise.
        :param board: A sudoku board.
        :param row: The index of the column to be validated.
        :return: A boolean value denoting if the row is valid or now.
        """
        # Initialize an empty set to store values which have been encountered.
        unique_values = set()

        # Iterate through all the tiles in a given row of the sudoku board.
        for value in board[row]:
            # If the value of the tile has not been set yet, the tile need not be checked.
            if value == ".":
                continue

            # If the value of the tile has been encountered earlier in the row, the row is invalid, hence it immediately
            # returns false.
            if value in unique_values:
                return False

            # Else add the value of the tile to the set.
            unique_values.add(value)

        # If the code runs until this point, the row being checked is valid.
        return True

    def validate_column(self, board: List[List[str]], col: int) -> bool:
        """
        This function returns true if the entire column is valid and false otherwise.
        :param board: A sudoku board.
        :param col: The index of the column to be validated.
        :return: A boolean value denoting if the column is valid or not.
        """
        # Initialize an empty set to store values which have been encountered.
        unique_values = set()

        # Iterate through all the tiles in a given column of the sudoku board.
        for row in range(len(board)):
            column_value = board[row][col]

            # If the value of the tile has not been set yet, the tile need not be checked.
            if column_value == ".":
                continue

            # If the value of the tile has been encountered earlier in the column, the column is invalid, hence it
            # immediately returns false.
            if column_value in unique_values:
                return False

            # Else add the value of the tile to the set.
            unique_values.add(column_value)

        # If the code runs until this point, the column being checked is valid
        return True

    def validate_grid(self, board: List[List[str]], row: int, col: int) -> bool:
        """
        This function returns true if the current 3x3 grid is valid and false otherwise.
        :param board: A sudoku board.
        :param row: The start row index of the grid to validate.
        :param col: The start col index of the row to validate.
        :return: A boolean value denoting if the 3x3 grid is valid or not.
        """
        # Initialize an empty set to store values which have been encountered.
        unique_values = set()

        # The following 2 lines are a redundancy to ensure that the starting row and column will be correct even if the
        # values passed to the function do not actually reference the correct start row and column of the sudoku board.
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3

        # Iterate through all the tiles in a given 3x3 grid of the sudoku board.
        for row in range(start_row, start_row + 3):
            for col in range(start_col, start_col + 3):
                tile_value = board[row][col]

                # If the value of the tile has not been set yet, the tile need not be checked.
                if tile_value == ".":
                    continue

                # If the value of the tile has been encountered earlier in the grid, the grid is invalid, hence it
                # immediately returns false.
                if tile_value in unique_values:
                    return False

                # Else add the value of the tile to the set.
                unique_values.add(tile_value)

        # If the code runs until this point, the 3x3 grid being checked is valid.
        return True
