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

### Design decisions I
- Start simple
- Create basic classes with unit tests
- Networking should be probably in its own class
- UI should be last

### Implementation progress
- networks/netutils module with a server and a client in tcp for exchanging messages
- daemons module with an observer and a dispatcher with corresponding classes inside.
- Observer class just creates a client from networks/netutils module to send a message in a server listening to a port (now 9000)
- Dispatcher class creates a server from networks/netutils module to receive messages from any client like observer

### Next steps
- I am thinking if observer should also wait on a port for messages but not sure.
- Override HandleRequest class from Server inside Dispatcher and make it handle messages coming in.
- Add configuration reading from a config file for all modules/classes to share config between them
- Add logging to check for errors


### New additions as of 8th July 2019
New system as designed until now:
- A ui system that has two internal structures: A queue for holding jobs and a list for easily mapping the queue in a parsable
structure. This decision was made because in the future, jobs will be objects with a state and we do not want to map queue in a list for
every user interaction
- Daemons folder has also an observer and a dispatcher. Observer will be polling git for jobs in queue (the one in ui)
and when finds an update it will send a message to the listening socket of dispatcher.
- Dispatcher will listen to a specific port, there is a configuration file reading facility ready for that, and when a new update
arrives will call a build on the corresponding job.
- In general the workflow will be like this: UI accepts user jobs and puts them in a queue, dispatcher will be notified for those who should be 
running with a message from ui, observer will watch for changes in git to also call dispatcher.
- Dispatcher will also maintain a queue of workers and when a message arrives it will spawn one, run the build job and return 
result when ready on UI.


### Decisions in 10th of July 2019
- UI should NOT have an internal queue. Internal queue should be inside Dispatcher.
- UI will have a dictionary holding job data. A new structure for jobs should be created.
- When a job in UI changes, as an instruction from user, a message should be sent to Dispatcher to inform him of our intentions.
- Dispatcher will always run a server and report state of jobs.
- In order for UI to know current state of jobs, dispatcher should probably post in its port (in a different url), a list of jobs and their state
So after updating we will need: 
1. A new Job class to hold jobs data (url for scm, build instructions, state).
2. This class should also offer a way to (de)serialize itself to be send as a message to Dispatcher.
3. A method to redirect url in our dispatcher server to different methods
4. A handler for the state request
5. An observer that will poll SCM and send also a message to create jobs
6. A queue of jobs in Dispatcher that will hold current work to be done
7. A pool of workers in Dispatcher that will consume Job Queue.


### Afterthoughts on initial trial
It seems that working with synchronous servers is not going to work. We need more thought on this.
New design should be like this:
- Main running process is dispatcher. It should control every main aspect. Responsibilities:
   * Run a server to wait for messages 
   * Hold an internal job queue which holds jobs and their state 
   * It has a pool of workers to execute jobs.
   * Assigns a new job to a worker that is idle.
   * So we need a state table for workers also
   * When a new message arrives it acts accordingly:
       * If it is a new job it adds it to the queue
       * If it is a command for a job it acts accordingly ? (run/stop)
       * If it is a job state request status it checks its internal state table.
- Secondary process is workers. Responsibilities:
   * Waits idle or it is stopped. It runs when a new job is needed to run.
   * Runs job and updates job state in respective table
- UI runs on a separate process. Responsibilities:
   * Interacts with user and receives commands
   * Sends messages to dispatcher
   * Receives responses from dispatcher
- Observer also a separate process. Similar to UI just automated. Responsibilities:
   * For every job in Queue, it checks it's scm source and detects any changes.
   * If any change is found, it runs the respective job.
  
** Remarks:
   * We need to study on async io servers for handling of communications
   * We need to select thread/process/coroutine workers and how to control them
   * How to spawn workers?
   * Should the observer be checking only active jobs in Queue? Or it could be manipulated through UI?
   * What about branches? Other type of scm changes?
   * Error handling and Testing should be in place. 
