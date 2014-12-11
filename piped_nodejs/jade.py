from __future__ import print_function
import os
import sys
import subprocess


# class Jade:
#
#     class Singletone:
#
#         def __init__(self, length=1024):
#             self.fdr, self.fdw = os.pipe()
#             self.length = length
#             args = dict(fdr=self.fdr, fdw=self.fdw, length=self.length)
#             os.system('nodejs read_arg.js {fdr} {fdw} {len}'.format(**args))
#
#         def send_to_node(self, msg):
#             len_ = os.write(self.fdw, msg)
#             return len_
#
#         def get_from_node(self):
#             resp = os.read(self.fdr, self.length)
#             return resp
#
#     instance = None
#
#     def __init__(self, kwargs):
#         if not Jade.instance:
#             Jade.instance = Jade.Singletone(**kwargs)
#
#     def __getattr__(self, item):
#         return getattr(self.instance, item)


class Jade:

    fdr = None
    fdw = None
    length = None

    @staticmethod
    def start(js_file='read_arg.js', length=1024, stdout=sys.stdout):
        Jade.fdr, Jade.fdw = map(str, os.pipe())
        Jade.length = str(length)
        # args = dict(js_file=js_file, fdr=Jade.fdr, fdw=Jade.fdw, length=Jade.length)
        args = ['nodejs', js_file, Jade.fdr, Jade.fdw, Jade.length]
        # returncode = os.system('nodejs {js_file} {fdr} {fdw} {length}'.format(**args))
        # if returncode:
        #     print('Jade broken', file=stdout)
        # else:
        #     print('Jade started', file=stdout)
        p = subprocess.Popen(args)
        print('Jade started', file=stdout)

    @staticmethod
    def send_to_node(msg):
        len_ = os.write(Jade.fdw, msg)
        return len_

    @staticmethod
    def get_from_node():
        resp = os.read(Jade.fdr, Jade.length)
        return resp
