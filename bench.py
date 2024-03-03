import simulator.schedulers as schedulers
import simulator.support as support

def compare_lpt_list_schedulers(num_tasks, num_resources):
    print(f"LPT vs list-scheduler : {num_tasks} tasks and {num_resources} ressources")

    task_loads = support.generate_uniform_loads(num_tasks, 1, 10, 99)
    # Calls the scheduler and prints the schedule as it is computed
    mapping1 = schedulers.list_scheduler(task_loads, num_resources, False)
    mapping2 = schedulers.lpt(task_loads, num_resources, False)

    # Presents an analysis of the results
    print("List scheduler :")
    support.evaluate_mapping(mapping1, task_loads, num_resources)
    print("LPT scheduler :")
    support.evaluate_mapping(mapping2, task_loads, num_resources)

    # Plots the resulting mapping and saves it to a file
    support.plot_mapping(mapping1, task_loads, num_resources, f'list_bench{num_tasks}-{num_resources}.png')
    support.plot_mapping(mapping2, task_loads, num_resources, f'lpt_bench{num_tasks}-{num_resources}.png')


task_ressource = [(4, 3),
                  (10, 3),
                  (10, 5),
                  (10, 8),
                  (50, 2),
                  (50, 3),
                  (50, 15),
                  (50, 25),
                  (50, 40),
                  (100, 3),
                  (100, 4),
                  (100, 10),
                  (100, 25),
                  (100, 70)]

for task, ressource in task_ressource:
    compare_lpt_list_schedulers(task, ressource)