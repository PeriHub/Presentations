---
marp: true
theme: dlr
header: ""
footer: ""
title: Peridynamic Day
author: Jan-Timo Hesse, Christian Willberg
---

<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true,
  theme: 'white',
  circular: {
    radius: 300,
    direction: 'CW',
  }, });
</script>

<!-- _class: title-slide -->

## Feature overview of simulation framwework PeriLab

<div style="position: absolute; top: 20px; left: 1050px;"> 
    <img src="https://quickchart.io/qr?text=https://perihub.github.io/Presentations/PDDAY_2025/&light=0000&size=300" alt="Presentation link" style="height:180px;width:auto;vertical-align: top;background-color:transparent;">
</div>

Jan-Timo Hesse<a href="https://orcid.org/0000-0002-3006-1520"><img src="../assets/ORCIDiD_iconvector.png" alt="ORCID Symbol" style="height:15px;width:auto;vertical-align: top;background-color:transparent;"></a>, Christian Willberg<a href="https://orcid.org/0000-0003-2433-9183"><img src="../assets/ORCIDiD_iconvector.png" alt="ORCID Symbol" style="height:15px;width:auto;vertical-align: top;background-color:transparent;"></a>
<br />

> <h style="color: black; ">3th Peridynamic Day - 2025</h> 
> _11th December, 2025 - Magdeburg_

<div style="position: absolute; bottom: 10px; left: 100px; color: grray; font-size: 20px;">
Presentation URL: https://perihub.github.io/Presentations/PDDAY_2025
</div>




---
# What is PeriLab?
A solver for PD integral equation
$\int_{\mathcal{H}}(\underline{\textbf{T}}(\textbf{x},t)- \underline{\textbf{T}}(\textbf{x}',t))dV_{\textbf{x}}+\textbf{b} =\rho\ddot{\textbf{u}}$


- Open Source
- 🚀 Easy Installation and ✒️ Modularization
- 🎨 User Materials and 🧮 Abaqus Input
- 🧲 Multiphysics and 💻 HPC capabilities
- ...


</div>

![bg right fit](./assets/PeriLab_crack.gif)

---

# PeriLab vs. Alternative solutions

<div class=rdiv>

<div class=mermaid>
quadrantChart
  x-axis Low Functionalty --> High Functionalty
  y-axis Hard to use --> Simple to use
  Peridigm: [0.85, 0.2]
  PeriLab: [0.85, 0.8]
  EMU: [0.95, 0.1]
  PeriPy: [0.2, 0.7]
  Peridynamics.jl: [0.7, 0.6]
  PeriPyDIC: [0.2, 0.6]
  LAMMPS: [0.3, 0.3]
  PeriFlakes: [0.35, 0.4]
  Relation-Based Software: [0.4, 0.25]
  BB_PD: [0.2, 0.50]
  PeriDEM: [0.13, 0.3]
</div>
</div>

---

# Why PeriLab
![bg](./assets/chart.png)

---



# PD solving strategies


##  Material point method
$\begin{equation}
\mathbf{F}_{int,i}=\sum_{j \in \mathcal{H}_i}\underline{\mathbf{T}}_{ij}\langle\boldsymbol{\xi}_{ij}\rangle V_j,
\end{equation}$
__Advantages__  
- Fast to implement
- Failure propagation
- Discretization

__Diadvantages__  
- Convergence is lower
- Surfaces are not known

![bg right:50% width:900px](../assets/Fragmenting_Cylinder.gif)

---

## Matrix based approach

- use correspondence stiffness matrix based on material point method

__Advantages__ 
- linear static analysis possible
- less operations per time step if Verlet is used

__Diadvantages__  
- matrix update is costly
- algorithms are more complex

![bg right 90%](./assets/force_comp.png)

---

## Main Advantage

- it allows reduction methods
- currently under development
- static and dynamic reduction
 ![bg right 90%](./assets/coupling_nodes.png)



$\begin{equation}
\begin{bmatrix}
\boldsymbol{K}_{mm} & \boldsymbol{K}_{ms} \\
\boldsymbol{K}_{sm} & \boldsymbol{K}_{ss}
\end{bmatrix}
\begin{bmatrix}
\boldsymbol{u}_m \\ \boldsymbol{u}_s
\end{bmatrix}=
\begin{bmatrix}
\boldsymbol{F}_m \\ \boldsymbol{F}_s
\end{bmatrix}
\end{equation}$

$\boldsymbol{F}_s = \boldsymbol{0}$
$\begin{equation}
\boldsymbol{K}_{sm} \boldsymbol{u}_m + \boldsymbol{K}_{ss} \boldsymbol{u}_s = \boldsymbol{0}
\end{equation}$

---

$\begin{equation}
\boldsymbol{u}_s = -\boldsymbol{K}_{ss}^{-1} \boldsymbol{K}_{sm} \boldsymbol{u}_m
\end{equation}$

$\begin{equation}
\boldsymbol{K}_{mm} \boldsymbol{u}_m + \boldsymbol{K}_{ms} \left(-\boldsymbol{K}_{ss}^{-1} \boldsymbol{K}_{sm} \boldsymbol{u}_m\right) = \boldsymbol{F}_m
\end{equation}$

$\begin{equation}
\boldsymbol{K}_{\text{red}} = \boldsymbol{K}_{mm} - \boldsymbol{K}_{ms} \boldsymbol{K}_{ss}^{-1} \boldsymbol{K}_{sm}
\end{equation}$

- currently under testing
- split $\mathbf{K}_{mm}$ in material point part and matrix part
  - allows easy implementation of fracture or non-linear material
  - reduction of degrees of freedoms

 ![bg right 90%](./assets/coupling_nodes.png)

---

<!--_class: cols-2-->

# Peridynamic Framework (PeriLab)

<div class=ldiv>

- No pre-processing required, mesh will be generated based on the gcode
- Material Models:
  - PD Solid Elastic/Plastic
- Thermal Models:
  - Thermal Flow
  - Heat Transfer
  - HETVAL subroutine
- Damage Models:
  - Critical Stretch
</div>
<div class=rdiv style="margin-top:80px">

![width:500px](https://raw.githubusercontent.com/PeriHub/PeriLab.jl/main/assets/PeriLab_crack.gif)

</div>

---

# Solver Overview

- **Verlet**
  - Explicit solver for non-linear problems
- **Static**
  - Static solver for linear problems
- **Matrix Verlet**
  - Efficient matrix-based explicit solver for non-linear problems
- **Matrix Linear Static**
  - Efficient matrix-based static solver for linear problems

---
<style scoped>
table {
    width: 100%;
    font-size: 24px;
}
</style>

# Module Overview

|Material|Damage|Thermal|Contact|Coupling|Additive|Degradation|
|---|---|---|---|---|---|---|
|Bond-Based|Critical Stretch|Thermal Flow|Penalty|FEM-PD|Damage-based|*Bond-based Corrosion*
|PD Solid Elastic/Plastic|Critical Energy|Heat Transfer|*Short-Range*|Guyan Reduction||*Thermal Decomposition*
|Correspondence Elastic/Plastic||Thermal Expansion|
|Correspondence UMAT/VUMAT||HETVAL|
|Bond Associated Correspondence|


---

## FEM Coupling

![bg 160% right](./assets/cauchy_yy_mix_static.png)

---


## Temperature

- convection
- heat transfer
- thermo-mechanical coupling

![bg right fit](https://github.com/PeriHub/PeriLab.jl/blob/main/docs/src/assets/temperature_distribution_cooling.png?raw=true)


---

## Interblock damage

- damage between layers or material
- bonds handled differently if they exist in two blocks

![bg right fit](https://raw.githubusercontent.com/PeriHub/PeriLab.jl/cf3b50528edaf2744fcaeb94e0133fc801dd2418/docs/src/assets/InterBlockDamage.svg)

---

# Input and Output Formats

- Input
  - Text file
  - Exodus file
  - Abaqus model
- Output
  - Exodus file
  - CSV file

---

<!-- _class: section-slide-plane -->

## Examples

---
# Examples - RVE

<br/>
<iframe width="1150" height="500" src="https://www.youtube.com/embed/ClV2ojQPrFM?si=eROuZGPdBpXTnmef" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---
# Examples - Impact
<br/>
<iframe width="1150" height="500" src="https://www.youtube.com/embed/qj7xGgmjEdE?si=wTN42HPnBmSPxwJ4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---
# Examples - Additive
<br/>
<iframe width="1150" height="500" src="https://www.youtube.com/embed/dGfJG9AoL4g?si=-i41xB0_XemF87ts" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---




# Live Demonstration

## Module integration


```
module my_demo_mod
```

```
function damage_name()
    return "module name"
end
```

- define a yaml file
- define variables and call them
- write variable to nodes
- [Examplary models](https://github.com/PeriHub/PeriLab.jl/tree/main/examples/Seminars/) 

---
<!-- _class: section-slide-rocket -->
## Get-Started
 

---

# How to get started with PeriLab?

- Ready to use application:
  - Download and install [PeriHub](https://github.com/PeriHub/PeriHub)
- Just the simulation core:
  - Download the docker image from [Docker Hub](https://hub.docker.com/r/perihub/perilab)
  - Download the julia package with: `Pkg.add("PeriLab")`
  - Download the [release files](https://github.com/PeriHub/PeriLab.jl/releases)
- Develop and contribute:
  - Clone the [repository](https://github.com/PeriHub/PeriLab.jl) and follow the development guide
    - Implement your own peridynamic models (don't worry it's easy!)
    - Create a pull request in order to contribute 


---

# Planned Features

-
-

---

# Feedback Time

- Scan the QR-code
- What is missing for you to use PeriLab?
- Further questions?

![bg right:50% width:500px](https://quickchart.io/qr?text=https://app.sli.do/event/5mmfvHmXVAHMyJPJJY11dA&light=0000&size=300)

---

# Feedback Time

<iframe src="https://app.sli.do/event/5mmfvHmXVAHMyJPJJY11dA" width="90%" height="85%" style="border: 0; margin-left: 70px"></iframe>

---

<!-- _class: title-slide -->

## Introduction to Peridynamic Web-Framework PeriHub 

<div style="position: absolute; top: 20px; left: 1050px;"> 
    <img src="https://quickchart.io/qr?text=https://perihub.github.io/Presentations/PDDAY_2025/&light=0000&size=300" alt="Presentation link" style="height:180px;width:auto;vertical-align: top;background-color:transparent;">
</div>

Jan-Timo Hesse<a href="https://orcid.org/0000-0002-3006-1520"><img src="../assets/ORCIDiD_iconvector.png" alt="ORCID Symbol" style="height:15px;width:auto;vertical-align: top;background-color:transparent;"></a>, Christian Willberg<a href="https://orcid.org/0000-0003-2433-9183"><img src="../assets/ORCIDiD_iconvector.png" alt="ORCID Symbol" style="height:15px;width:auto;vertical-align: top;background-color:transparent;"></a>
<br />

> <h style="color: black; ">3th Peridynamic Day - 2025</h> 
> _11th December, 2025 - Magdeburg_

<div style="position: absolute; bottom: 10px; left: 100px; color: grray; font-size: 20px;">
Presentation URL: https://perihub.github.io/Presentations/PDDAY_2025
</div>

---

# PeriHub


- **Peridynamic simulation engine** – extends PeriLab for detailed material‑science studies.  
- **Easy to use & portable** – GUI, REST API, and Docker for quick setup on any platform.  
- **Trusted, FAIR‑compliant** – built by experts (incl. DLR) with rigorous quality and open‑science standards.

![bg right width:250px](https://raw.githubusercontent.com/PeriHub/PeriHub/refs/heads/main/docs/assets/images/PeriHubLogo2b.png)

---

# Features - What can I do with PeriHub?


- **Peridynamic simulation engine** – extends PeriLab for detailed material‑science studies.  
- **Easy to use & portable** – GUI, REST API, and Docker for quick setup on any platform.  
- **Trusted, FAIR‑compliant** – built by experts (incl. DLR) with rigorous quality and open‑science standards.

---

<!-- _class: section-slide-vulcan -->

## Overview

---

![width:1070px](./assets/PeriHub.svg)


---

<!-- _class: section-slide-rocket -->

## Simulation Results

---

<iframe src="https://perihub.nimbus.dlr.de" width="148%" height="180%" style="border: 0; margin-left: 70px; transform: scale(0.6); transform-origin: 0 0;"></iframe>

---

<iframe src="https://perihub.nimbus.dlr.de" width="90%" height="100%" style="border: 0; margin-left: 70px"></iframe>

---

# Thank you!

[Jan-Timo Hesse](mailto:jan-timo.hesse@dlr.de) (DLR)
[Christian Willberg](mailto:christian.willberg@h2.de) (h2)
![bg right height:8cm](https://gitlab.com/dlr-perihub/PeriLab.jl/-/raw/main/assets/PeriLab_crack.gif)

---