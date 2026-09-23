"""Submit water B3LYP/6-31G(d) gas-phase thermochemistry via Slurm."""
from maestro import DFT, Maestro, OrcaEngine, SystemQM, ThermoTask
from maestro.engines.jobspec import Resources

mae = Maestro(mode="slurm", workdir=".", runinfo_path="orca_runinfo.toml")
system = SystemQM(geometry="inputs/water.xyz", charge=0, spin=0)
task = ThermoTask(
    system=system,
    theory=DFT(functional="B3LYP", basis="6-31G(d)"),
    temperature=298.15,
    pressure=1.0,
)
result = mae.run(
    rundir="runs/water_thermo_work",
    task=task,
    engines=OrcaEngine(resources=Resources(cores=1, partition="32core_partition", time="24:00:00")),
)
print("water Gibbs free energy:", result.load("gibbs_free_energy"), result.unit("gibbs_free_energy"))
