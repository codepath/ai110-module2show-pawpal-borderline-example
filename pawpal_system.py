# pawpal_system.py
from dataclasses import dataclass, field
from typing import List, Optional


"""
Intentionally partial / off-spec implementation for a low-scoring example repo.

Notes (intentional):
- Task does NOT include due time/date.
- Task does NOT include a meaningful method like mark_complete().
- Scheduler logic is shallow and does not implement meaningful algorithmic features.
- Cross-pet scheduling is incomplete.

2/4 points for 2. Implementation of core classes matches the design
"""


@dataclass
class Task:
    description: str
    completed: bool = False
    # Intentionally missing: due_time / due_date, frequency, etc.
    # Intentionally missing: mark_complete() method


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


class Scheduler:
    """
    Intentionally shallow "scheduler":
    - Only returns tasks for the first pet (does not operate across multiple pets)
    - No sorting/filtering/conflict detection/recurrence logic
    """

    def get_todays_tasks(self, owner: Owner) -> List[Task]:
        if not owner.pets:
            return []

        # Intentionally incomplete: only handles the first pet.
        return owner.pets[0].tasks

    def summarize(self, tasks: List[Task]) -> str:
        # Intentionally low-quality output formatting.
        return str(tasks)
    
    def sort_by_time(self, tasks: List[Task]) -> List[Task]:
        return tasks  # TODO
    

# GRADER CALIBRATION NOTE:
# Scheduler implementation is intentionally shallow:
# - No sorting/filtering/conflict detection/recurrence logic
# - Does not operate across multiple pets
# - Returns tasks without additional processing
# Expected score for rubric section #3: 0/3


