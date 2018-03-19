from jenkinsapi.jenkins import Jenkins

def get_server_instance():
    jenkins_url = 'https://prod-jenkins.newforma.io/'
    server = Jenkins(jenkins_url, username = 'jkinville', password = '8c3423388555cb0e1b53357a7db585d57302d37e')
    jobs = server.get_jobs_info()
    for job in jobs:
        job_instance = server.get_job('Newforma/cloud-action-items-api/acceptance-tests')
        latestBuild = job_instance.get_last_build()
        print(latestBuild.get_status())
    return server

if __name__ == '__main__':
    jobs = get_server_instance().get_jobs_list()
    print(jobs)