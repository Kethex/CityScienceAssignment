import unittest
import Dijkstra


class TestDijkstra(unittest.TestCase):
    
    def test_example(self):
        path = Dijkstra.dijkstra("exmouth-links.dat", "J1053", "J1037")
        self.assertEqual(path, ['J1053', 'J1035', 'J1036', 'J1037'])
        
        path_to_itself = Dijkstra.dijkstra("exmouth-links.dat", "J1053", "J1053")
        self.assertEqual(path_to_itself, ['J1053'])
        
    def test_node(self):
        with self.assertRaises(KeyError):
            Dijkstra.dijkstra("exmouth-links.dat", "J1053", "Y3284")
            
            
if __name__ == '__main__':
    unittest.main()
        