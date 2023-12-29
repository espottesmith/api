from __future__ import annotations

from typing import Literal

from emmet.core.molecules.electric import ElectricMultipoleDoc
from emmet.core.mpid import MPculeID

from mp_api.client.core import BaseRester


class MoleculesElectricMultipoleRester(BaseRester[ElectricMultipoleDoc]):
    suffix = "molecules/multipoles"
    document_model = ElectricMultipoleDoc
    primary_key = "property_id"

    def search(
        self,
        molecule_ids: MPculeID | list[MPculeID] | None = None,
        property_ids: str | list[str] | None = None,
        charge: int | None = None,
        spin_multiplicity: int | None = None,
        level_of_theory: str | None = None,
        solvent: str | None = None,
        lot_solvent: str | None = None,
        formula: str | list[str] | None = None,
        chemsys: str | list[str] | None = None,
        elements: list[str] | None = None,
        exclude_elements: list[str] | None = None,
        moment_type: Literal["dipole", "resp_dipole", "quadrupole", "octopole", "hexadecapole"] | None = None,
        component: str | None = None,
        min_component_value: float | None = None,
        max_component_value: float | None = None,
        total_dipole: Tuple[float, float] | None = None,
        resp_total_dipole: Tuple[float, float] | None = None,
        num_chunks: int | None = None,
        chunk_size: int = 1000,
        all_fields: bool = True,
        fields: list[str] | None = None,
    ):
        """Query molecules partial charges docs using a variety of search criteria.

        Arguments:
            molecule_ids (MPculeID, List[MPculeID]): List of Materials Project Molecule IDs (MPculeIDs) to return data
                for.
            property_ids (str, List[str]): List of property IDs to return data for.
            charge (Tuple[int, int]): Minimum and maximum charge for the molecule.
            spin_multiplicity (Tuple[int, int]): Minimum and maximum spin for the molecule.
            level_of_theory (str): Desired level of theory (e.g. "wB97X-V/def2-TZVPPD/SMD")
            solvent (str): Desired solvent (e.g. "SOLVENT=WATER")
            lot_solvent (str): Desired combination of level of theory and solvent
                (e.g. "wB97X-V/def2-TZVPPD/SMD(SOLVENT=THF)")
            formula (str, List[str]): An alphabetical formula or list of formulas
                (e.g. "C2 Li2 O4", ["C2 H4", "C2 H6"]).
            chemsys (str, List[str]): A chemical system, list of chemical systems
                (e.g., Li-C-O, [C-O-H-N, Li-N]), or single formula (e.g., C2 H4).
            elements (List[str]): A list of elements.
            exclude_elements (List(str)): List of elements to exclude.
            moment_type (Literal["dipole", "resp_dipole", "quadrupole", "octopole", "hexadecapole"]): Type of multipole
                moment to query on.
            component (str): Multipole component to query on. Valid entries depend on moment type. For instance, for
                "dipole", valid components are "X", "Y", and "Z".
            min_component_value (float): Minimum value for the multipole moment component of interest.
            max_component_value (float): Maximum value for the multipole moment component of interest.
            total_dipole (float): Minimum and maximum value for the total dipole.
            resp_total_dipole (float): Minimum and maximum value for the total dipole calculated with the restrained
                electrostatic potential (RESP) method.
            num_chunks (int): Maximum number of chunks of data to yield. None will yield all possible.
            chunk_size (int): Number of data entries per chunk.
            all_fields (bool): Whether to return all fields in the document. Defaults to True.
            fields (List[str]): List of fields in ElectricMultipoleDoc to return data for.
                Default is "molecule_id", "property_id", "solvent", "last_updated"
                if all_fields is False.

        Returns:
            ([ElectricMultipoleDoc]) List of partial charges documents
        """
        query_params = dict()  # type: dict

        min_max = [
            "total_dipole",
            "resp_total_dipole"
        ]

        for param, value in locals().items():
            if param in min_max and value:
                if isinstance(value, (int, float)):
                    value = (value, value)
                query_params.update(
                    {
                        f"{param}_min": value[0],
                        f"{param}_max": value[1],
                    }
                )

        if molecule_ids:
            if isinstance(molecule_ids, str):
                molecule_ids = [molecule_ids]

            query_params.update({"molecule_ids": ",".join(molecule_ids)})

        if property_ids:
            if isinstance(property_ids, str):
                property_ids = [property_ids]

            query_params.update({"property_ids": ",".join(property_ids)})

        if charge:
            query_params.update({"charge": charge})

        if spin_multiplicity:
            query_params.update({"spin_multiplicity": spin_multiplicity})

        if level_of_theory:
            query_params.update({"level_of_theory": level_of_theory})

        if solvent:
            query_params.update({"solvent": solvent})

        if lot_solvent:
            query_params.update({"lot_solvent": lot_solvent})

        if formula:
            if isinstance(formula, str):
                formula = [formula]

            query_params.update({"formula": ",".join(formula)})

        if chemsys:
            if isinstance(chemsys, str):
                chemsys = [chemsys]

            query_params.update({"chemsys": ",".join(chemsys)})

        if elements:
            query_params.update({"elements": ",".join(elements)})

        if exclude_elements:
            query_params.update({"exclude_elements": ",".join(exclude_elements)})

        if moment_type:
            query_params.update({"moment_type": moment_type})

        if component:
            query_params.update({"component": component})
        
        if min_component_value:
            query_params.update({"min_component_value": min_component_value})

        if max_component_value:
            query_params.update({"max_component_value": max_component_value})

        return super()._search(
            num_chunks=num_chunks,
            chunk_size=chunk_size,
            all_fields=all_fields,
            fields=fields,
            **query_params,
        )
