from ast import Import

from mp_api.client.routes.materials.eos import EOSRester
from mp_api.client.routes.materials.materials import MaterialsRester
from mp_api.client.routes.materials.similarity import SimilarityRester
from mp_api.client.routes.materials.tasks import TaskRester
from mp_api.client.routes.materials.xas import XASRester
from mp_api.client.routes.materials.fermi import FermiRester
from mp_api.client.routes.materials.grain_boundary import GrainBoundaryRester
from mp_api.client.routes.materials.substrates import SubstratesRester
from mp_api.client.routes.materials.surface_properties import SurfacePropertiesRester
from mp_api.client.routes.materials.phonon import PhononRester
from mp_api.client.routes.materials.elasticity import ElasticityRester
from mp_api.client.routes.materials.thermo import ThermoRester
from mp_api.client.routes.materials.dielectric import DielectricRester
from mp_api.client.routes.materials.doi import DOIRester
from mp_api.client.routes.materials.piezo import PiezoRester
from mp_api.client.routes.materials.magnetism import MagnetismRester
from mp_api.client.routes.materials.summary import SummaryRester
from mp_api.client.routes.materials.synthesis import SynthesisRester
from mp_api.client.routes.materials.electrodes import ElectrodeRester
from mp_api.client.routes.materials.electronic_structure import (
    ElectronicStructureRester,
    BandStructureRester,
    DosRester,
)
from mp_api.client.routes.materials.oxidation_states import OxidationStatesRester
from mp_api.client.routes.materials.provenance import ProvenanceRester
from mp_api.client.routes.materials.bonds import BondsRester
from mp_api.client.routes.materials.robocrys import RobocrysRester
from mp_api.client.routes.materials.absorption import AbsorptionRester

from mp_api.client.routes.molecules.summary import MPculesSummaryRester

from mp_api.client.routes.legacy.jcesr import MoleculesRester

from ._user_settings import UserSettingsRester
from ._general_store import GeneralStoreRester


try:
    from .alloys import AlloysRester
except ImportError:
    AlloysRester = None  # type: ignore

try:
    from .charge_density import ChargeDensityRester
except ImportError:
    ChargeDensityRester = None  # type: ignore
