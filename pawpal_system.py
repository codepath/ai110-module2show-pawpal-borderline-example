# pawpal_system.py
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Task:
    description: str
    time: str  # "HH:MM" as a string (borderline choice)
    completed: bool = False

    def mark_complete(self) -> None:
        self.completed = True


@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def list_tasks(self) -> List[Task]:
        return self.tasks


@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        self.pets.append(pet)

    # Borderline: No clean get_all_tasks() helper (Scheduler must dig through pets)


class Scheduler:
    """
    Borderline scheduler:
    - Implements ONE algorithmic feature: sorting by time
    - But only sorts tasks for the FIRST pet (does not operate across multiple pets)
    - No conflict detection / recurrence / filtering

    3. Algorithmic Features:
    Implements sorting by time ✅ (1 feature)
    Does not implement a second feature ❌
    Does not operate across multiple pets ❌
    1/3 points
    """

    def get_tasks_for_first_pet(self, owner: Owner) -> List[Task]:
        if not owner.pets:
            return []
        return owner.pets[0].tasks

    def sort_by_time(self, tasks: List[Task]) -> List[Task]:
        # Borderline: assumes "HH:MM" always valid; no validation
        return sorted(tasks, key=lambda t: t.time)


"""
2) Core Classes

Task.description, Task.time, Task.completed, Task.mark_complete() ✅
Pet requirements: identifying info + tasks + methods to manage (Pet.name/species, tasks, add_task, list_tasks) ✅
Owner requirements: identifying info + pets + methods (Owner.name, pets, add_pet) ✅
Scheduler requirement: retrieve/organize/manage tasks across pets (not just hold data)
Borderline issue: your scheduler retrieves tasks for only the first pet and sorting applies only to that list. That’s still “some retrieval/organize,” but not robust and not truly “across pets.”

3/4 points
"""