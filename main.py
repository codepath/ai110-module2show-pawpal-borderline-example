# main.py
from pawpal_system import Owner, Pet, Task, Scheduler

def main():
    # Create owner
    owner = Owner(name="Amelia")

    # Create two pets
    pet1 = Pet(name="Milo", species="Dog")
    pet2 = Pet(name="Luna", species="Cat")

    # Create several tasks (3+)
    task1 = Task(description="Walk the dog")
    task2 = Task(description="Feed the cat")
    task3 = Task(description="Clean litter box")

    # Assign tasks
    pet1.add_task(task1)
    pet1.add_task(task2)
    pet2.add_task(task3)

    # Add pets to owner
    owner.add_pet(pet1)
    owner.add_pet(pet2)

    # Scheduler is created but not meaningfully used
    scheduler = Scheduler()

    # Minimal / unclear output
    print("\n")
    print(owner)
    print("\n\nPartial credit: Demo creates objects but does not use the Scheduler meaningfully.")

if __name__ == "__main__":
    main()
