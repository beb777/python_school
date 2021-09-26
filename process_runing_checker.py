# import psutil
#
#
# def process_is_running(terminal):
#     return any(process for process in psutil.process_iter()
#                if terminal.lower() in process.name().lower())
#
#
# process_is_running('vim')
#
#
# from functools import partial
#
# python_is_running = partial(process_is_running, 'python')
# python_is_running()
import psutil

import psutil


def checkIfProcessRunning(terminal):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
             if terminal.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;


# Check if any chrome process was running or not.
if checkIfProcessRunning('terminal'):
    print('terminal is running')
else:
    print('no terminal is running')

