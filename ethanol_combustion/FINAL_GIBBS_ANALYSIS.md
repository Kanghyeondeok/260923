# Ethanol combustion thermochemistry

## Result

Gas-phase reaction at 298.15 K and 1 bar:

`C2H5OH + 3 O2 -> 2 CO2 + 3 H2O`

| Quantity | Value |
| --- | ---: |
| Internal energy, ΔU | -1041.57 kJ mol⁻¹ |
| Enthalpy, ΔH | -1039.09 kJ mol⁻¹ |
| Entropy, ΔS | +104.38 J mol⁻¹ K⁻¹ |
| Gibbs free energy, ΔG | **-1070.21 kJ mol⁻¹** |

All values use the completed B3LYP/6-31G(d) optimization and harmonic-Hessian workflows, with ideal-gas rigid-rotor/harmonic-oscillator (RRHO) corrections. The result applies to gas-phase water, not liquid water. Each stationary point has zero imaginary frequencies.

## Species results

Energies are Hartree; entropy is J mol⁻¹ K⁻¹.

| Species | Electronic energy | ZPE correction | Enthalpy | Gibbs energy | Entropy |
| --- | ---: | ---: | ---: | ---: | ---: |
| Ethanol | -154.935538992 | 0.080254337 | -154.850074917 | -154.880657740 | 269.311 |
| O₂ (triplet) | -150.256757806 | 0.003771825 | -150.249678761 | -150.273619624 | 210.822 |
| CO₂ | -188.494971274 | 0.011600181 | -188.479784426 | -188.504744252 | 219.795 |
| H₂O | -76.369990619 | 0.021107709 | -76.345104117 | -76.366550415 | 188.855 |

## Reaction contribution breakdown

Products minus reactants. Energy terms are kJ mol⁻¹.

| Contribution | Δ value |
| --- | ---: |
| Electronic energy | -1034.71 |
| Zero-point energy | -13.25 |
| Translational thermal internal energy | +3.72 |
| Rotational thermal internal energy | +4.96 |
| Vibrational thermal internal energy | -2.29 |
| **Internal energy** | **-1041.57** |
| pV | +2.48 |
| **Enthalpy** | **-1039.09** |
| Translational entropy | +133.88 J mol⁻¹ K⁻¹ |
| Rotational entropy | +10.82 J mol⁻¹ K⁻¹ |
| Vibrational entropy | -40.32 J mol⁻¹ K⁻¹ |
| **Total entropy** | **+104.38 J mol⁻¹ K⁻¹** |
| -TΔS | -31.12 kJ mol⁻¹ |
| **Gibbs free energy** | **-1070.21 kJ mol⁻¹** |

The thermal internal-energy contributions were obtained from the MAESTRO Hessian results: `U_thermal = U_trans + U_rot + U_vib`; `U = E_electronic + ZPE + U_thermal`; `H = U + pV`; and `G = H - TS`.

## Provenance and archived results

- Method: B3LYP/6-31G(d), ORCA 6.0.1 through MAESTRO.
- Resources: one SLURM task and one CPU core per optimization and Hessian job.
- Temperatures and pressure: 298.15 K and 1 bar.
- Raw optimized geometries, Hessians, frequencies, normal modes, ORCA inputs/outputs, job scripts, MAESTRO graph metadata, and parsed `result.json` files are retained under `runs/`.
- Per-species run summaries are retained in `../maestro-episodes/`.
