# docker_project_99


OK, so taking them one by one.


Couldn't figure out what would this app purpose would be and how could I just use it from k8s cluster.

So the only logic I could find to this app is if it can just be mapped to a place where the documents are constantly changing and the purpose could be to check what is the most common word in each file separately + from all files in there whenever any of the file is changed.


Now, I started by creating the script that stays in a loop (so that it won't kill the container when it's finished) and checks every minute the status of all files and compares it to the previous status.

Then, after checked if it was working on my PC, I edited the path to accept it from the os environment (which I will publish later in docker-compose.yml)


After this was done, I created a dockerfile that copies the script and puts it into working dir and runs it when container is starting.


Then created the docker-compose.yml which is building the dockerfile and uses 1. volumes in order for those files to be accessed from our machine that hosts the container and 2. environment variables that could be used by python script to figure out where are the files going to be (path to the volume)




Now, the tricky part is that I never used repositories and kubernetes locally, only in the already created environments at work so that would take me a considerable amount of time to understand and setup, which I don't really have sadly.
So based on that, I created a persistent volume clain and a deployment to have there but I could't test them.

Technically what is left is to update the image to a repository and make the kubernetes deployment take it from there.



As I tried my best to make everything usable in any possible environment, my project can be tested by following the next steps:

1. Clone the repository
2. Have docker installed on pc
3. Go in the folder that contains docker-compose.yaml
4. Use command "docker-compose up --build -d" to build the image and run it

5. Change anything you would like in the data folder and you will see the script in action. (needs to be .txt tho)
