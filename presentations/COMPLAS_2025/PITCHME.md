---
marp: true
theme: dlr
header: ""
footer: ""
title: Multiphysics Simulation of Additive Manufacturing-Induced Fracture Mechanics using Peridynamic Theory
author: Jan-Timo Hesse, Grigori Oehl
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

## Multiphysics Simulation of Additive Manufacturing-Induced Fracture Mechanics using Peridynamic Theory 

<div style="position: absolute; top: 20px; left: 1050px;"> 
    <img src="https://quickchart.io/qr?text=https://perihub.github.io/Presentations/COMPLAS_2025/&light=0000&size=300" alt="Presentation link" style="height:180px;width:auto;vertical-align: top;background-color:transparent;">
</div>

Jan-Timo Hesse<a href="https://orcid.org/0000-0002-3006-1520"><img src="../assets/ORCIDiD_iconvector.png" alt="ORCID Symbol" style="height:15px;width:auto;vertical-align: top;background-color:transparent;"></a>, Christian Willberg<a href="https://orcid.org/0000-0003-2433-9183"><img src="../assets/ORCIDiD_iconvector.png" alt="ORCID Symbol" style="height:15px;width:auto;vertical-align: top;background-color:transparent;"></a>, Felix Winkelmann, Robert Hein<a href="https://orcid.org/0000-0002-6258-3673"><img src="../assets/ORCIDiD_iconvector.png" alt="ORCID Symbol" style="height:15px;width:auto;vertical-align: top;background-color:transparent;"></a>
<br />

> <h style="color: black; ">18th International Conference on Computational Plasticity - COMPLAS 2025</h> 
> _2-5 September, 2025 - Barcelona_

<div style="position: absolute; bottom: 10px; left: 100px; color: grray; font-size: 20px;">
Presentation URL: https://perihub.github.io/Presentations/COMPLAS_2025
</div>

---

<!--header: '
<details style="position: absolute; z-index: 2;
  top: 0%;
  left: 0%">
  <span style="background: #009938;">
    <iframe src="https://app.sli.do/event/iZoQmywsAFqX7iApJ5f8sp" width="500px" height="600px" style="border: 0;"></iframe>
  </span>
<summary>Questions</summary>
</details>'-->
<!--paginate: true-->
<!--footer: 'https://perihub.github.io/Presentations/COMPLAS_2025'-->

# Introduction

---

<!-- _class: section-slide-vulcan -->

## Experiment

---

<!--footer: 'Specimen Geometry: ASTM E647-15'
_class: cols-2 -->

<div class=ldiv>

## Dogbone Specimen

| Parameter | Value  |
| --------- | ------ |
| $W$       | $75mm$ |
| $B$       | $12mm$ |
| $a$       | $21mm$ |

</div>
<div class=rimg>

![width:600px](./assets/compact_tension.svg)

</div>

---

<!--footer: ''
_class: cols-2-1-->

# Experimental Setup

<div class=ldiv>

## Loading Force

| Parameter | Value     |
| --------- | --------- |
| $F_{max}$ | $4.5\ kN$ |
| $R$       | $0.1$     |
| $f$       | $20\ Hz$  |

</div>
<div class=rdiv>

## Material: AA7010-T7452

| Parameter     | Value                |
| ------------- | -------------------- |
| $E$           | $71700\ MPa$         |
| $\nu$         | $0.33$               |
| $K_{IC_{LT}}$ | $37.44\ MPa\sqrt{m}$ |
| $K_{IC_{TL}}$ | $21.24\ MPa\sqrt{m}$ |

</div>

<div class=bdiv>

$F(t) = -2025 * sin(2 * pi * 20 * t - pi / 2) -2475$

</div>

---

<!-- _class: section-slide-rocket -->

## Experimental Results

---

# Experimental Results
<br/>
<iframe width="95%" height="95%" src="https://www.youtube-nocookie.com/embed/8V8CkSvO0Ok?si=2roU3VJ4qxuXFLeV" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

<!--footer: 'Results: https://perilab-results.nimbus-extern.dlr.de/models/ForgedCT'-->

## Dogbone Specimen | PeriLab Results

<iframe src="https://perilab-results.nimbus-extern.dlr.de/models/ForgedCT?step=10&variable=von Mises Stress&displFactor=20" width="1150" height="600"></iframe>

---

<!--footer: ''-->

# Load-Displacement

<iframe src="assets/plot.html" width="95%" height="95%" style="border: 0; margin-left: 70px"></iframe>

---

<!--header: ''-->

# Questions

<iframe src="https://app.sli.do/event/iZoQmywsAFqX7iApJ5f8sp" width="90%" height="85%" style="border: 0; margin-left: 70px"></iframe>

---

<!--footer: ''-->
<!-- _class: cols-2 -->
<!-- -We could determine three diferent failure mechanisms by looking at the crack surface-->

## Discussion and further work

<div class=ldiv>

- Lorum

</div>
<div class=rdiv>

![width:600px](./assets/Mechanism.png)

</div>

---

# Thank you

[Jan-Timo Hesse](mailto:jan-timo.hesse@dlr.de) (DLR)
[Christian Willberg](mailto:christian.willberg@h2.de) (DLR)
[Felix Winkelmann](mailto:felix.winkelmann@dlr.de) (h2)
[Robert Hein](mailto:robert.hein@dlr.de) (DLR)
![bg right height:8cm](https://gitlab.com/dlr-perihub/PeriLab.jl/-/raw/main/assets/PeriLab_crack.gif)

---

# References

1. [Foster, John & Silling, Stewart & Chen, Weinong. (2011). An energy based failure criterion for use with peridynamic states.](http://dx.doi.org/10.1615/IntJMultCompEng.2011002407)
2. [Willberg, Christian & Wiedemann, Lasse & Rädel, Martin. (2019). A mode-dependent energy-based damage model for peridynamics and its implementation.](https://doi.org/10.2140/jomms.2019.14.193)
3. [Willberg, Christian & Hesse, Jan-Timo & Pernatii, Anna. (2024). PeriLab - Peridynamic Laboratory.](https://doi.org/10.1016/j.softx.2024.101700)

---

## Funding

| Name                                                                                                         | Logo                                                                                                                 | Grant number                                                  |
| ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| [German Research Foundation](https://www.dfg.de/)                                                            | <img align="middle" src="https://raw.githubusercontent.com/PeriHub/PeriLab.jl/main/assets/dfg.jpg" height="120">     | [WI 4835/5-1](https://gepris.dfg.de/gepris/projekt/456427423) |
| [Saxon State Parliament](https://www.landtag.sachsen.de/de)                                                  | <img align="middle" src="https://raw.githubusercontent.com/PeriHub/PeriLab.jl/main/assets/sachsen.jpg" height="120"> | [3028223](https://www.m-era.net/materipedia/2020/emma)        |
| [Federal Ministry for Economic Affairs and Climate Action](https://www.bmwk.de/Navigation/DE/Home/home.html) | <img align="middle" src="https://raw.githubusercontent.com/PeriHub/PeriLab.jl/main/assets/hytank.jpg" height="120">  | 20W2214G                                                      |
