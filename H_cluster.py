# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 17:50:38 2017

@author: Mike
"""

"""
hierarchical_clustering
"""

import sys
import os
import argparse
import logging
import math

import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from dtaidistance import dtw

logger = logging.getLogger(__name__)


def size_cond(size):
    n = size
    r = 2
    f = math.factorial
    return int(f(n) / f(r) / f(n-r))


def h_clust():
    """
    Import cryptocurrency series, r = beginning range buffer

    """
    r = 20
    
    series = [
        AMPy[r:], ARDRy[r:],
        BCNy[r:],BCYy[r:],BELAy[r:],BLKy[r:],BTCDy[r:],BTMy[r:],BTSy[r:],BURSTy[r:],
        CLAMy[r:],
        DASHy[r:],DCRy[r:],DGBy[r:],DOGEy[r:],
        ETCy[r:],ETHy[r:],EXPy[r:],
        FLDCy[r:],FLOy[r:],
        GAMEy[r:],GRCy[r:],
        HUCy[r:],
        LBCy[r:],LSKy[r:],LTCy[r:],
        MAIDy[r:],
        NAVy[r:],NEOSy[r:],NMCy[r:],NXTy[r:],
        OMNIy[r:],
        PINKy[r:],POTy[r:],PPCy[r:],
        RADSy[r:],REPy[r:],RICy[r:],
        SBDy[r:],SCy[r:],STEEMy[r:],STRy[r:],SYSy[r:],
        VIAy[r:],VRCy[r:],VTCy[r:],
        XBCy[r:],XCPy[r:],XEMy[r:],XMRy[r:],XPMy[r:],XRPy[r:],XVCy[r:],
        ZECy[r:]
   
    ]
    
    series_labels = [
        'AMPy', 'ARDRy',
        'BCNy','BCYy','BELAy','BLKy','BTCDy','BTMy','BTSy','BURSTy',
        'CLAMy',
        'DASHy','DCRy','DGBy','DOGEy',
        'ETCy','ETHy','EXPy',
        'FLDCy','FLOy',
        'GAMEy','GRCy',
        'HUCy',
        'LBCy','LSKy','LTCy',
        'MAIDy',
        'NAVy','NEOSy','NMCy','NXTy',
        'OMNIy',
        'PINKy','POTy','PPCy',
        'RADSy','REPy','RICy',
        'SBDy','SCy','STEEMy','STRy','SYSy',
        'VIAy','VRCy','VTCy',
        'XBCy','XCPy','XEMy','XMRy','XPMy','XRPy','XVCy',
        'ZECy'
   
    ]

    dists = dtw.distance_matrix(series)
    print("Distance matrix:\n{}".format(dists))

    dists_cond = np.zeros(size_cond(len(series)))
    idx = 0
    for r in range(len(series)-1):
        dists_cond[idx:idx+len(series)-r-1] = dists[r, r+1:]
        idx += len(series)-r-1

    z = linkage(dists_cond, method='complete', metric='euclidean')

    fig, axes = plt.subplots(2, 1, figsize=(8, 3))
    for idx, serie in enumerate(series):
        axes[0].plot(serie, label=str(series_labels[idx]))

    dendrogram(z, ax=axes[1])
    plt.show()


def main(argv=None):
    parser = argparse.ArgumentParser(description='Cryptocurrency')
    parser.add_argument('--verbose', '-v', action='count', help='Verbose output')
    args = parser.parse_args(argv)

    logger.setLevel(logging.ERROR - 10 * (0 if args.verbose is None else args.verbose))
    logger.addHandler(logging.StreamHandler(sys.stdout))

    h_clust()

main()
    
