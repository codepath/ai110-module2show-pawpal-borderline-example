# main.py
from pawpal_system import Owner, Pet, Task, Scheduler


def main():
    owner = Owner(name="Amelia")

    pet1 = Pet(name="Milo", species="Dog")
    pet2 = Pet(name="Luna", species="Cat")

    # 3+ tasks across pets
    pet1.add_task(Task(description="Walk", time="09:00"))
    pet1.add_task(Task(description="Feed", time="08:00"))
    pet2.add_task(Task(description="Medication", time="07:30"))

    owner.add_pet(pet1)
    owner.add_pet(pet2)

    scheduler = Scheduler()

    # Borderline: only uses scheduler for first pet tasks
    tasks = scheduler.get_tasks_for_first_pet(owner)
    sorted_tasks = scheduler.sort_by_time(tasks)

    print("Today's Schedule:")
    # Borderline output: prints raw dataclass objects (messy)
    print(sorted_tasks)


if __name__ == "__main__":
    main()


"""
5) Pytest

2 tests exist and pass ✅
They’re meaningful-ish but narrow (don’t test sorting/scheduler behavior) → borderline “tests only check trivial behaviors” risk

2/3 points

"""