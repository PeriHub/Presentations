---
marp: true
theme: dlr
header: ""
footer: ""
title: Micromechanical analysis via Peridynamics 
author: Jan-Timo Hesse, Christian Willberg
---

<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true });
</script>

<!-- _class: title-slide -->

## Micromechanical analysis via Peridynamics 

<div style="position: absolute; top: 20px; left: 1050px;"> 
    <img src="assets/qr.png" alt="Presentation link" style="height:180px;width:auto;vertical-align: top;background-color:transparent;">
</div>

Jan-Timo Hesse<a href="https://orcid.org/0000-0002-3006-1520"><img src="../assets/ORCIDiD_iconvector.png" alt="ORCID Symbol" style="height:15px;width:auto;vertical-align: top;background-color:transparent;"></a>, Christian Willberg<a href="https://orcid.org/0000-0003-2433-9183"><img src="../assets/ORCIDiD_iconvector.png" alt="ORCID Symbol" style="height:15px;width:auto;vertical-align: top;background-color:transparent;"></a>
<br />

> <a href="https://sites.google.com/usacm.org/pd25/home" style="color: black; text-decoration: underline;">PeriHub - Empowering Research with Peridynamic Modeling</a> 
> _October 8th, 2024, Braunschweig_

<div style="position: absolute; bottom: 10px; left: 100px; color: grray; font-size: 20px;">
Presentation URL: https://perihub.github.io/Presentations/MICRO_ANALYSIS
</div>

---

<!--paginate: true-->
<!--footer: 'Pres. URL: https://perihub.github.io/Presentations/MICRO_ANALYSIS'-->

## Motivation Peridynamics (PD)

- alternative to classcical continuum mechanics $\text{div}(\mathbf{\sigma})+\textbf{b} =\rho\ddot{\textbf{u}}$
- PD integral equation
  $\int_{\mathcal{H}}(\underline{\textbf{T}}(\textbf{x},t)- \underline{\textbf{T}}(\textbf{x}',t))dV_{\textbf{x}}+\textbf{b} =\rho\ddot{\textbf{u}}$
- focus material modeling and crack propagation no $C^1$ continuity for the displacement


![bg right:44% fit transparent](../assets/PeriMesh.png)

---

## PD Solving the integral - Material point method

__Advantages__  
- fast to implement
- cracks are easy to include
- discretization

__Diadvantages__  
- convergence is lower
- surfaces are not known

![bg right:48% transparent](assets/examples.png)

---

## PeriHub - Empowering Research with Peridynamic Modeling

- Web Framework for Peridynamic Analysis
- Open Source
- Features
  - Generate 2D or 3D peridynamic meshes
  - Run simulation locally or on clusters
  - Analyse results directly in the browser

<img src="https://avatars.githubusercontent.com/u/102970205?v=4" style="position: absolute; top: 20px; right: 150px" width="100px">

---

## Generate model

![width:1020px](https://raw.githubusercontent.com/PeriHub/PeriHub/main/docs/assets/gif/generateModel.gif)

---
<!--header: ''-->

## RVE

<iframe src="https://perilab-results.nimbus-extern.dlr.de/models/RVE" width="1150" height="600"></iframe>

---

## Composite

![width:1200px](assets/smetana.png)

---

## Crack Analysis Tool ([CrackPy](https://github.com/dlr-wf/crackpy))

![width:900px](assets/CrackPy.png)

---

# Thank you

[Jan-Timo Hesse](mailto:jan-timo.hesse@dlr.de) (DLR)
[Christian Willberg](christian.willberg@h2.de) (h2)
![bg right height:8cm](https://gitlab.com/dlr-perihub/PeriLab.jl/-/raw/main/assets/PeriLab_crack.gif)