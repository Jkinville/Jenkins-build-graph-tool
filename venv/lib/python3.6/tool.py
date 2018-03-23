from jenkinsapi.jenkins import Jenkins
import excel_output
from datetime import date

class mostRecentBuildData:

    def __init__(self):
        self.date = date
        self.success = 0
        self.fail = 0
        self.unstable = 0
        self.aborted = 0
        self.jobs = 0

    def setSuccess(self):
        self.success += 1
        self.jobs += 1
        print('jobs ' + str(self.jobs) + ' total ' + str(self.success))

    def setFail(self):
        self.fail += 1
        self.jobs += 1
        print('jobs ' + str(self.jobs) + ' total ' + str(self.fail))

    def setUnstable(self):
        self.unstable += 1
        self.jobs += 1
        print('jobs ' + str(self.jobs) + ' total ' + str(self.unstable))

    def setAborteted(self):
        self.aborted += 1
        self.jobs += 1
        print('jobs ' + str(self.jobs) + ' total ' + str(self.aborted))

    def calc_prcent(self):
        self.success /= self.jobs
        self.fail /= self.jobs
        self.unstable /= self.jobs
        self.aborted /= self.jobs

        print(str(self.date) + ' ' + str(self.success) + ' ' + str(self.fail) + ' ' + str(self.unstable) + ' ' + str(self.aborted) )


def get_server_instance():
    jenkins_url = 'https://prod-jenkins.newforma.io/'
    server = Jenkins(jenkins_url, username = 'USERNAME', password = 'PASSWORD')
    jobs = server.get_jobs_info()
    todaysJobs = mostRecentBuildData()
    for job in jobs:
        job_instance = server.get_job(job[1])
        latestBuild = job_instance.get_last_build()
        print(latestBuild.get_status())
        if latestBuild.get_status() == 'SUCCESS':
            todaysJobs.setSuccess()
        if latestBuild.get_status() == 'FAILURE':
            todaysJobs.setFail()
        if latestBuild.get_status() == 'UNSTABLE':
            todaysJobs.setUnstable()
        if latestBuild.get_status() == 'ABORTED':
            todaysJobs.setAborteted()
    todaysJobs.calc_prcent()
    return server

if __name__ == '__main__':
    excel_output.get_excel_data()
    jobs = get_server_instance()
    print(jobs)