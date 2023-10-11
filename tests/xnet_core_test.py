import unittest
import igraph as ig
import xnetwork as xn

class TestXnetCore(unittest.TestCase):

    def test_load(self):
        # Create a sample xnet file
        fileName = 'test.xnet'
        with open(fileName, 'w') as f:
            f.write('#vertices 4\n')
            f.write('"A"\n')
            f.write('"B"\n')
            f.write('"C"\n')
            f.write('"D"\n')
            f.write('#edges weighted directed\n')
            f.write('0 1 0.5\n')
            f.write('1 2 1.0\n')
            f.write('2 3 1.5\n')
            f.write('3 0 2.0\n')

        # Load the graph from the file
        g = xn.load(fileName)

        # Check the contents of the graph
        self.assertEqual(g.vcount(), 4)
        self.assertEqual(g.ecount(), 4)
        self.assertEqual(g.vs['name'], ['A', 'B', 'C', 'D'])
        self.assertEqual(g.es['weight'], [0.5, 1.0, 1.5, 2.0])

    def test_save(self):
        # Create a sample igraph object
        g = ig.Graph([(0,1), (1,2), (2,3), (3,0)], directed=True)
        g.vs['name'] = ['A', 'B', 'C', 'D']
        g.es['weight'] = [0.5, 1.0, 1.5, 2.0]

        # Save the graph to a file
        fileName = 'test.xnet'
        xn.save(g, fileName)

        # Load the graph from the file
        with open(fileName, 'r') as f:
            lines = f.readlines()

        # Check the contents of the file
        self.assertEqual(lines[0], '#vertices 4\n')
        self.assertEqual(lines[1], '"A"\n')
        self.assertEqual(lines[2], '"B"\n')
        self.assertEqual(lines[3], '"C"\n')
        self.assertEqual(lines[4], '"D"\n')
        self.assertEqual(lines[5], '#edges weighted directed\n')
        self.assertEqual(lines[6], '0 1 0.5\n')
        self.assertEqual(lines[7], '1 2 1.0\n')
        self.assertEqual(lines[8], '2 3 1.5\n')
        self.assertEqual(lines[9], '3 0 2.0\n')

if __name__ == '__main__':
    unittest.main()
