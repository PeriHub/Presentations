---
marp: true
theme: dlr
header: ""
footer: ""
title: Advanced Peridynamics Modeling for Predicting Anisotropic Crack Growth in Forged Materials
author: Jan-Timo Hesse, Christian Willberg, Eric Breitbarth, Florian Paysan
---

<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true });
</script>

<!-- _class: title-slide -->

## Advanced Peridynamics Modeling for Predicting Anisotropic Crack Growth in Forged Materials

<div style="position: absolute; top: 20px; left: 1050px;"> 
    <img src="assets/qr.png" alt="Presentation link" style="height:180px;width:auto;vertical-align: top;background-color:transparent;">
</div>

Jan-Timo Hesse<a href="https://orcid.org/0000-0002-3006-1520"><img src="../assets/ORCIDiD_iconvector.png" alt="ORCID Symbol" style="height:15px;width:auto;vertical-align: top;background-color:transparent;"></a>, Christian Willberg<a href="https://orcid.org/0000-0003-2433-9183"><img src="../assets/ORCIDiD_iconvector.png" alt="ORCID Symbol" style="height:15px;width:auto;vertical-align: top;background-color:transparent;"></a></a>, Eric Breitbarth<a href="https://orcid.org/0000-0002-3479-9143"><img src="../assets/ORCIDiD_iconvector.png" alt="ORCID Symbol" style="height:15px;width:auto;vertical-align: top;background-color:transparent;"></a> and Florian Paysan<a href="https://orcid.org/0000-0001-5575-1002"><img src="../assets/ORCIDiD_iconvector.png" alt="ORCID Symbol" style="height:15px;width:auto;vertical-align: top;background-color:transparent;"></a>
<br />

> <a href="https://sites.google.com/usacm.org/pd25/home" style="color: black; text-decoration: underline;">USACM Thematic Conference, Quarter Century of Peridynamics</a> 
> _April 23th to 25th, 2024, Tucson_

<div style="position: absolute; bottom: 10px; left: 100px; color: grray; font-size: 20px;">
Presentation URL: https://perihub.github.io/Presentations/USACM_2024
</div>

---

<!--paginate: true-->
<!--footer: 'Pres. URL: https://perihub.github.io/Presentations/USACM_2024'-->

## Forged Components

- Metals
- Compressive force
- Alluminium alloy:
  - High tensile strength
  - Applications in aerospace

![bg right width:350px](https://images.pexels.com/photos/3680094/pexels-photo-3680094.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1)

---

<!--footer: 'EBSD Scans by: Otto Fuchs'
_class: cols-2 -->
<!-- -Electron backscatter diffraction
-Grain structure of an alluminium alloy
- -->

## Forged Components

<div class=ldiv>

### Isotropic

![width:400px](./assets/Isotropic_Scan.png)

</div>
<div class=rdiv>

### Anisotropic

![width:500px](./assets/Anisotropic_Scan.png)

</div>

---

<!--footer: 'EBSD Scans by: Otto Fuchs'
_class: cols-2 -->

<div class=ldiv>

- Highly diverse material properties
- Anisotropic damage behavior depends on material orientations
- Time and cost-consuming identification of material properties

</div>
<div class=rdiv>

## Orientations

![width:500px](./assets/ebsd.png)

</div>

---

<!--footer: 'Specimen Geometry: ASTM E647-15'
_class: cols-2 -->

<div class=ldiv>

## Compact Tension Specimen

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
<!-- -Fracture Toughness
-Sine wave function -->

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

<!--footer: 'Video by: Carl Zeiss GOM Metrology GmbH'-->
<!-- -Black-white pattern
-Compression test
-Resulting surface stresses and displacments -->

## ARAMIS High-Speed DIC Systems

<div style="text-align: center;">
  <video src="./assets/zeiss_topics_aramis-high-speed_buckling-compression.mp4" controls width="90%"></video>
<div>

---

<!--footer: ''
_class: cols-2-->

# Experimental Results

<div class=limg>

![width:500px](./assets/CrackPath.png)

</div>
<div class=rimg>

![width:500px](./assets/CT_crack.png)

</div>

---

<!-- -Critical Energy
-Energy release rate
-Fracture toughness
-Damage index
-Bond energy
-Bond force density vector states
- -->

# Peridynamics

## Energy-based damage model by Foster

$$
\begin{align}
w_C&= \frac{4G_I}{\pi\delta^4} \qquad\qquad \tag{1}\label{eq:wc}\\
G_I&= K_I^2(\frac{1}{E}), \quad \text{plane stress} \tag{2}\label{eq:g1}\\
\chi(\underline{e}\langle\xi\rangle,t)&=
  \begin{cases}
      1,  & \text{if } w(\underline{e}\langle\xi\rangle) > w_C \\
      0,  & \text{otherwise}
  \end{cases} \tag{3}\label{eq:chi}\\
w &= \int_\eta (\mathbf{\underline{T}}[x,t]\langle x'-x\rangle - \mathbf{\underline{T}}[x',t]\langle x-x'\rangle)d\eta \tag{4}\label{eq:w}\\
\end{align}
$$

---

<!-- _class: cols-2 -->
<!-- -Two displaced bonds eta_a and eta_b -->

## Advanced energy-based damage model

<div class=ldiv>

- Material orientation angle $\alpha = 45\degree$
- Inverse rotation of Bonds $\eta_a$ and $\eta_b$
- Projection of $\eta_a$ and $\eta_b$ in the $L$ and $T$ directions

| Bond                                     | Bond components |
| ---------------------------------------- | --------------- |
| $(\eta_{a_{r_{LT}}}, \eta_{a_{r_{TL}}})$ | $(0,1)$         |
| $(\eta_{b_{r_{LT}}}, \eta_{b_{r_{TL}}})$ | $(0.5,0.5)$     |

</div>
<div class=rdiv>

![width:500px](./assets/3dPlot.svg)

</div>

---

<!-- -Critical Energy
-Energy release rate dependend on alpha
-Rotated Bond
-Rotated Bond components
-Bond energy components-->

## Advanced energy-based damage model

$$
\begin{align}
w_C(\alpha)&= \frac{4G_1(\alpha)}{\pi\delta^4} \tag{5}\label{eq:wca}\\
\mathbf{\eta}_{Rot}&= R^{-1}(\alpha)\mathbf{\eta} \tag{6}\label{eq:eta}\\
(\eta_{r_{LT}}, \eta_{r_{TL}})&= \frac{|\eta_{Rot_x}|}{||\mathbf{\eta}||} \tag{7}\label{eq:etax}\\
w(\underline{e}\langle\xi\rangle,\alpha)&= w(\underline{e}\langle\xi\rangle)(\eta_{r_{LT}}, \eta_{r_{TL}}) \tag{8}\label{eq:we}\\
\chi(\underline{e}\langle\xi\rangle,t,\alpha)&=
\begin{cases}
    1,  & \text{if } w(\underline{e}\langle\xi\rangle,\alpha) > w_C(\alpha) \\
    0,  & \text{otherwise}
\end{cases} \tag{9}\label{eq:chia}
\end{align}
$$

---

<!--footer: 'PeriLab Repository: https://github.com/PeriHub/PeriLab.jl'-->
<!-- _class: cols-2 -->
<!-- -Goal: as easy to use while keeping it modular and extensible --->

# PeriLab - Peridynamic Laboratory

<div class=ldiv>

- 🔑 **Open Source**

- 🚀 **Easy Installation**

- ✒️ **Modularization**

- 🎨 **User Materials**

- 🧲 **Multiphysics**

- 💻 **HPC capabilities**

- 📤📥 **Exodus Input/Output**

- 🧮 **Abaqus Input**

</div>

<div class=rdiv>

<div class=mermaid>
quadrantChart
  x-axis Low Functionalty --> High Functionalty
  y-axis Hard to use --> Simple to use
  Peridigm: [0.85, 0.2]
  PeriLab: [0.5, 0.8]
  EMU: [0.95, 0.1]
  PeriPy: [0.2, 0.7]
  PeriPyDIC: [0.2, 0.6]
  LAMMPS: [0.3, 0.3]
  PeriFlakes: [0.35, 0.4]
  Relation-Based Software: [0.4, 0.25]
  BB_PD: [0.2, 0.50]
  PeriDEM: [0.13, 0.3]
</div>
</div>

---

<!--footer: 'Results: https://perilab-results.nimbus-extern.dlr.de/models/ForgedCT'-->

## Compact Tension $45\degree$ Specimen | PeriLab Results

<iframe src="https://perilab-results.nimbus-extern.dlr.de/models/ForgedCT?step=10&variable=von Mises Stress&displFactor=20" width="1150" height="600"></iframe>

---

<!--footer: 'Julia Script: https://github.com/PeriHub/PeriLab.jl/blob/main/scripts/crack_path.jl'-->
<!-- _class: cols-2 -->

# Crack Path

<div class=ldiv>

- Resulting Damage indices extracted
- Weighted least-squares approximation
- Crack angle $\approx 26.6\degree$

</div>
<div class=rdiv>

![width:600px](./assets/plot.svg)

</div>

---

<!-- -Gradient is quite similar in the right section
-Gradient is to high in the start of the crack propagation -->
<!--footer: 'Results: https://perilab-results.nimbus-extern.dlr.de/plots/ForgedCTCrack'-->

## Compact Tension Crack Path

<iframe src="https://perilab-results.nimbus-extern.dlr.de/plots/ForgedCTCrack" width="1150" height="600"></iframe>

---

<!--footer: ''-->
<!-- _class: cols-2 -->
<!-- -We could determine three diferent failure mechanisms by looking at the crack surface-->

## Discussion and further work

<div class=ldiv>

- Basic phenomenon can be represented
- How to deal with occuring failure mechanisms
- Material Models
  - Plasticity
- Discretization and non uniform mesh
- Sensitivity Analysis

</div>
<div class=rdiv>

![width:600px](./assets/Mechanism.png)

</div>

---

# Thank you

[Jan-Timo Hesse](mailto:jan-timo.hesse@dlr.de) (DLR)
[Christian Willberg](christian.willberg@h2.de) (h2)
[Florian Paysan](florian.paysan@dlr.de) (DLR)
[Eric Breitbarth](eric.breitbarth@dlr.de) (DLR)
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
