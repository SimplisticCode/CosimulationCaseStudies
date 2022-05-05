import unittest

import utils
from execute_algorithm.test import executeAlgorithm
from generate_algorithm_from_scenario.test import generateAlgorithmFromScenario
from verify_algorithm.test import verifyAlgorithm
from visualize_traces.test import visualizeTraces


class TestAllExamples(unittest.TestCase):
    jarPath = utils.getMaestroJarPath()

    def test_execute_algorithm(self):
        batch_mode = True
        executeAlgorithm(batch_mode, self.jarPath)

    def test_generate_algorithm_from_scenario(self):
        generateAlgorithmFromScenario(self.jarPath)

    def test_verify_algorithm(self):
        verifyAlgorithm(self.jarPath)

    def test_visualize_traces(self):
        visualizeTraces(self.jarPath)


if __name__ == '__main__':
    unittest.main()

