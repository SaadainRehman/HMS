from BL.Staff import Staff

class Nurse(Staff):
    def __init__(self, name, shift, address, phone, salary, cnic, specialization, department):
        super().__init__(name, shift, address, phone, salary, cnic)
        self._specialization = specialization
        self._department = department
        self._task_list = [
            "Assist in Surgery",
            "Check Patient Vitals",
            "Administer Medicine",
            "Monitor Blood Pressure",
            "Prepare Patient for Surgery",
        ]

    def assist_doctor(self):
        return f"Nurse {self._name} is assisting in {self._department}."

    def view_tasks(self):
        if not self._task_list:
            return "No tasks assigned."
        result = "\n--- Nurse Tasks ---\n"
        for idx, task in enumerate(self._task_list, start=1):
            result += f"{idx}. {task}\n"
        return result

    def perform_task(self, task_index):
        if 0 <= task_index < len(self._task_list):
            task = self._task_list.pop(task_index)
            return f"Task performed: {task}"
        else:
            return "Invalid task index."

    def task_index(self):
        try:
            task_index = int(input("Enter Task No. to be Performed: "))
            new_index = task_index -1
            return new_index
        except ValueError:
            return -1

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, Specialization: {self._specialization}, Department: {self._department}"