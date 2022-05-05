import json
import os
import re
import subprocess
from zipfile import ZipFile
import shutil
import matplotlib.pyplot as plt
import pathlib

fmuDir = os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir), "FMUs")

def plot_data(data, resultsPath):
    for i in range(1,8):
        plt.plot(data["time"], data["{QuarterCar}.qcar.x["+str(i)+"]"], label=f"x[{i}]")
    plt.legend()
    plt.title("QuarterCar x")
    plt.savefig(os.path.join(resultsPath, "results_qcar.pdf"))

    plt.figure()
    plt.plot(data["time"], data["{QuarterCar}.qcar.RattleAcc"], label=f"RattleAcc")
    plt.legend()
    plt.title("QuarterCar RattleAcc")
    plt.savefig(os.path.join(resultsPath, "results_qcar_acc.pdf"))

    plt.figure()
    plt.title("Damper Force")
    plt.plot(data["time"], data["{Damper}.damper.DamperForce_N_"], label=f"damper_force")
    plt.savefig(os.path.join(resultsPath, "results_damper.pdf"))


def removeIfExists(fileOrDirectory):
    if os.path.exists(fileOrDirectory):
        if os.path.isfile(fileOrDirectory):
            os.remove(fileOrDirectory)
        else:
            shutil.rmtree(fileOrDirectory)

def zipdir(output_filename, path):
    zipf = ZipFile(output_filename, 'w')
    length = len(path)

    for root, dirs, files in os.walk(path):
        folder = root[length:]  # path without "parent"
        for file in files:
            zipf.write(os.path.join(root, file), os.path.join(folder, file))
    zipf.close()

def printSection(section):
    hashes = "###############################"
    print("\n" + hashes)
    print(section)
    print(hashes)

def getMaestroJarPath():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), "maestro.jar"))
    if not os.path.exists(path):
        raise Exception("maestro.jar needs to be located in the same folder as utils.py")
    return path

def getMultiModelWithFMUPaths(multiModelPath, resultsPath):
    with open(multiModelPath) as f:
        multiModel = json.load(f)

    for fmu in multiModel["fmus"]:
        fmuNameMatch = re.match("{(\w+)}", fmu)
        assert len(fmuNameMatch.groups()) == 1, f"Problem extracting fmu name from FMU key {fmu}. Name should be { '{FMUName}' }."
        assert os.path.isdir(fmuDir), f"Problem finding fmu directory {fmuDir}."
        fmuName = fmuNameMatch.groups()[0]
        fmuPath = os.path.join(fmuDir, f"{fmuName}.fmu")
        fmuPath = os.path.normpath(fmuPath)
        multiModel["fmus"][fmu] = pathlib.Path(fmuPath).as_uri()

    correctedMultiModelPath = os.path.join(resultsPath, "multiModel.json")

    with open(correctedMultiModelPath, "w") as f:
        json.dump(multiModel, f)

    return correctedMultiModelPath


def execCliCommand(cmd, callBack, cwd=None):
    print("Cmd: " + cmd)
    p = subprocess.run(cmd, shell=True, cwd=cwd)
    if p.returncode != 0:
        raise Exception(f"Error executing {cmd}")
    else:
        callBack()