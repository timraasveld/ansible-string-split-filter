from ansible import errors
import re

def split_string(string, seperator=' '):
    try:
        return string.split(seperator)
    except Exception, e:
        raise errors.AnsibleFilterError('split plugin error: %s, provided string: "%s"' % str(e),str(string) )

def split_regex(string, seperator_pattern='\s+'):
    try:
        return re.split(seperator_pattern, string)
    except Exception, e:
        raise errors.AnsibleFilterError('split plugin error: %s, provided string: "%s"' % str(e),str(string) )

class FilterModule(object):
    ''' A filter to split a string into a list. '''
    def filters(self):
        return {
            'split' : split_string,
            'split_regex' : split_regex,
        }
