from pawpal_system import Task, Pet, Owner, Scheduler


def test_task_creation():
    # Very trivial test (not meaningful)
    task = Task(description="Walk")
    assert task.description == "Walk"


def test_scheduler_returns_tasks():
    # This will fail because scheduler only returns first pet tasks
    owner = Owner(name="Test")
    pet1 = Pet(name="A", species="Dog")
    pet2 = Pet(name="B", species="Cat")

    pet1.add_task(Task(description="Task 1"))
    pet2.add_task(Task(description="Task 2"))

    owner.add_pet(pet1)
    owner.add_pet(pet2)

    scheduler = Scheduler()
    tasks = scheduler.get_todays_tasks(owner)

    # Expect both pets' tasks (but implementation only returns first pet's tasks)
    assert len(tasks) == 2


"""
5. Basic Pytest Suite Verifies System Behavior (1/3 pints)
✔ Test file exists → 1 point
❌ One test is trivial
❌ Second test fails
❌ Tests do not pass without modification
"""