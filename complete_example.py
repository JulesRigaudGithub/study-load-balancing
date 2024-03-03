"""Complete example of use of the simulator.

To run, use 'python3 complete_example.py'.

This example uses two schedulers for two different scenarios:
    - The round-robin scheduler is used to schedule 5 tasks over
    3 resources. The tasks have exponentially larger loads.
    An analysis of the schedule is presented.
    - The list scheduler is used to schedule 20 tasks over
    4 resources. The tasks have loads taken from a uniform
    distribution. An analysis of the schedule is presented
    and plotted.
"""

import simulator.schedulers as schedulers
import simulator.support as support


print("Scenario 1: LPT")
# Setup
num_tasks = 20
num_resources = 2
task_loads = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 19]#[1, 2, 4, 8, 16]
# Calls the scheduler and prints the schedule as it is computed
mapping = schedulers.lpt(task_loads, num_resources)
# Presents an analysis of the results
support.evaluate_mapping(mapping, task_loads, num_resources)

print("\nScenario 2: LPT with task limit")
# Setup
# num_tasks = 5
# num_resources = 3
# task_loads = [1, 2, 4, 8, 16]
#support.generate_uniform_loads(num_tasks, 1, 5, 99)
# Calls the scheduler
mapping = schedulers.lpt_with_limits(task_loads, num_resources, 10)
# Presents an analysis of the results
support.evaluate_mapping(mapping, task_loads, num_resources)
# Plots the resulting mapping and saves it to a file
# support.plot_mapping(mapping, task_loads, num_resources, 'example_lpt.png')
