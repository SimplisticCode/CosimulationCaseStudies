import unittest

import utils
from execute_algorithm.test import executeAlgorithm


class TestAllExamples(unittest.TestCase):
    jarPath = utils.getMaestroJarPath()

    def test_execute_algorithm(self):
        batch_mode = True
        executeAlgorithm(batch_mode, self.jarPath)


if __name__ == '__main__':
    unittest.main()

