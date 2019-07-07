import configparser
import queue

class UI():

    def __init__(self, config_path = "config/config.ini"):
        print("UI initiated")
        self._queue = queue.Queue()
        self.job_list = []

    def start(self):
        res = self.menu()
        while res != "Q":
            res = self.menu()

    def menu(self):
        print("\nPlease select from following:")
        choice = input("""
            L: List jobs
            A: Add a new job
            D: Delete a job
            U: Update a job
            R: Run job
            S: Stop job
            Q: Quit
            Please enter your choice:""")
        choice = choice.capitalize()
        if choice == "L":
            self._list_jobs()
        if choice == "A":
            print("Adding a new job in job Queue")
            self.add_job()
        if choice == "D":
            print("Please select a job to delete")
            self.delete_job()
        if choice == "U":
            print("Please select a job to update/edit")
            self.update_job()
        if choice == "R":
            print("Please select a job to run")
            self.run_job()
        if choice == "S":
            print("Please select a job to stop")
            self.stop_job()
        if choice == "Q":
            print("Exiting")
            return "Q"
        else:
            return None

    def _list_jobs(self):
        print("Listing jobs in queue")
        for item in self.job_list:
            print(">{}", item)

    def _get_job_name(self):
        job_name = input("Please enter your job name:")
        return job_name

    def add_job(self):
        print("Adding new job to queue")
        job_name = self._get_job_name()
        self.job_list.append(job_name)
        self._queue.put(job_name)

    def delete_job(self):
        self._list_jobs()
        print("Deleting job from queue")
        job_name = self._get_job_name()
        if job_name in self.job_list:
            self._queue.get(job_name)
            self.job_list.remove(job_name)

    def update_job(self):
        self._list_jobs()
        print("Updating job in job queue")
        job_name = self._get_job_name()
        if job_name in self.job_list:
            #self.job_list.remove(job_name)
            temp_job = self._queue.get(job_name)
            # Do some work updating here
            self._queue.put(temp_job)
            #self.job_list.append(temp_job)

    def run_job(self):
        self._list_jobs()
        print("Running job in queue")
        job_name = self._get_job_name()
        if job_name in self.job_list:
            # Run job by invoking some kind of remote call
            print("Setting state of job")

    def stop_job(self):
        self._list_jobs()
        print("Stopping job in queue")
        job_name = self._get_job_name()
        if job_name in self.job_list:
            # Run job by invoking some kind of remote call
            print("Setting state of job")


