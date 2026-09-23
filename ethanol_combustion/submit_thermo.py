"""Gas-phase thermochemistry for ethanol combustion species at 298.15 K, 1 atm.

Each ThermoTask performs geometry optimization followed by a Hessian/frequency
calculation.  MAESTRO submits the intensive work to Slurm through ORCA.
"""

from maestro import DFT, Maestro, OrcaEngine, SystemQM, ThermoTask
from maestro.engines.jobspec import Resources


TEMPERATURE_K = 298.15
PRESSURE_ATM = 1.0
THEORY = DFT(functional="B3LYP", basis="6-31G(d)")
ENGINE = OrcaEngine(
    resources=Resources(cores=1, partition="32core_partition", time="24:00:00")
)

SPECIES = {
    "ethanol": {"geometry": "inputs/ethanol.xyz", "charge": 0, "spin": 0},
    "oxygen": {"geometry": "inputs/oxygen.xyz", "charge": 0, "spin": 2},
    "carbon_dioxide": {
        "geometry": "inputs/carbon_dioxide.xyz",
        "charge": 0,
        "spin": 0,
    },
    "water": {"geometry": "inputs/water.xyz", "charge": 0, "spin": 0},
}


def run_species(maestro, name, spec):
    system = SystemQM(
        geometry=spec["geometry"], charge=spec["charge"], spin=spec["spin"]
    )
    task = ThermoTask(
        system=system,
        theory=THEORY,
        temperature=TEMPERATURE_K,
        pressure=PRESSURE_ATM,
    )
    result = maestro.run(
        rundir=f"runs/{name}_thermo_work", task=task, engines=ENGINE
    )
    print(name)
    for quantity in ("electronic_energy", "zpe_correction", "enthalpy", "entropy", "gibbs_free_energy"):
        print(f"  {quantity} [{result.unit(quantity)}]: {result.load(quantity)}")


def main():
    maestro = Maestro(mode="slurm", workdir=".", runinfo_path="orca_runinfo.toml")
    for name, spec in SPECIES.items():
        run_species(maestro, name, spec)


if __name__ == "__main__":
    main()
