from jenkinsapi.jenkins import Jenkins

def get_server_instance():
    jenkins_url = 'https://prod-jenkins.newforma.io/'
    server = Jenkins(jenkins_url, username = 'USERNAME_HERE', password = 'PASSWORD_HERE')
    jobs = server.get_jobs_info()
    for job in jobs:
        job_instance = server.get_job(job[1])
        latestBuild = job_instance.get_last_build()
        print(job[0] + ' ' + latestBuild.get_status())
    return server

if __name__ == '__main__':
    jobs = get_server_instance().get_jobs_list()
    print(jobs)