import os
from copy import deepcopy
import pytest
from pytest import approx

import numpy as np
from astropy import units as u

import simcado as sim
from simcado.optics import image_plane_utils as imp_utils
from simcado.optics.optical_train import OpticalTrain
from simcado.utils import find_file
from simcado.commands.user_commands2 import UserCommands

from simcado.tests.mocks.py_objects.source_objects import _image_source, \
    _single_table_source

import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
PLOTS = False

FILES_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                          "../mocks/files/"))
YAMLS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                          "../mocks/yamls/"))

sim.rc.__search_path__ += [FILES_PATH, YAMLS_PATH]


def _basic_cmds():
    return UserCommands(filename=find_file("CMD_unity_cmds.config"))


@pytest.fixture(scope="function")
def cmds():
    return _basic_cmds()


@pytest.fixture(scope="function")
def tbl_src():
    return _single_table_source()


@pytest.fixture(scope="function")
def im_src():
    return _image_source()


@pytest.mark.usefixtures("cmds", "im_src", "tbl_src")
class TestObserve:
    def test_flux_is_conserved_and_emission_level_correct(self, cmds, tbl_src):
        opt = OpticalTrain(cmds)
        opt.observe(tbl_src)
        assert tbl_src.photons_in_range(1, 2, 1)[0].value == approx(1) # * u.Unit("ph s-1")
        assert np.sum(opt.image_plane.image) == approx(1, rel=2e-3)    # given a 1 um bandpass

        if PLOTS:
            plt.imshow(opt.image_plane.image.T, origin="lower", norm=LogNorm())
            plt.colorbar()
            plt.show()

