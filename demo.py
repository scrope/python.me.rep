'''
Created on 2013-11-1

@author: chenming
'''

import os, sys
from optparse import OptionParser, OptionGroup

reload(sys)
sys.setdefaultencoding('utf8')  

def analysis():
    usage = '%prog'
    parser = OptionParser(usage, prog=u'模板脚本', version='%prog 1.0')
    group = OptionGroup(parser, 
                        'desc and example', 
                        u'''
                            python简易工具脚本模板
                        ''')
    
    group.add_option('-a', action='store', dest='CTCIP', default='', help=u'')

    parser.add_option_group(group)
    
    (options, _) = parser.parse_args()
    return options

def insertServer():
    cmd = 'ls'
    file = os.popen(cmd)
    for line in file:
        line = str(line).replace('\n', '')

if __name__ == '__main__':
    options = analysis()
    print('Over!!!')