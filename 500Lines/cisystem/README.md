## A Continuous Integration System

This exercise is for creating a CI system in Python in less than 500 lines of code.
Stolen idea from the Architecture of Open Source Applications online book, I will try this as an exercise to see how
close my code would be comparing to a professional written program.

### Description of the exercise
_The basic structure of a continuous integration system consists of three components: an observer, a test job dispatcher,
and a test runner. The observer watches the repository. When it notices that a commit has been made, it notifies the job
 dispatcher. The job dispatcher then finds a test runner and gives it the commit number to test._

_There are many ways to architect a CI system. We could have the observer, dispatcher and runner be the same process on
a single machine. This approach is very limited since there is no load handling, so if more changes are added to the
repository than the CI system can handle, a large backlog will accrue. This approach is also not fault-tolerant at all;
if the computer it is running on fails or there is a power outage, there are no fallback systems, so no tests will run.
The ideal system would be one that can handle as many test jobs as requested, and will do its best to compensate when
machines go down._

_To build a CI system that is fault-tolerant and load-bearing, in this project, each of these components is its own
process. This will let each process be independent of the others, and let us run multiple instances of each process.
This is useful when you have more than one test job that needs to be run at the same time.
We can then spawn multiple test runners in parallel, allowing us to run as many jobs as needed, and prevent us from
accumulating a backlog of queued tests._

_In this project, not only do these components run as separate processes, but they also communicate via sockets,
which will let us run each process on a separate, networked machine. A unique host/port address is assigned to each
component, and each process can communicate with the others by posting messages at the assigned addresses._

_This design will let us handle hardware failures on the fly by enabling a distributed architecture. We can have the
observer run on one machine, the test job dispatcher on another, and the test runners on another, and they can all
communicate with each other over a network. If any of these machines go down, we can schedule a new machine to go up
on the network, so the system becomes fail-safe._

_This project does not include auto-recovery code, as that is dependent on your distributed system's architecture,
but in the real world, CI systems are run in a distributed environment like this so they can have failover redundancy
(i.e., we can fall back to a standby machine if one of the machines a process was running on becomes defunct)._

_For the purposes of this project, each of these processes will be locally and manually started distinct local ports._


### Design decisions
We need three classes which will spawn as new processes.

1. An Observer class that will watch a specific repository and when it detects a commit it will create a notification
message for the Dispatcher. Message should contain the repo and possible changes detected.
2. A Dispatcher class that will listen on a socket and when it receives a notification message from Observer will
create a new task and will assign the task message to next TaskRunner registered in a Queue object.
Dispatcher will send a message to the TaskRunner with commit changes.
3. A TestRunner that will register itself to the Dispatcher though a socket and will listen to a socket for a new job.
Any new jobs will be sent from Dispatcher and be executed by the Task Runner.

### Questions:
- How do we run jobs in TaskRunner? User should have a way to define build details like build executable and parameters.
- Do we need a UI? Even a text based should be enough.
- How does the TaskRunner registers itself to Dispatcher Queue? By sending a message in a socket with its own socket
details?
- What happens when a TaskRunner is assigned a job? It should be removed from the Queue and give access to UI
- Seems that UI should have an async system receiving events from every component running.

### Design decisions
- Start simple
- Create basic classes with unit tests
- Networking should be probably in its own class
- UI should be last

### Implementation progress
- networks/utilities module with a server and a client in tcp for exchanging messages
- daemons module with an observer and a dispatcher with corresponding classes inside.
- Observer class just creates a client from networks/utilities module to send a message in a server listening to a port (now 9000)
- Dispatcher class creates a server from networks/utilities module to receive messages from any client like observer

### Next steps
- I am thinking if observer should also wait on a port for messages but not sure.
- Override HandleRequest class from Server inside Dispatcher and make it handle messages coming in.
- Add configuration reading from a config file for all modules/classes to share config between them
- Add logging to check for errors
