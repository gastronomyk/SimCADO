import os
import yaml

YAMLS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                          "../yamls/"))
FILES_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                          "../files/"))


def _atmo_yaml_dict():
    text = """
# ATMOSPHERE
object : atmosphere
name : armazones

properties :
    temperature : 0         # [-270..270] deg C
    pressure : 0.6          # [0..1] bar

effects :
-   name : super_psf
    class : GaussianDiffractionPSF
    z_order : 300
    kwargs :
        diameter : 39
"""
    return yaml.load(text)


def _inst_yaml_dict():
    text = """
# INSTRUMENT OPTICS
object : instrument
name : micado_wide_field
inst_pkg_name : micado

properties :
    temperature : -190
    plate_scale : 0.004

effects :
-   name : micado_surface_list
    class : SurfaceList
    z_order : 200
    kwargs :
        file_name : micado_mirror_list.tbl

-   name : micado_adc
    class : AtmosphericDispersion
    z_order : 0
    kwargs :
        zenith_distance : 30
        reverse_shifts : True

-   name : pupil_mask
    class : ApertureList
    z_order : 0
    kwargs :
        file_name : aperture_list.tbl        
        
    """
    return yaml.load(text)


def _detector_yaml_dict():
    text = """
# Detector array
object : detector
name : micado_detector_array
inst_pkg_name : micado

properties :
    temperature : -190
    dark_current : 0.1

effects :
-   name : detector_qe_curve
    class : TERCurve
    z_order : [0, 200]
    kwargs :
        filename : TC_blank.dat

-   name : micado_detector_geometry
    class : DetectorList
    z_order : [0, 100]
    kwargs:
        filename: FPA_array_layout.dat
    """
    return yaml.load(text)


def _yaml_min_viable_scope():
    with open(os.path.join(YAMLS_PATH, "min_viable_sys.yaml")) as f:
        dicts = [dic for dic in yaml.load_all(f)]
    return dicts


def _usr_cmds_min_viable_scope():
    from simcado.commands.user_commands_utils import read_config
    config_dict = read_config(os.path.join(FILES_PATH, "CMD_mvs_cmds.config"))
    return config_dict
