import concurrent.futures
import os

def process_task(task_number):
    print(f"Processing task {task_number}")
    return f"Task {task_number} complete"

if __name__ == "__main__":
    print(f"CPU Count: {os.cpu_count()}")  # Mostra o número de núcleos de CPU disponíveis
    
    tasks = [1, 2, 3, 4, 5]
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(process_task, tasks))
    
    for result in results:
        print(result)
