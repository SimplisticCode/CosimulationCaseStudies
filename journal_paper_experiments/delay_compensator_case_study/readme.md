# Environment

To run the examples, you need (see also script [setup_dev.ps1](Examples/setup_dev.ps1)):
- Python Version 3.9.x
- Python packages: see [requirements.txt](./Examples/requirements.txt)
- Java 11

If you want to run the FMUs in Linux, then you need to use docker. 
Install docker and run the following:
- build images: `docker-compose build`
- start interactive shell: `docker-compose.exe run --rm delaycompensator`

Then run the python script as you would from your host machine.

# Examples

The folder [Examples](./Examples) contains the Maestro co-simulation jar, common python utility files and subfolders with the individual examples.

There are two ways to run the examples: 
- run all examples as batch -- ideal for checking that everything is working as it should. Plotting, printing, etc... are disabled.
- run individual examples -- ideal for development

## Running All Examples As Batch

```
python run_all_examples.py
```
or, if on linux or mac,
```
python3 run_all_examples.py
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


