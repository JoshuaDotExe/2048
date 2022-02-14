from tfe import twenty_forty_eight
import numpy as np
import unittest

class TestTFE(unittest.TestCase):
    
    def setUp(self) -> None:
        self.boardOne = twenty_forty_eight(1)
        self.boardOne.board = np.array([[16, 0, 4, 4],
                                   [0, 2, 0, 0],
                                   [0, 4, 4, 4],
                                   [16, 8, 8, 0]])
        self.boardTwo = twenty_forty_eight(2)
        self.boardTwo.board = np.array([[2, 4, 4, 2],
                                   [4, 8, 8, 4],
                                   [4, 8, 8, 4],
                                   [2, 4, 4, 2]])
        self.boardThr = twenty_forty_eight(3)
        self.boardThr.board = np.array([[2, 4, 8, 16],
                                   [2, 4, 8, 16],
                                   [2, 4, 8, 16],
                                   [2, 4, 8, 16]])

    def test_arr_transpose(self):
        self.boardOne.arr_transpose(0)
        self.assertEqual(self.boardOne.board.tolist(), np.array([[16, 0, 4, 4],
                                                            [0, 2, 0, 0],
                                                            [0, 4, 4, 4],
                                                            [16, 8, 8, 0]]).tolist())
        self.boardOne.arr_transpose(3)
        self.assertEqual(self.boardOne.board.tolist(), np.array([[16, 0, 0, 16],
                                                            [8, 4, 2, 0],
                                                            [8, 4, 0, 4],
                                                            [0, 4, 0, 4]]).tolist())
        self.boardTwo.arr_transpose(2)
        self.assertEqual(self.boardTwo.board.tolist(), np.array([[2, 4, 4, 2],
                                                            [4, 8, 8, 4],
                                                            [4, 8, 8, 4],
                                                            [2, 4, 4, 2]]).tolist())
        self.boardThr.arr_transpose(1)
        self.assertEqual(self.boardThr.board.tolist(), np.array([[16, 16, 16, 16],
                                                            [8, 8, 8, 8],
                                                            [4, 4, 4, 4],
                                                            [2, 2, 2, 2]]).tolist())

    def test_move(self):
        self.boardOne.move(0)
        self.boardTwo.move(0)
        self.boardThr.move(0)
        self.assertEqual(self.boardOne.board.tolist(), np.array([[32, 2, 16, 8],
                                                            [0, 4, 0, 0],
                                                            [0, 8, 0, 0],
                                                            [0, 0, 0, 0]]).tolist())
        self.assertEqual(self.boardTwo.board.tolist(), np.array([[2, 4, 4, 2],
                                                            [8 , 16, 16, 8],
                                                            [2, 4, 4, 2],
                                                            [0, 0, 0, 0]]).tolist())
        self.assertEqual(self.boardThr.board.tolist(), np.array([[4, 8, 16, 32],
                                                            [4, 8, 16, 32],
                                                            [0, 0, 0, 0],
                                                            [0, 0, 0, 0]]).tolist())
    
    def test_empty_spaces(self):
        self.assertEqual(self.boardOne.empty_spaces(), {1: (0,1), 2: (1,0), 3: (1,2), 4: (1,3), 5: (2,0), 6: (3,3)})
        self.assertEqual(self.boardTwo.empty_spaces(), {})

if __name__ == '__main__':
    unittest.main()