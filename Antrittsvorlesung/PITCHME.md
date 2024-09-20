---
marp: true

theme: h2
header: ""
footer: ""
title: Antrittsvorlesung
author: Christian Willberg
---

<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true });
</script>

<!-- _class: title-slide -->

# Modellierung von Schädigungsmechanismen

<div style="position: absolute; top: 150px; left: 1050px;">
  <img src="assets/qr.png" alt="Presentation link"
    style="height:180px;width:auto;vertical-align: top;background-color:transparent;">
</div>

Christian Willberg<a href="https://orcid.org/0000-0003-2433-9183"><img src="../assets/ORCIDiD_iconvector.png"
    alt="ORCID Symbol" style="height:15px;width:auto;vertical-align: top;background-color:transparent;"></a>

Antrittsvorlesung Hochschule Magdeburg-Stendal HS 2, 08.10.2024, Magdeburg



<!---
- not the typical computational engineering presentation
- algorithms are impresive, but we asked ourself, why so few algorithms reach the productive phase
-  are our results in paper realy reproducible?
- We discuss all the time about fast algorithms and run time but -> next slide
-->


<!--paginate: true-->
<!--footer: 'https://github.com/PeriHub/Presentations/tree/master/Antrittsvorlesung'-->

---

## Leichtbau und effizienter Ressourceneinsatz
![bg right](assets/IWES_test.jpg)
- große Zahl von Variationen
- Experimente sind teuer
- Zuverlässigkeit


---
## Testpyramide

![bg fit right](assets/Testpyramide.png)

---

## Mikrostruktur

- Mikrostruktur beeinflusst die Initiierung
- Simulationen und Experimente zum Ableiten von Kennwerten für die Mesoskala

![bg right 60%](assets/crack.jpg)
![bg vertical 60%](https://upload.wikimedia.org/wikipedia/commons/e/e2/TiAl_Lammelar.jpg)


---
## Klassische Modellierung
- klassische Kontinuumsmechanische Formulierung $\text{div}(\mathbf{\sigma})+\textbf{b} =\rho\ddot{\textbf{u}}$
- Approximation der partiellen DGL mittels der Finiten Elemente Methode
- Zentrale Annahme:
  - $C^1$ Stetigkeit des Verschiebungsfeldes

---

## Problem der unendlichen Spannungen
  - Interfaces
  - Rissspitzen
  - Ecken

![bg right 100%](assets/Pruefung.png)

---

## Peridynamics (PD)

$\int_{\mathcal{H}}(\underline{\textbf{T}}(\textbf{x},t)
\underline{\textbf{T}}(\textbf{x}',t))dV_{\textbf{x}}+\textbf{b} =\rho\ddot{\textbf{u}}$

![bg right 70%](assets/PeriMesh.PNG)

---


## Peridynamics (PD)

$$\mathbf{F}=\left[\int\limits_{\mathcal{H}}\underline{\omega}\langle 
\boldsymbol{\xi}\rangle\underline{\mathbf{Y}}\langle 
\boldsymbol{\xi}\rangle\otimes\underline{\mathbf{X}}\langle 
\boldsymbol{\xi}\rangle dV_{\textbf{x}}\boldsymbol{\xi}\right]\cdot \mathbf{K}^{-1}$$


$$\mathbf{K}=\int\limits_{\mathcal{H}}\underline{\omega}\langle 
\boldsymbol{\xi}\rangle\underline{\mathbf{X}}\langle 
\boldsymbol{\xi}\rangle\otimes\underline{\mathbf{X}}\langle 
\boldsymbol{\xi}\rangle dV_{\textbf{x}}$$ 

$$\underline{\mathbf{T}}\langle \boldsymbol{\xi}\rangle = 
\underline{\omega}\langle 
\boldsymbol{\xi}\rangle\mathbf{P}\mathbf {K}^{ -1 } \boldsymbol { \xi }\quad\text{with}\quad\mathbf{P}=\text{det}\mathbf{F}\boldsymbol{\sigma}\mathbf{F}^{
-1}$$

![bg right 70%](assets/PeriMesh.PNG)

---
## Beispiele

- Anisotropie in Metallen
- Additive Fertigung

![bg right:47% transparent](assets/examples.png)

---

## Geschiedete Bautteile


<!--footer: 'EBSD Scans by: Otto Fuchs'
_class: cols-2 -->
<!-- -Electron backscatter diffraction
-Grain structure of an alluminium alloy
- -->

<div class=ldiv>

  ### Isotropic

  ![width:400px](./assets/Isotropic_Scan.png)

</div>
<div class=rdiv>

  ### Anisotropic

  ![width:500px](./assets/Anisotropic_Scan.png)

</div>

---


<!--footer: ''
_class: cols-2 -->
<!-- -Electron backscatter diffraction
-Grain structure of an alluminium alloy
- -->


# Experimentelle Ergebnisse

<div class=limg>

![width:500px](./assets/CrackPath.png)

</div>

<div class=rimg>

![width:500px](./assets/CT_crack.png)

</div>


---

## KIC $45\degree$ Specimen | PeriLab Ergebnisse

<iframe src="https://perilab-results.nimbus-extern.dlr.de/models/ForgedCT?step=10&variable=von Mises Stress&displFactor=20" width="1150" height="600"></iframe>


---

## Additive Fertigung

<iframe src="https://perilab-results.nimbus-extern.dlr.de/models/RVE?step=25&variable=Displacements&displFactor=100"
      width="1150" height="600"></iframe>

---


<div style="text-align: center;">
  <video src="./assets/zeiss_topics_aramis-high-speed_buckling-compression.mp4" controls width="90%"></video>
<div>

## Performanc
-a
-a
-d
-a
-g
-f
-g
-5
-5
-8

<div class="container">
  <div class="col">
    <div style="position: absolute; bottom: 120px; left: 50px; color: blue; font-size: 20px;">
      <img src="assets/Benchmark_mesh.png"
        style="height:430px;width:auto;vertical-align: top;background-color:transparent;">
    </div>
  </div>
  <div class="col"
  </div>
  <div style="position: absolute; bottom: 50px; left: 650px; color: blue; font-size: 20px;">
    <img src="assets/benchmark.svg"
      style="height:550px;width:auto;vertical-align: top;background-color:transparent;">
  </div>
</div>

---
## Conclusio
- modern language should be preferred if new projects are started
- Julia is a great alternative to C++ and for PhD students easier to learn and to handle
- installation time was reduced to minutes from hours (if it even works)
- more user focussed developement

---
## Upcomming
- Coupled PD-FEM
- Axissymmetric
- New solver
- ...

    
---

## Danke für die Aufmerksamkeit
Christian Willberg: Magdeburg-Stendal University of Applied Sciences 
christian.willberg@h2.de

    

![bg right height:7cm](https://gitlab.com/dlr-perihub/PeriLab.jl/-/raw/main/assets/PeriLab_crack.gif)