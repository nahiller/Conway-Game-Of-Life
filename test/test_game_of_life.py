import enum
import unittest
from src.gameoflife import *

DEAD = CellState.DEAD 
ALIVE = CellState.ALIVE

class GameOfLifeTests(unittest.TestCase):
  def test_Canary(self): 
    self.assertTrue(True)

  def test_dead_cell_behavior(self):
    number_of_live_neighbors_and_next_state = [(0, DEAD), (1, DEAD), (2, DEAD), (5, DEAD), (8, DEAD), (3, ALIVE)]
    
    for number_of_live_neighbors, next_state in number_of_live_neighbors_and_next_state:
      with self.subTest(msg = "next_cell_state for number_of_live_neighbors", number_of_live_neighbors = number_of_live_neighbors):          
        self.assertEqual(next_state, next_generation_status(DEAD, number_of_live_neighbors))

  def test_live_cell_behavior(self):
    number_of_live_neighbors_and_next_state = [(1, DEAD), (4, DEAD), (8, DEAD), (2, ALIVE), (3, ALIVE)]

    for number_of_live_neighbors, next_state in number_of_live_neighbors_and_next_state:
      with self.subTest(msg = "next_cell_state for number_of_live_neighbors", number_of_live_neighbors = number_of_live_neighbors):
        self.assertEqual(next_state, next_generation_status(ALIVE, number_of_live_neighbors))

  def test_generate_signal_for_a_cell_from_position_2_3(self):
    self.assertEqual([(1, 2), (1, 3), (1, 4), (2, 2), (2, 4), (3, 2), (3, 3), (3, 4)], generate_signal_for_a_cell((2, 3)))

  def test_generate_signal_for_a_cell_from_position_3_3(self):
    self.assertEqual([(2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4)], generate_signal_for_a_cell((3, 3)))

  def test_generate_signal_for_a_cell_from_position_2_4(self):
    self.assertEqual([(1, 3), (1, 4), (1, 5), (2, 3), (2, 5), (3, 3), (3, 4), (3, 5)], generate_signal_for_a_cell((2, 4)))

  def test_generate_signal_for_a_cell_from_position_0_0(self):
    self.assertEqual([(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)], generate_signal_for_a_cell((0, 0)))

  def test_no_position_generate_signals_returns_empty_list(self):
    self.assertEqual([], generate_signal_for_cells(()))

  def test_one_position_generate_signal_for_a_cellreturns_8_positions(self):
    self.assertEqual([(1, 3), (1, 4), (1, 5), (2, 3), (2, 5), (3, 3), (3, 4), (3, 5)], generate_signal_for_cells([(2, 4)]))
    
  def test_two_position_generate_signal_for_a_cellreturns_16_positions(self):
    self.assertEqual([(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 4), (3, 2), (3, 3), (3, 4)], generate_signal_for_cells([(0, 0),(2, 3)]))
    
  def test_three_position_generate_signal_for_a_cellreturns_24_positions(self):
    self.assertEqual([(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 4), (3, 2), (3, 3), (3, 4), (2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4)], generate_signal_for_cells([(0, 0),(2, 3),(3, 3)]))
    
  def test_count_live_neighbors_returns_empty_map_given_no_positions(self):
    self.assertEqual({}, count_live_neighbors([]))

  def test_count_live_neigbors_returns_position_with_one_count_given_one_position(self):
    self.assertEqual({(2, 3): 1}, count_live_neighbors([(2, 3)]))
  
  def test_count_live_neighbors_returns_position_with_count_two_given_one_position_twice(self):
    self.assertEqual({(2, 4): 2}, count_live_neighbors([(2, 4), (2, 4)]))

  def test_count_live_neighbors_returns_one_position_with_count_two_and_another_with_count_one_given_one_position_twice_and_another_once(self):
    self.assertEqual({(2, 4): 2, (1, 3): 1}, count_live_neighbors([(2, 4), (1, 3), (2, 4)]))

  def test_block_returns_same_block_next_generation(self):
    self.assertCountEqual([(0, 0), (0, 1), (1, 0), (1, 1)], compute_next_generation(([(0, 0), (0, 1), (1, 0), (1, 1)])))

  def test_beehive_returns_same_beehive_next_generation(self):
    self.assertCountEqual([(1, 0), (0, 1), (0, 2), (1, 3), (2, 1), (2, 2)], compute_next_generation(([(1, 0), (0, 1), (0, 2), (1, 3), (2, 1), (2, 2)])))

  def test_horizontal_blinker_returns_vertical_blinker_next_generation(self):
    self.assertCountEqual([(2, 2), (2, 1), (2, 3)], compute_next_generation([(1, 2), (2, 2), (3, 2)]))
 
  def test_vertical_blinker_returns_horizontal_blinker_next_generation(self):
    self.assertCountEqual([(2, 2), (1, 2), (3, 2)], compute_next_generation([(2, 1), (2, 2), (2, 3)]))

  def test_glider_with_one_live_cell_at_the_top_returns_the_live_cell_moving_to_the_right(self):
    self.assertCountEqual([(2, 2), (1, 3), (2, 3), (0, 2), (1, 4)], compute_next_generation([(1, 1), (2, 2), (0, 3), (1, 3), (2, 3)]))

  def test_empty_list_returns_0_0_and_100_100_from_get_bounds(self):
    self.assertEqual([(0, 0), (100, 100)], get_bounds([]))

  def test_one_point_returns_neg10_and_pos10_from_get_bounds(self):
    self.assertEqual([(10, 5), (30, 25)], get_bounds([(20, 15)]))

  def test_two_points_return_neg10_and_pos10_from_get_bounds(self):
    self.assertEqual([(10, 5), (60, 35)], get_bounds([(20, 15), (50, 25)]))

  def test_three_points_return_neg10_and_pos10_from_get_bounds(self):
    self.assertEqual([(10, 5), (85, 53)], get_bounds([(20, 25), (50, 15), (75, 43)]))

  def test_four_points_return_neg10_and_pos10_from_get_bounds(self):
    self.assertEqual([(10, 5), (85, 92)], get_bounds([(20, 15), (50, 25), (75, 43), (22, 82)]))
  
if __name__ == '__main__': 
  unittest.main()
