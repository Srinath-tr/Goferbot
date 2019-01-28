import random
import sys
import time
import GoogleText
import frontend
import requests
import speech
# This string needs to be defined for each front end.  It should
# contain the name of the front-end class defined in this module.
frontEndClass = "FrontEndTTY"

# List the default values for the INI file.  This should be a dictionary
# with keys of the form "<fe>.<entry>", where <fe> is the name of the
# frontend (e.g. "aim", "msn"), and entry is the name of the configuration
# variable (e.g. "username", "password").  All values should be strings.
#
# Each frontend must define an "active" entry, whose possible values
# are "yes" and "no", which indicates whether that frontend should
# be activated.

configDefaults = {
    "tty.active":       "yes"
    }

class FrontEndTTY(frontend.IFrontEnd):
    """
    A butt-simple class demonstrating the bare minimum needed to
    implement a new front-end for Howie.
    """    
    def go(self):
        post_cmd = "http://goferiot.16mb.com/default.php"
        tag = 'price of','cost of','rate of','prize of'
        iot = 'lights on','lights off','lights of','light on','light of','switch on the light','switch off the light','switch on the fan','switch off the fan','switch of the light','switch of the fan'
        self._sessionID = "localhost@TTY"
        import howie.core
        howie.core.kernel.setPredicate("secure", "yes", self._sessionID)
        while True:
            input = raw_input(">>> ")
            for t in tag:
                if t in input:
                    print 'ok, let me search in the net'
                    response = GoogleText.price_search(input)
                    break
            else:
                for i in iot:
                    if i in input:
                        form_data={
                            'text_box':input,
                            'search-submit':'submit',
                            }
                        try:
                            requests.post(post_cmd, data=form_data)
                            print 'just a second'
                            break
                        except:
                            print "can't connect to the internet"
                            break
                else:
                    response = self.submit(input, self._sessionID)
                    #time.sleep(random.random() * 4)
                    self.display(response, self._sessionID)
    
    def display(self, output, user):
        print output
        speech.say(output)
