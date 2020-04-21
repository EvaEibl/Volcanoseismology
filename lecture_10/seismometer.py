"""Seismometer class code for use in lecture_11_modules.ipynb"""


# By default all classes are descendants of "object". You do not have to worry about this.
class Seismometer(object):
    """An example of a Seismometer Class"""
    
    # This is a global attribute. It is the same for all seismometer objects.
    # It is identical to writing `self.owner = 'I_Rule_Volcanoes' within `__init__()`.
    owner = 'I_Rule_Volcanoes'
    
    # __init__ is a Method of Seismometer. It is the method that is called when you create a new Seismometer object with
    # seismometer3 = Seismometer(min_signal=0.2, max_signal=0.6, calibration_factor=0.06, storage_size=1024)
    #
    # The first argument of __init__ is always called 'self'. 'self' refers to the object itself (e.g. seismometer3).
    # This is necessary because the object has to know where it can "find" the attributes and methods stored with it.
    #
    # The variables that are listed after self need to be passed to Seismometer(...) when creating a new object. 'self' does
    # not need to be passed, it is a special Python keyword.
    def __init__(self, min_signal, max_signal, calibration_factor, storage_size):
        # Here we add the arguments to the object itself (with self.name = ...) so they do not get discarded after __init__ completes
        # and we can access them later from our methods. These are local attributes.
        #
        # Note: It is possible to store values in `self` from outside this class or from methods of class. But...
        # It is good practice to define everything you want to store in that object within `__init__`
        self.min_signal = min_signal
        self.max_signal = max_signal
        self.calibration_factor = calibration_factor
        self.storage_size = storage_size
        
        # This will not be stored in self and therefore cannot be accessed later on with `self.a_test`.
        a_test = 1
        
        # This is where we store data when we call start_recording()
        self.data = []
        
        # We can also save additional information with our object. This will always be False for all newly created seismometer objects.
        self.started = False
        self.calibrated = False
        
        # Tell the world a new Seismometer Object exists
        print(f'Created Seismometer with min_signal={min_signal}, max_signal={max_signal}, calibration_factor={calibration_factor}, '
              f'storage_size={storage_size}, owner={self.owner}') # We can access the global attribute 'owner' with 'self.owner'
    
    # This is a Method of Seismometer.
    def start_recording(self):
        # It can access "calibrated", "started" and the list "data" defined above because it has access to "self"
        if self.calibrated:
            # We can also call methods of this object. Note: The "self" argument is automatically added by Python.
            if self.check_storage(False):
                self.started = True
                new_data = 1.0 + self.calibration_factor
                self.data.append(new_data)
            else:
                print('No more storage!')
        else:
            print('Instrument not yet calibrated!')
        
    def stop_recording(self):
        self.started = False
        
    def calibrate(self):
        if not self.calibrated:
            print('Calibrating ...')
            # This is made up ;)
            self.calibration_factor += 2.0 * 0.001 ** 2 - self.min_signal + self.max_signal
            self.calibrated = True
    
    # This is an example of a docstring (documentation) of a method.
    def check_storage(self, verbose=True):
        """Prints how much storage has been used and returns True if storage is still available, otherwise False.
        
        Args:
            verbose: If True, will print the used vs total storage.
            
        Returns:
            True, if storage is still available.
        """
        if verbose:
            print(f'{len(self.data)}/{self.storage_size} available.')
        return self.storage_size - len(self.data) > 0
        
    def download(self):
        if not self.started:
            print('Downloading data')
            return self.data
        else:
            print('Stop recording first to download data!')