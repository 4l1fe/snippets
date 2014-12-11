from __future__ import print_function
import os


if __name__ == '__main__':
    fdr, fdw = os.pipe()
    len = 1024
    args = dict(fdw=fdw, fdr=fdr, len=len)
    os.write(fdw, 'python')
    os.system('nodejs read_arg.js {fdr} {fdw} {len}'.format(**args))
    resp = os.read(fdr, len+len)
    print(resp)
