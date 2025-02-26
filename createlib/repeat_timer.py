from threading import Timer, Lock
import time

####################
#  Sources:
#    https://stackoverflow.com/questions/2398661/schedule-a-repeating-event-in-python-3/18942977
#    https://stackoverflow.com/questions/474528/what-is-the-best-way-to-repeatedly-execute-a-function-every-x-seconds
#####################
class RepeatTimer:
    """A periodic timer running with threading.Timers."""

    def __init__(self, interval, function, autostart=True):
        self._lock = Lock()
        self.function = function
        self.interval = interval
        self._timer = None
        self._stopped = True
        if autostart:
            self.start()

    def start(self, from_run=False):
        """
        Starts the timer if it's not already running.
        """
        with self._lock:
            if not self._stopped and not from_run:
                return
            self._timer = Timer(self.interval, self._run)
            self._stopped = False
            self._timer.start()

    def _run(self):
        """
        Executes the function and restarts the timer.
        """
        self.start(from_run=True)
        self.function()

    def stop(self):
        """
        Stops the timer safely.
        """
        with self._lock:
            if self._timer:
                self._timer.cancel()
                self._timer = None
            self._stopped = True