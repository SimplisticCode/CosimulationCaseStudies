# Environment

To run the examples, you need (see also script [setup_dev.ps1](Examples/setup_dev.ps1)):
- Python Version 3.9.x
- Python packages: see [requirements.txt](./Examples/requirements.txt)
- Java 11
- Verification and trace visualization requires UPPAAL Version 4.1 with bin in PATH.

# FMUS
 - Located in FMUS.
 - Should not be renamed as it will break examples.

# Examples

The folder [Examples](./Examples) contains the Maestro co-simulation jar, common python utility files and subfolders with the individual examples.

There are two ways to run the examples: 
- run all examples as batch -- ideal for checking that everything is working as it should. Plotting, printing, etc... are disabled.
- run individual examples -- ideal for development

## Running All Examples As Batch

```
python run_all_examples.py
```

## Running Individual Examples

Examples should be executed from their folders, e.g. [execute algorithm](./Examples/execute_algorithm).

Each example folder includes both `test.py` which can be executed to run the concrete example and either a `scenario.conf` or a `mastermodel.conf` which defines the scenario.

During example execution relevant test information is displayed in the console.

### Execute_algorithm

Example of executing an algorithm generated from a [scenario](./Examples/execute_algorithm/scenario.conf)

First the example generates a master model (defining both the scenario and algorithm) by calling the Maestro CLI with the scenario file and places the master model in the results folder. The example then passes the resulting master model, the [multi model](./Examples/execute_algorithm/multiModel.json) and execution parameters in its call to the Maestro CLI to execute the algorithm.

Then any resulting execution artifacts are placed in a results folder, this includes a MaBL spec, output values and fmu logs. Lastly the output is plotted and a graf is displayed.

The file [executionParameters](./Examples/execute_algorithm/executionParameters.json) can be configured as needed (e.g. step size and start and stop time for the execution).
The file [multiModel](./Examples/execute_algorithm/multiModel.json) should not be changed as the example ensures that the correct FMU paths are inserted into the file as needed.
The file [scenario](./Examples/execute_algorithm/scenario.conf) defines a scenario with a name, the scenario, but no initialization or cosim-step instructions are present as these are part of the algorithm which is being generated as part of the example.

### Generate_algorithm_from_scenario

Example of generating an algorithm from a [scenario](./Examples/generate_algorithm_from_scenario/scenario.conf).

The test example calls the Maestro CLI with the scenario file.

The resulting master model which contains both the scenario and algorithm is placed in a results folder.

The scenario.conf file can be changed as needed.

### Verify_algorithm

Example of verifying an algorithm. Requires UPPAAL in PATH.

The example calls the Maestro CLI with the [master model file](./Examples/verify_algorithm/masterModel.conf).

This prints a message in the shell indicating if the master model is successfully verified or not.

In this example there is introduced an error in the algorithm in the mater model file, so it should not verify.

### Visualize_traces

Example of visualizing possible traces generated from verification. Requires UPPAAL in PATH.

The example calls the Maestro CLI with the [master model file](./Examples/visualize_traces/masterModel.conf).

As there is introduced an error in the algorithm in the mater model file, this call returns an mp4 that visualizes the traces.



