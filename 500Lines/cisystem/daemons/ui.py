import configparser
from networks import netutils
from models import job


class UI(object):

    def __init__(self, config_path = "config/config.ini"):
        print("UI initiated")
        self.jobs = dict()
        self._client = netutils.Client(config_path, target='dispatcher')

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
        print("Listing jobs")
        for name, details in self.jobs.items():
            print(details)

    def _get_job_name(self, message="Please enter job name:", exist=True):
        job_name = input(message)
        if exist and job_name not in self.jobs.keys():
            print("Error, job name not found")
            return None
        else:
            return job_name

    def add_job(self):
        print("Adding new job to queue")
        job_name = self._get_job_name(exist=False)
        job_scm = input("Please give me job SCM url (eg. github):")
        job_instructions = input("Please provide build command for job:")
        current_job = job.Job(job_name, job_scm, job_instructions)
        self.jobs[job_name] = current_job

    def delete_job(self):
        self._list_jobs()
        print("Deleting job from queue")
        job_name = self._get_job_name("Please select job to delete")
        del self.jobs[job_name]

    def update_job(self):
        self._list_jobs()
        job_name = self._get_job_name("Please select job to update")
        print("Updating job in job queue")
        item = self.jobs[job_name]
        job_name = self._get_job_name("Please enter new job name:", exist=False)
        job_scm = input("Please give me job SCM url (eg. github):")
        job_instructions = input("Please provide build command for job:")
        item.data['name'] = job_name
        item.data['scm_url'] = job_scm
        item.data['instructions'] = job_instructions

    def run_job(self):
        self._list_jobs()
        job_name = self._get_job_name("Please select job to run")
        if job_name in self.jobs.keys():
            self.jobs[job_name].state = "R"
            self._client.send_message(self.jobs[job_name].serialize())
        else:
            print("Wrong job name")

    def stop_job(self):
        self._list_jobs()
        print("Stopping job in queue")
        job_name = self._get_job_name("Please select job to stop")
        self.jobs[job_name].state = "S"
        self._client.send_message(self.jobs[job_name].serialize())
