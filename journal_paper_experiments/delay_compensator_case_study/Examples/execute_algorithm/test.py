import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
import utils

resourcesPath = os.path.dirname(__file__)
multiModelPath = os.path.join(resourcesPath, "multiModel.json")
resultsPath = os.path.join(resourcesPath, "results")
masterModelPath = os.path.join(resultsPath, "masterModel.conf")
executionParametersPath = os.path.join(resourcesPath, "executionParameters.json")


def executeAlgorithm(batch_mode, maestroJarPath):
    utils.removeIfExists(resultsPath)
    os.mkdir(resultsPath)

    utils.printSection("GENERATING ALGORITHM")

    scenarioPath = os.path.join(resourcesPath, "scenario.conf")
    cmd = "java -jar {0} sigver generate-algorithm {1} -output {2}".format(maestroJarPath, scenarioPath, resultsPath)
    callBack = lambda: print("Successfully written algorithm to masterModel.conf") if(masterModelPath) else lambda: (Exception("Master model was not generated"))
    utils.execCliCommand(cmd, callBack)

    utils.printSection("EXECUTING ALGORITHM")

    multiModel = utils.getMultiModelWithFMUPaths(multiModelPath, resultsPath)

    cmd = "java -jar {0} sigver execute-algorithm -mm {1} -ep {2} -al {3} -output {4} -vim FMI2".format(maestroJarPath, multiModel, executionParametersPath, masterModelPath, resultsPath)
    callBack = lambda: print(f"Results of execution are located in {resultsPath}") if(os.path.exists(os.path.join(resultsPath, "outputs.csv"))) else lambda: (Exception("No output was returned from executing the algorithm"))
    utils.execCliCommand(cmd, callBack)
        
    # Plot
    print("Plotting results...")
    results = pd.read_csv(os.path.join(resultsPath, "outputs.csv"))
    utils.plot_data(results, resultsPath)
    if not batch_mode:
        plt.show()

if __name__ == '__main__':
    executeAlgorithm(False, utils.getMaestroJarPath())
