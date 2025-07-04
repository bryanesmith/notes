# Electronic Components

## Silicon Control Rectifier (SCR), aka Thyristor

Type of **control diode** (diode used to regulate current flow or voltage)

**SCR** is the General Electric (GE) name for a **thyristor**

Rectifier consisting of 4 layers of alternating P-type and N-type semiconductor materials (PNPN)

Primarily used in high current and high voltage switching

Three electrodes: anode (A), cathode (C), gate  (G)

**Adjustable Gate Control** regulates how much SCR conducts

**Holding current**: minimum amount of anode current must flow to keep in "on" state

Once threshold current flows through gate, allows forward flow of electricity (as long as meets holding current)

SCR is a **metastable device**, meaning once its in a state of forward flow, it stays in this state, even when the trigger isn't present.

Three modes: 
1. reverse blocking (unidirectional)
2. forward blocking
3. forward conducting

Common uses: 
* light bulb dimmers (more efficient than variable resistor)
* variable-speed drives
* conveyor belts (smooth acceleration/deceleration)
* pressure control systems
* controlled rectifier circuits (e.g., power supplies), stable output voltage

Pros: (1) longevity (solid-state devices with no moving parts), (2) handle significant power levels, (3) energy efficient

# Transistor

Semiconductor device made of three alternating layers of doped semiconductor material, either "NPN" or "PNP".

Contains three terminals: Collector (C), Emitter (E), and Base (B)

Usually, if the small resin transitors facing flat side forward, the pins are (left-to-right): emitter, base, collector. However, not always, so check part sheet.

Control larger current flowing between **Collector** and **Emitter** based on a smaller current at the **Base**. 

Typically requires 0.6 - 0.7V to base pin for transistor to turn on.

When working with transistors, the **main circuit** does not flow if the **control ciruit** is off.

Two main functions: (1) switch circuits on and off, (2) amplify signals

With **NPN transistor**, the current combines. E.g., if 20mA flow into the Collector and 5mA flow into the base, then 25mA flow out of the emittor.

With **PNP transistor**, the current divides. E.g., if 25mA flow into the emittor and 5mA flow out of the collector, then 20mA flow out of the collector.

The transitor conducts in two modes: a linear mode, and a saturation mode.

**Linear mode**: The stronger the current across the Base (up to a maximum point), the more current flows between the Collector and Emitter. Once the current across the Base stops, so does the current between the Emitter and Collector.

I.e., the transistor (unlike the SCR) is *not* a **metastable device**, which stays in a forward flow state even when the trigger is no longer present.

**Saturation mode**: Once the current across the Base exceeds a threshold called **saturation**, the same currrent flows between the Collector and Emitter but the transister stars to heat up. Once the current across the base stops, there's a **turn-off delay** before the Emitter and Collector stops.

Used in low-to-moderate power circuits.

Small, low power transistors have resin case; whereas higher power transistors have partially metal cases to dissipate heat, often attached to a heat sink.

Broad set of use cases in digital circuits, amplifiers, signal processing.

Use cases:
* microprocessors
* radios
* other electronic devices

For **amplifiers**, the ratio of the collector current to the base current is called the **gain**. E.g., if base current of 1mA and collector current 100mA, β = 100mA/1mA = 100

# Glossary

* **Bohr model**: model of the aton describing electrons orbiting nucleus in specific, quantized energy levels. The outer layer contains valence electrons.

* **chemical bondings**: three ways atoms share electrons
    - **covalent bonding**: atoms share covalent electrons in a stable electron configuration. E.g., Silicon atoms have 4 covalent electrons, but "want" 8 covalent electrons - so neighboring silicon atoms "share" their covalent electrons. 
    - **ionic bonds**
    - **metallic bonds**: atoms share a "sea" of delocalized electrons, allowing free movement of electrons, enabling good electric conductance. (E.g., copper, iron)

* **controlled rectifier**: AC-to-DC converter allowing control over output voltage or power

* **conventional current**: We always design circuits such that electricity flows from positive to negative. (In reality, electrons flows from negative to positive.)

* **doping**: adding impurities to a pure semiconductor materia to modify its electrical conductivity and increase conductivity. 
    - **N-type doping** adds impurities with extra valence electrons. (E.g., phosophorous has 5 covalent electrons, silicon has 4 covalent eletrons; so with covalent bonding, there's a free covalent electron to move around.)
    - **P-type doping** adds impurities with fewer valence electrons, creating holes. (E.g., aluminum has 3 covalent electrons, silicon has 4 covalent electrons; so with covalent bonding, they are missing a covalent electron, creating a postively-charged hole)

* **semiconductor**: material with a conduction band close to the valence shell; requires some energy to conduct, but can also act as insulator

* **signals**: physical quantities carrying information, e.g., audio, image, telecommunications

* **signal processing**: field of engineering focused on transforming signals to extract information or achieve other goals