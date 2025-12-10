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

<!--_class: cols-2-->

# Peridynamic Framework (PeriLab)

<div class=ldiv>

-  A high-performance, open-source peridynamic framework in Julia
- Designed to be extensible and modular, allowing users to easily add new features and solvers
- Built-in support for various material models and boundary conditions
- Support for multiphysics and multi-step simulations.
- Extensive documentation and community support
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

# Input and Output Formats

- Input
  - Text file
  - Exodus file
  - Abaqus model
- Output
  - Exodus file
  - CSV file

![bg right:50% width:900px](../assets/Fragmenting_Cylinder.gif)

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

# Examples - Anisotropic Material

![bg width:1200px](./assets/smetana.png)

---

# Examples - Anisotropic Damage

![bg width:750px](./assets/Aniso_crack2.png)

---

# Examples - Interlaminar Failure

![bg width:1200px](./assets/waviness.png)

---

# Examples - PD-FEM-Coupling

![bg width:700px](./assets/disp_mix_static.png)

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
    1. Implement your own peridynamic models (don't worry it's easy!)
    2. Create a pull request in order to contribute 


---

# Planned Features

- Dynamic solver switch
- Corrosive material models
- Performance and usability improvements
- More material and damage models 

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
- 

![bg right width:250px](https://raw.githubusercontent.com/PeriHub/PeriHub/refs/heads/main/docs/assets/images/PeriHubLogo2b.png)

---

# Features - What can I do with PeriHub?


- **Model Creation** - Create models using predefined templates or import your own.
- **Simulation Execution** - Run simulations using our powerful engine.
- **Data Visualization** - Visualize results using our built-in tools or export data for further analysis.
- **Analysis** - Analyze results and generate reports using your own python methods.

---

<!-- _class: section-slide-vulcan -->

## Overview

---

![width:1070px](./assets/PeriHub.svg)


---

<!-- _class: section-slide-rocket -->

## Live Demo

---

# How to get started with PeriHub?

- Ready to use application:
  - Follow the guide [here](https://github.com/PeriHub/PeriHub?tab=readme-ov-file#getting-started-with-perihub-services) to get started with PeriHub services.
- Develop and contribute:
  - Go to the [Cintribution guide](https://github.com/PeriHub/PeriHub?tab=readme-ov-file#contributing)
  - Submit your changes as a Pull Request

---

## Planned Features

- Live Demo will be released
- Stability and user experience improvements
- Improve Documentation

---

# Thank you!

[Jan-Timo Hesse](mailto:jan-timo.hesse@dlr.de) (DLR)
[Christian Willberg](mailto:christian.willberg@h2.de) (h2)
![bg right height:8cm](https://gitlab.com/dlr-perihub/PeriLab.jl/-/raw/main/assets/PeriLab_crack.gif)
